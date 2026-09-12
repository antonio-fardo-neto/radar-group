# BRIEF DE ESCOPO · RADAR URBANO (produto inicial = o antigo "Radar Maps")

> Este brief governa a reescrita dos quatro documentos (Mapa de Entregas, Mapa de Acessos, Mapa Mundi, Bíblia) e do Roadmap. Tudo que contradiz este brief está errado. Quando o brief não fala, siga o documento original correspondente (em `/tmp/claude-0/-home-user-radar-group/e80c3efa-81bf-5532-873e-a80e69af07bc/scratchpad/in/handoff/handoff/`), adaptado ao escopo abaixo.

## 0. O pedido do Victor (dono do projeto)

"Adapta tudo desse modelo, enxugando tudo para um produto inicial radar urbano e radar maps (chame tudo de radar urbano), considerando todos os detalhes e intricacias. E além disso produz um arquivo que me coloque em fases as implementações dos outros produtos de forma faseada e modular." O primeiro conjunto (Bíblia, Mapa Mundi, Entregas, Acessos) pode ser detalhado e profundo. O roadmap não precisa ser tão aprofundado.

## 1. O que é o Radar Urbano agora

- **Radar Urbano** é o nome de tudo: da empresa, do produto e da máquina. O produto inicial é o que o dossiê chamava "Radar Maps (Core)": posicionamento e captura de intenção no Google Maps e na Busca local, por assinatura, entregue por agentes de IA, com zero tempo do dono.
- **Nunca** escreva "Radar Maps" nos quatro documentos principais. Os nomes dos outros módulos (Radar Stars, Radar Chat, Radar Concorrência, Radar Ads, Radar Menu) só aparecem no Roadmap e, nos quatro documentos, apenas em notas curtas do tipo "entra com o módulo Stars" quando for indispensável explicar por que algo não está aqui. Prefira não citar.
- **Preço:** R$ 499/mês, fixo. Equivalente a R$ 16,63 por dia. Mensal, cancelável, sem fidelidade abusiva. Verba de mídia não existe neste produto.
- **Trava territorial (nova intricacia, vinda da página comercial):** o Radar Urbano atende no máximo **2 empresas por segmento por zona** (bairro ou raio equivalente). Motivo técnico: dois perfis concorrentes na mesma malha de busca disputam as mesmas posições e degradam o resultado de ambos. Consequências: verificação de disponibilidade da zona antes de vender; cláusula contratual de exclusividade limitada; campo `zona` e `segmento` no tenant; job `zone.check`; verbete na Bíblia.
- **Promessa oficial:** "captura de intenção otimizada, lucrativa e eficiente". Nunca conversão, nunca receita atribuída, nunca "novos clientes", nunca ROI projetado. A página comercial antiga tinha um simulador de retorno com "novos clientes" e "receita gerada": isso é proibido (decisão D5). Se precisar de conta, é sempre **custo por contato** (mensalidade ÷ contatos) e o dono coloca o valor dele por cima.
- **Setup:** a promessa pública continua "até 15 minutos no Dia 0". Sem WhatsApp da empresa e sem telefonia, o roteiro real fecha em cerca de dez; os cinco restantes são folga para quem trava no perfil. Use "os únicos 15 minutos" como teto e diga isso.

## 2. Regras inegociáveis (herdadas e novas)

1. Nenhuma métrica de conversão ou receita atribuída. Só o que se conta.
2. Gemini é o cérebro obrigatório para dados, medição, aferição e tudo que toca API ou superfície do Google. Outros modelos só para linguagem, atrás do `LLMGateway`.
3. Nunca a senha do cliente. Acesso por papel (Gerente no Perfil da Empresa). Senha nova só no dashboard, criada pelo cliente.
4. Zero tempo do dono. Os únicos minutos são no Dia 0.
5. Sem raspagem do Google. Places API (New) dentro dos termos (cache 30 dias; só `place_id` é armazenável).
6. Só avaliações reais, sem incentivo, sem seleção. (Convite ativo por WhatsApp para clientes finais não existe neste produto; existe link curto e QR de avaliação para o balcão.)
7. Diário de Bordo append-only com print é a prova de tudo.
8. Custo de tecnologia por cliente é métrica de primeira classe: **alerta em R$ 25/cliente/mês** (antes era R$ 35; caiu porque não há telefonia nem WhatsApp da empresa).
9. Métricas do Google exibidas com data de referência (atraso típico de 2–3 dias). Neste produto **não há dado em tempo real** de ligações ou conversas: tudo que é contato vem do Google com atraso; o que é próprio (medições, avaliações respondidas, ações) é atualizado de hora em hora.
10. Estética e idioma: português do Brasil, direto, sem hype; a mesma voz dos documentos originais (frases curtas, nomes próprios, cenas reais, nada de jargão sem tradução).

## 3. Dentro e fora do escopo

| Fica (Radar Urbano) | Sai (vai para o Roadmap) |
|---|---|
| Perfil da Empresa no Google: auditoria, categorias, atributos, serviços (lista, sem catálogo com preço), descrição, horários inclusive feriados, fotos, posts, perguntas e respostas | Catálogo/cardápio com preços e o card "O que te procuram" (Radar Menu) |
| Medição de posição em grade (Places API) e Mapa de Domínio | Comparação nominal com concorrentes, snapshots de concorrentes, card "Quem ganhou a semana", sinais de concorrente (Radar Concorrência) |
| Respostas a todas as avaliações em até 2 h; respostas a perguntas do perfil; Boletim de Reputação mensal; link curto e QR de avaliação para o balcão | Convite ativo de avaliação por WhatsApp a clientes finais, evento `atendimento.concluido`, modelo `convite_avaliacao`, WhatsApp da empresa do cliente (Radar Stars) |
| Métricas do Google (ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil, impressões na Busca e no Maps, palavras-chave de descoberta) | Recepcionista 24/7, Agenda das 7h, Resgate de Ligações Perdidas, telefonia, número de rastreamento, WhatsApp da empresa, Meta Embedded Signup, Tech Provider, "pediu preço", "horários marcados" (Radar Chat) |
| Entregas ao dono pelo WhatsApp **do Radar Urbano** (número da casa, uma conta única da empresa na plataforma Meta) | Google Ads, MCC, developer token, Estrategista, Extrato de Mídia (Radar Ads) |
| Sentinela de calendário **dentro do Editor**: feriados nacionais e municipais viram ajuste de horário e post 72 h antes | Sentinela como agente, clima, sinais de concorrente, ofertas relâmpago com Sim/Não (Radar Concorrência e Radar Ads) |
| Dashboard Radar, Boletim de Segunda, extratos, PDFs, Horas Devolvidas, Voz do Cliente (só de avaliações e perguntas), Fechamento Executivo | Voz do Cliente a partir de conversas de WhatsApp |

## 4. As onze entregas (numeração fixa)

Dois objetos de entrada (uma vez) e nove recorrentes. Grupos: **Entrada**, **Vendas & Performance**, **Controladoria & Eficiência**.

| Nº | Entrega | Grupo | Quando | Por onde chega | Quem faz |
|---|---|---|---|---|---|
| 01 | Diagnóstico de Posição | Entrada | Dia 0, na mesma conversa, minutos depois do acesso | Card no WhatsApp do dono; PDF de uma página no dashboard | Cartógrafo (medição reduzida) + Editor (auditoria de completude do perfil) + Redator-chefe (três frases) |
| 02 | Antes e Depois do Perfil | Entrada | Dia 7, automático | Card lado a lado no WhatsApp; arquivo no dashboard | Editor (diff do perfil) + Cartógrafo (segunda medição) |
| 03 | Dashboard Radar | Vendas & Performance | Atualizado a cada hora; dados do Google com data de referência | Link fixo no WhatsApp, ícone no celular; senha opcional | Tesoureiro |
| 04 | Boletim de Segunda | Vendas & Performance | Segunda, 7h | Áudio ≤ 60 s + card no WhatsApp | Redator-chefe, com dados do Tesoureiro e do Cartógrafo |
| 05 | Mapa de Domínio | Vendas & Performance | Mensal, dia 1 (edição reduzida no Dia 0 e no Dia 7) | Imagem no WhatsApp; versão interativa no dashboard | Cartógrafo |
| 06 | Diário de Bordo do Perfil | Vendas & Performance | Contínuo; resumo no Boletim; registro completo no dashboard | Seção do dashboard; linha curta no WhatsApp quando há ação relevante | Editor (o Cartógrafo diz o que otimizar) |
| 07 | Motor de Reputação | Vendas & Performance | Respostas contínuas (≤ 2 h); Boletim de Reputação mensal, dia 1 | Respostas no próprio Google; card no WhatsApp; material do QR em PDF | Anfitrião |
| 08 | Extrato de Demanda | Controladoria & Eficiência | Mensal, dia 1 | PDF de uma página no WhatsApp; série no dashboard | Tesoureiro |
| 09 | Horas Devolvidas | Controladoria & Eficiência | Mensal, dia 1 | Card no WhatsApp | Tesoureiro, a partir do Diário de Bordo |
| 10 | Voz do Cliente | Controladoria & Eficiência | Mensal, dia 1; alerta quando um tema dispara | Card no WhatsApp | Anfitrião classifica; Redator-chefe sintetiza |
| 11 | Fechamento Executivo | Controladoria & Eficiência | Mensal, dia 1; trimestral | PDF no WhatsApp; arquivo permanente no dashboard | Redator-chefe, com Tesoureiro e Cartógrafo |

Detalhes que precisam estar certos:

- **Contato**, neste produto, é o que o Google conta a partir do perfil: toques em **Ligar** (chame de "ligações pelo perfil"), pedidos de **rota**, cliques no **site**, e **mensagens pelo perfil** (o chat do próprio Perfil da Empresa, quando o cliente o mantém ligado). Explique uma vez, no Extrato de Demanda e no dashboard, que "ligações pelo perfil" são toques no botão Ligar contados pelo Google, não ligações atendidas.
- **Impressões** (Busca e Maps) e **palavras-chave de descoberta** são métricas de contexto; não entram na soma de contatos.
- **Custo por contato** = R$ 499 ÷ contatos do mês.
- **Mapa de Domínio:** grade de 3×3 a 5×5 pontos sobre o raio do cliente; para cada termo, posição do perfil do cliente em cada ponto. Cores: **verde = top 3**, **cinza = 4º a 10º**, **vermelho = fora do top 10 (ou não encontrado no top 20)**. Não há comparação nominal com concorrentes. Rodapé declara o método (busca por texto na Places API como proxy da lista local; validação mensal com 20 buscas manuais).
- **Boletim de Segunda:** cobre a semana fechada disponível (dados do Google até a data de referência, tipicamente a quinta ou sexta anterior) e diz isso em uma frase. Números: ligações pelo perfil, rotas, cliques no site, mensagens, avaliações novas e respondidas, posição nos termos-chave (da medição reduzida de sábado), ações do Diário, o que vem.
- **Diário de Bordo do Perfil** inclui: post semanal com foto real (nunca gerar foto do estabelecimento), fotos novas, descrição, horários (feriados 72 h antes: calendário nacional e municipal em tabela própria), serviços e atributos, categorias (sempre com aprovação humana), respostas a perguntas do perfil (Anfitrião registra ali também).
- **Motor de Reputação:** resposta humanizada e específica a toda avaliação em até 2 h (notas ≤ 2 passam pelo Guardião mesmo no patamar P2); respostas a perguntas públicas do perfil; sinal de avaliação suspeita para o Guardião denunciar; link curto oficial "Receber mais avaliações" e QR gerados pela máquina em PDF para o balcão/comanda (o cliente imprime ou a máquina manda o arquivo); Boletim de Reputação mensal com nota, novas avaliações, temas elogiados e de atenção. **Sem** convite ativo por mensagem.
- **Horas Devolvidas:** tabela de equivalência publicada no rodapé do card: post 20 min · foto selecionada e publicada 10 min · resposta a avaliação 6 min · resposta a pergunta 4 min · ajuste de campo/horário 10 min · medição de posição 0,5 min por termo-ponto · auditoria mensal do perfil 60 min · Boletim 30 min · extrato/PDF 45 min · Mapa de Domínio 60 min. Tempo do dono = minutos das respostas Sim/Não registradas.

## 5. Personas e números de exemplo (use exatamente estes; marque sempre como exemplo)

Personas: **Seu Jorge, Padaria Pão da Praça** (alimentação) · **Marcão, Oficina Marcão Auto Center** (automotivo) · **Dra. Lívia, Clínica Lívia Odonto** (saúde).

Mês típico (Extrato de Demanda; "A conta na mesa"):

| | Padaria | Oficina | Clínica |
|---|---|---|---|
| Ligações pelo perfil | 118 | 96 | 58 |
| Pedidos de rota | 97 | 41 | 37 |
| Cliques no site | 31 | 22 | 44 |
| Mensagens pelo perfil | 14 | 9 | 21 |
| **Contatos no mês** | **260** | **168** | **160** |
| Impressões (Busca + Maps) | 9.400 | 6.100 | 5.300 |
| Nota · avaliações | 4,7 · 128 | 4,8 · 214 | 4,9 · 96 |
| Termos no top 3 (pontos verdes / pontos medidos) | 7 de 9 em "padaria perto de mim" | 7 de 9 em "oficina mecânica" | 6 de 9 em "dentista perto de mim" |
| Mensalidade | R$ 499 | R$ 499 | R$ 499 |
| **Custo por contato** | **R$ 1,92** | **R$ 2,97** | **R$ 3,12** |

Semana típica da padaria (Boletim): 31 ligações pelo perfil, 22 rotas, 8 cliques no site, 3 avaliações novas (todas respondidas), 1º lugar para "padaria perto de mim" em 7 dos 9 pontos, 1 post publicado, horário de feriado ajustado.

Horas Devolvidas de exemplo (clínica, um mês): 8 posts (2h40) · 6 fotos (1h) · 27 avaliações respondidas (2h42) · 5 perguntas respondidas (20 min) · 4 ajustes de perfil (40 min) · 240 medições de posição (2h) · auditoria mensal (1h) · Boletins, extratos, mapa e fechamento (3h45) = **14h07**. Tempo da Dra. Lívia: 2 minutos, em uma resposta de sim ou não. A frase de balcão passa a ser **"catorze horas por R$ 499"**.

Vinhetas: reescreva todas as cenas sem Recepcionista, Resgate, WhatsApp da empresa, Sentinela ou concorrentes nomeados. Cenas boas: o Boletim às 7h02 na fornada; a avaliação de duas estrelas respondida às 20h50; o mapa do dia 1; o feriado ajustado 72 h antes com post; a pergunta pública "vocês têm estacionamento?" respondida em 40 minutos; o Fechamento encaminhado ao contador com "segue o mês".

## 6. Os agentes (cinco e um humano)

1. **Cartógrafo** — mede posição por termo e ponto, desenha o Mapa de Domínio, faz o Diagnóstico de Posição e diz ao Editor o que otimizar. Gatilhos: Dia 0 (reduzida), Dia 7 (reduzida), sábado 03h (reduzida, termos-chave), dia 1 02h (completa). Cérebro: Gemini Pro com Grounding com Google Maps + Gemini Flash para normalizar.
2. **Editor** — mantém o perfil vivo: posts, fotos, descrição, horários (inclusive feriados), serviços, atributos; auditoria de completude; categorias só com Guardião. Gatilhos: segunda 04h (post), diário 05h (horários e feriados: calendário nacional e municipal, ação 72 h antes), eventos `editor.tasks` do Cartógrafo, dia 1 (auditoria mensal). Cérebro: linguagem para texto; Gemini multimodal para fotos; Gemini para qualquer campo do perfil.
3. **Anfitrião** — responde todas as avaliações em até 2 h, responde perguntas do perfil, classifica temas e sentimento, sinaliza avaliações suspeitas, gera o material de QR. Gatilhos: polling de avaliações e perguntas a cada 30 min; lote noturno de classificação; dia 1 Boletim de Reputação e Voz do Cliente. Cérebro: Gemini Flash para classificar; linguagem para responder; Gemini para violação de política.
4. **Tesoureiro** — consolida tudo em número: coleta do Performance API, visões do dashboard, Extrato de Demanda, Horas Devolvidas, custo por tenant. Gatilhos: a cada hora (visões), diário 03h (coleta D-3..D-1), dia 1 05h (extratos). Cérebro: Gemini Pro só para as três frases; números só de SQL.
5. **Redator-chefe** — transforma dado em 60 segundos de áudio e uma página: Diagnóstico (três frases), Boletim, Voz do Cliente, Fechamento Executivo e Trimestral; verificação cruzada de números pelo Gemini antes de sintetizar; lembretes de pendência do onboarding. Gatilhos: segunda 06h, dia 1 06h, trimestral.
6. **Guardião** (humano com painel) — aprova em lote, audita por amostragem (10% no P2), trata exceções; regra dos dois olhos para categoria, nome, endereço e respostas a notas ≤ 2.

Frase de contagem: "cinco agentes e um humano com painel".

## 7. Os conectores

- **GBP Connector** (Google Business Profile): Business Information API v1 (`locations.get`, `locations.patch`, atributos, horários, categorias, serviços), Business Profile Performance API v1 (`getDailyMetricsTimeSeries`, `searchkeywords/impressions/monthly`), API v4 para avaliações (`reviews.list`, `reviews.reply`), posts (`localPosts.create`) e mídia (`media.create`), My Business Q&A API (perguntas e respostas). Acesso: formulário oficial de acesso às Business Profile APIs (1–2 semanas), OAuth 2.0 com a conta operacional (papel Gerente em cada perfil), escopo `business.manage`, refresh token no Secret Manager. Armadilhas: categoria principal só com humano; nunca termos de busca no nome; diff antes/depois; detectar `SUSPENDED`/`PENDING_VERIFICATION`.
- **Places Connector**: Places API (New), `places:searchText` com `locationBias` por ponto da grade, máscara mínima de campos; chave restrita; sem extração em massa; nada além de 30 dias exceto `place_id`. Neste produto guardamos: `place_id`, data, termo, ponto, posição. **Não** guardamos rating/contagem de outros lugares.
- **WA Connector (número da casa)**: uma única conta do Radar Urbano na WhatsApp Business Platform (Cloud API), com um número da empresa (o "número da casa"). Serve **só para falar com o dono**: entregas (áudio, card, PDF), perguntas de sim ou não, avisos de uma linha, lembretes de pendência. O dono consente no Dia 0 e sai com uma palavra (SAIR). Modelos aprovados: `boletim_segunda`, `entrega_radar` (cards e PDFs mensais), `pergunta_sim_nao` (interativo com botões), `aviso_radar` (uma linha). Webhooks: `messages` (respostas do dono: Sim, Não, SAIR, texto livre → transbordo humano) e `statuses` (sent/delivered/read). Cadastro: Portfólio de negócios do Radar Urbano verificado, app com produto WhatsApp, usuário de sistema com token. **Sem** Tech Provider, **sem** Embedded Signup, **sem** WhatsApp do cliente.
- **TTS Connector**: Cloud Text-to-Speech, Chirp 3 HD pt-BR, `voice_id` fixo da casa, OGG/Opus, ≤ 60 s.
- **Render & Delivery**: cards PNG (HTML → PNG, Chrome headless), Mapa de Domínio em SVG a partir do BigQuery, PDFs de uma página (Diagnóstico, Extrato, Fechamento, material do QR), Dashboard (Next.js no Cloud Run, link com token, senha opcional via Identity Platform), serviço `Delivery` com status e reenvio após 2 h.

Frase de contagem: "quatro conectores e um serviço de entrega" (GBP, Places, WA da casa, TTS + Render & Delivery). Interfaces com o mundo: Perfil da Empresa (Busca e Maps), Places API, WhatsApp do dono, dashboard.

## 8. Fundação e modelo de dados

- Google Cloud, projetos `radar-hml` e `radar-prd`, região `southamerica-east1`; Cloud Run e Cloud Run Jobs; ADK em Python; Cloud Scheduler → Pub/Sub → Jobs; Cloud Tasks; Firestore; BigQuery; Cloud Storage; Secret Manager; Identity Platform; Logging/Monitoring; GitHub → Cloud Build; Terraform. APIs habilitadas: Vertex AI, Places API (New), Business Profile APIs (após aprovação), Cloud Text-to-Speech, Cloud Run, Cloud Build, BigQuery, Firestore, Secret Manager, Scheduler, Pub/Sub, Identity Toolkit. (**Sem** Google Ads API.)
- Tabelas BigQuery:
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
- Tópicos Pub/Sub: `wa.inbound` (respostas do dono) · `wa.status` · `gbp.review.new` · `gbp.question.new` · `editor.tasks` · `approvals.decided` · `deliveries.send` · `tenant.state.changed` · `cost.alert` · `zone.changed`.
- Ferramentas (ADK): `gbp.get_location` · `gbp.patch_location` · `gbp.update_hours` · `gbp.create_post` · `gbp.upload_media` · `gbp.list_reviews` · `gbp.reply_review` · `gbp.list_questions` · `gbp.answer_question` · `gbp.get_daily_metrics` · `gbp.get_keywords` · `gbp.update_services` · `gbp.get_review_link` · `places.search_text` · `wa.send_template` · `wa.send_media` · `wa.send_interactive` · `tts.synthesize` · `render.card` · `render.pdf` · `render.map_svg` · `render.qr` · `guardiao.submit` · `diario.log` · `delivery.send` · `cost.per_tenant` · `vision.assess_photo` · `classify.review` · `zone.check` · `calendar.holidays`.
- Variáveis e segredos: `GCP_PROJECT`, `GCP_REGION=southamerica-east1`, `GEMINI_MODEL_PRO`, `GEMINI_MODEL_FLASH` (ou a geração vigente), `LLM_LANGUAGE_PRIMARY`, `LLM_LANGUAGE_FALLBACK`, `PLACES_API_KEY`, `GBP_OAUTH_CLIENT_ID/SECRET`, `GBP_OPERATOR_REFRESH_TOKEN`, `META_APP_ID/SECRET`, `META_SYSTEM_USER_TOKEN`, `WA_WEBHOOK_VERIFY_TOKEN`, `DELIVERY_SENDER_PHONE_ID`, `TTS_VOICE_ID`, `GUARDIAO_BASE_URL`, `DASHBOARD_BASE_URL`, `COST_ALERT_PER_TENANT_BRL=25`, `MAX_TENANTS_PER_ZONE_SEGMENT=2`.
- Estados do onboarding: `created` → `billing_active` → `profiled` → `gbp_linked` (ou `gbp_pending_verification`) → `live`. Antes de `created`: `zone.check` aprova a zona (senão o tenant nem nasce; vai para lista de espera da zona).
- Tenancy: um documento Firestore por tenant; segredos por tenant (`tenant-{id}-gbp-oauth`); contas de serviço mínimas por agente; hash com sal para o número do dono.

## 9. Operação

Cadências (horário de Brasília):

| Quando | Job | Agente |
|---|---|---|
| Contínuo | Webhooks do número da casa (respostas do dono, status de entrega) | Delivery / Guardião |
| A cada 30 min | Polling de avaliações e perguntas; respostas | Anfitrião |
| A cada hora | Visões do dashboard | Tesoureiro |
| Diário 03h | Coleta Performance API (D-3..D-1) | Tesoureiro |
| Diário 05h | Checagem de horários e feriados (72 h antes) | Editor |
| Segunda 04h / 06h / 07h | Post semanal / Boletim gerado / Boletim enviado | Editor / Redator-chefe |
| Sábado 03h | Medição reduzida dos termos-chave | Cartógrafo |
| Dia 1, 02h → 08h | Medição completa → auditoria do perfil → extratos → cards → PDFs → envios (ordem: Cartógrafo, Editor, Tesoureiro, Anfitrião, Redator-chefe) | Todos |
| Dia 7 do tenant | Antes e Depois | Editor + Cartógrafo |
| Trimestral, dia 1 | Fechamento Trimestral | Redator-chefe |

Papéis humanos: Head de Operação (1 desde o P0), Engenheiro de automação (1), Operadores/Guardiões (30 → 80 → 150 clientes por operador; sobe porque não há atendimento em tempo real), Comercial/SDR (verificação de zona e onboarding assistido), Jurídico externo.

Runbooks: perfil suspenso ou pendente; cota ou erro de API do Google; custo por tenant acima de R$ 25; modelo de IA fora do ar; número da casa com qualidade baixa (opt-outs dos donos); zona lotada com pedido de venda; offboarding (remover Gerente, exportar histórico, apagar dados, liberar a vaga da zona).

Custo de tecnologia por cliente (referência): Gemini R$ 3–5 · linguagem R$ 2–4 · Places R$ 3–8 · WhatsApp da casa (≈ 25 mensagens de utilidade/mês) R$ 1–2 · TTS, Cloud Run, BigQuery, Storage R$ 3–6 · **Total ≈ R$ 12–25**, alerta em R$ 25.

SLOs: entregas no horário ≥ 99%; resposta a avaliações mediana < 2 h e 100% em 24 h; perguntas do perfil respondidas em < 4 h; frescor: dados próprios < 1 h, dados do Google ≤ D-3 com data de referência; Diário 100% com print; Dia 0 em até 15 minutos cronometrados.

Plano de montagem: **seis semanas**. S1 Fundação e pedidos de acesso (dia 1: formulário das Business Profile APIs; verificação da empresa Radar Urbano na Meta e número da casa). S2 Conectores GBP e Places, LLMGateway, Diário, custo. S3 Cartógrafo, Tesoureiro, Dashboard, Diagnóstico de Posição. S4 Editor, Anfitrião, Guardião (planilha → painel), Antes e Depois. S5 Redator-chefe, TTS, Delivery pelo número da casa, Boletim, extratos e PDFs, onboarding automático, verificação de zona. S6 Endurecimento (runbooks, SLOs, offboarding, custo) e piloto com 3 clientes por 30 dias.
Definição de "montei": os 11 testes de aceitação passam; o Dia 0 leva até 15 minutos cronometrados; o piloto fecha um mês com as 11 entregas e custo por tenant abaixo de R$ 25; ninguém tem senha de ninguém; nenhuma zona com mais de 2 tenants do mesmo segmento.

## 10. Acessos (Mapa de Acessos)

Sistemas (reletrados): **A** Perfil da Empresa no Google (papel Gerente) · **B** WhatsApp do dono (só recebe; consente no Dia 0; SAIR interrompe) · **C** Dashboard Radar (conta criada pelo Radar Urbano; senha nova criada pelo cliente; link mágico) · **D** Contrato, pagamento e nota fiscal.

Base legal (pauta para advogado, 8 itens): 1 contrato com mandato de operação (o que faz sem perguntar: posts, fotos, horários, respostas a avaliações e perguntas, ajustes de campos; o que exige um sim: categoria principal, nome, endereço, ofertas; o que nunca: prometer posição ou resultado, incentivo por avaliação); 2 LGPD (dados do dono: nome e número; textos públicos de avaliações e perguntas de terceiros tratados apenas para responder em nome da empresa, armazenados como hash e temas; nenhuma mensagem ativa a clientes finais; suboperadores: Google Cloud e APIs, Meta (só para o número da casa), provedor do cérebro de linguagem, provedor de pagamento); 3 política de avaliações e de conteúdo do Google (sem incentivo, sem seleção, respostas verdadeiras, sem dados do avaliador); 4 marca, fotos e imagem; 5 preços, horários e informações comerciais (responsabilidade do cliente; origem registrada); 6 exclusividade limitada por zona (no máximo dois do mesmo segmento na mesma zona; como a zona é definida; o que acontece se a zona muda); 7 limitação de responsabilidade (a promessa é a operação medida e registrada); 8 reversibilidade e encerramento (remoção do Gerente, entrega do histórico, exclusão de dados no prazo, liberação da vaga na zona).

Roteiro do Dia 0: (1) Antes: verificação da zona pelo comercial, contrato por link, cartão no provedor (5 min). (2) Minuto 0 a 5: cinco perguntas por áudio (o que você mais vende e como o cliente procura; bairros ou raio que importam; o jeito da casa de falar; o que a máquina pode fazer sem perguntar; em que número recebe as entregas e como quer ser chamado). (3) Minuto 5 a 8: Gerente no Perfil da Empresa, um toque; se não verificado, passo a passo e o resto não espera. (4) Minuto 8 a 10: link do dashboard, senha opcional, Diagnóstico de Posição na mesma conversa. (5) Encerramento, quando houver.

## 11. Estrutura fixa do Mapa Mundi (Manual de Montagem)

Capítulos e ordem: I Visão e organograma (cinco camadas; sete regras) · II Os cérebros (tabela sem linha de conversa em tempo real; LLMGateway; cinco regras) · III Os conectores (GBP, Places, WA da casa, TTS e Render & Delivery) · IV A fundação (tabela de peças; modelo de dados; tenancy) · V Os agentes (cinco + Guardião, cada um com missão, gatilho, entradas, ferramentas, cérebro, prompt-esqueleto, saídas, guardrails, métricas, teste de aceitação) · VI As receitas (onze pipelines, uma por entrega, com critério de pronto) · VII O onboarding técnico (toques do cliente → estados; regras: nada bloqueia nada, dia 7 automático, pendências viram uma pergunta, zona antes de tudo) · VIII A operação (cadências, papéis, runbooks, custo por cliente, SLOs) · IX Segurança e LGPD técnico · X O plano de montagem (seis semanas; definição de "montei") · Apêndice (variáveis, tópicos, ferramentas, contas que precisam existir) · Encerramento.

## 12. Lista fixa de verbetes da Bíblia (57)

Antes de tudo: Como usar este livro (sete partes; a regra do livro).
- I.1 O que é "a máquina" · I.2 O que é um conector · I.3 O que é um agente (e o ADK) · I.4 O que é "tenant" · I.5 O que é "job idempotente" · I.6 O que é o Diário de Bordo
- II.1 O que é um "cérebro" e como se contrata · II.2 Como ligar o Gemini (Vertex AI) · II.3 Como contratar o Claude (opcional) · II.4 Saída estruturada (JSON) · II.5 Prompt de sistema · II.6 Avaliação cega mensal
- III.1 Google Cloud: conta, projeto, faturamento · III.2 Pedir acesso às Business Profile APIs · III.3 Conta operacional e OAuth · III.4 Ser adicionado como Gerente · III.5 Perfil não reivindicado ou não verificado · III.6 Places API e chave restrita · III.7 Meta: portfólio, verificação da empresa, app e o número da casa · III.8 Modelos de mensagem para o dono (e o SAIR) · III.9 Cloud Text-to-Speech: a voz da casa · III.10 Webhook: status e respostas do dono, e como testar · III.11 Link curto e QR de avaliação (o material do balcão)
- IV.1 Cloud Run · IV.2 BigQuery · IV.3 Firestore · IV.4 Secret Manager · IV.5 Cloud Scheduler e Pub/Sub · IV.6 GitHub e deploy automático · IV.7 Terraform
- V.1 ADK: primeiro agente em 20 minutos · V.2 Dar uma ferramenta a um agente · V.3 Sandbox · V.4 Painel do Guardião (planilha e versão de verdade) · V.5 A grade de medição: raio, termos, pontos e a validação com 20 buscas
- VI.01 a VI.11 versões de bicicleta das onze entregas (na numeração da seção 4 deste brief)
- VII.1 O roteiro literal do Dia 0 · VII.2 Verificar a disponibilidade da zona (a trava territorial)
- VIII.1 QA por amostragem · VIII.2 Custo por cliente (e o que fazer acima de R$ 25) · VIII.3 Runbook: perfil suspenso · VIII.4 Runbook: API do Google parou · VIII.5 Runbook: número da casa com qualidade baixa · VIII.6 Runbook: offboarding
- IX.1 Pedido de titular (avaliador, autor de pergunta ou dono) · IX.2 Suboperadores e retenção
- X.1 O quadro das seis semanas
Glossário A–Z (sem Embedded Signup, MCC, Token (Meta) de cliente; com Zona, Grade, Data de referência, Número da casa, Link curto de avaliação) · Encerramento.

Cada verbete tem sempre as sete partes na ordem: **O que é, em uma frase de gente** · **Por que existe** · **Antes de começar, tenha na mão** · **Passo a passo** · `> **Como saber que deu certo** — ...` · **Se deu errado** · **Palavras deste verbete** (opcional).

## 13. Roadmap (segundo arquivo, menos profundo)

Fases modulares depois do Radar Urbano (Fase 0):
- **Fase 1 · Radar Concorrência + Radar Menu** (só Google, sem acesso novo do cliente): Sentinela como agente, snapshots de concorrentes (30 dias), "Quem ganhou a semana", sinais de clima e concorrente; catálogo com preços e "O que te procuram".
- **Fase 2 · Radar Stars** (Fundação Meta para o cliente: Tech Provider, Embedded Signup, WABA do cliente, modelos, consentimento; Anfitrião convida após atendimento; QR + WhatsApp).
- **Fase 3 · Radar Chat** (Recepcionista 24/7, Agenda das 7h, Fundação Telefonia: número de rastreamento, Resgate de Ligações Perdidas; contatos em tempo real; "pediu preço", "horários marcados" voltam ao Extrato).
- **Fase 4 · Radar Ads** (MCC, developer token, Estrategista, Extrato de Mídia, corte por custo por contato; depende do número de rastreamento da Fase 3 para atribuição).
- **Fase 5 · A suíte** (bundle R$ 1.500–2.200; proposta automática de expansão no mês 3; cross-sell por dado; agentes compartilhados).
Para cada fase: o que adiciona (entregas, agentes, conectores, acessos e cláusulas, verbetes, tabelas), pré-requisitos e caminho crítico, prazo de montagem estimado, o que muda nos quatro documentos, critério de pronto. Modularidade: cada módulo é um conjunto de agentes/conectores/tabelas ligável por tenant (`modules_json` no tenant), sem tocar no núcleo.

## 14. Convenções de escrita (o gerador `src/build.py` lê o Markdown)

- Primeira linha: `# RADAR URBANO: O NOME DO DOCUMENTO` · segunda: `*subtítulo em uma frase*`.
- Eyebrow em itálico numa linha sozinha imediatamente antes do `##`: `*Capítulo I · A Regra do Zero*`, `*Entrega 03 · Vendas & Performance*`, `*Verbete III.2 · Manual, capítulo III*`, `*Sistema A · Os sistemas*`, `*Encerramento*`.
- `## TÍTULO DA SEÇÃO` (caixa alta para títulos de capítulo; título normal para entregas/verbetes/sistemas). Atributos opcionais: `## TÍTULO {.dark}`, `{.alt}`, `{.fecho}` (encerramento com o texto em `*itálico*` logo abaixo).
- Tagline da entrega: linha `*em itálico*` logo após o `##`.
- Divisória de capítulo (só na Bíblia): `---` e depois `# Capítulo III — Os conectores (Verbetes III.x)`.
- `### Nome do bloco` para agentes, conectores, receitas (ex.: `### 05 Mapa de Domínio`, `### Cartógrafo`).
- Linhas numeradas com lead: `1. **Lead** — texto`. Passos simples: `1. texto`.
- Pares rótulo/valor: `- **Rótulo:** valor` (dois-pontos dentro do negrito).
- Definições/glossário: `- **Termo**: definição` (dois-pontos fora do negrito).
- Cartões: `- **01 · Nome** — frase` ou `- **Segunda, 7h02** — cena`; linhas de conta aninhadas: `  - Contatos no mês: 260`.
- Faixa preta: `> **Rótulo** — texto`. Vinheta: `> *Na vida real · Seu Jorge, Padaria Pão da Praça*` e na linha seguinte `> texto da cena`.
- Calendário: `#### Dia 0 — Os únicos 15 minutos` seguido de bullets simples; blocos `####` consecutivos viram uma grade.
- Etiqueta de bloco: `**Rótulo**` sozinho numa linha.
- Tabelas em Markdown; código em cercas ```.
- Comentário HTML na primeira linha do arquivo com a descrição do documento (como nos originais).
- Sem emojis. Sem travessão em prosa corrida além do padrão dos originais (usar ponto ou dois-pontos). Aspas retas.

## 15. Adendo de alinhamento (decisões tomadas durante a redação; valem para todos os documentos)

1. **Segmento** = a categoria principal do perfil no Google (padaria e pizzaria são segmentos diferentes). As famílias (alimentação, automotivo, saúde) são só linguagem de conversa e das personas.
2. **Zona** = o bairro do Google Maps, ou um raio equivalente, escrita no contrato com cidade e segmento. Não é a sobreposição de grades.
3. **Reserva de vaga**: conversa não reserva nada; a proposta escrita reserva a vaga pelo prazo da proposta (5 dias úteis); a vaga só se ocupa de fato na assinatura (transação em `zones`).
4. **Fila**: ordem de chegada, sempre; ninguém fura a fila, nem cliente antigo. Cliente que muda de endereço ou de categoria principal para uma zona lotada mantém a operação até o fim do ciclo pago e entra na lista de espera da zona nova na ordem de chegada; o endereço no perfil muda mesmo assim (é dado dele); a vaga antiga libera no dia da mudança confirmada. Se o Radar Urbano redesenhar uma zona, quem já está fica.
5. **Modelos da Meta**: `boletim_segunda` (cabeçalho de vídeo: card parado + a voz da casa em MP4, usado quando a janela de 24 h está fechada; com a janela aberta vão o card PNG e o áudio OGG livres), `entrega_radar` (cabeçalho de imagem, para cards) e `entrega_radar_pdf` (cabeçalho de documento, para PDFs; no código é um nome lógico só, `entrega_radar`), `pergunta_sim_nao` (botões Sim/Não) e `aviso_radar` (dois parâmetros: {{1}} nome, {{2}} a linha). Todos categoria Utilidade, rodapé "Responda SAIR para parar".
6. **Primeira mensagem do Dia 0**: o número do dono e o aceite de receber mensagens do número da casa são marcados na página do contrato. A conversa abre pelo link da página do contrato (o dono manda a primeira mensagem, o que abre a janela de 24 h); se ele não abrir em 1 hora, o número da casa manda o modelo `pergunta_sim_nao` ("Podemos começar?"). O Sim ao fim das cinco perguntas confirma o número e fica registrado, com hora, como opt-in.
7. **Dia 7** conta a partir de `created`.
8. **Descrição do perfil**: limite de 750 caracteres (o do produto do Google).
9. **Retenção**: `actions_log` 5 anos; `llm_calls` 12 meses; `reviews`, `questions` e demais dados do tenant enquanto durar o contrato + 90 dias; respostas da Places API 30 dias (só o `place_id` fica; a posição do próprio cliente por termo, ponto e data é medição própria e fica na série); áudio do Dia 0 apagado 7 dias depois da confirmação por escrito.
10. **Patamares do Guardião**: P0 tudo aprovado antes; P1 aprovação em lote com meta de > 85% sem edição; P2 publicação direta com QA de 10%; notas 1 e 2, categoria principal, nome e endereço sempre com dois olhos, em qualquer patamar.
11. **Cópia do Fechamento a terceiros**: não existe neste produto. O dono encaminha o PDF a quem quiser ("segue o mês").
12. **Horários de envio ao dono**: Boletim segunda 7h; entregas do dia 1 e do dia 7 até as 8h; a linha de uma frase (`aviso_radar`) e as perguntas de sim ou não saem em horário comercial (8h às 19h), mesmo que a ação no perfil tenha sido de madrugada.
13. **Link do dashboard**: "link fixo" (com token, vira ícone no celular); "link mágico" é a entrada sem senha; "link único" é só o de criar ou redefinir a senha.
14. **Numeração dos capítulos no Mapa de Acessos**: como no Mapa de Entregas, sequencial e sem buracos: I Princípios · II Os sistemas (seção de abertura + Sistemas A–D) · III A base legal · IV O mapa por entrega (seção de abertura + Entregas 01–11) · V O roteiro · VI A zona.
15. **Comentário da primeira linha** dos arquivos da raiz: "Fonte de verdade: este Markdown, lido por src/build.py" (a pasta `_work/` não vai para o repositório).
