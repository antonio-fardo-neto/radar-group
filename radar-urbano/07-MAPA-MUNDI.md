# Radar Urbano · 07-MAPA-MUNDI

Manual de montagem da máquina. Régua: BRIEF (seções 6–9 e 15). Nomes de tabelas, tópicos, ferramentas e variáveis são os mesmos no código, no Diário de Bordo e aqui.

## 1. Arquitetura

Cinco agentes em fila por tenant, cadência fixa, memória única, quatro conectores e um serviço de entrega. Sem tempo real; sem conversa com cliente final. O que entra vem do Google com data de referência; o que sai vai para o dono.

Cinco camadas:

1. Interfaces: Perfil da Empresa no Google (Busca e Maps), Places API (New), WhatsApp do dono (número da casa), Dashboard Radar. Nenhuma outra.
2. Conectores: GBP, Places, WA, TTS; ao lado, Render & Delivery (cards, mapa, PDFs, QR, dashboard, envio com status). Conector executa, registra custo, devolve JSON; nunca decide.
3. Agentes, orquestrador e Guardião: Cartógrafo, Editor, Anfitrião, Tesoureiro, Redator-chefe. Cloud Scheduler → Pub/Sub → Cloud Run Jobs; Cloud Tasks por tenant. Guardião: humano com painel.
4. Cérebros: Gemini na Vertex AI (obrigatório para dado, medição, aferição, áudio, foto e decisão que toca o Google); linguagem intercambiável atrás do `LLMGateway`; Cloud TTS. Nenhum agente chama modelo direto.
5. Memória e prova: Firestore (estado por tenant), BigQuery (métricas, medições, Diário, custo, zonas), Cloud Storage (fotos, prints, PDFs, áudios), Secret Manager (nunca senha de cliente).

Sete regras:

1. Camadas estritas: cada camada fala só com a de baixo; trocar modelo, voz ou template não toca agente; trocar endpoint toca só o conector.
2. Gemini é o cérebro de dados e de Google: extração, aferição, classificação e toda decisão sobre API ou superfície do Google, com saída estruturada e Grounding com Google Maps quando cabe.
3. Um cliente é um tenant com zona: todo dado carrega `tenant_id`; o tenant só nasce se `zone.check` confirmar vaga (máximo 2 por segmento por zona, em transação).
4. Tudo é job idempotente: chave `tenant_id + agente + entrega + período`, verificada antes da ação externa e gravada com ela.
5. Humano aprova, IA executa: P0 tudo antes; P1 lote (meta > 85% sem edição); P2 direto com QA de 10%; categoria principal, nome, endereço e notas 1 e 2 sempre com dois olhos.
6. Diário de Bordo é a verdade: toda ação externa grava linha imutável em `actions_log` com print; sem linha, não aconteceu.
7. Custo por cliente é métrica de primeira classe: alerta em R$ 25/cliente/mês.

## 2. Cérebros

| Função | Modelo | Como |
|---|---|---|
| Extração e normalização (perfil, métricas, avaliações, perguntas, palavras-chave) | Gemini Flash (volume) · Pro (análise mensal) | `generateContent` + `responseSchema` |
| Aferição de posição e leitura de superfícies Google | Gemini + Grounding com Google Maps | Medição é `places.search_text`; o Gemini interpreta e propõe termos |
| Decisões que tocam API do Google (campo, categoria, o que otimizar) | Gemini Pro | Function calling com ferramentas do GBP |
| Transcrição dos áudios do Dia 0 | Gemini multimodal | Áudio OGG + `responseSchema`: termos, raio, tom, limites, nome |
| Classificação de avaliações e perguntas | Gemini Flash | Polling 30 min; lote noturno; cache de contexto |
| Julgar fotos | Gemini multimodal | `vision.assess_photo`; nunca gera foto |
| Posts, respostas, roteiros, três frases | Linguagem (Claude Sonnet ou Gemini Pro) | `LLMGateway.generate`; avaliação cega mensal |
| Verificação cruzada de números | Gemini Flash | `CROSSCHECK` → `{ok, numeros_fora[]}`; bloqueia a síntese |
| Voz do Boletim | Cloud TTS Chirp 3 HD pt-BR | `TTS_VOICE_ID` fixo |
| Ordenar a fila do Guardião | Gemini Flash | Agrupa e ordena; não aprova |

```
LLMGateway
  generate(task, tenant, input, schema?) -> Output
  policy(task) -> {primary, fallback[], max_cost}
  Gemini obrigatório, sem fallback (fora do ar = espera na fila):
    EXTRACT, MEASURE, CLASSIFY, GOOGLE_DECISION, AUDIO_IN, VISION, CROSSCHECK
  linguagem (LLM_LANGUAGE_PRIMARY / LLM_LANGUAGE_FALLBACK):
    POST, REPLY_REVIEW, REPLY_QUESTION, BOLETIM, THREE_SENTENCES
  anonimiza antes da chamada (dono, avaliador -> ids internos), salvo tarefa que exige
  telemetria: tokens, custo, latência, prompt_versao, tenant -> llm_calls
```

Regras: (1) saída estruturada sempre; sem JSON válido, retry com temperatura menor e, na terceira falha, exceção no Guardião; (2) prompts versionados no repositório, versão em `actions_log` e `llm_calls`; (3) avaliação cega mensal: 100 amostras por agente, dois humanos, sem saber o modelo; tarefas Gemini só entram na auditoria; (4) cache de contexto renovado a cada 24 h, custo em `llm_calls`; (5) nenhum dado pessoal no prompt sem necessidade; o modelo nunca vê número da casa nem token.

## 3. Conectores

### GBP Connector

| | |
|---|---|
| APIs | Business Information v1: `accounts.locations.list`, `locations.get` (`readMask`), `locations.patch` (`updateMask`, `validateOnly`), `getAttributes`/`updateAttributes`, `attributes.list`, `categories.list`; campos `regularHours`, `specialHours`, `profile.description`, `serviceItems`, `categories`, `metadata.newReviewUri`, `metadata.mapsUri` · Performance v1: `fetchMultiDailyMetricsTimeSeries` (`CALL_CLICKS`, `BUSINESS_DIRECTION_REQUESTS`, `WEBSITE_CLICKS`, `BUSINESS_CONVERSATIONS`, `BUSINESS_IMPRESSIONS_{DESKTOP,MOBILE}_{SEARCH,MAPS}`), `searchkeywords/impressions/monthly` · v4: `reviews.list/reply`, `localPosts.create`, `media.create` · Q&A: `questions.list`, `questions.answers.upsert` · `locations.admins.list` · `getVoiceOfMerchantState` |
| Acesso | Formulário oficial das Business Profile APIs (1–2 semanas; dia 1 da semana 1). OAuth 2.0 com a conta operacional (2FA), Gerente em cada perfil, escopo `business.manage`; `GBP_OPERATOR_REFRESH_TOKEN`; `tenant-{id}-gbp-oauth` aponta por padrão para o token da casa. Gerente removido = `locations.status` marcado, incidente |
| Cotas | Baixas para edição; pedir aumento com o acesso. Desempenho em lote 03h (D-3..D-1); edições por Cloud Tasks, uma por tenant, retry em 429/5xx; polling 30 min, `pageSize` 50. Palavras-chave abaixo do limiar chegam como faixa |
| Termos | Nome real sem termo de busca; categoria descreve o negócio; horários e fotos reais; posts sem promessa; avaliações sem incentivo, seleção ou dado do avaliador; suspeita denunciada pelo fluxo oficial |
| Armadilhas | Categoria principal só com humano; `patch` sem `updateMask` apaga o resto (conector recusa); detectar `SUSPENDED`/`PENDING_VERIFICATION`; `hasGoogleUpdated` = revisar antes de sobrescrever; nota chega como enum `ONE..FIVE`; foto e post exigem URL assinada curta; v4 pode migrar; descrição ≤ 750 caracteres |

### Places Connector

| | |
|---|---|
| Endpoints | `places:searchText` com `textQuery`, `locationBias` circular no ponto (raio = passo), `rankPreference` padrão, `languageCode=pt-BR`, `regionCode=BR`, `pageSize=20`, máscara `places.id` · `places/{place_id}` só no Dia 0 |
| Acesso | Chave restrita à API e ao IP de saída (Cloud NAT); `PLACES_API_KEY`; ativa na hora; nunca no navegador |
| Cotas | Uma chamada por termo por ponto; grade 3×3 a 5×5; ≤ 25 termos; ≈ 240 chamadas/tenant/mês; teto em `limites_json`; R$ 3–8 |
| Termos | Sem extração em massa; nada além de 30 dias exceto `place_id`. Guardamos só `place_id` do cliente, data, termo, ponto, lat/lng, posição |
| Método | Centro no endereço; passo = raio (3×3) ou raio ÷ 2 (5×5); posição = índice do `place_id` (1–20) ou "não encontrado". Verde top 3, cinza 4º–10º, vermelho fora do top 10. Mesmo horário sempre. Validação mensal: 20 buscas manuais, ≥ 85% no top 3, em `qa_samples` |
| Armadilhas | `locationBias` é viés, não cerca; `rankPreference=DISTANCE` mede outra coisa; sem `languageCode`/`regionCode` a lista muda; não paginar além de 20; `place_id` pode mudar em fusão (reconfirmar por `metadata.mapsUri`); alerta de orçamento contra chave vazada |

### WA Connector (número da casa)

| | |
|---|---|
| Endpoints | `POST /{phone_number_id}/messages` (`template`, `audio`, `image`, `document`, `interactive`) · `POST /{phone_number_id}/media` · `GET /{media_id}` · webhooks `messages` e `statuses` (`sent`, `delivered`, `read`, `failed`) · `/{waba_id}/message_templates` · `/{waba_id}/phone_numbers` (`quality_rating`) |
| Acesso | Portfólio do Radar Urbano verificado (dia 1); app com WhatsApp; número dedicado "Radar Urbano"; usuário de sistema → `META_SYSTEM_USER_TOKEN`; `META_APP_ID/SECRET`; `WA_WEBHOOK_VERIFY_TOKEN`; `DELIVERY_SENDER_PHONE_ID`. Sem Tech Provider, sem Embedded Signup, sem conta do cliente |
| Modelos (Utilidade; rodapé "Responda SAIR para parar") | `boletim_segunda`: cabeçalho de vídeo (card + voz em MP4), números e data de referência, botão do dashboard; só com a janela de 24 h fechada · `entrega_radar`: cabeçalho de imagem · `entrega_radar_pdf`: cabeçalho de documento (nome lógico `entrega_radar` no código) · `pergunta_sim_nao`: botões · `aviso_radar`: {{1}} nome, {{2}} linha |
| Janela | Mensagem livre só na janela de 24 h aberta pelo dono (toque em botão conta). Dia 0: o dono abre pelo link da página do contrato; sem mensagem em 1 h, sai `pergunta_sim_nao` ("Podemos começar?"). Segunda: janela aberta → PNG + OGG livres; fechada → `boletim_segunda`. Delivery registra o caminho |
| Horários | ≈ 25 mensagens/dono/mês. Boletim 7h; dia 1 e Dia 7 até 8h; `aviso_radar` e perguntas 8h–19h. R$ 1–2 |
| Armadilhas | Modelo com cara de marketing = rejeição; `quality_rating` cai com bloqueios (SAIR honrado na hora em `wa_optout`); nunca celular de alguém; `audio/ogg` Opus, PNG ≤ 5 MB, MP4 ≤ 16 MB; número do dono só como hash nas tabelas; texto livre vai a humano; token rotacionado a cada 90 dias |

### TTS + Render & Delivery

| | |
|---|---|
| TTS | Chirp 3 HD pt-BR, `TTS_VOICE_ID` fixo; `OGG_OPUS` 48 kHz; ≤ 60 s (corte por ≤ 150 palavras; conector mede e recusa); números por extenso; custo em `llm_calls` (`task=TTS`); card + OGG viram MP4 para o modelo |
| Cards e mapa | HTML → PNG (Chrome headless), templates versionados; Mapa em SVG de `rank_measurements` (`render.map_svg`), PNG no WhatsApp, SVG no dashboard; todo card traz cliente, período, data de referência |
| PDFs | Uma página: Diagnóstico, Extrato, Fechamento, material do QR. `radar-{amb}-artefatos/{tenant_id}/{entrega}/{periodo}.pdf`; URL assinada 30 dias; cópia no dashboard |
| QR | `gbp.get_review_link` (`metadata.newReviewUri`) → `render.qr` → PDF de balcão e comanda, frase neutra; sem prêmio; único pedido de avaliação do produto |
| Dashboard | Next.js no Cloud Run; link fixo `DASHBOARD_BASE_URL/t/{token}`; senha opcional criada pelo cliente (Identity Platform; link mágico = sem senha; link único = criar/redefinir); visões de hora em hora; seções: números, Mapa, Diário com prints, Voz do Cliente, Reputação, arquivos, Horas, custo por contato; abertura grava `lido_em` |
| Delivery | Recebe (tenant, entrega, período, artefatos); decide janela × modelo; sobe mídia; envia; grava `enviado_em`, `entregue_em`, `lido_em`; linha no Diário; chave `tenant + entrega + período`; reenvio único após 2 h, depois incidente; respeita `wa_optout` e horários; fila `deliveries.send` |

## 4. Fundação

| Peça | Escolha |
|---|---|
| Projetos | `radar-hml`, `radar-prd`, `southamerica-east1` |
| APIs | Vertex AI, Places API (New), Business Profile APIs, Cloud TTS, Cloud Run, Cloud Build, BigQuery, Firestore, Secret Manager, Scheduler, Pub/Sub, Identity Toolkit. Sem Google Ads API |
| Execução | Cloud Run (webhooks, dashboard, painel, render); Cloud Run Jobs (um container por agente) |
| Agentes | ADK em Python; ferramentas dos conectores; opção Vertex AI Agent Engine |
| Orquestração | Scheduler → Pub/Sub → Jobs; Cloud Tasks por tenant |
| Estado | Firestore, documento por tenant |
| Analítico | BigQuery particionado por data, clusterizado por `tenant_id` |
| Calendário | Tabela de feriados nacionais e municipais (cidade, data), lida por `calendar.holidays` |
| Arquivos | Cloud Storage, bucket por ambiente, prefixo por tenant, ciclo de vida |
| Segredos e identidade | Secret Manager (um por uso); Identity Platform (cliente; painel com 2FA) |
| Observabilidade | Logging, Error Reporting, Monitoring; `llm_calls`; painel de custo por tenant |
| Código | GitHub → Cloud Build → Cloud Run; Terraform; prompts e templates versionados |

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

Contatos = `call_clicks + directions + website_clicks + conversations`; impressões e palavras-chave são contexto. `posicao` nula = não encontrado. `profile_audits` com `origem='diagnostico'` é o "antes" do Dia 7. `actions_log` só `INSERT`.

Tenancy: (1) documento `tenants/{id}` com configuração, `limites_json`, tom, termos, raio, segmento, zona, estado, consentimento e opt-out, subcoleções `approvals` e `queue`; nasce só após `zone.check`; (2) segredos por tenant (`tenant-{id}-gbp-oauth`), segredos da casa lidos só pelo conector dono, rotação 90 dias, revogação no offboarding; (3) contas de serviço mínimas por agente e conector (só WA Connector lê token da Meta; só Delivery lê o número claro; ninguém tem `UPDATE`/`DELETE` em `actions_log`); (4) `dono_wa_hash` com sal por tenant; textos de terceiros só como hash, temas e sentimento; nenhum cliente final na base.

Estados: `zone.check` (antes de existir) → `created` → `billing_active` → `profiled` → `gbp_linked` ou `gbp_pending_verification` → `live`.

## 5. Agentes

Todos em ADK; nenhum chama API direto; nenhum fala com o dono senão via `delivery.send`. Sentinela de calendário é rotina do Editor. Convite de avaliação não existe.

### Cartógrafo

| | |
|---|---|
| Gatilho | Dia 0 após `gbp_linked` (reduzida: 3×3, até 5 termos); Dia 7 (reduzida); sábado 03h (reduzida); dia 1 02h (completa) |
| Entradas | `tenants`, `locations`, `keywords_monthly`, `rank_measurements` do mês anterior |
| Ferramentas | `places.search_text` · `gbp.get_keywords` · `gbp.get_location` · `render.map_svg` · `render.card` · `cost.per_tenant` · `diario.log` |
| Cérebro | Gemini Pro + Grounding com Google Maps; Flash para normalizar; sem linguagem |
| Saídas | `rank_measurements`; Mapa SVG/PNG; JSON do Diagnóstico; `editor.tasks`; sugestão de categoria ao Guardião |
| Guardrails | ≤ 25 termos; grade ≤ 5×5; teto em `limites_json` (reduz grade antes de termos); só o `place_id` do cliente; nunca cita outro perfil; mede mesmo em `gbp_pending_verification` |
| Métricas | Custo de medição; cobertura da grade; variação de verdes; concordância com 20 buscas; duração da reduzida (< 2 min) |
| Teste | 20 buscas manuais com ≥ 85% no top 3; reduzida < 2 min; nenhum `place_id` de terceiros gravado |

```
Você é o Cartógrafo. Verde = top 3, cinza = 4–10, vermelho = fora do top 10 ou não encontrado.
JSON: {territorio:[{termo,pontos_verde,pontos_cinza,pontos_vermelho,variacao_mes}], diagnostico:{termos_no_top3,termos_fora,maior_lacuna}, oportunidades:[{termo,motivo,acao_sugerida}], auditoria_perfil:[{campo,atual,sugerido,impacto}], nap_consistente:bool}
Não invente termos sem impressões. Não cite outro perfil. Não sugira termos no nome. Não prometa posição.
```

### Editor

| | |
|---|---|
| Gatilho | Segunda 04h (post); diário 05h (feriados 72 h antes); `editor.tasks`; Dia 0 (auditoria); Dia 7 (diff); dia 1 (auditoria mensal); `approvals.decided` |
| Entradas | `tom_json`, `limites_json`, perfil atual, fotos, `calendar.holidays`, tarefas do Cartógrafo, `profile_audits` |
| Ferramentas | `gbp.get_location` · `gbp.create_post` · `gbp.upload_media` · `gbp.patch_location` · `gbp.update_hours` · `gbp.update_services` · `calendar.holidays` · `vision.assess_photo` · `guardiao.submit` · `diario.log` · `render.card` · `delivery.send` |
| Cérebro | Linguagem (post, descrição); Gemini multimodal (fotos); Gemini (qualquer campo do perfil) |
| Saídas | Guardião (P0/P1) ou publicação (P2), sempre com Diário e print; `posts`; `profile_audits`; horários de feriado; auditoria de completude; diff do Dia 7; `aviso_radar` |
| Guardrails | Só fotos com `assess_photo.ok`; categoria principal, nome, endereço via Guardião; ≤ 1 post/dia; descrição ≤ 750 caracteres; serviços sem preço; feriado sem padrão vira `pergunta_sim_nao` (sem resposta até 24 h antes, horário normal fica); nada publica em perfil suspenso ou pendente |
| Métricas | Aprovação sem edição (> 85% no P1); posts/semana; feriados com ≥ 72 h (100%); completude |
| Teste | Uma semana gera 1 post aprovado; feriado de teste vira horário + post 72 h antes com aviso; 100% com print; nenhum campo sensível sem aprovação |

```
Você é o Editor da {casa}. Tom: {tom}. Nunca prometa resultado, posição ou desconto. Nunca termos de busca no nome. Só {fatos_da_casa} e {limites}.
Post ≤ 300 caracteres com foto entre as disponíveis (nunca gerar). Feriado a 72 h: horário pelo padrão da casa e post ≤ 200 caracteres. requer_guardiao para categoria, nome, endereço, feriado sem padrão.
JSON: {post, foto_uri, justificativa, horario_feriado, publicar_em, requer_guardiao:bool}
```

### Anfitrião

| | |
|---|---|
| Gatilho | Polling 30 min (→ `gbp.review.new`, `gbp.question.new`); lote noturno; dia 1 (Reputação, Voz do Cliente); primeira semana (QR); `approvals.decided` |
| Entradas | Avaliações, perguntas, tom, fatos da casa, responsável e canal para quem reclamou, políticas do Google |
| Ferramentas | `gbp.list_reviews` · `gbp.reply_review` · `gbp.list_questions` · `gbp.answer_question` · `gbp.get_review_link` · `render.qr` · `render.pdf` · `render.card` · `classify.review` · `guardiao.submit` · `diario.log` |
| Cérebro | Gemini Flash (classificar); linguagem (responder); Gemini (violação de política) |
| Saídas | Respostas no Google; `reviews`, `questions`; Diário; Boletim de Reputação; classificação do mês; sinal de suspeita; QR em PDF |
| Guardrails | Nunca mensagem a cliente final; link oficial sem encurtador próprio; responde todas; notas 1 e 2 via Guardião em qualquer patamar; nunca dado do avaliador, compensação ou pedido de nota; texto só como hash; dúvida = `exige_humano`; chave por `review_id` |
| Métricas | Mediana < 2 h e 100% em 24 h; perguntas < 4 h; nota; edição pelo Guardião; sinalizadas/mês |
| Teste | Avaliação de teste respondida em < 2 h; "vocês têm estacionamento?" em < 4 h com dado do perfil; QR abre a tela oficial; nenhuma mensagem a outro número |

```
Você responde avaliações e perguntas públicas em nome da {casa}. Sem chavão; ao ponto; nunca compensação, dado do avaliador, discussão ou pedido de nota.
Nota ≤ 3: desculpa, explicação, convite a falar com {responsavel} pelo {canal}. Pergunta: só perfil ou {fatos_da_casa}; sem certeza, exige_humano. ≤ 400 caracteres.
JSON: {resposta, tom_detectado, temas[], sentimento, suspeita_de_violacao:bool, exige_humano:bool}
```

### Tesoureiro

| | |
|---|---|
| Gatilho | A cada hora (visões); diário 03h (coleta D-3..D-1); dia 1 05h (Extrato, Horas, custo, JSON do mês); segunda 06h (JSON da semana); `cost.alert` |
| Entradas | `metrics_daily`, `keywords_monthly`, `rank_measurements`, `reviews`, `questions`, `actions_log`, `llm_calls`, `hours_equivalence`, `deliveries` |
| Ferramentas | `gbp.get_daily_metrics` · `gbp.get_keywords` · `render.pdf` · `render.card` · `cost.per_tenant` · `diario.log` |
| Cérebro | Gemini Flash (normalizar); Pro só para três frases; números só de SQL |
| Saídas | Visões do dashboard; `metrics_daily`; Extrato (PDF); Horas Devolvidas (card); custo por tenant e alerta; JSONs para o Redator-chefe |
| Guardrails | Nenhum número de modelo; reconciliação < 2%; sempre `data_referencia`; contato = 4 métricas; custo por contato = R$ 499 ÷ contatos; nenhum campo de conversão, receita ou "novos clientes"; coleta por (tenant, data) substitui, nunca soma |
| Métricas | Frescor (próprio < 1 h; Google ≤ D-3); reconciliação; custo vs R$ 25; entregas do dia 1 na janela |
| Teste | Extrato sintético bate 100%; padaria (118 + 97 + 31 + 14) = 260 contatos e R$ 1,92; nenhuma visão sem `data_referencia` |

```
Três frases sobre este extrato, sem número fora do JSON, sem conversão, receita ou "novos clientes". Chame toques em Ligar de "ligações pelo perfil". Destaque a maior variação e o custo por contato. Diga até que data vão os dados.
```

### Redator-chefe

| | |
|---|---|
| Gatilho | Dia 0 (três frases); segunda 06h (Boletim; envio 07h); dia 1 06h (Voz do Cliente, Fechamento); trimestral; pendência há 72 h (≤ 1 lembrete/semana) |
| Entradas | JSONs do Tesoureiro, Cartógrafo, Anfitrião, Editor; nome do dono; tom; estados do tenant; `data_referencia` |
| Ferramentas | `tts.synthesize` · `render.card` · `render.pdf` · `delivery.send` · `diario.log` |
| Cérebro | Linguagem; Gemini (verificação cruzada); Cloud TTS |
| Saídas | OGG ≤ 60 s + card; PDFs (Diagnóstico, Fechamento mensal e trimestral); card Voz do Cliente; `aviso_radar` de pendência |
| Guardrails | Número fora dos dados bloqueia; ≤ 60 s; Boletim só 7h–8h; lembrete nunca após SAIR; nunca "novos clientes", conversão, receita, ROI, outro perfil; nenhum texto sem `prompt_versao` |
| Métricas | Leitura/escuta (`read`); duração média; correções manuais; bloqueios da verificação; pendências resolvidas em 7 dias |
| Teste | Boletim sintético passa na verificação com áudio ≤ 60 s; Diagnóstico em três frases só com números da medição; número plantado bloqueia |

```
Boletim para {nome}, ≤ 150 palavras, falado, começa com "Bom dia, {nome}"; primeira frase diz até que dia vão os dados ({data_referencia}).
O que mudou; contatos (ligações pelo perfil, rotas, cliques no site, mensagens); avaliações; posição nos termos-chave; o que a máquina fez; o que vem. Só números do JSON. Termine com uma ação da semana.
Diagnóstico: três frases: onde a casa está; a maior lacuna do perfil; o que a máquina faz primeiro. Sem promessa de posição.
```

### Guardião (humano com painel)

| | |
|---|---|
| Gatilho | Fila contínua; SLA 4 h úteis em P0/P1; amostragem diária de 10% no P2; texto livre do dono (`wa.inbound`); suspeita de avaliação; `cost.alert`; estado do perfil |
| Entradas | `approvals` (item, contexto, sugestão, risco); prints e diffs; resposta proposta com nota; estado do tenant e da zona |
| Ferramentas | Painel (Cloud Run + Identity Platform, 2FA): aprovar, editar, rejeitar em lote; incidente; denúncia pelo fluxo do Google; `qa_samples`; resposta humana ao dono |
| Cérebro | Nenhum; Gemini Flash só ordena a fila |
| Saídas | `approvals.decided`; edições devolvidas com motivo; feedback para a avaliação cega; incidentes; denúncias; `qa_samples` |
| Guardrails | ≤ 60 itens/hora por operador; categoria, nome, endereço e notas 1 e 2 com dois olhos em qualquer patamar; sem senha de cliente em tela; dono por nome e hash |
| Métricas | Itens/hora; taxa de edição; tempo de fila; incidentes por 100 clientes; clientes por operador (30 → 80 → 150) |
| Teste | 100 itens sintéticos em < 90 min por um operador; categoria só com duas aprovações; texto livre na fila em < 1 min |

```
Ordene por risco (categoria, nome, endereço e notas ≤ 2 primeiro; depois prazo), agrupe parecidos do mesmo tenant. JSON: {ordem:[item_id], grupos:[[item_id]]}. Não altere nenhum item.
```

## 6. Receitas

Chave em todo job: `tenant_id + agente + entrega + período`. Toda entrega passa pelo Delivery. Todo dado do Google com data de referência.

### 01 Diagnóstico de Posição

1. `gbp_linked` (ou pendente com `place_id` casado) → `cartografo.measure(modo='reduzida')` → `rank_measurements`.
2. Em paralelo `editor.audit_profile` → `profile_audits` com `origem='diagnostico'`.
3. `redator.diagnostico` (três frases) + `crosscheck`; `render.card` e `render.pdf`.
4. `delivery.send` na mesma conversa (janela aberta); chave `tenant + diagnostico + dia0`. Lacunas e termos vermelhos → `editor.tasks`.

Pronto: card e PDF em ≤ 2 min após `gbp_linked`; três frases sem número fora da medição; `profile_audits` guarda o "antes".

### 02 Antes e Depois do Perfil

1. Scheduler diário 06h → `onboarding.day7` para `created` + 7, com ou sem pendências.
2. `editor.profile_diff` (`profile_audits` do Dia 0 vs hoje, com Diário e print) + `cartografo.measure` reduzida nos mesmos termos e pontos.
3. `render.card` lado a lado; `delivery.send` até 8h; pendência aberta termina o card como uma `pergunta_sim_nao`. Chave `tenant + onboarding + day7`.

Pronto: sai no Dia 7 até 8h; toda diferença existe em `profile_audits`, `actions_log` ou `rank_measurements`.

### 03 Dashboard Radar

1. Hourly → `tesoureiro.refresh_views`.
2. Diário 03h → `tesoureiro.collect_gbp` D-3..D-1 → `metrics_daily` (impressões = desktop + mobile); `data_referencia` = último dia publicado; chave (tenant, data).
3. Dia 1 → `gbp.get_keywords` → `keywords_monthly`.
4. Seis números com setas vs 7 dias anteriores; linha fixa: "Dados do Google até {data_referencia}. O Google publica com 2 a 3 dias de atraso. 'Ligações pelo perfil' são toques no botão Ligar contados pelo Google, não ligações atendidas."
5. Link fixo com token; senha opcional; abertura grava `lido_em`.

Pronto: abre em < 2 s; seis números com data de referência; sem campo de conversão; padaria = 260 contatos e R$ 1,92.

### 04 Boletim de Segunda

1. Sábado 03h: medição reduzida.
2. Segunda 06h: `tesoureiro.week_summary` (4 métricas até a `data_referencia`, tipicamente quinta ou sexta; avaliações; posição; ações; o que vem).
3. `redator.boletim` ≤ 150 palavras + `crosscheck`; `tts.synthesize` → OGG ≤ 60 s; `render.card`.
4. 07h: `delivery.send`: janela aberta → livres; fechada → `boletim_segunda`. Chave `tenant + boletim + semana ISO`; janela 7h–8h perdida → incidente + `aviso_radar`.

Pronto: áudio ≤ 60 s às 7h ± 5 min; nenhum número fora do JSON; padaria = 31 ligações pelo perfil, 22 rotas, 8 cliques, 3 avaliações respondidas, 1º em 7 de 9 pontos, 1 post, feriado ajustado.

### 05 Mapa de Domínio

1. Dia 1 02h: `cartografo.measure(modo='completa')` → `rank_measurements`.
2. `gemini.analyze_territory` (Pro): cores, variação mensal, oportunidades só com termos que têm impressões.
3. `render.map_svg` com legenda e rodapé "Busca por texto na Places API como proxy da lista local do Maps; validação mensal com 20 buscas manuais"; envio até 8h; reduzido no Dia 0 e Dia 7.
4. Termos vermelhos → `editor.tasks`; categoria → Guardião; validação em `qa_samples` (< 85% = incidente); chamadas = termos × pontos, teto em `limites_json`.

Pronto: legenda, rodapé, ≥ 85%; nenhum dado de outro perfil; padaria = 7 de 9 verdes em "padaria perto de mim".

### 06 Diário de Bordo do Perfil

1. Segunda 04h: `editor.weekly_post` (foto real via `vision.assess_photo`, ≤ 300 caracteres); chave `tenant + post + semana ISO`.
2. Diário 05h: `editor.hours_check` com `calendar.holidays(cidade, hoje, hoje + 10)`; a 72 h → `gbp.update_hours` + post; sem padrão → `pergunta_sim_nao`; chave `tenant + feriado + data`.
3. `editor.tasks` → `gbp.patch_location` com diff em `profile_audits`; fotos via `gbp.upload_media`.
4. Toda ação: `diario.log` com print da tela pública; verificação diária confere 100%. Dia 1: `editor.audit_profile`. `aviso_radar` (8h–19h) em ação relevante.

Pronto: uma semana produz ≥ 1 post, 100% com print, feriado tratado 72 h antes, nenhum campo sensível sem aprovação.

### 07 Motor de Reputação

1. Primeira semana: `gbp.get_review_link` → `render.qr` → PDF → `delivery.send`.
2. Polling 30 min → `classify.review` → `anfitriao.reply_review`; notas 1 e 2 via Guardião; `gbp.reply_review`; Diário com print; chave por `review_id`.
3. Pergunta → `anfitriao.answer_question` só com perfil e fatos da casa; dúvida = `exige_humano` (4 h).
4. Violação → Guardião denuncia no fluxo do Google. Lote noturno `classify_batch`; dia 1 `reputation_report` (nota, novas, respondidas, mediana, perguntas, temas); chave `tenant + reputacao + AAAA-MM`.

Pronto: mediana < 2 h e 100% em 24 h; pergunta < 4 h; QR abre a tela oficial; nenhuma mensagem a outro número.

### 08 Extrato de Demanda

1. Dia 1 05h: SQL do mês até a `data_referencia`: contatos = 4 métricas; impressões e palavras-chave como contexto; nota; verdes ÷ medidos; custo por contato = R$ 499 ÷ contatos.
2. Série de 6 meses com setas; explica "ligações pelo perfil"; três frases (Gemini Pro) validadas.
3. `render.pdf`; `delivery.send` até 8h; chave `tenant + extrato + AAAA-MM`; dias não publicados entram na coleta seguinte.

Pronto: 100% dos números de SQL; sem campo de conversão; padaria 260 e R$ 1,92; oficina 168 e R$ 2,97; clínica 160 e R$ 3,12.

### 09 Horas Devolvidas

1. `hours_equivalence`: post 20 · foto 10 · resposta a avaliação 6 · resposta a pergunta 4 · ajuste de campo/horário 10 · medição 0,5 por termo-ponto · auditoria mensal 60 · Boletim 30 · extrato/PDF 45 · Mapa 60.
2. Dia 1 05h: SQL soma `actions_log` do mês (uma vez por chave, só com print ou saída) × minutos; tempo do dono = minutos entre cada `pergunta_sim_nao` e a resposta.
3. `render.card` com total, detalhamento, tempo do dono e tabela no rodapé; `delivery.send` até 8h; chave `tenant + horas + AAAA-MM`.

Pronto: reconcilia com `actions_log` linha a linha; clínica de exemplo = 14h07 e 2 min do dono.

### 10 Voz do Cliente

1. Lote noturno: `classify_batch` (temas por segmento + emergentes; sentimento); só avaliações e perguntas públicas.
2. Dia 1 06h: `redator.voz_do_cliente`: top 3 elogios e top 3 atritos com frequência, variação e frase anonimizada; Gemini valida frequências.
3. Atrito resolvível no perfil → `editor.tasks` no mesmo dia + "corrigi: {o que}" no card; tema acima do limiar (padrão 3 menções em 7 dias) → `aviso_radar`, ≤ 1/semana.
4. `render.card` com 6 itens; `delivery.send` até 8h; chave `tenant + voz + AAAA-MM`.

Pronto: 6 itens com frequência e evidência anonimizada; atrito resolvível vira tarefa no mesmo dia.

### 11 Fechamento Executivo

1. Dia 1 06h, após Cartógrafo → Editor → Tesoureiro → Anfitrião: `tesoureiro.month_summary` (cinco números com variação, extrato em três linhas, horas, mapa em miniatura, ações por tipo, o que vem).
2. `redator.fechamento` + `crosscheck`; `render.pdf`; `delivery.send` até 8h; o dono encaminha a quem quiser.
3. Trimestral desde o Dia 0: série de contatos, custo por contato, verdes, nota. Chave `tenant + fechamento + AAAA-MM` (e `+ trimestre`).

Pronto: PDF até 8h; nenhum número fora do JSON; oficina = 168 contatos, R$ 2,97, 4,8 · 214, 7 de 9 verdes.

## 7. Onboarding técnico

| Toque | Máquina | Estado |
|---|---|---|
| Comercial verifica a zona | `zone.check` em transação: `tenants_ativos < 2` → disponível; senão lotada + lista de espera. Proposta escrita reserva por 5 dias úteis; conversa não reserva | Nenhum |
| Assina o contrato (marca número e aceite) | Cria `tenants/{id}` com segmento, zona, `termos[]`, `limites_json` do mandato; ocupa a vaga (`zone.changed`); bucket, segredos, permissões. Reserva expirada → novo `zone.check` | `created` |
| Cadastra o cartão | Webhook do provedor; atraso não segura o Dia 0 | `billing_active` |
| Abre a conversa pelo link e responde 5 áudios | Primeira mensagem abre a janela (sem ela em 1 h: `pergunta_sim_nao` "Podemos começar?"). Gemini transcreve → `termos[]`, `raio_m`, `tom_json`, `limites_json`, `dono_nome`, `dono_wa_hash`. Confirmação por escrito + `pergunta_sim_nao`; o Sim é o opt-in registrado | `profiled` |
| Adiciona a conta operacional como Gerente | `gbp.discover` casa o local, grava `locations`, lê o estado; medição reduzida, auditoria, três frases, PDF. Pendente → passo a passo pelo WhatsApp, o resto não espera | `gbp_linked` ou `gbp_pending_verification` |
| Abre o dashboard | Token; `lido_em`; senha opcional | `live` |
| `created` + 7 | `onboarding.day7` | `live` |

Regras: (1) zona antes de tudo: `MAX_TENANTS_PER_ZONE_SEGMENT=2`, `zone.check` transacional; segmento = categoria principal do perfil; zona = bairro do Google Maps ou raio equivalente, no contrato com cidade e segmento; fila por ordem de chegada; mudança de endereço ou categoria para zona lotada opera até o fim do ciclo pago e entra na fila; redesenho de zona não expulsa quem está; (2) nada bloqueia nada: perfil pendente não impede dashboard, medição (`place_id` público) nem fila do Editor; Anfitrião e Tesoureiro esperam o vínculo; (3) Dia 7 automático a partir de `created`; (4) pendência há 72 h vira `aviso_radar` com link do passo, ≤ 1/semana, em horário comercial, nunca pede senha; persistindo, exceção do Guardião; SAIR interrompe os lembretes.

## 8. Operação

| Quando (Brasília) | Job | Agente |
|---|---|---|
| Contínuo | Webhooks do número da casa | Delivery / Guardião |
| A cada 30 min | Polling de avaliações e perguntas; respostas | Anfitrião |
| A cada hora | Visões do dashboard | Tesoureiro |
| Diário 03h | Coleta Performance API (D-3..D-1) | Tesoureiro |
| Diário 05h | Horários e feriados (72 h antes) | Editor |
| Segunda 04h / 06h / 07h | Post / Boletim gerado / Boletim enviado | Editor / Redator-chefe |
| Sábado 03h | Medição reduzida | Cartógrafo |
| Dia 1, 02h → 08h | Medição completa → auditoria → extratos → cards → PDFs → envios (Cartógrafo, Editor, Tesoureiro, Anfitrião, Redator-chefe) | Todos |
| Dia 7 do tenant | Antes e Depois | Editor + Cartógrafo |
| Trimestral, dia 1 | Fechamento Trimestral | Redator-chefe |

Papéis: Head de Operação (1 desde o P0; SLA, runbooks, avaliação cega, zonas) · Engenheiro de automação (1) · Operadores/Guardiões (30 → 80 → 150 clientes por operador) · Comercial/SDR (zona, contrato, onboarding assistido) · Jurídico externo.

Runbooks (todo runbook termina com linha no Diário e uma frase ao cliente; o resto é incidente do Head):

1. Perfil suspenso ou pendente: Editor congelado; Anfitrião lê e não responde; apelação pelo fluxo do Google com o dono; auditoria de conformidade em 100% dos tenants em 48 h.
2. Cota ou erro de API do Google: retry por tenant; dashboard mostra a última data boa; medições retomam pela chave; > 24 h avisa o cliente; nunca raspagem.
3. Custo > R$ 25: `cost.alert`; diagnóstico por `llm_calls`; reduzir grade e termos, renovar cache, mover volume para Flash; revisar em 48 h.
4. Modelo fora do ar: linguagem usa `LLM_LANGUAGE_FALLBACK`; tarefas Gemini esperam (alerta > 2 h); Boletim sem verificação não sai, sai `aviso_radar` de atraso.
5. Número da casa com qualidade baixa: ler `quality_rating` e SAIRs; pausar tudo que não é Boletim; revisar modelos e frequência; contestação na Meta; número reserva só com o Head.
6. Zona lotada com pedido: não vende, não cria tenant provisório; lista de espera; `zone.changed` avisa o primeiro da fila; zona não se redefine.
7. Offboarding: remove Gerente; desliga cadência; exporta histórico (ZIP); apaga no prazo (exceto `actions_log` e prints); encerra segredos; opt-out; libera a vaga.

| Custo por cliente/mês | R$ |
|---|---|
| Gemini (~100k in, 30k out, cache) | 3–5 |
| Cérebro de linguagem (~40k in, 10k out) | 2–4 |
| Places API (1 completa + 4 reduzidas) | 3–8 |
| WhatsApp da casa (≈ 25 mensagens) | 1–2 |
| TTS, Cloud Run, BigQuery, Storage | 3–6 |
| Total (alerta em 25) | ≈ 12–25 |

SLOs: entregas na janela ≥ 99% · avaliações mediana < 2 h, 100% em 24 h · perguntas < 4 h · frescor: próprio < 1 h, Google ≤ D-3 com data de referência · Diário 100% com print (verificação diária cruza `actions_log` com a API) · Dia 0 ≤ 15 min.

## 9. LGPD técnico

1. Nenhuma senha de cliente: só papel Gerente com token OAuth da nossa conta; código de verificação nunca passa por nós; senha do dashboard criada pelo cliente, como hash; nenhuma tabela, segredo ou log tem campo para credencial de cliente.
2. Segredos: da casa fora de qualquer tenant; um por tenant; acesso por conta de serviço; rotação 90 dias; revogação no offboarding; auditoria de acesso.
3. Dados pessoais: dono = nome e número (hash nas tabelas; claro só no Firestore, lido pelo Delivery); terceiros = textos públicos só para responder, guardados como hash, temas e sentimento; anonimização antes do `LLMGateway`; nenhum canal com cliente final.
4. Zona em código: `zones` com `limite=2`; segmento e zona não mudam sem Guardião; auditoria diária: `tenants` por segmento e zona com > 2 ativos deve devolver zero linhas.
5. Número da casa: opt-in com data, hora, texto e hash; só modelos de utilidade; SAIR em qualquer grafia marca opt-out na mesma transação; volta exige novo Sim; texto livre vai a humano.
6. Retenção: `actions_log` e prints 5 anos · `llm_calls` 12 meses · demais dados do tenant, PDFs, cards e áudios: contrato + 90 dias · Places: nada além de 30 dias (só `place_id`; a posição do próprio cliente é medição própria) · áudio do Dia 0 apagado 7 dias após a confirmação por escrito.
7. Titular: endpoint `dsr(tenant, hash)` localiza, exporta ou apaga em até 15 dias (dono; avaliador ou autor de pergunta, com remoção da resposta pública via API); pedido vira linha no Diário.
8. Suboperadores em página pública versionada: Google Cloud e APIs, Meta (número da casa), provedor do cérebro de linguagem, provedor de pagamento.
9. Cloud Audit Logs nos dois projetos; painel com identidade nominal e 2FA; toda aprovação com autor; `actions_log` append-only por permissão de tabela.

## 10. Plano de seis semanas

Equipe: um engenheiro sênior e o Head; jurídico na semana 6. Caminho crítico: acesso às Business Profile APIs e verificação na Meta, ambos no dia 1.

| Semana | Entrega | Prova |
|---|---|---|
| 1 | Projetos, Terraform, Cloud Build, BigQuery e Firestore com o modelo (inclusive `zones`), Secret Manager, Identity Platform; conta operacional com 2FA; chave da Places. Dia 1: formulário das Business Profile APIs; verificação na Meta, app, número da casa, modelos submetidos | `terraform apply` sobe os dois ambientes; job vazio escreve linha em `actions_log` |
| 2 | GBP Connector (respostas gravadas até a aprovação), Places Connector, `LLMGateway`, `diario.log` com print, `llm_calls`, `cost.per_tenant` | Busca por termo e ponto devolve a posição do `place_id` de teste; edição de horário gera diff e print |
| 3 | Cartógrafo, Mapa SVG, coleta do Performance API, visões, dashboard, Diagnóstico de ponta a ponta | 20 buscas manuais ≥ 85%; dashboard abre no celular com data de referência |
| 4 | Editor, Anfitrião, Guardião (planilha → painel), `onboarding.day7` | Tenant interno uma semana: post aprovado, feriado ajustado, avaliação respondida, tudo com print |
| 5 | Redator-chefe + TTS + verificação cruzada; Delivery com modelos, status e reenvio; webhooks (Sim, Não, SAIR, transbordo); Extrato, Horas, Voz do Cliente, Fechamento; onboarding automático; `zone.check` | Boletim sintético às 7h no celular do Head; Dia 0 cronometrado; terceira empresa da zona recusada |
| 6 | Runbooks, SLOs, offboarding, revisão LGPD com o jurídico, alerta de custo. Piloto com 3 clientes por 30 dias em P0 | Três Dias 0 em ≤ 15 min; primeiro Boletim real na segunda às 7h |

"Montei": (1) os 11 testes de aceitação passam; (2) Dia 0 em até 15 min com três pessoas que nunca viram o produto; (3) piloto fecha um mês com as 11 entregas, Diário completo e custo por tenant < R$ 25; (4) zero credenciais de cliente armazenadas; (5) nenhuma zona com mais de 2 tenants do mesmo segmento; `zone.check` recusa a terceira em teste.

## 11. Apêndice

```
GCP_PROJECT, GCP_REGION=southamerica-east1
GEMINI_MODEL_PRO=gemini-2.5-pro  GEMINI_MODEL_FLASH=gemini-2.5-flash   (ou a geração vigente)
LLM_LANGUAGE_PRIMARY=claude-sonnet|gemini-2.5-pro   LLM_LANGUAGE_FALLBACK=gemini-2.5-pro
PLACES_API_KEY   GBP_OAUTH_CLIENT_ID / SECRET   GBP_OPERATOR_REFRESH_TOKEN
META_APP_ID / META_APP_SECRET / META_SYSTEM_USER_TOKEN   WA_WEBHOOK_VERIFY_TOKEN   DELIVERY_SENDER_PHONE_ID
TTS_VOICE_ID   GUARDIAO_BASE_URL   DASHBOARD_BASE_URL
COST_ALERT_PER_TENANT_BRL=25   MAX_TENANTS_PER_ZONE_SEGMENT=2
```

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
zone.changed          zone.check, offboarding    -> painel do comercial; lista de espera
```

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

Contas antes da semana 2: (1) Google Cloud: organização, faturamento, `radar-hml` e `radar-prd`, APIs da seção 4; (2) conta operacional Google com 2FA, Gerente nos perfis, usada só pelo GBP Connector, assina o formulário das Business Profile APIs; (3) Meta, só para o número da casa: portfólio verificado, app com WhatsApp, número dedicado "Radar Urbano", usuário de sistema com token, modelos `boletim_segunda`, `entrega_radar`, `entrega_radar_pdf`, `pergunta_sim_nao`, `aviso_radar` aprovados, webhook; nenhum cadastro em nome de cliente; (4) provedor de pagamento: assinatura R$ 499/mês, webhook de status (vira `billing_active`), nota fiscal, cancelamento pelo próprio cliente.
