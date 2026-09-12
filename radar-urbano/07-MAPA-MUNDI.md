# Radar Urbano · 07-MAPA-MUNDI

Manual de montagem da máquina. Régua: BRIEF (seções 6–9 e 15). Nomes de tabelas, tópicos, ferramentas e variáveis são os mesmos no código, no Diário de Bordo e aqui.

## 1. Arquitetura

Cinco agentes em fila por tenant, em cadência fixa, sobre uma memória única, usando quatro conectores e um serviço de entrega. Sem atendimento em tempo real; a máquina não fala com cliente final. Tudo que entra vem do Google com data de referência; tudo que sai vai para o dono.

Cinco camadas (de cima para baixo):

1. Interfaces com o mundo: Perfil da Empresa no Google (Busca e Maps), Places API (New), WhatsApp do dono (via número da casa), Dashboard Radar. Nenhuma outra.
2. Conectores: GBP, Places, WA (número da casa), TTS; ao lado, Render & Delivery (cards, mapa, PDFs, QR, dashboard, envio com status). Conector executa, registra custo, devolve JSON; nunca decide.
3. Agentes, orquestrador e Guardião: Cartógrafo, Editor, Anfitrião, Tesoureiro, Redator-chefe. Orquestração: Cloud Scheduler → Pub/Sub → Cloud Run Jobs; Cloud Tasks para filas por tenant. Guardião: humano com painel.
4. Cérebros: Gemini na Vertex AI (obrigatório para dado, medição, aferição, áudio, foto, decisão que toca o Google); cérebro de linguagem intercambiável atrás do `LLMGateway`; Cloud Text-to-Speech. Nenhum agente chama modelo direto.
5. Memória e prova: Firestore (estado por tenant), BigQuery (métricas, medições, Diário, custo, zonas), Cloud Storage (fotos, prints, PDFs, áudios), Secret Manager (credenciais, nunca senha de cliente).

Regra da pilha: cada camada fala só com a imediatamente abaixo. Guardião entra pela camada 3, pelo painel.

Sete regras:

1. Camadas estritas: interface → conector → agente → cérebro → memória; trocar modelo, voz ou template não toca agente; trocar endpoint toca só o conector.
2. Gemini é o cérebro de dados e de Google: toda leitura, extração, aferição, classificação e decisão que envolva API ou superfície do Google passa pelo Gemini com saída estruturada (e Grounding com Google Maps quando cabe).
3. Um cliente é um tenant, e um tenant tem zona: todo dado carrega `tenant_id`; todo tenant nasce com `segmento` e `zona` e só nasce se `zone.check` confirmar vaga (máximo 2 por segmento por zona, em transação).
4. Tudo é job idempotente: chave `tenant_id + agente + entrega + período`, verificada antes da ação externa e gravada com ela.
5. Humano aprova, IA executa: P0 tudo antes; P1 lote (meta > 85% sem edição); P2 publicação direta com QA de 10%; categoria principal, nome, endereço e respostas a notas 1 e 2 sempre com dois olhos.
6. Diário de Bordo é a verdade: toda ação externa escreve linha imutável em `actions_log` com agente, modelo, versão do prompt, entrada, saída, print e hora; sem linha, não aconteceu.
7. Custo por cliente é métrica de primeira classe: cada chamada grava custo por tenant; alerta em R$ 25/cliente/mês.

## 2. Cérebros

| Função | Modelo | Como |
|---|---|---|
| Extração e normalização (perfil, métricas, avaliações, perguntas, palavras-chave) | Gemini Flash (volume) · Gemini Pro (análise mensal) | Vertex AI `generateContent` + `responseSchema` |
| Aferição de posição e leitura de superfícies Google | Gemini + Grounding com Google Maps | A medição é `places.search_text`; o Gemini interpreta e propõe termos |
| Decisões que tocam API do Google (campo, categoria, o que otimizar) | Gemini Pro | Function calling com ferramentas do GBP Connector |
| Transcrição dos áudios do Dia 0 | Gemini multimodal | Parte de áudio (OGG) + `responseSchema`: termos, raio, tom, limites, nome |
| Classificação de avaliações e perguntas (temas, sentimento, suspeita) | Gemini Flash | Polling 30 min; lote noturno; cache de contexto |
| Julgar fotos (nitidez, rosto, adequação, é o lugar) | Gemini multimodal | `vision.assess_photo(uri)`; nunca gera foto |
| Posts, respostas, roteiros, três frases | Cérebro de linguagem (Claude Sonnet ou Gemini Pro) | `LLMGateway.generate(task, tenant)`; escolha por avaliação cega mensal |
| Verificação cruzada de números | Gemini Flash | `task=CROSSCHECK` → `{ok, numeros_fora[]}`; bloqueia a síntese |
| Voz do Boletim | Cloud TTS, Chirp 3 HD pt-BR | `TTS_VOICE_ID` fixo da casa |
| Ordenar a fila do Guardião | Gemini Flash | Agrupa e ordena por risco; não aprova |

```
LLMGateway
  generate(task: TaskKind, tenant, input, schema?) -> Output
  policy(task) -> {primary, fallback[], max_cost}
  Gemini obrigatório (sem fallback; se fora do ar, espera na fila):
    EXTRACT, MEASURE, CLASSIFY, GOOGLE_DECISION, AUDIO_IN, VISION, CROSSCHECK
  linguagem (primary=LLM_LANGUAGE_PRIMARY, fallback=LLM_LANGUAGE_FALLBACK):
    POST, REPLY_REVIEW, REPLY_QUESTION, BOLETIM, THREE_SENTENCES
  anonimiza antes da chamada (dono, avaliador -> ids internos), salvo tarefa que exige
  telemetria: tokens, custo, latência, prompt_versao, tenant -> BigQuery.llm_calls
```

Regras:

1. Saída estruturada sempre; texto livre só no artefato final. Sem JSON válido: retry com temperatura menor; na terceira falha, exceção no Guardião.
2. Prompts versionados no repositório; versão gravada em `actions_log` e `llm_calls`; mudar prompt é deploy com avaliação.
3. Avaliação cega mensal: 100 amostras por agente, dois humanos, sem saber o modelo. Tarefas Gemini-obrigatórias não disputam; entram na auditoria.
4. Cache de contexto do Gemini (perfil, tom, termos, raio, regras), renovado a cada 24 h; custo entra em `llm_calls`.
5. Nenhum dado pessoal no prompt sem necessidade; o modelo nunca recebe número da casa nem token.

## 3. Conectores

### GBP Connector

| Item | Detalhe |
|---|---|
| APIs | Business Information API v1: `accounts.locations.list` (descoberta no Dia 0), `locations.get` (`readMask`), `locations.patch` (`updateMask` obrigatório, `validateOnly`), `getAttributes`/`updateAttributes`, `attributes.list`, `categories.list`; campos `regularHours`, `specialHours`, `profile.description`, `serviceItems`, `categories`, `metadata.newReviewUri`, `metadata.mapsUri` · Performance API v1: `fetchMultiDailyMetricsTimeSeries` (`CALL_CLICKS`, `BUSINESS_DIRECTION_REQUESTS`, `WEBSITE_CLICKS`, `BUSINESS_CONVERSATIONS`, `BUSINESS_IMPRESSIONS_{DESKTOP,MOBILE}_{SEARCH,MAPS}`), `searchkeywords/impressions/monthly` · API v4: `reviews.list`, `reviews.reply`, `localPosts.create`, `media.create` · My Business Q&A API: `questions.list`, `questions.answers.upsert` · Account Management: `locations.admins.list` · Verifications: `getVoiceOfMerchantState` |
| Acesso | Formulário oficial de acesso às Business Profile APIs (1–2 semanas; pedido no dia 1 da semana 1). OAuth 2.0 com a conta operacional (2FA), papel Gerente em cada perfil, escopo `business.manage`. `GBP_OPERATOR_REFRESH_TOKEN` no Secret Manager; `tenant-{id}-gbp-oauth` aponta por padrão para o token da casa. Nunca senha de cliente. Gerente removido = acesso perdido na hora, `locations.status` marcado, incidente |
| Cotas | Baixas por padrão para edição; pedir aumento com o acesso. Desempenho em lote 03h (D-3..D-1, `data_referencia`); edições por Cloud Tasks (uma por tenant, retry exponencial em 429/5xx); polling de avaliações e perguntas a cada 30 min, `pageSize` 50, `updateTime`. Palavras-chave abaixo do limiar chegam como faixa |
| Termos | Nome real, sem termo de busca; categoria descreve o negócio; horários e fotos reais; posts sem promessa; política de avaliações (sem incentivo, seleção ou dado do avaliador); suspeita denunciada pelo fluxo oficial, nunca respondida com acusação |
| Armadilhas | Categoria principal só com humano; `patch` sem `updateMask` apaga o resto (conector recusa); detectar `SUSPENDED`/`PENDING_VERIFICATION`; `hasGoogleUpdated` = revisar antes de sobrescrever; nota chega como enum `ONE..FIVE`; foto/post exigem URL pública (assinada, curta); recursos v4 podem migrar (por isso ficam atrás do conector); descrição até 750 caracteres |

### Places Connector

| Item | Detalhe |
|---|---|
| Endpoints | `places:searchText` com `textQuery`, `locationBias` circular no ponto (raio = passo), `rankPreference` padrão, `languageCode=pt-BR`, `regionCode=BR`, `pageSize=20`, máscara `places.id` (validação: + `displayName`) · `places/{place_id}` só no Dia 0 (`id,displayName,formattedAddress`) |
| Acesso | Chave restrita à Places API (New) e ao IP de saída (Cloud NAT fixo); `PLACES_API_KEY` no Secret Manager; ativa na hora; nunca no navegador |
| Cotas | Uma chamada por termo por ponto; grade 3×3 a 5×5; até 25 termos por tenant; ≈ 240 chamadas/tenant/mês (completa dia 1 + reduzidas); teto em `limites_json`; R$ 3–8/cliente/mês |
| Termos | Sem extração em massa, sem raspagem; nada além de 30 dias exceto `place_id`. Guardamos só `place_id` do cliente, data, termo, ponto, lat/lng, posição. Nada de outros lugares |
| Método | Ponto central no endereço; passo = raio (3×3) ou raio ÷ 2 (5×5); posição = índice do `place_id` no resultado (1–20) ou "não encontrado". Verde top 3, cinza 4º–10º, vermelho fora do top 10 ou não encontrado no top 20. Mesmo horário sempre (02h dia 1, 03h sábado). Validação mensal: 20 buscas manuais, concordância ≥ 85% no top 3, em `qa_samples` |
| Armadilhas | `locationBias` é viés, não cerca (`locationRestriction` distorce); `rankPreference=DISTANCE` mede outra coisa; sem `languageCode`/`regionCode` a lista muda; não paginar além de 20; `place_id` pode mudar em fusão (reconfirmar via `metadata.mapsUri` no Dia 0 e dia 1); alerta de orçamento contra chave vazada |

### WA Connector (número da casa)

| Item | Detalhe |
|---|---|
| Endpoints | `POST /{phone_number_id}/messages` (`template`, `audio`, `image`, `document`, `interactive`) · `POST /{phone_number_id}/media` · `GET /{media_id}` (áudios do Dia 0) · webhooks `messages` e `statuses` (`sent`, `delivered`, `read`, `failed`) · `/{waba_id}/message_templates` · `/{waba_id}/phone_numbers` (`quality_rating`, `messaging_limit_tier`) |
| Acesso | Portfólio de negócios do Radar Urbano verificado (CNPJ; começa no dia 1); app com produto WhatsApp; número dedicado, nome de exibição "Radar Urbano"; usuário de sistema → `META_SYSTEM_USER_TOKEN`; `META_APP_ID/SECRET` (assinatura dos webhooks); `WA_WEBHOOK_VERIFY_TOKEN`; `DELIVERY_SENDER_PHONE_ID`. Sem Tech Provider, sem Embedded Signup, sem conta do cliente |
| Modelos (Utilidade, rodapé "Responda SAIR para parar") | `boletim_segunda`: cabeçalho de vídeo (card parado + voz da casa em MP4), corpo com números e data de referência, botão do dashboard; usado com a janela de 24 h fechada · `entrega_radar`: cabeçalho de imagem (cards) · `entrega_radar_pdf`: cabeçalho de documento (PDFs; no código é o nome lógico `entrega_radar`) · `pergunta_sim_nao`: botões Sim/Não · `aviso_radar`: {{1}} nome, {{2}} a linha |
| Janela | Mensagem livre (OGG, PNG, PDF, texto) só na janela de 24 h aberta pelo dono (toque em botão conta). Dia 0: o dono abre a conversa pelo link da página do contrato; sem mensagem em 1 h, o número da casa manda `pergunta_sim_nao` ("Podemos começar?"). Segunda: janela aberta → card PNG + OGG livres; fechada → `boletim_segunda`. O Delivery registra o caminho |
| Cotas | ≈ 25 mensagens/dono/mês (4–5 Boletins, 6 entregas do dia 1, avisos, perguntas). Envios: Boletim 7h; dia 1 e Dia 7 até 8h; `aviso_radar` e perguntas entre 8h e 19h. R$ 1–2/cliente/mês |
| Armadilhas | Modelo com cheiro de marketing = custo maior e rejeição; `quality_rating` cai com bloqueios (SAIR honrado na hora em `tenants.wa_optout`); número dedicado, nunca celular de alguém; áudio `audio/ogg` Opus, PNG ≤ 5 MB, MP4 ≤ 16 MB; número do dono só como `dono_wa_hash` nas tabelas; texto livre do dono vai a humano, nunca a modelo; token rotacionado a cada 90 dias |

### TTS + Render & Delivery

| Item | Detalhe |
|---|---|
| TTS | Cloud Text-to-Speech, Chirp 3 HD pt-BR, `TTS_VOICE_ID` fixo (a voz é do Radar Urbano, igual para todos); `OGG_OPUS` 48 kHz; ≤ 60 s (corte por ≤ 150 palavras antes; conector mede e recusa acima); números e horas por extenso; custo em `llm_calls` com `task=TTS`. Para o modelo de vídeo, card + OGG viram MP4 de 60 s |
| Cards e mapa | HTML → PNG (Chrome headless, Cloud Run), templates versionados por entrega; Mapa de Domínio em SVG a partir de `rank_measurements` (`render.map_svg`), PNG para WhatsApp e SVG interativo no dashboard; todo card traz cliente, período e data de referência |
| PDFs | HTML → PDF, uma página: Diagnóstico, Extrato, Fechamento (mensal e trimestral), material do QR. Storage `radar-{amb}-artefatos/{tenant_id}/{entrega}/{periodo}.pdf`; URL assinada 30 dias; cópia permanente no dashboard |
| QR e link curto | `gbp.get_review_link` lê `metadata.newReviewUri`; `render.qr` gera QR + PDF de balcão e comanda com frase neutra; sem prêmio, sem filtro; enviado na primeira semana por `entrega_radar`; único pedido de avaliação do produto |
| Dashboard | Next.js no Cloud Run; link fixo `DASHBOARD_BASE_URL/t/{token}` (ícone no celular); senha opcional criada pelo cliente no Identity Platform (link mágico = entrada sem senha; link único = criar/redefinir senha); lê visões materializadas de hora em hora; seções: números com data de referência, Mapa interativo, Diário com prints, Voz do Cliente, Boletim de Reputação, arquivos, Horas Devolvidas, custo por contato; abertura grava `lido_em` |
| Delivery | Recebe (tenant, entrega, período, artefatos); decide janela × modelo e o modelo por artefato; sobe mídia; envia; grava `enviado_em`, `entregue_em`, `lido_em` via `statuses`; linha no Diário; chave `tenant + entrega + período`; reenvio único após 2 h sem `delivered`, depois incidente; respeita `wa_optout` e janelas de horário; fila `deliveries.send` |

## 4. Fundação

| Peça | Escolha | Papel |
|---|---|---|
| Projetos | `radar-hml`, `radar-prd`, `southamerica-east1` | Isolamento, dados no Brasil |
| APIs | Vertex AI, Places API (New), Business Profile APIs (após aprovação), Cloud TTS, Cloud Run, Cloud Build, BigQuery, Firestore, Secret Manager, Scheduler, Pub/Sub, Identity Toolkit | Nada além disso; sem Google Ads API |
| Execução | Cloud Run (webhooks, dashboard, painel do Guardião, render) e Cloud Run Jobs (agentes) | Escala a zero; um container por agente |
| Agentes | ADK em Python; ferramentas expostas pelos conectores; opção Vertex AI Agent Engine | Padrão Google para agentes com Gemini |
| Orquestração | Cloud Scheduler → Pub/Sub → Jobs; Cloud Tasks por tenant | Cadência, retry, idempotência |
| Estado | Firestore: documento por tenant | Fonte do que a máquina pode fazer sem perguntar |
| Analítico | BigQuery particionado por data, clusterizado por `tenant_id` | Métricas, medições, Diário, custo, zonas |
| Calendário | Tabela própria de feriados nacionais e municipais (linha por cidade e data), lida por `calendar.holidays` | Editor age 72 h antes |
| Arquivos | Cloud Storage, bucket por ambiente, prefixo por tenant, ciclo de vida | Fotos, prints, PDFs, cards, áudios |
| Segredos | Secret Manager | Um segredo por uso; nunca senha de cliente |
| Identidade | Identity Platform | Dashboard do cliente; painel interno com 2FA |
| Observabilidade | Logging, Error Reporting, Monitoring; `llm_calls`; painel de custo por tenant | Alerta em R$ 25 |
| Código | GitHub → Cloud Build → Cloud Run; Terraform; prompts e templates versionados | Reproduzível |

Modelo de dados (BigQuery):

```
tenants(tenant_id, nome, segmento, zona, tom_json, limites_json, termos[], raio_m, dono_nome, dono_wa_hash, criado_em)
zones(segmento, zona, cidade, tenants_ativos, limite=2)
locations(tenant_id, gbp_location_id, place_id, categoria, endereco, telefone, status)
metrics_daily(tenant_id, data, call_clicks, directions, website_clicks, conversations, impressions_search, impressions_maps, data_referencia, coletado_em)
keywords_monthly(tenant_id, mes, termo, impressoes)
rank_measurements(tenant_id, data, termo, grid_point, lat, lng, posicao)
reviews(tenant_id, review_id, data, nota, texto_hash, temas[], sentimento, respondida_em, resposta_id)
questions(tenant_id, question_id, data, texto_hash, respondida_em, resposta_id)
posts(tenant_id, post_id, data, tipo, foto_uri, texto, aprovado_por, publicado_em)
profile_audits(tenant_id, data, campo, antes, depois, origem)
actions_log(tenant_id, ts, agente, entrega, acao, alvo, entrada_uri, saida_uri, print_uri, prompt_versao, modelo, custo)   -- Diário de Bordo, append-only
deliveries(tenant_id, entrega, periodo, artefato_uri, canal, enviado_em, entregue_em, lido_em)
llm_calls(tenant_id, ts, agente, task, modelo, tokens_in, tokens_out, custo, latencia_ms, prompt_versao)
hours_equivalence(acao, minutos)
qa_samples(tenant_id, data, action_id, veredito, nota_operador)
```

Notas: contatos = `call_clicks + directions + website_clicks + conversations`; impressões e palavras-chave são contexto. `rank_measurements.posicao` nula = não encontrado. `profile_audits` com `origem='diagnostico'` é o "antes" do Dia 7. `actions_log` só `INSERT`, toda linha com `print_uri`; dele saem as Horas Devolvidas cruzando `acao` com `hours_equivalence`.

Tenancy:

1. Um documento Firestore `tenants/{tenant_id}`: configuração, `limites_json`, tom, termos, raio, `segmento`, `zona`, estado do onboarding, consentimento e opt-out, subcoleções `approvals` e `queue`. Nasce só depois de `zone.check` aprovar; zona lotada vai para lista de espera.
2. Segredos por tenant (`tenant-{id}-gbp-oauth`); segredos da casa lidos só pelo conector dono; rotação 90 dias; revogação no offboarding.
3. Contas de serviço mínimas por agente e conector (Editor não lê `metrics_daily`; Tesoureiro não escreve `posts`; só WA Connector lê token da Meta; só Delivery lê o número claro; ninguém tem `UPDATE`/`DELETE` em `actions_log`).
4. Hash de dados pessoais: `dono_wa_hash` com sal por tenant; textos de terceiros só como `texto_hash` + temas + sentimento; nenhum nome de avaliador em tabela; nenhum cliente final na base.

Estados do onboarding: `zone.check` (antes de existir) → `created` → `billing_active` → `profiled` → `gbp_linked` ou `gbp_pending_verification` → `live`.

## 5. Agentes

Todos em ADK; nenhum chama API direto; nenhum fala com o dono por conta própria (só via `delivery.send`). Sentinela de calendário é rotina do Editor, não agente. Convite de avaliação não existe.

### Cartógrafo

| | |
|---|---|
| Gatilho | Dia 0 após `gbp_linked` (reduzida); Dia 7 (reduzida); sábado 03h (reduzida, termos-chave); dia 1 02h (completa). Reduzida = 3×3 e até 5 termos; completa = grade do tenant e todos os termos |
| Entradas | `tenants` (`termos[]`, `raio_m`, `limites_json`), `locations` (`place_id`, `status`), `keywords_monthly`, `rank_measurements` do mês anterior, grade gerada do raio |
| Ferramentas | `places.search_text` · `gbp.get_keywords` · `gbp.get_location` · `render.map_svg` · `render.card` · `cost.per_tenant` · `diario.log` |
| Cérebro | Gemini Pro + Grounding com Google Maps (território, termos, diagnóstico); Gemini Flash (normalizar). Sem cérebro de linguagem |
| Saídas | `rank_measurements`; Mapa de Domínio SVG/PNG (edição reduzida no Dia 0 e Dia 7); JSON do Diagnóstico para o Redator-chefe; `editor.tasks`; sugestão de categoria para o Guardião; variação mensal de pontos verdes |
| Guardrails | ≤ 25 termos; grade ≤ 5×5; chamadas limitadas por `limites_json` (reduz grade antes de termos); grava só o `place_id` do cliente; nunca cita outro perfil; categoria só via Guardião; mede mesmo em `gbp_pending_verification` |
| Métricas | Custo de medição; cobertura da grade; variação de pontos verdes; concordância com 20 buscas; sugestões aceitas; duração da reduzida (< 2 min) |
| Teste de aceitação | Mapa reproduz 20 buscas manuais com ≥ 85% no top 3; reduzida em < 2 min; `rank_measurements` sem `place_id` que não seja o do tenant |

```
Você é o Cartógrafo. Recebe posição por termo e ponto (índice do place_id do cliente ou "não encontrado"), palavras-chave com impressões e o perfil atual.
Classifique: verde = top 3, cinza = 4–10, vermelho = fora do top 10 ou não encontrado.
JSON: {territorio:[{termo,pontos_verde,pontos_cinza,pontos_vermelho,variacao_mes}], diagnostico:{termos_no_top3,termos_fora,maior_lacuna}, oportunidades:[{termo,motivo,acao_sugerida}], auditoria_perfil:[{campo,atual,sugerido,impacto}], nap_consistente:bool}
Não invente termos sem impressões. Não compare nem cite outro perfil. Não sugira termos no nome. Não prometa posição.
```

### Editor

| | |
|---|---|
| Gatilho | Segunda 04h (post); diário 05h (horários e feriados, 72 h antes); `editor.tasks` (Cartógrafo, Voz do Cliente); Dia 0 (auditoria de completude); Dia 7 (diff); dia 1 (auditoria mensal); `approvals.decided` |
| Entradas | `tom_json`, `limites_json`, perfil atual, fotos existentes, `calendar.holidays`, tarefas do Cartógrafo, `profile_audits` |
| Ferramentas | `gbp.get_location` · `gbp.create_post` · `gbp.upload_media` · `gbp.patch_location` · `gbp.update_hours` · `gbp.update_services` · `calendar.holidays` · `vision.assess_photo` · `guardiao.submit` · `diario.log` · `render.card` · `delivery.send` |
| Cérebro | Linguagem para post e descrição; Gemini multimodal para fotos; Gemini para qualquer campo do perfil |
| Saídas | Itens no Guardião (P0/P1) ou publicação (P2), sempre com Diário e print; `posts`; `profile_audits`; horários de feriado; auditoria de completude (Dia 0, dia 1); diff do Dia 7; `aviso_radar` quando há ação relevante |
| Guardrails | Só fotos com `assess_photo.ok` e sem rosto sem termo; categoria principal, nome e endereço sempre via Guardião; ≤ 1 post/dia; descrição ≤ 750 caracteres; serviços em lista, sem preço; feriado sem padrão vira `pergunta_sim_nao` (sem resposta até 24 h antes, horário normal fica, Diário registra); nada publica em `SUSPENDED`/`PENDING_VERIFICATION`; nunca cita outro perfil |
| Métricas | Aprovação sem edição (> 85% no P1); posts/semana; fila → publicação; feriados com ≥ 72 h (100%); completude do perfil |
| Teste de aceitação | Uma semana gera 1 post aprovado; feriado de teste vira horário + post 72 h antes com aviso ao dono; 100% das ações com print; nenhum campo sensível muda sem aprovação |

```
Você é o Editor da {casa}. Tom: {tom}. Nunca prometa resultado, posição ou desconto não autorizado. Nunca termos de busca no nome. Nunca invente preço, serviço ou horário: use só {fatos_da_casa} e {limites}.
Gere post ≤ 300 caracteres, foto entre as disponíveis (nunca gerar), justificativa em uma linha. Feriado a 72 h: horário pelo padrão da casa, post de aviso ≤ 200 caracteres, data de publicação.
requer_guardiao para categoria, nome, endereço ou feriado sem padrão.
JSON: {post, foto_uri, justificativa, horario_feriado, publicar_em, requer_guardiao:bool}
```

### Anfitrião

| | |
|---|---|
| Gatilho | Polling 30 min (avaliações e perguntas → `gbp.review.new`, `gbp.question.new`); lote noturno de classificação; dia 1 (Boletim de Reputação, classificação para Voz do Cliente); primeira semana após `gbp_linked` (QR); `approvals.decided` |
| Entradas | Avaliações (v4), perguntas (Q&A API), tom, fatos da casa do Dia 0, responsável e canal para quem reclamou, políticas do Google, `limites_json` |
| Ferramentas | `gbp.list_reviews` · `gbp.reply_review` · `gbp.list_questions` · `gbp.answer_question` · `gbp.get_review_link` · `render.qr` · `render.pdf` · `render.card` · `classify.review` · `guardiao.submit` · `diario.log` |
| Cérebro | Gemini Flash (classificar); linguagem (responder); Gemini (violação de política) |
| Saídas | Respostas no Google; `reviews` e `questions` atualizadas; Diário por resposta; Boletim de Reputação (card, dia 1); classificação do mês; sinal de suspeita; link curto oficial + QR em PDF |
| Guardrails | Nunca manda mensagem a cliente final; link oficial, sem encurtador próprio; responde todas, sem selecionar; notas 1 e 2 via Guardião em qualquer patamar; nunca dado do avaliador, compensação ou pedido de nota; texto de terceiros só como hash; dúvida vira `exige_humano`; chave por `review_id` |
| Métricas | Mediana de resposta (< 2 h; 100% em 24 h); perguntas < 4 h; avaliações/semana; nota; edição pelo Guardião; sinalizadas/mês |
| Teste de aceitação | Avaliação de teste respondida em < 2 h; pergunta "vocês têm estacionamento?" respondida em < 4 h com dado do perfil; QR abre a tela oficial; nenhuma mensagem a número que não seja o do dono |

```
Você responde avaliações e perguntas públicas em nome da {casa}. Agradeça sem chavão, responda ao ponto, nunca ofereça compensação, nunca exponha dados do avaliador, nunca discuta, nunca peça mudança de nota.
Nota ≤ 3: desculpa, explicação sem justificativa, convite a falar com {responsavel} pelo {canal}.
Pergunta: só com o perfil ou {fatos_da_casa}; se não souber, diga que a casa vai confirmar e marque exige_humano. ≤ 400 caracteres.
JSON: {resposta, tom_detectado, temas[], sentimento, suspeita_de_violacao:bool, exige_humano:bool}
```

### Tesoureiro

| | |
|---|---|
| Gatilho | A cada hora (visões); diário 03h (coleta D-3..D-1); dia 1 05h (Extrato, Horas Devolvidas, custo, JSON do mês); segunda 06h (JSON da semana); `cost.alert` acima de R$ 25 |
| Entradas | `metrics_daily`, `keywords_monthly`, `rank_measurements`, `reviews`, `questions`, `actions_log`, `llm_calls`, `hours_equivalence`, `deliveries` |
| Ferramentas | `gbp.get_daily_metrics` · `gbp.get_keywords` · `render.pdf` · `render.card` · `cost.per_tenant` · `diario.log` |
| Cérebro | Gemini Flash (normalizar Performance API); Gemini Pro só para as três frases. Números só de SQL |
| Saídas | Visões do dashboard (seis números com setas e data de referência); `metrics_daily`; Extrato de Demanda (PDF, série de 6 meses); Horas Devolvidas (card com equivalência no rodapé); custo por tenant e alerta; JSONs para o Redator-chefe |
| Guardrails | Nenhum número de modelo; reconciliação < 2%; sempre `data_referencia` e aviso de atraso de 2–3 dias; contato = 4 métricas, nada mais; custo por contato = R$ 499 ÷ contatos; nenhum campo de conversão, receita ou "novos clientes"; coleta idempotente por (tenant, data): substitui, nunca soma |
| Métricas | Frescor (próprio < 1 h; Google ≤ D-3); reconciliação; custo vs R$ 25; atraso da coleta; entregas do dia 1 na janela |
| Teste de aceitação | Extrato sintético bate com soma manual em 100%; padaria de exemplo (118 + 97 + 31 + 14) = 260 contatos e R$ 1,92; nenhuma visão sem `data_referencia` |

```
Três frases sobre este extrato, sem número fora do JSON, sem conversão, receita ou "novos clientes", sem promessa.
Chame toques em Ligar de "ligações pelo perfil". Destaque a maior variação e o custo por contato. Diga até que data vão os dados do Google.
```

### Redator-chefe

| | |
|---|---|
| Gatilho | Dia 0 (três frases); segunda 06h (Boletim; envio 07h); dia 1 06h (Voz do Cliente, Fechamento); trimestral; lembrete de pendência (estado pendente há 72 h, ≤ 1/semana/tenant) |
| Entradas | JSONs do Tesoureiro, Cartógrafo, Anfitrião, Editor; nome do dono e como quer ser chamado; tom; estados do tenant; `data_referencia` |
| Ferramentas | `tts.synthesize` · `render.card` · `render.pdf` · `delivery.send` · `diario.log` |
| Cérebro | Linguagem (roteiro, três frases, página); Gemini (verificação cruzada antes de sintetizar ou renderizar); Cloud TTS |
| Saídas | OGG ≤ 60 s + card (Boletim); PDFs (Diagnóstico, Fechamento mensal e trimestral); card Voz do Cliente; três frases do Dia 0; `aviso_radar` de pendência |
| Guardrails | Número fora dos dados bloqueia e abre item; ≤ 60 s com corte por palavras; Boletim só entre 7h e 8h; lembrete ≤ 1/semana e nunca após SAIR; nunca "novos clientes", conversão, receita, ROI; nunca outro perfil; nenhum texto sem `prompt_versao` |
| Métricas | Leitura/escuta (`read`); duração média; correções manuais; bloqueios da verificação; pendências resolvidas em 7 dias |
| Teste de aceitação | Boletim sintético passa na verificação e tem áudio ≤ 60 s com pronúncia correta; Diagnóstico sai em três frases só com números da medição; número plantado fora do JSON bloqueia |

```
Boletim de Segunda para {nome}, ≤ 150 palavras, falado, começa com "Bom dia, {nome}". Primeira frase: até que dia vão os dados do Google ({data_referencia}).
Estrutura: o que mudou; contatos (ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil); avaliações novas e respondidas; posição nos termos-chave; o que a máquina fez; o que vem. Só números do JSON. Sem "novos clientes", receita, outro perfil. Termine com uma ação da semana.
Diagnóstico: três frases: onde a casa está (termos e pontos verdes); o que falta no perfil (maior lacuna); o que a máquina faz primeiro. Sem promessa de posição.
```

### Guardião (humano com painel)

| | |
|---|---|
| Gatilho | Fila contínua; SLA 4 h úteis para P0/P1; amostragem diária de 10% no P2; texto livre do dono (`wa.inbound`); suspeita de avaliação; `cost.alert`; estado do perfil |
| Entradas | `approvals` no Firestore (item, contexto, sugestão, risco); prints e diffs; resposta proposta com nota e texto; estado do tenant e da zona; `qa_samples` |
| Ferramentas | Painel (Cloud Run + Identity Platform, 2FA): aprovar, editar, rejeitar em lote; visão por tenant e agente; incidente; denúncia pelo fluxo do Google; `qa_samples`; resposta humana ao dono |
| Cérebro | Nenhum. Gemini Flash só ordena a fila |
| Saídas | `approvals.decided`; edições devolvidas com motivo; feedback para a avaliação cega; incidentes; denúncias; `qa_samples` |
| Guardrails | ≤ 60 itens/hora por operador; categoria, nome, endereço e notas 1 e 2 com dois olhos em qualquer patamar; sem senha de cliente em tela; dono exibido por nome e hash |
| Métricas | Itens/hora; taxa de edição; tempo de fila; incidentes por 100 clientes; clientes por operador (30 → 80 → 150) |
| Teste de aceitação | 100 itens sintéticos em < 90 min por um operador; item de categoria só sai com duas aprovações; texto livre do dono aparece na fila em < 1 min |

```
Ordene estes itens por risco (categoria, nome, endereço e notas ≤ 2 primeiro; depois por prazo), agrupe parecidos do mesmo tenant.
JSON: {ordem:[item_id], grupos:[[item_id]]}. Não altere nenhum item.
```

## 6. Receitas

Chave de idempotência em todo job: `tenant_id + agente + entrega + período`. Toda entrega passa pelo Delivery; reenvio único após 2 h sem `delivered`. Todo dado do Google com data de referência.

### 01 Diagnóstico de Posição

1. `tenant.state.changed` → `gbp_linked` (ou `gbp_pending_verification` com `place_id` casado) enfileira `cartografo.measure(modo='reduzida')`: 3×3, até 5 termos-chave do Dia 0 normalizados pelo Gemini.
2. `places.search_text` por termo e ponto; grava `rank_measurements`.
3. Em paralelo `editor.audit_profile`: campos vazios ou fracos com peso; `profile_audits` com `origem='diagnostico'`.
4. `redator.diagnostico`: três frases; `crosscheck` bloqueia número fora da medição.
5. `render.card` (grade por termo, nota, três frases) e `render.pdf` (mapa reduzido, auditoria, método).
6. `delivery.send(tenant, 'diagnostico', [card, pdf])` na mesma conversa (janela aberta pelos áudios). Chave `tenant + diagnostico + dia0`.
7. Lacunas e termos vermelhos com impressões → `editor.tasks`.

Pronto: card e PDF em até 2 min após `gbp_linked`; três frases sem número fora da medição; nenhum outro perfil; `profile_audits` guarda o "antes".

### 02 Antes e Depois do Perfil

1. Scheduler diário 06h → `onboarding.day7` para tenants com `created` + 7 dias, independentemente de pendências.
2. `editor.profile_diff`: `profile_audits` do Dia 0 vs perfil de hoje (campos, descrição, horários, serviços, atributos, fotos, posts, respostas), com Diário e print; legenda de uma linha por diferença via linguagem.
3. `cartografo.measure(modo='reduzida')` com os mesmos termos e pontos do Dia 0.
4. `render.card` lado a lado (Dia 0 | Dia 7): pontos verdes, completude, nota, fotos, posts, respostas, ações.
5. `delivery.send` até 8h; arquivo no dashboard.
6. Pendência aberta termina o card como uma `pergunta_sim_nao`, e só ela.
7. Chave `tenant + onboarding + day7`.

Pronto: sai no Dia 7 até 8h sem depender de pendências; toda diferença existe em `profile_audits`, `actions_log` ou `rank_measurements`; mesma grade do Dia 0.

### 03 Dashboard Radar

1. Hourly → `tesoureiro.refresh_views`: 7 e 28 dias de `metrics_daily`, posição por termo, nota, perguntas, Diário, série de 6 meses.
2. Diário 03h → `tesoureiro.collect_gbp` D-3..D-1: `call_clicks`, `directions`, `website_clicks`, `conversations`, `impressions_search` (desktop + mobile), `impressions_maps` (desktop + mobile); `data_referencia` = último dia publicado; chave (tenant, data) substitui.
3. Dia 1 → `gbp.get_keywords` → `keywords_monthly` (contexto).
4. Seis números com setas vs 7 dias anteriores: ligações pelo perfil, rotas, cliques no site, mensagens, pontos verdes, nota · avaliações. Linha fixa: "Dados do Google até {data_referencia}. O Google publica com 2 a 3 dias de atraso. 'Ligações pelo perfil' são toques no botão Ligar contados pelo Google, não ligações atendidas."
5. Seções: números; Mapa interativo; Diário com prints; arquivos; série.
6. Acesso: link fixo com token; conta no Identity Platform; senha opcional; link mágico.
7. Abertura grava `deliveries.lido_em` (entrega `dashboard`).

Pronto: abre em < 2 s no celular; seis números com data de referência; nenhum campo de conversão; padaria de exemplo mostra 260 contatos e R$ 1,92.

### 04 Boletim de Segunda

1. Sábado 03h: medição reduzida dos termos-chave.
2. Segunda 06h: `tesoureiro.week_summary`: 4 métricas até a `data_referencia` (tipicamente quinta ou sexta anterior) vs semana anterior; avaliações novas e respondidas; posição de sábado; ações do Diário; o que vem (fila do Editor, feriados em 10 dias).
3. `redator.boletim` ≤ 150 palavras; `crosscheck`; corte por palavras.
4. `tts.synthesize` → OGG ≤ 60 s; `render.card` com cinco números, posição e data de referência.
5. 07h: `delivery.send(tenant, 'boletim', [audio, card])`: janela aberta → livres; fechada → `boletim_segunda` (MP4).
6. Chave `tenant + boletim + semana ISO`; se a janela 7h–8h passa: incidente + `aviso_radar` de atraso.

Pronto: áudio ≤ 60 s às 7h ± 5 min com card; nenhum número fora do JSON; primeira frase com a data; semana da padaria = 31 ligações pelo perfil, 22 rotas, 8 cliques, 3 avaliações respondidas, 1º em 7 de 9 pontos, 1 post, feriado ajustado.

### 05 Mapa de Domínio

1. Dia 1 02h: `cartografo.measure(modo='completa')`: grade 3×3 a 5×5, até 25 termos, `searchText` por termo e ponto.
2. Grava `rank_measurements`; nada de outros lugares.
3. `gemini.analyze_territory` (Pro, JSON): cores, variação mensal, oportunidades só com termos que têm impressões.
4. `render.map_svg`: grade sobre o raio, painel por termo, legenda, rodapé: "Busca por texto na Places API como proxy da lista local do Maps; validação mensal com 20 buscas manuais". PNG para WhatsApp, SVG no dashboard.
5. Termos vermelhos com impressões → `editor.tasks`; categoria → Guardião.
6. Envio até 8h por `entrega_radar`; edição reduzida no Dia 0 e Dia 7.
7. Validação mensal: 20 buscas manuais em `qa_samples`; < 85% abre incidente.
8. Chamadas = termos × pontos, teto em `limites_json`; grade cai antes dos termos.

Pronto: legenda, rodapé de método, concordância ≥ 85%; nenhum dado de outro perfil; nada além de `place_id` por mais de 30 dias; padaria = 7 de 9 verdes em "padaria perto de mim".

### 06 Diário de Bordo do Perfil

1. Segunda 04h: `editor.weekly_post`: foto real avaliada por `vision.assess_photo`, post ≤ 300 caracteres, Guardião ou publicação; chave `tenant + post + semana ISO`.
2. Diário 05h: `editor.hours_check` com `calendar.holidays(cidade, hoje, hoje + 10)`; feriado a 72 h: `gbp.update_hours` pelo padrão + post de aviso; sem padrão: `pergunta_sim_nao`; chave `tenant + feriado + data`.
3. `editor.tasks`: descrição, serviços (sem preço), atributos, categoria secundária via `gbp.patch_location` com diff em `profile_audits`; categoria principal, nome, endereço só via Guardião.
4. Fotos novas via `gbp.upload_media`, uma linha por foto.
5. Toda ação: `diario.log` com print da tela pública após publicar, `prompt_versao`, `modelo`, `custo`; verificação diária confere print em 100%.
6. Dia 1: `editor.audit_profile` (60 min nas Horas Devolvidas).
7. Dashboard lista `actions_log` com prints; `aviso_radar` (8h–19h) quando há ação relevante; resumo no Boletim.

Pronto: uma semana produz ≥ 1 post, 100% com print, feriado de teste tratado 72 h antes, nenhum campo sensível sem aprovação; a linha nasce antes de a ação contar.

### 07 Motor de Reputação

1. Primeira semana após `gbp_linked`: `gbp.get_review_link` → `render.qr` → `render.pdf(material_qr)` → `delivery.send`.
2. Polling 30 min: `gbp.list_reviews`, `gbp.list_questions` → eventos; texto só como hash.
3. Avaliação → `classify.review` → `anfitriao.reply_review`; notas 1 e 2 via Guardião em qualquer patamar; `gbp.reply_review`; Diário com print; `respondida_em`, `resposta_id`; chave por `review_id`; edição pelo autor reabre.
4. Pergunta → `anfitriao.answer_question` só com perfil e fatos da casa; dúvida = `exige_humano` (Guardião em 4 h); `gbp.answer_question`.
5. Violação → item no Guardião; denúncia por gente, no fluxo do Google.
6. Lote noturno: `anfitriao.classify_batch` (temas, sentimento).
7. Dia 1: `anfitriao.reputation_report`: nota, novas, respondidas, mediana, perguntas, temas elogiados e de atenção; até 8h; chave `tenant + reputacao + AAAA-MM`.

Pronto: mediana < 2 h e 100% em 24 h; pergunta < 4 h; QR abre a tela oficial; Boletim de Reputação no dia 1; nenhuma mensagem a não ser ao dono.

### 08 Extrato de Demanda

1. Dia 1 05h: SQL do mês até a `data_referencia`: contatos = 4 métricas; impressões e palavras-chave como contexto; nota e avaliações; verdes ÷ medidos; custo por contato = R$ 499 ÷ contatos.
2. Dias não publicados entram na coleta seguinte (linha substituída); PDF diz "dados até {data_referencia}".
3. Série de 6 meses com setas; explica uma vez o que é "ligações pelo perfil".
4. Três frases (Gemini Pro) validadas contra o JSON; sem conversão, receita ou "novos clientes".
5. `render.pdf` (uma página, URL assinada 30 dias, cópia no dashboard); `delivery.send` até 8h.
6. Chave `tenant + extrato + AAAA-MM`.

Pronto: 100% dos números de SQL; template sem campo de conversão; padaria 260 e R$ 1,92; oficina 168 e R$ 2,97; clínica 160 e R$ 3,12; PDF com data de referência.

### 09 Horas Devolvidas

1. `hours_equivalence` (rodapé do card): post 20 · foto 10 · resposta a avaliação 6 · resposta a pergunta 4 · ajuste de campo/horário 10 · medição 0,5 por termo-ponto · auditoria mensal 60 · Boletim 30 · extrato/PDF 45 · Mapa de Domínio 60.
2. Dia 1 05h: SQL soma `actions_log` do mês (uma vez por chave, só com `print_uri` ou `saida_uri`) × minutos, por tipo.
3. Tempo do dono = minutos entre cada `pergunta_sim_nao` e a resposta (`deliveries`, `wa.inbound`), arredondados para cima.
4. `render.card`: total, detalhamento, tempo do dono, tabela no rodapé.
5. `delivery.send` até 8h; chave `tenant + horas + AAAA-MM`.

Pronto: reconcilia com `actions_log` linha a linha; clínica de exemplo = 14h07 e 2 min do dono ("catorze horas por R$ 499").

### 10 Voz do Cliente

1. Lote noturno: `classify_batch` (lista fechada de temas por segmento + emergentes; sentimento); só avaliações e perguntas públicas.
2. Dia 1 06h: `redator.voz_do_cliente`: top 3 elogios e top 3 atritos por frequência com variação, uma frase real anonimizada cada; Gemini valida frequências.
3. Atrito resolvível no perfil → `editor.tasks` no mesmo dia + linha "corrigi: {o que}" no card; atrito de operação fica com o dono.
4. Tema de atenção acima do limiar (`limites_json`, padrão 3 menções em 7 dias) → `aviso_radar`, ≤ 1/semana.
5. `render.card` com 6 itens; `delivery.send` até 8h; chave `tenant + voz + AAAA-MM`.

Pronto: 6 itens com frequência e evidência anonimizada; sem identificação de autor; atrito resolvível vira tarefa no mesmo dia.

### 11 Fechamento Executivo

1. Dia 1 06h, após Cartógrafo → Editor → Tesoureiro → Anfitrião: `tesoureiro.month_summary`: cinco números com variação (contatos, custo por contato, nota · avaliações, pontos verdes, impressões como contexto), extrato em três linhas, horas devolvidas, mapa em miniatura, ações por tipo, o que vem.
2. `redator.fechamento`; `crosscheck`.
3. `render.pdf` (uma página, data de referência); URL assinada 30 dias; arquivo permanente.
4. `delivery.send` até 8h; o dono encaminha a quem quiser.
5. Trimestral (a cada 3 meses desde o Dia 0): série de contatos, custo por contato, verdes, nota.
6. Chave `tenant + fechamento + AAAA-MM` (e `+ trimestre`).

Pronto: PDF até 8h; nenhum número fora do JSON; trimestral com a curva desde o Dia 0; oficina de exemplo = 168 contatos, R$ 2,97, 4,8 · 214, 7 de 9 verdes.

## 7. Onboarding técnico

| Toque | Máquina | Estado |
|---|---|---|
| Comercial verifica a zona | `zone.check(segmento, zona)` em transação sobre `zones`: `tenants_ativos < 2` → "disponível"; senão "lotada" + lista de espera. Conversa não reserva; a proposta escrita reserva por 5 dias úteis | Nenhum (só reserva em `zones`) |
| Assina o contrato (link; marca número e aceite) | Cria `tenants/{id}` com `segmento`, `zona`, `termos[]`, `limites_json` do mandato; ocupa a vaga (`tenants_ativos` + 1, `zone.changed`); prefixo no bucket, segredos, permissões. Reserva expirada → novo `zone.check` | `created` |
| Cadastra o cartão | Webhook do provedor grava a assinatura; atraso não segura o Dia 0 | `billing_active` |
| Abre a conversa pelo link e responde 5 perguntas por áudio | Primeira mensagem abre a janela de 24 h (sem ela em 1 h: `pergunta_sim_nao` "Podemos começar?"). Gemini transcreve → `termos[]`, `raio_m`, `tom_json`, `limites_json`, `dono_nome`, `dono_wa_hash`. Confirmação por escrito + `pergunta_sim_nao`; o Sim é o opt-in (data, hora, texto) no tenant e no Diário | `profiled` |
| Adiciona a conta operacional como Gerente | `gbp.discover`: lista locais, casa por nome e endereço, grava `locations`, lê o estado; na sequência medição reduzida, auditoria, três frases, PDF: Diagnóstico em minutos. `PENDING_VERIFICATION` → passo a passo pelo WhatsApp, o resto não espera | `gbp_linked` ou `gbp_pending_verification` |
| Abre o link do dashboard | Token emitido; `lido_em`; senha opcional (nunca passa por nós) | `live` |
| Nenhum toque: Dia 7 (`created` + 7) | `onboarding.day7`: diff + segunda medição; card e arquivo | `live` (entrega 02 em `deliveries`) |

Regras:

1. Zona antes de tudo: `MAX_TENANTS_PER_ZONE_SEGMENT=2`, `limite=2` em `zones`, `zone.check` transacional (conta e reserva juntos). Segmento = categoria principal do perfil; zona = bairro do Google Maps ou raio equivalente, escrita no contrato com cidade e segmento. Fila por ordem de chegada; ninguém fura. Cliente que muda de endereço ou categoria para zona lotada mantém a operação até o fim do ciclo pago e entra na fila da zona nova; a vaga antiga libera na mudança confirmada. Redesenho de zona não expulsa quem está.
2. Nada bloqueia nada: cada sistema é um estado independente. Perfil pendente não impede dashboard, medição (usa o `place_id` público) nem fila do Editor (publica em `gbp_linked`). Anfitrião e Tesoureiro esperam o vínculo. Único pré-requisito: a zona.
3. Dia 7 é automático: 7 dias após `created`, roda mesmo com pendências; chave `tenant + onboarding + day7`.
4. Pendências viram uma pergunta: estado pendente por 72 h → `aviso_radar` com link do passo, ≤ 1/semana, em horário comercial, nunca pede senha ou código; aparece para o comercial no painel; persistindo, vira exceção do Guardião. SAIR interrompe também os lembretes.

## 8. Operação

| Quando (Brasília) | Job | Agente |
|---|---|---|
| Contínuo | Webhooks do número da casa (respostas, status) | Delivery / Guardião |
| A cada 30 min | Polling de avaliações e perguntas; respostas | Anfitrião |
| A cada hora | Visões do dashboard | Tesoureiro |
| Diário 03h | Coleta Performance API (D-3..D-1) | Tesoureiro |
| Diário 05h | Horários e feriados (72 h antes) | Editor |
| Segunda 04h / 06h / 07h | Post / Boletim gerado / Boletim enviado | Editor / Redator-chefe |
| Sábado 03h | Medição reduzida dos termos-chave | Cartógrafo |
| Dia 1, 02h → 08h | Medição completa → auditoria → extratos → cards → PDFs → envios em sequência (Cartógrafo, Editor, Tesoureiro, Anfitrião, Redator-chefe) | Todos |
| Dia 7 do tenant | Antes e Depois | Editor + Cartógrafo |
| Trimestral, dia 1 | Fechamento Trimestral | Redator-chefe |
| Madrugada (fora da tabela) | Lote de classificação | Anfitrião |

Papéis: Head de Operação (1 desde o P0; SLA, runbooks, avaliação cega, tabela de zonas) · Engenheiro de automação (1) · Operadores/Guardiões (30 → 80 → 150 clientes por operador) · Comercial/SDR (zona, contrato, onboarding assistido) · Jurídico externo (sob demanda, revisão trimestral).

Runbooks (todo runbook termina com linha no Diário e uma frase ao cliente; o que não está aqui é incidente do Head):

1. Perfil suspenso ou pendente: incidente; Editor congelado; Anfitrião lê e não responde; apelação pelo fluxo do Google com passo a passo ao dono; auditoria de conformidade em 100% dos tenants em 48 h; dashboard segue com data de referência.
2. Cota ou erro de API do Google: retry exponencial por tenant; dashboard mostra a última data boa; medições retomam pela chave; Mapa sai com a data real; > 24 h avisa cliente; nunca raspagem.
3. Custo por tenant > R$ 25: `cost.alert`; diagnóstico por `llm_calls`; reduzir grade e termos, renovar cache, mover volume para Flash, procurar loop; revisar em 48 h.
4. Modelo fora do ar: linguagem usa `LLM_LANGUAGE_FALLBACK`; tarefas Gemini esperam na fila (alerta > 2 h); Boletim sem verificação não sai, sai `aviso_radar` de atraso.
5. Número da casa com qualidade baixa: ler `quality_rating` e SAIRs; pausar tudo que não é Boletim; revisar modelos e frequência; contestação na Meta se bloqueado; número reserva só com o Head após corrigir a causa.
6. Zona lotada com pedido: não vende, não cria tenant provisório; lista de espera com data; zona vizinha só se o dono quiser; `zone.changed` avisa o primeiro da fila; zona não se redefine para caber mais um.
7. Offboarding: remove Gerente; desliga cadência; exporta histórico (ZIP: PDFs, Diário, prints, fotos, CSV); apaga no prazo (exceto `actions_log` e prints); encerra segredos; opt-out; libera a vaga (`zone.changed`).

Custo de tecnologia por cliente:

| Item | Base | R$/cliente/mês |
|---|---|---|
| Gemini (Flash em volume, Pro na análise) | ~100k in, 30k out, cache | 3–5 |
| Cérebro de linguagem | ~40k in, 10k out | 2–4 |
| Places API (New) | 1 completa + 4 reduzidas, máscara só `id` | 3–8 |
| WhatsApp da casa | ≈ 25 mensagens de utilidade | 1–2 |
| TTS, Cloud Run, BigQuery, Storage | rateio | 3–6 |
| Total | alerta em R$ 25 | ≈ 12–25 |

SLOs: entregas na janela ≥ 99% (`deliveries`) · avaliações: mediana < 2 h, 100% em 24 h (`reviews`) · perguntas < 4 h (`questions`) · frescor: próprio < 1 h, Google ≤ D-3 com data de referência · Diário 100% com print (verificação diária cruza `actions_log` com a API) · Dia 0 ≤ 15 min cronometrados.

## 9. LGPD técnico

1. Nenhuma senha de cliente: acesso só por papel Gerente com token OAuth da nossa conta; código de verificação nunca passa por nós; senha do dashboard criada pelo cliente e guardada como hash; nenhuma tabela, segredo ou log tem campo para credencial de cliente.
2. Segredos no Secret Manager; da casa fora de qualquer tenant; um por tenant para revogar sem tocar nos outros; acesso por conta de serviço do conector; rotação 90 dias; revogação automática no offboarding; auditoria de acesso ativa.
3. Dados pessoais: dono = nome e número (`dono_wa_hash` nas tabelas; claro só no Firestore, lido só pelo Delivery); terceiros = textos públicos tratados só para responder, guardados como hash, temas e sentimento; nome do avaliador nunca em tabela, só o primeiro nome no prompt quando a resposta pede; anonimização antes do `LLMGateway`; nenhum canal com cliente final.
4. Zona em código: `zones` com `limite=2`, `MAX_TENANTS_PER_ZONE_SEGMENT=2`, `zone.check` transacional; `segmento` e `zona` do tenant não mudam sem Guardião; auditoria diária: `tenants` agrupado por segmento e zona com > 2 ativos deve devolver zero linhas.
5. Número da casa: opt-in com data, hora, texto e hash no tenant e em `actions_log`; só os modelos de utilidade; SAIR em qualquer grafia marca opt-out na mesma transação, Delivery recusa, volta exige novo Sim; texto livre vai a humano.
6. Retenção por ciclo de vida: `actions_log` e prints 5 anos · `llm_calls` 12 meses · `metrics_daily`, `keywords_monthly`, `rank_measurements`, `reviews`, `questions`, PDFs, cards e áudios de entregas: contrato + 90 dias · Places: nada além de 30 dias (só `place_id`; a posição do próprio cliente é medição própria) · áudio do Dia 0 apagado 7 dias após a confirmação por escrito (fica a transcrição).
7. Direitos do titular: endpoint interno `dsr(tenant, hash)` localiza, exporta ou apaga em até 15 dias (dono; avaliador ou autor de pergunta, com remoção da resposta pública via API); pedido vira linha no Diário.
8. Suboperadores em página pública versionada: Google Cloud e APIs, Meta (só número da casa), provedor do cérebro de linguagem, provedor de pagamento.
9. Cloud Audit Logs nos dois projetos; painel com identidade nominal e 2FA; toda aprovação com autor; logs exportados com retenção travada; `actions_log` append-only por permissão de tabela.

A auditoria da semana 6 roda os nove itens e guarda o resultado com o Diário.

## 10. Plano de seis semanas

Equipe: um engenheiro sênior e o Head de Operação; jurídico na semana 6. Caminho crítico: acesso às Business Profile APIs (1–2 semanas) e verificação da empresa na Meta; os dois começam no dia 1.

| Semana | Entrega | Prova |
|---|---|---|
| 1 | Projetos `radar-hml`/`radar-prd`, Terraform, GitHub → Cloud Build, BigQuery e Firestore com o modelo (inclusive `zones`), Secret Manager, Identity Platform, Logging. Conta operacional com 2FA. Chave restrita da Places. Dia 1: formulário das Business Profile APIs; verificação na Meta, app, número da casa, modelos submetidos | `terraform apply` sobe os dois ambientes do zero; job vazio no Scheduler escreve linha em `actions_log` |
| 2 | GBP Connector (contratos e respostas gravadas até a aprovação), Places Connector com grade e limites, `LLMGateway` com Gemini + linguagem, `diario.log` com print, `llm_calls` e `cost.per_tenant` | Busca por termo e ponto devolve a posição do `place_id` de teste; edição de horário gera diff e print no Diário |
| 3 | Cartógrafo (reduzida e completa), Mapa SVG, coleta do Performance API, visões horárias, dashboard com link e senha opcional, Diagnóstico de ponta a ponta (auditoria de completude, três frases, PDF) | 20 buscas manuais ≥ 85%; dashboard abre no celular com números e data de referência |
| 4 | Editor (posts, fotos, descrição, feriados 72 h, serviços, atributos, categoria via Guardião), Anfitrião (polling 30 min, respostas, classificação, suspeita, QR), Guardião em planilha → painel, `onboarding.day7` | Tenant interno de ponta a ponta: uma semana com post aprovado, feriado ajustado, avaliação respondida, tudo com print |
| 5 | Redator-chefe + TTS + verificação cruzada; Delivery pelo número da casa com os modelos, status e reenvio; webhooks (Sim, Não, SAIR, transbordo); Extrato, Horas Devolvidas, Voz do Cliente, Fechamento; onboarding automático; `zone.check` e lista de espera | Boletim sintético às 7h no celular do Head; Dia 0 completo cronometrado; terceira empresa do mesmo segmento na zona é recusada |
| 6 | Runbooks, SLOs e alertas, offboarding com liberação de vaga, revisão LGPD e políticas com o jurídico, custo com alerta em R$ 25. Piloto com 3 clientes (padaria, oficina, clínica) por 30 dias, Guardião em P0 | Três Dias 0 em ≤ 15 min; primeiro Boletim real na segunda às 7h |

Definição de "montei":

1. Os 11 testes de aceitação passam (homologação com dados sintéticos; produção com o tenant interno).
2. Dia 0 em até 15 minutos cronometrados com três pessoas que nunca viram o produto.
3. Piloto fecha um mês com as 11 entregas no calendário, Diário completo e custo por tenant < R$ 25.
4. Ninguém tem senha de ninguém: zero credenciais de cliente armazenadas.
5. Nenhuma zona com mais de 2 tenants do mesmo segmento; `zone.check` recusa a terceira em teste.

## 11. Apêndice

Variáveis e segredos (por ambiente):

```
GCP_PROJECT, GCP_REGION=southamerica-east1
GEMINI_MODEL_PRO=gemini-2.5-pro  GEMINI_MODEL_FLASH=gemini-2.5-flash   (ou a geração vigente)
LLM_LANGUAGE_PRIMARY=claude-sonnet|gemini-2.5-pro   LLM_LANGUAGE_FALLBACK=gemini-2.5-pro
PLACES_API_KEY (restrita)   GBP_OAUTH_CLIENT_ID / SECRET   GBP_OPERATOR_REFRESH_TOKEN
META_APP_ID / META_APP_SECRET / META_SYSTEM_USER_TOKEN   WA_WEBHOOK_VERIFY_TOKEN   DELIVERY_SENDER_PHONE_ID
TTS_VOICE_ID (Chirp 3 HD pt-BR)
GUARDIAO_BASE_URL   DASHBOARD_BASE_URL
COST_ALERT_PER_TENANT_BRL=25   MAX_TENANTS_PER_ZONE_SEGMENT=2
```

Tópicos Pub/Sub:

```
wa.inbound            webhook messages           -> Delivery (Sim/Não), onboarding (áudios), opt-out (SAIR), Guardião (texto livre)
wa.status             webhook statuses           -> Delivery (reenvio 2 h); deliveries
gbp.review.new        polling do Anfitrião       -> Anfitrião; Guardião (notas 1 e 2)
gbp.question.new      polling do Anfitrião       -> Anfitrião
editor.tasks          Cartógrafo; Voz do Cliente -> Editor
approvals.decided     painel do Guardião         -> Editor, Anfitrião
deliveries.send       todos, via delivery.send   -> Delivery
tenant.state.changed  onboarding, offboarding    -> cadências, dashboard, painel
cost.alert            Tesoureiro                 -> Head; painel
zone.changed          zone.check, criação, offboarding -> painel do comercial; lista de espera
```

Ferramentas ADK:

```
gbp.get_location(tenant) · gbp.patch_location(tenant, campos) · gbp.update_hours(tenant, horarios) · gbp.create_post(tenant, texto, foto_uri)
gbp.upload_media(tenant, uri) · gbp.list_reviews(tenant, desde) · gbp.reply_review(tenant, review_id, texto)
gbp.list_questions(tenant, desde) · gbp.answer_question(tenant, question_id, texto) · gbp.get_review_link(tenant)
gbp.get_daily_metrics(tenant, de, ate) · gbp.get_keywords(tenant, mes) · gbp.update_services(tenant, itens)
places.search_text(termo, lat, lng, raio)
wa.send_template(tenant, nome, params) · wa.send_media(tenant, uri, tipo) · wa.send_interactive(tenant, pergunta, botoes)
tts.synthesize(texto, voice_id) · render.card(template, dados) · render.pdf(template, dados) · render.map_svg(tenant, mes) · render.qr(tenant)
guardiao.submit(tenant, item, risco) · diario.log(tenant, agente, entrega, acao, alvo, entrada, saida, print) · delivery.send(tenant, entrega, artefatos)
cost.per_tenant(tenant, periodo) · vision.assess_photo(uri) · classify.review(texto) · zone.check(segmento, zona) · calendar.holidays(cidade, de, ate)
```

Quem chama: `gbp.*` de perfil, posts e mídia → Editor (Cartógrafo só lê) · `gbp.*` de avaliações, perguntas e link → Anfitrião · `gbp.get_daily_metrics`, `gbp.get_keywords` → Tesoureiro (Cartógrafo lê palavras-chave) · `places.search_text` → Cartógrafo · `wa.*` → Delivery e onboarding (destinatário sai do tenant, nunca do parâmetro) · `tts.*`, `render.*` → Redator-chefe, Cartógrafo, Tesoureiro, Anfitrião · `guardiao.submit`, `diario.log`, `delivery.send` → todos · `zone.check` → comercial e onboarding · `calendar.holidays`, `vision.assess_photo` → Editor · `classify.review` → Anfitrião · `cost.per_tenant` → Tesoureiro.

Contas que precisam existir antes da semana 2:

1. Google Cloud: organização, faturamento, `radar-hml` e `radar-prd`, APIs habilitadas (lista da seção 4).
2. Conta operacional Google: Gerente nos perfis dos clientes; 2FA; usada só pelo GBP Connector; assina o formulário das Business Profile APIs; é o nome que o cliente vê na lista de usuários do perfil.
3. Meta, só para o número da casa: portfólio verificado; app com WhatsApp; número dedicado na Cloud API com nome "Radar Urbano"; usuário de sistema com token; modelos `boletim_segunda`, `entrega_radar`, `entrega_radar_pdf`, `pergunta_sim_nao`, `aviso_radar` aprovados; webhook com `WA_WEBHOOK_VERIFY_TOKEN`. Nenhum cadastro em nome de cliente.
4. Provedor de pagamento: assinatura recorrente R$ 499/mês, webhook de status (vira `billing_active`), nota fiscal integrada, cancelamento pelo próprio cliente.
