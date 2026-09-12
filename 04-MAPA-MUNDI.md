<!-- Radar Urbano · Mapa Mundi (Manual de Montagem da Máquina): organograma em cinco camadas e sete regras, cérebros (Gemini obrigatório para dados, medição e tudo que toca o Google), quatro conectores e um serviço de entrega, fundação no Google Cloud e modelo de dados, cinco agentes e o Guardião, onze receitas com critério de pronto, onboarding técnico com a trava de zona, operação (cadências, papéis, runbooks, custo, SLOs), LGPD técnico, plano de seis semanas, apêndice. Fonte: src/build.py -->

# RADAR URBANO: O MAPA MUNDI DA MÁQUINA

*O manual de montagem da máquina: organograma, cérebros, conectores, fundação em nuvem, cada agente, cada entrega, a operação e o plano de seis semanas. Escrito para um tecnólogo pegar, montar e dizer: pronto. Gemini é o cérebro de dados, medição e tudo que toca o Google.*

*Capítulo I · Visão e organograma*

## A MÁQUINA EM CINCO CAMADAS

A máquina é um conjunto de cinco agentes que trabalham em fila, por cliente, em cadência fixa, sobre uma memória única, usando quatro conectores e um serviço de entrega para falar com o Google e com o WhatsApp do dono. Um orquestrador dita o ritmo. Um painel humano aprova em lote e audita por amostragem. Uma contagem em código garante que nenhuma zona tenha mais de duas empresas do mesmo segmento. Não há atendimento em tempo real e a máquina não conversa com cliente final: tudo que entra vem do Google, com data de referência, e tudo que sai vai para o dono. O cliente só vê as entregas: o card, o áudio, o PDF, o dashboard.

As cinco camadas, de cima para baixo:

- **Camada 1 · Interfaces com o mundo:** O que a máquina toca fora dela. Quatro superfícies, e nenhuma outra: o Perfil da Empresa no Google (Busca e Maps), onde vivem o perfil, as avaliações, as perguntas, as fotos e as métricas; a Places API (New), de onde vem a posição por termo e ponto; o WhatsApp do dono, alcançado pelo número da casa; e o Dashboard Radar, aberto no celular do dono por link fixo. Nada é raspado, nada é digitado por gente.
- **Camada 2 · Conectores:** Um serviço pequeno por sistema externo, com contrato fixo: GBP Connector (ler e editar o perfil, posts, fotos, avaliações, perguntas, desempenho, link de avaliação), Places Connector (medição em grade), WA Connector (o número da casa, só para o dono), TTS Connector (a voz da casa). Ao lado deles, Render & Delivery: cards, mapa, PDFs, QR, dashboard e o envio com status. Um conector nunca decide; executa, registra custo e devolve JSON.
- **Camada 3 · Agentes, orquestrador e Guardião:** Cinco agentes com nome e missão: Cartógrafo (posição e território), Editor (o perfil vivo, inclusive feriados), Anfitrião (avaliações, perguntas, reputação), Tesoureiro (números, extratos, custo) e Redator-chefe (áudio, três frases, uma página). O orquestrador é o Cloud Scheduler disparando tópicos no Pub/Sub que acordam Cloud Run Jobs, com Cloud Tasks para as filas por tenant. O Guardião é gente com painel: aprova em lote, audita 10% no P2, decide categoria, nome, endereço e respostas a notas baixas.
- **Camada 4 · Cérebros:** Gemini na Vertex AI, obrigatório para tudo que é dado, medição, aferição, áudio, foto e decisão que toca o Google (Pro para análise e decisão, Flash para volume, Grounding com Google Maps quando cabe). Um cérebro de linguagem intercambiável (Claude Sonnet ou Gemini Pro) para posts, respostas e roteiros, sempre atrás do `LLMGateway`. Cloud Text-to-Speech para a voz. Nenhum agente chama um modelo direto.
- **Camada 5 · Memória e prova:** Firestore guarda o estado de cada tenant: configuração, limites pré-autorizados, zona e segmento, estado do onboarding, aprovações pendentes, consentimento do dono. BigQuery guarda o que se conta e o que se prova: métricas do Google com data de referência, medições, avaliações e perguntas como hash e temas, o Diário de Bordo append-only, custo por chamada, a contagem de zonas. Cloud Storage guarda fotos, prints, PDFs e áudios. Secret Manager guarda credenciais, uma por uso, nunca a senha de ninguém.

> **A regra da pilha** — Tudo que está acima fala só com a camada imediatamente abaixo. Um agente nunca chama uma API direto; chama um conector. Um conector nunca decide; executa. Um cérebro nunca toca a memória; devolve JSON para quem o chamou. O Guardião entra pela camada 3, pelo painel, e nunca pela 2.

**As sete regras de arquitetura**

1. **Camadas estritas** — Interface → conector → agente → cérebro → memória. Nenhum agente chama API direto. Nenhum conector chama cérebro. Trocar o modelo de linguagem, a voz da casa ou o jeito de desenhar um card não toca a lógica de nenhum agente; trocar um endpoint do Google toca um conector, e só ele.
2. **Gemini é o cérebro de dados e de Google** — Toda leitura, extração, aferição, classificação de dados e toda decisão que envolva API ou superfície do Google passa pelo Gemini, na Vertex AI, com saída estruturada (JSON com esquema) e, quando aplicável, Grounding com Google Maps. Vale para o áudio do Dia 0, para julgar fotos e para conferir os números de um roteiro antes de virar voz. É regra de arquitetura, não preferência.
3. **Um cliente é um tenant, e um tenant tem zona** — Todo dado carrega `tenant_id`. Toda fila é por tenant. Todo segredo tem um dono só no Secret Manager: o tenant, ou o conector da casa. Todo tenant nasce com `segmento` e `zona`, e só nasce se `zone.check` confirmar que a zona tem vaga: no máximo duas empresas do mesmo segmento na mesma zona, contadas em `zones`, em código, antes do contrato. Um incidente em um cliente nunca vaza para outro; um cliente novo nunca disputa a malha de busca de um cliente antigo.
4. **Tudo é job idempotente** — Cada tarefa tem uma chave (`tenant_id + agente + entrega + período`). Rodar duas vezes não publica duas vezes, não responde duas vezes, não mede duas vezes, não envia duas vezes. A chave é verificada antes da ação externa e gravada junto com ela.
5. **Humano aprova, IA executa** — Até o patamar P1, nada é publicado ou respondido sem aprovação em lote no Guardião. No P2, aprovação por exceção com amostragem de QA de 10%. Categoria principal, nome, endereço e respostas a avaliações com nota ≤ 2 passam pelo Guardião em qualquer patamar. O limiar é configuração por tenant, não código.
6. **Diário de Bordo é a verdade** — Toda ação externa (post, foto, edição de campo ou horário, resposta a avaliação, resposta a pergunta, envio ao dono) escreve uma linha imutável em `actions_log` com autor (agente), modelo, versão do prompt, entrada, saída, print e hora. Sem linha, a ação não aconteceu. Das linhas saem as Horas Devolvidas.
7. **Custo por cliente é métrica de primeira classe** — Cada chamada de API e de modelo grava custo estimado por tenant. Alerta acima de R$ 25/cliente/mês. O teto é baixo de propósito: a máquina paga Google, cérebros, o número da casa e nuvem, e nada mais. A margem da tese depende disso.

*Capítulo II · Os cérebros*

## QUEM PENSA O QUÊ

Podemos usar qualquer inteligência. Mas há uma divisão de trabalho fixa: o Gemini é o cérebro de dados, medição, aferição e de tudo que toca o Google, porque está na posição mais favorecida para isso. Os demais cérebros são intercambiáveis e vivem atrás de uma camada de abstração. As versões citadas são as vigentes na escrita; o `LLMGateway` lê `GEMINI_MODEL_PRO` e `GEMINI_MODEL_FLASH` e troca de geração sem tocar em agente nenhum.

| Função | Cérebro | Por quê | Como se chama |
|---|---|---|---|
| Extração e normalização de dados do perfil, métricas, avaliações, perguntas, palavras-chave | **Gemini 2.5 Flash** (volume) · **Gemini 2.5 Pro** (análise mensal) | Nativo do ecossistema; saída estruturada confiável; contexto longo para séries | Vertex AI, `generateContent` com `responseSchema` (JSON) |
| Aferição de posição e leitura de superfícies Google | **Gemini** com **Grounding com Google Maps** | Acesso oficial a dados de lugares dentro do modelo, sem raspagem; interpreta o que a Places API devolveu e propõe termos | Vertex AI, ferramenta de grounding habilitada; a medição em si é `places.search_text`, o Gemini lê o resultado |
| Decisões que envolvem API do Google (o que editar, que campo tocar, o que otimizar) | **Gemini 2.5 Pro** | Mesma família que a plataforma; melhor aderência às diretrizes do produto | Function calling com as ferramentas do GBP Connector |
| Transcrição do áudio do Dia 0 | **Gemini** multimodal | Entrada de áudio nativa, sem serviço separado; do áudio saem termos, raio, tom, autorizações e o número do dono em JSON | `generateContent` com parte de áudio (o OGG recebido pelo número da casa) e `responseSchema` |
| Classificação de avaliações e perguntas (temas, sentimento, suspeita) | **Gemini 2.5 Flash** | Custo por token baixo, JSON estável | No polling de 30 min, para a resposta; em lote noturno, para a Voz do Cliente; cache de contexto |
| Julgar fotos | **Gemini** multimodal | Julga nitidez, presença de rostos, adequação à categoria e se a foto é mesmo do lugar | `vision.assess_photo(uri)`; nunca gera foto do estabelecimento; só avalia e recorta |
| Redação de posts, respostas a avaliações e perguntas, roteiro do Boletim, as três frases do Diagnóstico | **Cérebro de linguagem** (Claude Sonnet, ou Gemini 2.5 Pro) | Qualidade de texto em PT-BR; escolha por avaliação cega mensal | Camada `LLMGateway.generate(task, tenant)` |
| Verificação cruzada de números antes de sintetizar | **Gemini 2.5 Flash** | Todo número do roteiro tem de existir no JSON de entrada; se não existe, bloqueia a síntese | `LLMGateway` com `task=CROSSCHECK`; devolve `{ok, numeros_fora[]}` |
| Voz do Boletim | **Cloud Text-to-Speech, Chirp 3 HD, pt-BR** | Voz natural, licenciada, estável | Um `voice_id` fixo da casa (`TTS_VOICE_ID`) |
| Ordenar a fila do Guardião | **Gemini 2.5 Flash** | Agrupa itens parecidos e ordena por risco; não aprova nada | Painel do Guardião, em lote, a cada abertura da fila |

**A camada de abstração**

```
LLMGateway
  generate(task: TaskKind, tenant, input, schema?) -> Output
  policy(task) -> {primary: "gemini-2.5-pro"|"gemini-2.5-flash"|"claude-sonnet"|..., fallback: [...], max_cost}
  regras fixas: task in {EXTRACT, MEASURE, CLASSIFY, GOOGLE_DECISION, AUDIO_IN, VISION, CROSSCHECK} => primary DEVE ser Gemini
                (sem fallback para outro cérebro: se o Gemini está fora, a tarefa espera na fila)
  tarefas de linguagem: task in {POST, REPLY_REVIEW, REPLY_QUESTION, BOLETIM, THREE_SENTENCES}
                => primary = LLM_LANGUAGE_PRIMARY, fallback = LLM_LANGUAGE_FALLBACK
  anonimização antes da chamada: nome e número do dono, nome do avaliador -> identificadores internos, salvo tarefa que exige
  telemetria: tokens, custo, latência, versão do prompt, tenant -> BigQuery.llm_calls
```

**Regras de uso dos cérebros**

1. **Saída estruturada sempre** — Todo agente pede JSON com esquema. Texto livre só no artefato final (post, resposta, áudio). Sem JSON válido, o job falha alto e tenta de novo com temperatura menor; na terceira falha, o item vai para o Guardião como exceção, com o erro anexado.
2. **Prompts versionados** — Cada prompt de sistema tem versão semântica e vive no repositório. O Diário de Bordo registra a versão usada em cada ação, e `llm_calls` em cada chamada. Mudar prompt é deploy, com avaliação antes.
3. **Avaliação cega mensal** — Cem amostras por agente, avaliadas por dois humanos sem saber o modelo. O cérebro de linguagem é escolhido pelo resultado, nunca por preferência. As tarefas obrigatórias do Gemini não entram na disputa; entram na auditoria, com a mesma amostra.
4. **Cache de contexto** — Perfil do cliente, tom da casa, termos, raio e regras fixas ficam em cache de contexto do Gemini, renovado a cada 24 h, para reduzir custo em lote. O custo do cache entra em `llm_calls` como qualquer chamada.
5. **Nada de dado pessoal no prompt sem necessidade** — Nome e número do dono, e o nome de quem avaliou ou perguntou, são substituídos por identificadores internos antes de ir ao modelo, exceto quando a tarefa exige (responder a pessoa pelo nome público que ela mesma deixou na avaliação). O modelo nunca recebe o número da casa nem token nenhum.

*Capítulo III · Os conectores*

## COMO A MÁQUINA FALA COM O MUNDO

Um conector por sistema externo. Cada um é um serviço pequeno, com contrato fixo, testes de contrato contra a API real em ambiente de homologação, e telemetria de custo. São quatro conectores e um serviço de entrega: GBP, Places, WA da casa, TTS, e Render & Delivery, que transforma dado em card, mapa, PDF e QR e leva tudo até o dono. Abaixo, o que cada um faz, por qual API, com qual acesso, e onde ele morde.

### GBP Connector — Google Business Profile

- **Para quê:** Ler e editar o perfil (categorias, atributos, lista de serviços, descrição, horários regulares e especiais), publicar posts e fotos, ler e responder avaliações, ler e responder perguntas do perfil, ler desempenho (ligações pelo perfil, pedidos de rota, cliques no site, mensagens pelo perfil, impressões na Busca e no Maps, palavras-chave de descoberta), obter o link oficial de avaliação, descobrir o local no Dia 0 e saber em que estado ele está (verificado, pendente, suspenso).
- **APIs:** **Business Information API v1** (`locations.get` com `readMask`; `locations.patch` com `updateMask` obrigatório e `validateOnly` para ensaiar; `locations.getAttributes` e `locations.updateAttributes`; `attributes.list` para saber quais atributos existem para a categoria e a região; `categories.list` para nomes válidos; campos `regularHours`, `specialHours`, `profile.description`, `serviceItems`, `categories`; `metadata.newReviewUri` e `metadata.mapsUri`; `accounts.locations.list` para descobrir o local no Dia 0) · **Business Profile Performance API v1** (`locations:getDailyMetricsTimeSeries`, uma métrica por chamada, ou `locations:fetchMultiDailyMetricsTimeSeries` para todas de uma vez: `CALL_CLICKS`, `BUSINESS_DIRECTION_REQUESTS`, `WEBSITE_CLICKS`, `BUSINESS_CONVERSATIONS`, `BUSINESS_IMPRESSIONS_DESKTOP_SEARCH`, `BUSINESS_IMPRESSIONS_MOBILE_SEARCH`, `BUSINESS_IMPRESSIONS_DESKTOP_MAPS`, `BUSINESS_IMPRESSIONS_MOBILE_MAPS`; `locations/{id}/searchkeywords/impressions/monthly` para as palavras-chave de descoberta) · **API v4** para avaliações (`accounts.locations.reviews.list` e `.reply`), posts (`accounts.locations.localPosts.create`) e mídia (`accounts.locations.media.create`), ainda em uso para esses recursos · **My Business Q&A API** (`locations.questions.list`, `locations.questions.answers.upsert`) para perguntas e respostas · **Account Management API** (`accounts.list`, `locations.admins.list`) para confirmar que a conta operacional é Gerente · **Verifications API** (`locations.getVoiceOfMerchantState`) para ler se o perfil está verificado, pendente ou suspenso.
- **Acesso e aprovação:** O projeto Google Cloud do Radar Urbano precisa solicitar acesso às Business Profile APIs pelo formulário oficial (prazo típico de uma a duas semanas; é o pedido do dia 1 da semana 1). Autenticação OAuth 2.0 com a conta operacional do Radar Urbano, com 2FA, que recebe papel Gerente em cada perfil de cliente. Escopo `https://www.googleapis.com/auth/business.manage`. Um único refresh token da conta operacional (`GBP_OPERATOR_REFRESH_TOKEN`, no Secret Manager) alcança todos os perfis em que ela é Gerente; o segredo por tenant `tenant-{id}-gbp-oauth` existe para o caso de um cliente exigir credencial dedicada e, por padrão, aponta para o token da casa. Nenhuma senha de cliente, nunca. Se o cliente remove o Gerente, o conector perde o acesso na hora, marca `locations.status` e abre incidente.
- **Cotas e ritmo:** Cotas por projeto e por minuto, baixas por padrão para edição; pedir aumento junto com o acesso quando passar de algumas dezenas de perfis. Leituras de desempenho em lote noturno (03h, D-3..D-1, sempre com `data_referencia`); edições por fila (Cloud Tasks, uma por tenant por vez, retentativa exponencial em 429 e 5xx); polling de avaliações e perguntas a cada 30 min por tenant, com `pageSize` 50 e ordenação por `updateTime`. O desempenho tem atraso típico de dois a três dias e não existe dado em tempo real neste produto: o dashboard mostra as métricas do Google com a data de referência explícita, e o que é próprio (medições, respostas, ações) de hora em hora. Palavras-chave com poucas impressões chegam como faixa (`threshold`), não como número: o Extrato mostra "menos de 15" e não inventa.
- **Termos:** Diretrizes do Perfil da Empresa: nome é o nome real do negócio, sem termo de busca; categoria descreve o que o negócio é, não o que ele quer ranquear; horários verdadeiros; fotos do lugar de verdade; posts sem promessa e sem oferta não autorizada. Política de avaliações: sem incentivo, sem seleção, respostas verdadeiras, sem expor dado do avaliador; avaliação suspeita é denunciada pelo fluxo oficial do Google, nunca respondida com acusação. Perguntas do perfil são públicas: a resposta fala em nome da empresa e só do que é fato do perfil.
- **Armadilhas:** Nunca alterar categoria principal sem aprovação humana (impacto grande). Nunca inserir termos de busca no nome do negócio (suspensão). Toda edição gera diff antes e depois no Diário de Bordo, e `profile_audits` guarda campo, antes, depois e origem. `patch` sem `updateMask` apaga o que não foi enviado: o conector recusa a chamada. Detectar `SUSPENDED` ou `PENDING_VERIFICATION` no estado do local e abrir incidente; `hasGoogleUpdated` indica que o Google alterou algo por conta própria, e o Editor revisa antes de sobrescrever. Nota de avaliação chega como enum (`ONE` a `FIVE`): o conector converte para 1 a 5 antes de gravar. Foto e post precisam de URL pública para o Google buscar: URL assinada de curta duração no Cloud Storage, nunca bucket aberto. Os recursos ainda na API v4 podem migrar: por isso vivem atrás do conector, e a troca é local.

### Places Connector — Places API (New)

- **Para quê:** Medir posição por termo e ponto da grade para o Cartógrafo: medição reduzida no Dia 0 (Diagnóstico de Posição), no Dia 7 (Antes e Depois) e aos sábados (termos-chave); medição completa no dia 1 (Mapa de Domínio). Confirmar no Dia 0 que o `place_id` do perfil é o lugar certo. Nada mais: este conector não lê dados de outros lugares.
- **Endpoints:** `places:searchText` com `textQuery` (o termo, como o cliente digita), `locationBias` circular por ponto da grade (centro no ponto, raio igual ao passo), `rankPreference` padrão (relevância), `languageCode=pt-BR`, `regionCode=BR`, `pageSize=20`, e máscara de campos mínima: `places.id` (na amostra de validação, também `places.displayName`) · `places/{place_id}` só no Dia 0, com máscara `id,displayName,formattedAddress`, para casar o perfil do cliente com o lugar.
- **Acesso e aprovação:** Chave de API restrita à Places API (New) e ao IP de saída do Cloud Run (Cloud NAT com IP fixo); guardada como `PLACES_API_KEY` no Secret Manager; faturamento no projeto do Radar Urbano. Não exige aprovação: ativa na hora. Monitorar SKUs: com máscara só de IDs, a busca por texto cai no SKU mais barato, e a cota gratuita mensal cobre os primeiros clientes. A chave nunca vai para o dashboard nem para qualquer código que rode no navegador.
- **Cotas e ritmo:** Uma chamada por termo por ponto. Grade de 3×3 a 5×5 sobre o raio do cliente (3×3, nove pontos, para raio de bairro, como nos exemplos deste manual; 5×5 para quem atende uma região maior); até 25 termos por tenant. A medição completa típica é nove pontos × 12 a 15 termos; a reduzida de sábado, nove pontos × 3 a 5 termos-chave; a do Dia 0 e a do Dia 7, nove pontos × os dois ou três termos-chave. Somadas, na casa de 240 chamadas por tenant por mês, como no exemplo das Horas Devolvidas. Fila com ritmo de poucas chamadas por segundo, retentativa exponencial em 429. Custo de referência: R$ 3–8 por cliente por mês, limitado por configuração em `limites_json`.
- **Termos:** Sem extração em massa; sem raspagem do Maps. O conteúdo de lugares não é armazenado além de 30 dias, exceto `place_id`, que é armazenável. Neste produto guardamos: `place_id`, data, termo, ponto da grade, latitude e longitude do ponto, posição. Não guardamos nome, nota nem contagem de avaliações de outros lugares; a lista devolvida pela API vive só na memória do job, o tempo de achar o índice do cliente. Nada da Places API é exibido ao cliente: o Mapa de Domínio mostra a posição do próprio perfil, calculada por nós.
- **Método de aferição:** Grade de 3×3 a 5×5 pontos sobre o raio do cliente, ponto central no endereço, passo = raio ÷ 2 na grade 5×5 e passo = raio na 3×3, de modo que a borda da grade cai sobre o raio do cliente; para cada termo, `searchText` com viés no ponto; posição = índice do `place_id` do cliente no resultado, de 1 a 20, ou "não encontrado" além de 20. Cores: verde = top 3, cinza = 4º a 10º, vermelho = fora do top 10 ou não encontrado no top 20. A busca por texto na API é um proxy da lista local do Maps; o Mapa de Domínio declara isso no rodapé. Validação mensal com amostra manual de 20 buscas (concordância ≥ 85% no top 3), registrada em `qa_samples`. Medições sempre no mesmo horário (02h no dia 1, 03h no sábado) para serem comparáveis mês a mês.
- **Armadilhas:** `locationBias` é viés, não cerca: a lista pode trazer lugares fora do raio, e é assim que o usuário vê; `locationRestriction` distorceria a medida. `rankPreference=DISTANCE` ignora relevância e mede outra coisa. Sem `languageCode` e `regionCode`, o mesmo termo devolve listas diferentes. Não paginar além dos 20 primeiros: custo sem informação, porque além de 20 é vermelho de qualquer jeito. O `place_id` de um perfil pode mudar quando o Google funde locais: o Dia 0 e a auditoria mensal reconfirmam pelo `metadata.mapsUri` do GBP. Chave vazada é custo sem teto: restrição por IP e alerta de orçamento no projeto.

### WA Connector — o número da casa

- **Para quê:** Falar com o dono, e só com ele. Uma única conta do Radar Urbano na WhatsApp Business Platform (Cloud API), com um número da empresa: o número da casa. Por ele saem as entregas (áudio do Boletim, cards PNG, PDFs, o Diagnóstico de Posição minutos depois do acesso), as perguntas de sim ou não (categoria principal, nome, endereço), os avisos de uma linha do Diário e os lembretes de pendência do onboarding. Por ele entram as cinco respostas em áudio do Dia 0, o Sim, o Não, o SAIR e qualquer texto livre do dono. Nunca fala com cliente final. Nunca fala em nome da empresa do cliente.
- **Endpoints:** `POST /{phone_number_id}/messages` (tipos `template`, `audio`, `image`, `document`, `interactive` com botões de resposta) · `POST /{phone_number_id}/media` para subir OGG, PNG e PDF antes de enviar, ou `link` assinado no objeto de mídia · `GET /{media_id}` e download do áudio recebido do dono no Dia 0 · webhooks `messages` (respostas do dono) e `statuses` (`sent`, `delivered`, `read`, `failed`) · `GET/POST /{waba_id}/message_templates` · `GET /{waba_id}/phone_numbers` para ler `quality_rating` e `messaging_limit_tier` do número da casa.
- **Acesso e aprovação:** Portfólio de negócios do Radar Urbano no Gerenciador da Meta, com a empresa verificada (CNPJ e documentos; começa no dia 1 da semana 1, porque demora). App na Meta for Developers com o produto WhatsApp. Conta do WhatsApp Business do Radar Urbano com um número dedicado, novo, que não esteja no aplicativo comum; nome de exibição "Radar Urbano" aprovado. Usuário de sistema com token permanente e permissões de mensagens e de gestão da conta, guardado como `META_SYSTEM_USER_TOKEN`; `META_APP_ID/SECRET` para validar a assinatura dos webhooks; `WA_WEBHOOK_VERIFY_TOKEN` para o aperto de mão; `DELIVERY_SENDER_PHONE_ID` é o número da casa. O cliente não cadastra nada na Meta: não há conta dele, não há parceria, não há fluxo de cadastro do lado dele. Ele só informa o número em que quer receber e diz Sim.
- **Modelos e janelas:** Mensagem iniciada pela empresa exige modelo aprovado e consentimento prévio; o dono consente no Dia 0 (o Sim à confirmação por escrito das cinco respostas, registrado com data, hora, texto e canal em `tenants`) e sai a qualquer momento com uma palavra (SAIR). Mensagem livre (áudio OGG, imagem, documento, texto) só dentro da janela de 24 h aberta por uma mensagem do dono, e um toque em botão de resposta rápida conta como mensagem dele. Os modelos, todos na categoria utilidade: `boletim_segunda` (cabeçalho de vídeo de 60 s com o card parado e a voz da casa por cima; corpo com os números da semana e a data de referência; botão que abre o dashboard), `entrega_radar` (cabeçalho de imagem, para os cards do dia 1; corpo de uma linha) e a versão `entrega_radar_pdf` (cabeçalho de documento, para os PDFs; a Meta não aceita um modelo com dois formatos de cabeçalho), `pergunta_sim_nao` (corpo com a pergunta e botões de resposta rápida Sim e Não), `aviso_radar` (uma linha, um parâmetro). O Delivery usa a janela quando ela está aberta e o modelo quando não está: no Dia 0 a janela está aberta pelos áudios do dono, e é assim que o Diagnóstico chega na mesma conversa, em minutos, como card e PDF livres; na segunda-feira, se o dono respondeu algo nas últimas 24 h, o card PNG e o áudio OGG vão livres, como nota de voz; se não, vai o modelo `boletim_segunda`, e o dono ouve do mesmo jeito, na mesma hora, com um toque. O Delivery registra qual caminho usou.
- **Cotas e ritmo:** Cerca de 25 mensagens de utilidade por dono por mês: 4 a 5 Boletins, 6 entregas do dia 1, uma linha do Diário quando há ação relevante, uma pergunta de vez em quando. O limite de conversas por 24 h do número sobe por faixa com o volume e a qualidade; com a empresa verificada, a primeira faixa já cobre centenas de donos por dia. Envios entre 7h e 8h na segunda e até 8h no dia 1, em fila, poucos por segundo. Custo de referência: R$ 1–2 por cliente por mês.
- **Armadilhas:** Categoria errada de modelo multiplica custo e arrisca rejeição: os modelos falam do serviço contratado, nunca de promoção. O `quality_rating` do número cai com bloqueios e denúncias: SAIR é honrado na hora (`tenants.wa_optout`), os avisos param antes do Boletim, e um número reserva só entra com aprovação do Head. Um número na plataforma sai do aplicativo comum: o número da casa é dedicado, nunca o celular de alguém. Áudio precisa ser `audio/ogg` com codec Opus; imagem em PNG até 5 MB; PDF como documento com nome de arquivo legível; vídeo em MP4 até 16 MB. O número do dono entra nas tabelas analíticas só como `dono_wa_hash`; o valor claro fica no documento do tenant, legível apenas pelo Delivery. Texto livre do dono não é respondido por modelo nenhum: vira transbordo para o Guardião e o Head, com resposta humana. O token de sistema é um só para a casa: rotação a cada 90 dias e alerta se aparecer em log.

### TTS e Render & Delivery — voz, arquivos, dashboard e entrega

- **Voz:** Cloud Text-to-Speech com voz Chirp 3 HD em pt-BR, `voice_id` fixo da casa (`TTS_VOICE_ID`), o mesmo para todos os clientes: a voz é do Radar Urbano, não da padaria, e nunca imita ninguém. Saída `OGG_OPUS` a 48 kHz, o formato que o WhatsApp toca. Duração máxima 60 s: o Redator-chefe corta o roteiro por contagem de palavras (≤ 150) antes de sintetizar, e o conector mede a duração do arquivo e recusa acima de 60 s. Números e horas vão por extenso no roteiro ("cento e dezoito ligações", "sete e dois") porque a voz lê o que está escrito; pausas por pontuação; SSML só se a voz escolhida aceitar. Quando o Boletim vai por modelo, o Render & Delivery junta o card e o OGG em um MP4 de 60 s (imagem parada, faixa de voz); o OGG continua sendo o arquivo guardado e o que toca no dashboard. Cada síntese grava custo em `llm_calls` com `task=TTS`.
- **Cards e mapas:** Renderização server-side (HTML → PNG com Chrome headless no Cloud Run) a partir de templates versionados no repositório, um por entrega: Diagnóstico, Antes e Depois (lado a lado), Boletim (cinco números com seta), Mapa de Domínio, Horas Devolvidas (com a tabela de equivalência no rodapé), Voz do Cliente, Boletim de Reputação. O Mapa de Domínio é SVG gerado do BigQuery (`rank_measurements` do mês) por `render.map_svg`: grade de pontos sobre o raio, verde, cinza e vermelho, legenda e rodapé com o método; a versão PNG vai pelo WhatsApp e a SVG, interativa, vive no dashboard. Todo card traz nome do cliente, período e a data de referência dos dados do Google.
- **PDFs:** Diagnóstico de Posição (Dia 0), Extrato de Demanda, Fechamento Executivo (mensal e trimestral) e o material do QR: HTML → PDF com Chrome headless, uma página, template com a marca do Radar Urbano e o nome do cliente; arquivo no Cloud Storage (`radar-{ambiente}-artefatos/{tenant_id}/{entrega}/{periodo}.pdf`), URL assinada de 30 dias para o envio e cópia permanente no dashboard. O Extrato explica em uma linha que "ligações pelo perfil" são toques no botão Ligar contados pelo Google, não ligações atendidas.
- **QR e link curto:** `gbp.get_review_link` lê o link oficial "Receber mais avaliações" do perfil (`metadata.newReviewUri`) e `render.qr(tenant)` gera o QR e um PDF de balcão e de comanda com o nome da casa e uma frase neutra ("Avalie a sua experiência"). Sem prêmio, sem condição, sem filtro: quem lê o QR cai na tela pública do Google. O PDF vai ao dono por `entrega_radar` na primeira semana, fica no dashboard e é reenviado quando ele pedir. É o único jeito de pedir avaliação que existe neste produto: passivo, no balcão, à vista de todo mundo.
- **Dashboard:** Aplicação web (Next.js no Cloud Run) por tenant, link único com token de acesso (`DASHBOARD_BASE_URL/t/{token}`), ícone na tela inicial do celular, e opção de senha criada pelo cliente no Identity Platform (link mágico enviado pelo número da casa; senha nova, nunca a de outro sistema; ninguém da operação a vê). Lê BigQuery por visões materializadas atualizadas de hora em hora pelo Tesoureiro; não lê nada em tempo real porque não há dado em tempo real. Seções: os números (com data de referência e o aviso de atraso), Mapa de Domínio interativo, Diário de Bordo completo com prints, Voz do Cliente, Boletim de Reputação, arquivos (todos os PDFs e cards), Horas Devolvidas, custo por contato do mês. Cada abertura registra `lido_em` em `deliveries`.
- **Delivery:** Serviço único `Delivery` que recebe (tenant, entrega, período, artefatos, canal), decide entre janela aberta e modelo, escolhe o modelo certo para o artefato (imagem, documento ou vídeo), sobe a mídia, envia pelo WA Connector ao número do dono e grava em `deliveries` os carimbos `enviado_em`, `entregue_em`, `lido_em` a partir do webhook `statuses`, com linha no Diário de Bordo. Chave idempotente (`tenant + entrega + período`): nunca envia duas vezes. Reenvio automático uma vez após 2 h sem `delivered`; depois, incidente. Respeita `wa_optout` e a janela de envio (7h às 8h na segunda; até 8h no dia 1). Fila pelo tópico `deliveries.send`; falha de modelo ou de mídia volta para a fila com retentativa e aparece no painel do Guardião.

*Capítulo IV · A fundação*

## O TERRENO ONDE A MÁQUINA É MONTADA

Tudo roda no Google Cloud, no mesmo projeto em que vive o Gemini, por simplicidade de identidade, faturamento e rede. Dois ambientes: homologação e produção. Infraestrutura como código desde o primeiro dia. Fora do Google Cloud só existem quatro coisas: a conta da Meta para o número da casa, o provedor de pagamento, o GitHub onde vive o código e, se a avaliação cega escolher, o cérebro de linguagem.

| Peça | Escolha | Papel |
|---|---|---|
| Projeto e ambientes | Google Cloud, projetos `radar-hml` e `radar-prd`, região `southamerica-east1` | Isolamento, dados no Brasil, faturamento separado |
| APIs habilitadas | Vertex AI, Places API (New), Business Profile APIs (após aprovação), Cloud Text-to-Speech, Cloud Run, Cloud Build, BigQuery, Firestore, Secret Manager, Cloud Scheduler, Pub/Sub, Identity Toolkit | Tudo que a máquina chama; nada além disso |
| Execução | **Cloud Run** (serviços: webhooks do número da casa, dashboard, painel do Guardião, renderização) e **Cloud Run Jobs** (agentes em lote) | Escala a zero; um container por agente |
| Agentes | **Agent Development Kit (ADK)** em Python, com ferramentas expostas pelos conectores; opção de hospedar no **Vertex AI Agent Engine** | Padrão Google para agentes com Gemini; sessões, ferramentas, avaliação |
| Orquestração | **Cloud Scheduler** (cadências) → **Pub/Sub** (tópicos por evento) → Jobs; **Cloud Tasks** para filas com retentativa por tenant | Cadência fixa, retentativa, idempotência |
| Estado e filas | **Firestore** (documento por tenant: configuração, limites pré-autorizados, tom, segmento e zona, estado do onboarding, consentimento do dono, aprovações pendentes) | Baixa latência; a fonte do que a máquina pode fazer sem perguntar |
| Dados analíticos | **BigQuery** (particionado por data, clusterizado por `tenant_id`) | Métricas, medições, extratos, séries, Diário, custos, zonas |
| Calendário | Tabela própria de feriados nacionais e municipais, uma linha por cidade e data, mantida pela operação e lida por `calendar.holidays` | O Editor ajusta o horário e publica o post 72 h antes |
| Arquivos | **Cloud Storage** (buckets por ambiente, prefixo por tenant, ciclo de vida de retenção) | Fotos, prints, PDFs, cards, áudios, QR |
| Segredos | **Secret Manager** (refresh token da conta operacional, token de sistema da Meta, chave da Places API, um segredo por tenant) | Credenciais por uso; nunca senha de cliente |
| Identidade | **Identity Platform** para o dashboard do cliente e o painel do Guardião | Senha criada pelo cliente; login por link mágico; papéis internos com 2FA |
| Observabilidade | **Cloud Logging, Error Reporting, Cloud Monitoring**; tabela `llm_calls` no BigQuery; painel interno de custo por tenant com alerta em R$ 25 | Falha alta, custo visível |
| Código e deploy | GitHub → Cloud Build → Cloud Run; Terraform para infraestrutura; prompts e templates no repositório com versão | Tudo revisável, tudo reproduzível |

**Modelo de dados (BigQuery, tabelas principais)**

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

O que cada tabela guarda, e por quê:

- **`tenants` e `zones`**: o tenant carrega `segmento` e `zona`; `zones` conta os ativos por par e trava em `limite=2`. `zone.check` lê `zones` antes de criar o tenant; o tópico `zone.changed` avisa quando um tenant entra, sai ou muda de zona, e a contagem é refeita.
- **`locations`**: o elo entre o perfil (`gbp_location_id`) e o lugar (`place_id`); `status` guarda o estado lido do Google (verificado, pendente, suspenso) e é o gatilho do runbook de perfil suspenso.
- **`metrics_daily`**: uma linha por tenant por dia, coletada em D-3..D-1; `call_clicks` são toques no botão Ligar, `directions` pedidos de rota, `website_clicks` cliques no site, `conversations` mensagens pelo perfil; os quatro somam os contatos do mês. As impressões são contexto e não entram na soma. `data_referencia` é a data a que o número se refere; `coletado_em`, quando o buscamos.
- **`keywords_monthly`**: as palavras-chave de descoberta do Performance API, uma linha por termo por mês; impressões abaixo do limiar do Google entram como faixa, nunca como número inventado.
- **`rank_measurements`**: uma linha por termo por ponto por medição; `posicao` de 1 a 20, ou nula quando não encontrado; é a única coisa que sobra da Places API, e é dela que saem o Diagnóstico, o Antes e Depois, o Boletim de sábado e o Mapa de Domínio.
- **`reviews` e `questions`**: texto só como hash, temas e sentimento; `respondida_em` e `resposta_id` provam a resposta e alimentam os SLOs de 2 h e de 4 h.
- **`posts` e `profile_audits`**: o que foi publicado, com que foto e quem aprovou; e cada mudança de campo com antes, depois e origem (Cartógrafo, Editor, Guardião, Google). É de `profile_audits` que sai o Antes e Depois do Dia 7.
- **`actions_log`**: o Diário de Bordo; só `INSERT`; toda linha tem `print_uri`; dela saem as Horas Devolvidas, cruzando `acao` com `hours_equivalence`.
- **`deliveries`, `llm_calls`, `qa_samples`**: prova de entrega com três carimbos de hora; custo e latência de cada chamada de modelo e de voz; vereditos da amostragem de 10% do Guardião e das 20 buscas manuais do Cartógrafo.

**Tenancy e segurança de base**

1. **Um documento Firestore por tenant** — `tenants/{tenant_id}` com configuração, limites pré-autorizados (o que a máquina faz sem perguntar), tom da casa, termos e raio, `segmento` e `zona`, estado do onboarding (`created` → `billing_active` → `profiled` → `gbp_linked` ou `gbp_pending_verification` → `live`), consentimento e opt-out do dono, e subcoleções `approvals` (itens para o Guardião) e `queue` (tarefas por agente). O documento nasce só depois de `zone.check` aprovar a zona; se a zona está lotada, o pedido vai para a lista de espera da zona e nenhum tenant é criado.
2. **Segredos por tenant** — `projects/*/secrets/tenant-{id}-gbp-oauth`, por padrão apontando para a credencial da conta operacional. Os segredos da casa (`GBP_OPERATOR_REFRESH_TOKEN`, `META_SYSTEM_USER_TOKEN`, `PLACES_API_KEY`) são únicos e lidos só pelo conector dono de cada um. Rotação a cada 90 dias; revogação no offboarding é um job, junto com a remoção do Gerente, a exportação do histórico e a liberação da vaga na zona.
3. **Contas de serviço mínimas** — Uma conta de serviço por agente e por conector, com acesso só às tabelas e segredos que usa. O Editor não lê `metrics_daily`; o Tesoureiro não escreve em `posts`; só o WA Connector lê o token da Meta; só o Delivery lê o número claro do dono; ninguém tem `UPDATE` ou `DELETE` em `actions_log`.
4. **Hash de dados pessoais** — O número do dono entra em `tenants.dono_wa_hash` como hash com sal por tenant; o valor claro fica no documento do tenant, em campo restrito ao Delivery. Textos de avaliações e perguntas entram como `texto_hash` mais temas e sentimento; o texto original é lido da API do Google na hora de responder e não fica em tabela nossa. Nenhuma tabela guarda nome de avaliador. Não existe cliente final na base: a máquina não conversa com ele.

*Capítulo V · Os agentes*

## CADA AGENTE, POR DENTRO

Seis peças: cinco agentes e um humano com painel. Para cada um: missão, gatilho, entradas, ferramentas, cérebro, esqueleto do prompt de sistema, saídas, guardrails, métricas e o teste que diz "montei". Todos os agentes são construídos com o Agent Development Kit, com ferramentas que são funções dos conectores: nenhum agente chama API direto, e nenhum agente fala com o dono por conta própria, só pelo serviço `Delivery` e pelo número da casa. Duas ausências são de propósito. A vigilância de calendário (feriado a 72 h vira horário e post) não é um agente: é uma rotina diária do Editor. Convite de avaliação não existe: o Anfitrião responde, não convida. Os patamares P0, P1 e P2 são os do Capítulo I: até o P1, tudo passa pelo Guardião em lote; no P2, aprovação por exceção com amostragem de 10%.

### Cartógrafo Medir a posição e o território, fazer o diagnóstico e dizer ao Editor o que otimizar.

- **Gatilho:** Dia 0, minutos depois de `gbp_linked` (medição reduzida, para o Diagnóstico de Posição); Dia 7 do tenant (medição reduzida, para o Antes e Depois); sábado, 03h (medição reduzida dos termos-chave, para o Boletim); dia 1, 02h (medição completa, para o Mapa de Domínio). A reduzida usa grade 3×3 e até 5 termos-chave; a completa usa a grade do tenant (3×3 a 5×5) e todos os termos.
- **Entradas:** `tenants` (`termos[]`, `raio_m`, `segmento`, `zona`, `limites_json` com o teto de chamadas à Places API), `locations` (`place_id`, `gbp_location_id`, `status`), `keywords_monthly` (palavras-chave de descoberta do Performance API), `rank_measurements` do mês anterior (para a variação), grade de pontos gerada a partir do raio.
- **Ferramentas:** `places.search_text(termo, lat, lng, raio)` · `gbp.get_keywords(tenant, mes)` · `gbp.get_location(tenant)` · `render.map_svg(tenant, mes)` · `render.card` (edição reduzida do mapa) · `cost.per_tenant(tenant, periodo)` · `diario.log(...)`.
- **Cérebro:** **Gemini Pro** com Grounding com Google Maps para interpretar o território, propor termos e montar o diagnóstico; **Gemini Flash** para normalizar as respostas da Places API e do Performance API em JSON com esquema. Nenhum cérebro de linguagem: o Cartógrafo entrega números e listas, não prosa.
- **Prompt de sistema (esqueleto):** "Você é o Cartógrafo. Recebe medições de posição por termo e ponto da grade (posição do place_id do cliente em cada ponto, ou 'não encontrado' quando fora do top 20), as palavras-chave de descoberta com impressões e o perfil atual. Classifique cada ponto: verde = top 3, cinza = 4º a 10º, vermelho = fora do top 10 ou não encontrado. Devolva JSON: {territorio: [{termo, pontos_verde, pontos_cinza, pontos_vermelho, variacao_mes}], diagnostico: {termos_no_top3, termos_fora, maior_lacuna}, oportunidades: [{termo, motivo, acao_sugerida}], auditoria_perfil: [{campo, atual, sugerido, impacto}], nap_consistente: bool}. Não invente termos sem impressões. Não compare com outros lugares nem cite outro perfil. Não sugira inserir termos no nome do negócio. Não prometa posição."
- **Saídas:** `rank_measurements` (tenant_id, data, termo, grid_point, lat, lng, posicao); Mapa de Domínio em SVG (dashboard) e PNG (WhatsApp), com edição reduzida no Dia 0 e no Dia 7; JSON do Diagnóstico de Posição para o Redator-chefe; lista de otimizações para o Editor no tópico `editor.tasks`; sugestão de categoria para o Guardião; variação mês a mês de pontos verdes.
- **Guardrails:** Máximo de 25 termos por tenant; grade máxima 5×5; chamadas à Places API por tenant e mês = termos × pontos, limitadas em `limites_json` (acima do teto, reduz a grade antes de reduzir termos); grava só o `place_id` do cliente, data, termo, ponto e posição: nada de nota, contagem ou `place_id` de outros lugares, e nada de conteúdo da Places API além de 30 dias; qualquer sugestão de categoria principal vai para o Guardião; nunca cita outro perfil pelo nome em nenhuma saída; a medição do Dia 0 sai mesmo com o perfil em `gbp_pending_verification`, porque o `place_id` público basta para medir.
- **Métricas:** Custo de medição por tenant; cobertura da grade (pontos medidos ÷ pontos planejados); variação mês a mês de pontos verdes; concordância com a validação manual de 20 buscas; taxa de sugestões aceitas pelo Editor e pelo Guardião; duração da medição reduzida (meta: menos de dois minutos, para caber nos minutos 8 a 10 do Dia 0).
- **Teste de aceitação:** Para um tenant de teste com `place_id` conhecido, o Mapa de Domínio reproduz a posição de 20 buscas manuais com concordância ≥ 85% no top 3; a medição reduzida termina em menos de dois minutos; `rank_measurements` não contém nenhum `place_id` que não seja o do tenant.

### Editor Manter o perfil vivo: posts, fotos, descrição, horários e feriados, serviços, atributos.

- **Gatilho:** Segunda, 04h (post da semana); diário, 05h (checagem de horários e feriados: a sentinela de calendário, que age 72 h antes); eventos `editor.tasks` do Cartógrafo (Dia 0, Dia 7, dia 1) e da Voz do Cliente (atrito que a máquina resolve no próprio perfil); Dia 0 (auditoria de completude, para o Diagnóstico de Posição); Dia 7 (diff do perfil, para o Antes e Depois); dia 1 (auditoria mensal do perfil). Eventos `approvals.decided` do Guardião publicam o que foi aprovado.
- **Entradas:** Tom da casa (`tom_json`), limites pré-autorizados (`limites_json`: o que publica sem perguntar, padrão de horário em feriado), perfil atual (`gbp.get_location`), fotos existentes (mídia atual do perfil e Cloud Storage do tenant), calendário de feriados (tabela própria, nacional e municipal por cidade, lida por `calendar.holidays`), tarefas do Cartógrafo, `profile_audits` (histórico de cada campo, antes e depois).
- **Ferramentas:** `gbp.get_location(tenant)` · `gbp.create_post(tenant, texto, foto_uri)` · `gbp.upload_media(tenant, uri)` · `gbp.patch_location(tenant, campos)` · `gbp.update_hours(tenant, horarios)` · `gbp.update_services(tenant, itens)` · `calendar.holidays(cidade, de, ate)` · `vision.assess_photo(uri)` · `guardiao.submit(tenant, item, risco)` · `diario.log(...)` · `render.card` (Antes e Depois) · `delivery.send` (pergunta de sim ou não e aviso de uma linha).
- **Cérebro:** Cérebro de linguagem (Claude Sonnet ou Gemini Pro, escolhido pela avaliação cega mensal) para o texto de post e de descrição; **Gemini** multimodal para julgar fotos (nitidez, rosto, adequação à categoria); **Gemini** para qualquer decisão de campo do perfil (categoria, atributo, serviço, horário), porque é decisão que toca a API do Google.
- **Prompt de sistema (esqueleto):** "Você é o Editor da {casa}. Tom: {tom}. Nunca prometa resultado, posição ou desconto não autorizado. Nunca use termos de busca no nome. Nunca invente preço, serviço ou horário: use só {fatos_da_casa} e {limites}. Gere: post de até 300 caracteres com chamada suave, sugestão de foto entre as disponíveis (nunca gerar foto do estabelecimento) e a justificativa em uma linha. Para feriado a 72 h: horário proposto a partir do padrão da casa, post de aviso de até 200 caracteres com o horário, e a data de publicação. Marque requer_guardiao para categoria, nome, endereço ou feriado sem padrão. JSON: {post, foto_uri, justificativa, horario_feriado, publicar_em, requer_guardiao: bool}."
- **Saídas:** Itens na fila do Guardião (P0/P1) ou publicação direta (P2), sempre com linha no Diário de Bordo e print da tela pública; `posts`; `profile_audits` (campo, antes, depois, origem); horários de feriado aplicados; auditoria de completude (lista de campos vazios ou fracos, com peso, no Dia 0 e a cada dia 1); diff do perfil do Dia 7; linha curta ao dono pelo número da casa quando há ação relevante (`aviso_radar`).
- **Guardrails:** Só fotos com `vision.assess_photo.ok = true` e sem rosto sem termo; mudanças de categoria principal, nome e endereço sempre para o Guardião (regra dos dois olhos); máximo de 1 post por dia; descrição respeita o limite de caracteres do produto; serviços entram como lista, sem preço; feriado sem padrão em `limites_json` vira uma pergunta de sim ou não ao dono (modelo `pergunta_sim_nao`) com o horário proposto, e sem resposta até 24 h antes o horário normal fica e o Diário registra; nada é publicado em perfil `SUSPENDED` ou `PENDING_VERIFICATION` (a fila congela e abre incidente); nunca cita outro perfil.
- **Métricas:** Taxa de aprovação sem edição (meta > 85% no P1); posts por semana; tempo fila → publicação; feriados tratados com 72 h ou mais de antecedência (meta 100%); completude do perfil (campos preenchidos ÷ campos auditados) no Dia 0, no Dia 7 e a cada dia 1.
- **Teste de aceitação:** Uma semana de tenant de teste gera 1 post aprovado; um feriado inserido no calendário de teste vira ajuste de horário e post 72 h antes, com aviso de uma linha ao dono; o Diário mostra 100% das ações com print; nenhum campo sensível muda sem aprovação.

### Anfitrião Responder todas as avaliações em até 2 h, responder perguntas do perfil, ler o que o bairro diz.

- **Gatilho:** Polling de avaliações e perguntas a cada 30 min (`gbp.list_reviews`, `gbp.list_questions`; novidade publica `gbp.review.new` e `gbp.question.new`); lote noturno de classificação (temas e sentimento); dia 1 (Boletim de Reputação e classificação do mês para a Voz do Cliente); primeira semana, assim que o tenant está `gbp_linked` (link curto oficial e QR do balcão). Eventos `approvals.decided` publicam as respostas que passaram pelo Guardião.
- **Entradas:** Avaliações (API v4), perguntas públicas (My Business Q&A API), tom da casa, fatos da casa do Dia 0 (o que vende, horários, o que pode responder), nome do responsável e canal para onde convidar quem reclamou (o telefone da casa ou o balcão), regras da política de avaliações e de conteúdo do Google, `limites_json`.
- **Ferramentas:** `gbp.list_reviews(tenant, desde)` · `gbp.reply_review(tenant, review_id, texto)` · `gbp.list_questions(tenant, desde)` · `gbp.answer_question(tenant, question_id, texto)` · `gbp.get_review_link(tenant)` · `render.qr(tenant)` · `render.pdf` (material do balcão) · `render.card` (Boletim de Reputação) · `classify.review(texto)` · `guardiao.submit` · `diario.log`.
- **Cérebro:** **Gemini Flash** para classificar (temas, sentimento); cérebro de linguagem para redigir a resposta; **Gemini** para detectar violação de política (avaliação falsa, spam, conteúdo proibido, dado pessoal exposto) e sinalizar ao Guardião, que denuncia pelo fluxo do Google.
- **Prompt de sistema (esqueleto):** "Você responde avaliações e perguntas públicas em nome da {casa}. Regras: agradecer sem repetir chavão, responder ao ponto específico, nunca oferecer compensação, nunca expor dados do avaliador, nunca discutir, nunca pedir que mude a nota. Nota ≤ 3: pedir desculpa, explicar sem justificar, convidar a falar com {responsavel} pelo {canal}. Pergunta: responder só com o que está no perfil ou em {fatos_da_casa}; se não souber, diga que a casa vai confirmar e marque exige_humano. Até 400 caracteres. JSON: {resposta, tom_detectado, temas[], sentimento, suspeita_de_violacao: bool, exige_humano: bool}."
- **Saídas:** Respostas publicadas no próprio Google; `reviews` e `questions` atualizadas (`texto_hash`, `temas[]`, `sentimento`, `respondida_em`, `resposta_id`); linha no Diário de Bordo para cada resposta, inclusive a perguntas; Boletim de Reputação (card, dia 1); classificação do mês para a Voz do Cliente; sinal de avaliação suspeita para o Guardião; link curto oficial "Receber mais avaliações" e QR em PDF para o balcão ou a comanda.
- **Guardrails:** Não existe convite ativo: o Anfitrião nunca manda mensagem a cliente final; o material do balcão é passivo e o link é o oficial do Google, sem encurtador próprio que rastreie a pessoa; responde todas, nunca seleciona; respostas a notas ≤ 2 passam pelo Guardião mesmo no P2; nunca cita dado do avaliador, nunca oferece compensação, nunca pede nota; texto de terceiros entra nas tabelas só como hash e temas; pergunta fora dos fatos da casa vira pendência humana, não invenção; duas respostas à mesma avaliação são impossíveis por construção (chave por `review_id`).
- **Métricas:** Tempo mediano de resposta a avaliações (meta < 2 h; 100% em 24 h); perguntas respondidas em < 4 h; avaliações novas por semana; nota média; taxa de edição pelo Guardião; avaliações sinalizadas por mês.
- **Teste de aceitação:** Avaliação de teste inserida em perfil de homologação é respondida em < 2 h com texto aprovado; pergunta de teste ("vocês têm estacionamento?") é respondida em < 4 h com o dado do perfil; o QR de teste abre a tela oficial de avaliação do perfil; nenhuma mensagem sai para nenhum número que não seja o do dono.

### Tesoureiro Consolidar tudo em número: dashboard, Extrato de Demanda, Horas Devolvidas, custo.

- **Gatilho:** A cada hora (visões do dashboard); diário, 03h (coleta do Performance API, D-3..D-1, com data de referência); dia 1, 05h (Extrato de Demanda, Horas Devolvidas, custo por tenant, JSON do mês para o Redator-chefe); segunda, 06h (JSON da semana para o Boletim); evento `cost.alert` quando um tenant passa de R$ 25 no mês.
- **Entradas:** `metrics_daily`, `keywords_monthly`, `rank_measurements`, `reviews`, `questions`, `actions_log`, `llm_calls`, `hours_equivalence`, `deliveries` (status de entrega e as respostas Sim/Não do dono, para o tempo do dono).
- **Ferramentas:** `gbp.get_daily_metrics(tenant, de, ate)` · `gbp.get_keywords(tenant, mes)` · `render.pdf(extrato_demanda)` · `render.card(horas_devolvidas)` · `cost.per_tenant(tenant, periodo)` · `diario.log`.
- **Cérebro:** **Gemini Flash** para normalizar a resposta do Performance API em linhas de `metrics_daily`; **Gemini Pro** só para redigir as três frases de leitura do extrato. Todos os números vêm de SQL, nunca do modelo.
- **Prompt de sistema (esqueleto):** "Você escreve três frases sobre este extrato, sem nenhum número que não esteja no JSON de entrada, sem estimar conversão, receita ou 'novos clientes', sem promessa. Chame os toques em Ligar de 'ligações pelo perfil'. Destaque a maior variação e o custo por contato. Diga até que data vão os dados do Google."
- **Saídas:** Visões materializadas do dashboard (seis números com setas e data de referência); `metrics_daily` (com `data_referencia` e `coletado_em`); Extrato de Demanda (PDF de uma página, série de 6 meses); Horas Devolvidas (card com a tabela de equivalência no rodapé); custo por tenant e alerta em R$ 25; JSON da semana e do mês para o Redator-chefe.
- **Guardrails:** Nenhum número gerado por modelo; contadores reconciliados com as fontes (diferença < 2%); métricas do Google sempre com data de referência e o aviso de atraso de 2 a 3 dias; contato = ligações pelo perfil + rotas + cliques no site + mensagens pelo perfil, e nada mais; impressões e palavras-chave nunca entram na soma; custo por contato = R$ 499 ÷ contatos do mês; nenhum campo de conversão, receita ou "novos clientes" existe em visão, card ou template; coleta idempotente por (tenant, data): reprocessar D-3..D-1 substitui a linha, nunca soma.
- **Métricas:** Frescor (dados próprios < 1 h; Google ≤ D-3); reconciliação; custo por tenant contra o alerta de R$ 25; atraso da coleta (dias entre `data_referencia` e hoje); entregas do dia 1 dentro da janela.
- **Teste de aceitação:** Extrato de um mês de dados sintéticos bate com a soma manual em 100% das linhas; com os dados da padaria de exemplo (118 ligações pelo perfil, 97 rotas, 31 cliques no site, 14 mensagens) o extrato mostra 260 contatos e R$ 1,92 por contato; nenhuma visão do dashboard responde sem `data_referencia`.

### Redator-chefe Transformar dado em 60 segundos de áudio e uma página.

- **Gatilho:** Dia 0 (três frases do Diagnóstico de Posição, minutos depois da medição reduzida); segunda, 06h (Boletim gerado; enviado às 07h); dia 1, 06h (Voz do Cliente e Fechamento Executivo); trimestral, dia 1 (Fechamento Trimestral); lembrete de pendência do onboarding (estado pendente há 72 h, no máximo uma vez por semana por tenant).
- **Entradas:** JSON do Tesoureiro (semana e mês), do Cartógrafo (diagnóstico, posição, mapa em miniatura), do Anfitrião (avaliações, perguntas, temas), do Editor (ações do Diário e o que vem na fila); nome do dono e como quer ser chamado; tom da casa; estados do tenant no Firestore (para as pendências); `data_referencia` dos dados do Google.
- **Ferramentas:** `tts.synthesize(texto, voice_id)` · `render.card` · `render.pdf` (Diagnóstico, Fechamento) · `delivery.send(tenant, entrega, artefatos)` (entregas e o lembrete de pendência, este pelo modelo `aviso_radar`) · `diario.log`.
- **Cérebro:** Cérebro de linguagem para o roteiro e as três frases; **Gemini** para validar que todo número do texto existe nos dados (verificação cruzada em JSON) antes de sintetizar ou renderizar; **Cloud Text-to-Speech** (Chirp 3 HD, pt-BR, `voice_id` fixo da casa) para a voz.
- **Prompt de sistema (esqueleto):** "Escreva o Boletim de Segunda para {nome}, ≤ 150 palavras, falado, começando com 'Bom dia, {nome}'. A primeira frase diz até que dia vão os dados do Google ({data_referencia}). Estrutura: o que mudou, quantos contatos (ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil), avaliações novas e respondidas, posição nos termos-chave, o que a máquina fez, o que vem. Use só números do JSON. Sem adjetivos vazios, sem 'novos clientes', sem receita, sem nome de outro perfil. Termine com uma ação da semana." Para o Diagnóstico de Posição, o mesmo esqueleto muda só a estrutura: "Três frases: onde a casa está hoje (termos e pontos verdes), o que falta no perfil (a maior lacuna da auditoria), o que a máquina faz primeiro. Sem promessa de posição."
- **Saídas:** Áudio OGG/Opus ≤ 60 s + card (Boletim); PDF de uma página (Diagnóstico de Posição, Fechamento Executivo, Fechamento Trimestral); card Voz do Cliente; três frases no card do Dia 0; lembrete de pendência de uma linha com o link do passo (`aviso_radar`).
- **Guardrails:** Verificação cruzada obrigatória: número fora dos dados bloqueia a síntese e abre item no painel; duração máxima 60 s, com corte por contagem de palavras antes de sintetizar; envio do Boletim só entre 7h e 8h; lembrete de pendência no máximo um por semana por tenant e nunca depois de SAIR; nunca "novos clientes", conversão, receita ou ROI; nunca nome de outro perfil; nenhum texto sai sem `prompt_versao` no Diário.
- **Métricas:** Taxa de leitura e escuta (status `read` do número da casa); duração média do áudio; correções manuais; bloqueios da verificação cruzada; pendências resolvidas em 7 dias depois do lembrete.
- **Teste de aceitação:** Boletim de dados sintéticos passa na verificação cruzada e tem áudio ≤ 60 s em pt-BR com pronúncia correta de valores e datas; Diagnóstico de teste sai em três frases, com os números da medição reduzida e nenhum outro; um número plantado fora do JSON bloqueia a síntese.

### Guardião (humano com painel) Aprovar em lote, auditar por amostragem, tratar exceções.

- **Gatilho:** Fila contínua; SLA de 4 h úteis para itens P0/P1; amostragem diária de 10% no P2; textos livres do dono que chegam pelo número da casa (tópico `wa.inbound`: tudo que não é Sim, Não ou SAIR vai para gente); sinais de avaliação suspeita; alertas de custo (`cost.alert`) e de estado do perfil.
- **Entradas:** `approvals` no Firestore com item, contexto, sugestão do agente e risco; prints e diffs do Editor; resposta proposta do Anfitrião com a nota e o texto da avaliação; estado do tenant e da zona; `qa_samples` do dia.
- **Ferramentas:** Painel interno (Cloud Run + Identity Platform, identidade nominal e 2FA): aprovar, editar, rejeitar, em lote; atalhos de teclado; visão por tenant e por agente; botão de incidente; atalho para denunciar avaliação pelo fluxo do Google; registro de QA em `qa_samples`; resposta ao dono pelo número da casa quando o texto livre pede gente.
- **Cérebro:** Nenhum. O Guardião é gente. O painel usa **Gemini** só para ordenar a fila por risco e agrupar itens parecidos.
- **Prompt de sistema (esqueleto):** Não há prompt para o humano. O único prompt do painel é o de ordenação: "Ordene estes itens de aprovação por risco (categoria, nome, endereço e notas ≤ 2 primeiro; depois por prazo), agrupe os parecidos do mesmo tenant e devolva JSON: {ordem: [item_id], grupos: [[item_id]]}. Não altere nenhum item."
- **Saídas:** Ações liberadas (tópico `approvals.decided`); edições que voltam ao agente com o motivo; feedback estruturado que alimenta a avaliação cega mensal dos prompts; incidentes abertos; denúncias de avaliação; linhas de `qa_samples` com veredito e nota do operador.
- **Guardrails:** Um Guardião não aprova mais de 60 itens por hora (qualidade); itens de categoria, nome, endereço e respostas a notas ≤ 2 exigem dois olhos até o P1 e passam pelo Guardião mesmo no P2; sem senha de cliente em nenhuma tela; o painel mostra o dono pelo nome e pelo hash, nunca o número em claro.
- **Métricas:** Itens por hora; taxa de edição; tempo de fila; incidentes por 100 clientes; clientes por operador (30 → 80 → 150, conforme o patamar).
- **Teste de aceitação:** Cem itens sintéticos passam pelo painel em menos de 90 minutos por um operador treinado, com registro completo; um item de categoria só sai com duas aprovações; um texto livre do dono aparece na fila em menos de um minuto.

*Capítulo VI · As receitas*

## ONZE ENTREGAS, ONZE PIPELINES

Para cada entrega: quem faz, qual cérebro, por quais conectores, o pipeline passo a passo e o critério de pronto. É a receita de montagem, uma por página. Duas entregas de entrada, que acontecem uma vez por cliente (01 e 02), e nove recorrentes. Todo job tem chave de idempotência `tenant_id + agente + entrega + período`: rodar duas vezes não publica, não cobra e não envia duas vezes. Toda entrega ao dono passa pelo serviço `Delivery` e pelo número da casa, com status `sent`, `delivered` e `read` em `deliveries` e reenvio único depois de 2 h sem `delivered`. Todo dado do Google carrega a data de referência.

### 01 Diagnóstico de Posição

- **Agente:** Cartógrafo (medição reduzida) + Editor (auditoria de completude) + Redator-chefe (três frases)
- **Cérebro:** Gemini + Grounding com Google Maps (medição) · Gemini (auditoria de campos) · linguagem (três frases) · Gemini (verificação cruzada)
- **Conectores:** Places API (New) · GBP Business Information · Render (card e PDF) · Delivery (número da casa, modelo `entrega_radar`)

1. O tenant chega a `gbp_linked` (ou a `gbp_pending_verification`, com o `place_id` casado por nome e endereço); o tópico `tenant.state.changed` enfileira no Cloud Tasks `cartografo.measure(tenant, modo='reduzida')`: grade 3×3 sobre o raio e até 5 termos-chave, os que o dono disse no Dia 0 ("como o cliente procura"), normalizados pelo Gemini.
2. Para cada termo e ponto, `places.search_text` com `locationBias` no ponto e máscara mínima de campos; posição = índice do `place_id` do tenant no resultado, ou "não encontrado" fora do top 20. Grava `rank_measurements` com a data de hoje. Nenhum dado de outro lugar é guardado.
3. Em paralelo, `editor.audit_profile(tenant)` lê o perfil (`gbp.get_location`) e lista o que falta ou está fraco, com peso: categoria secundária, descrição, horários e feriados, serviços, atributos, fotos (quantidade e idade), perguntas sem resposta, avaliações sem resposta. Grava `profile_audits` com `origem='diagnostico'`: é o "antes" que o Dia 7 vai usar. Se o perfil está pendente de verificação, a auditoria usa só o que é público e diz isso.
4. `redator.diagnostico(tenant, json)` escreve três frases: onde a casa está hoje (termos e pontos verdes), o que falta no perfil (a maior lacuna), o que a máquina faz primeiro. `gemini.crosscheck(texto, json)` bloqueia qualquer número fora da medição.
5. `render.card(diagnostico)`: um card de uma tela com a grade 3×3 por termo (verde, cinza, vermelho), nota e avaliações, e as três frases. `render.pdf(diagnostico)`: uma página com o mapa reduzido, a lista da auditoria e o método no rodapé. Arquivo no dashboard (`deliveries`).
6. `delivery.send(tenant, 'diagnostico', [card, pdf])` na mesma conversa do Dia 0, pelo número da casa; o comercial vê o status `delivered` e encerra o roteiro. Chave `tenant + diagnostico + dia0`: reexecutar regenera o arquivo e não reenvia se já há `enviado_em`.
7. As lacunas da auditoria e os termos vermelhos com impressões entram no tópico `editor.tasks`: o Editor começa a trabalhar antes de a conversa do Dia 0 acabar.

> **Critério de pronto** — Card e PDF chegam na mesma conversa do Dia 0, em até dois minutos depois de `gbp_linked` (dentro dos minutos 8 a 10 do roteiro); três frases sem número fora da medição; nenhum nome de outro perfil; `profile_audits` guarda o "antes" que o Dia 7 vai usar.

### 02 Antes e Depois do Perfil

- **Agente:** Editor (diff do perfil) + Cartógrafo (segunda medição)
- **Cérebro:** Gemini (diff de campos e fotos) · Gemini + Grounding com Google Maps (medição) · linguagem só para a legenda de uma linha por diferença
- **Conectores:** GBP Business Information e mídia · Places API (New) · Render (card lado a lado) · Delivery (modelo `entrega_radar`)

1. Cloud Scheduler diário, 06h → `onboarding.day7(tenant)` para todo tenant criado há sete dias (`created` + 7), independentemente do que ainda está pendente: nada bloqueia nada.
2. `editor.profile_diff(tenant)` compara o retrato do Dia 0 (`profile_audits` com `origem='diagnostico'`) com o perfil de hoje: campos preenchidos, descrição, horários e feriados, serviços, atributos, fotos (quantidade e as novas), posts publicados, perguntas respondidas e avaliações respondidas nos sete dias, tudo com a linha do Diário e o print. A legenda de uma linha por diferença vem do cérebro de linguagem; os fatos vêm do diff.
3. `cartografo.measure(tenant, modo='reduzida')` repete exatamente a grade 3×3 e os termos do Dia 0, para comparar igual com igual; posição por ponto lado a lado com a do Dia 0, cada coluna com a data da medição. Uma semana raramente mexe posição; o card diz isso com todas as letras.
4. `render.card(antes_depois)`: duas colunas, "Dia 0" e "Dia 7": pontos verdes por termo, completude do perfil (campos preenchidos ÷ auditados), nota e número de avaliações, fotos, posts, respostas; embaixo, a lista das ações do Diário. A versão do dashboard traz os prints em miniatura.
5. `delivery.send(tenant, 'antes_depois', [card])` às 08h pelo número da casa; arquivo permanente no dashboard.
6. Se um estado ainda está pendente (perfil sem verificação, dashboard nunca aberto), o card sai mesmo assim e termina com a pendência como uma pergunta de sim ou não, e só ela; o lembrete de pendência do Redator-chefe não se repete na mesma semana.
7. Chave `tenant + onboarding + day7`: o job não roda duas vezes para o mesmo tenant.

> **Critério de pronto** — Card sai no Dia 7 às 08h, independentemente de pendências; toda diferença mostrada existe em `profile_audits`, `actions_log` ou `rank_measurements`; a medição do Dia 7 usa exatamente os termos e pontos do Dia 0; sem métrica de conversão ou receita.

### 03 Dashboard Radar

- **Agente:** Tesoureiro
- **Cérebro:** Gemini Flash (normalizar a coleta) · nenhum modelo nos números
- **Conectores:** GBP Performance API · BigQuery · Next.js no Cloud Run · Identity Platform

1. Cloud Scheduler `hourly` → Job `tesoureiro.refresh_views(tenant)` atualiza as visões materializadas no BigQuery: 7 e 28 dias de `metrics_daily`, posição atual por termo (`rank_measurements`), nota e avaliações (`reviews`), perguntas (`questions`), ações do Diário (`actions_log`), série de 6 meses.
2. Job diário 03h `tesoureiro.collect_gbp(tenant)` chama `getDailyMetricsTimeSeries` para D-3..D-1 e grava `metrics_daily`: `call_clicks` ← `CALL_CLICKS`; `directions` ← `BUSINESS_DIRECTION_REQUESTS`; `website_clicks` ← `WEBSITE_CLICKS`; `conversations` ← `BUSINESS_CONVERSATIONS`; `impressions_search` ← `BUSINESS_IMPRESSIONS_DESKTOP_SEARCH` + `BUSINESS_IMPRESSIONS_MOBILE_SEARCH`; `impressions_maps` ← `BUSINESS_IMPRESSIONS_DESKTOP_MAPS` + `BUSINESS_IMPRESSIONS_MOBILE_MAPS`. `data_referencia` = último dia com dado publicado; `coletado_em` = agora. Chave (tenant, data): reprocessar substitui a linha.
3. Mensal, no dia 1: `gbp.get_keywords(tenant, mes)` (`searchkeywords/impressions/monthly`) grava `keywords_monthly`, que aparece no dashboard como palavras-chave de descoberta: contexto, nunca soma de contatos.
4. O dashboard (Cloud Run) lê só as visões e mostra seis números com setas contra os 7 dias anteriores: ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil, pontos verdes nos termos-chave, nota · avaliações. Impressões (Busca e Maps) e palavras-chave de descoberta ficam em segundo plano. Linha fixa sob os números: "Dados do Google até {data_referencia}. O Google publica com 2 a 3 dias de atraso. 'Ligações pelo perfil' são toques no botão Ligar contados pelo Google, não ligações atendidas."
5. Seções: números; Mapa de Domínio interativo (SVG); Diário de Bordo com print por linha; arquivos (Diagnóstico, Antes e Depois, extratos, Fechamentos, material do QR); série de 6 meses. Nada em tempo real: o que é próprio (medições, respostas, ações) tem frescor de até 1 h; o que é do Google tem data de referência.
6. Acesso: link fixo por tenant com token (`DASHBOARD_BASE_URL/t/{token}`), enviado no Dia 0 pelo número da casa e salvo como ícone no celular; conta criada pelo Radar Urbano no Identity Platform, senha opcional criada pelo cliente, link mágico se ele preferir. Nunca a senha de outro sistema.
7. Cada abertura do link registra `deliveries` com `lido_em` (entrega `dashboard`), para medir uso sem perguntar nada a ninguém.

> **Critério de pronto** — Painel abre em < 2 s no celular, mostra seis números com setas e a data de referência dos dados do Google; nenhum campo de conversão ou receita no template; abre sem senha pelo link e com senha quando o cliente a cria; a padaria de exemplo mostra 260 contatos no mês e R$ 1,92 por contato.

### 04 Boletim de Segunda

- **Agente:** Redator-chefe, com dados do Tesoureiro e do Cartógrafo
- **Cérebro:** Linguagem para o roteiro · Gemini para validar números · Cloud TTS (Chirp 3 HD, pt-BR)
- **Conectores:** BigQuery · TTS · Render (card) · Delivery (número da casa, modelo `boletim_segunda`)

1. Sábado, 03h: `cartografo.measure(tenant, modo='reduzida')` mede os termos-chave na grade 3×3, para o Boletim falar de posição com dois dias de idade, não trinta.
2. Segunda, 06h: `tesoureiro.week_summary(tenant)` gera o JSON da semana fechada disponível: ligações pelo perfil, rotas, cliques no site e mensagens pelo perfil de `metrics_daily` até a `data_referencia` (tipicamente a quinta ou a sexta anterior), comparados com os sete dias anteriores; avaliações novas e respondidas (`reviews`); posição nos termos-chave (sábado); ações do Diário da semana; o que vem (fila do Editor e feriados nos próximos 10 dias).
3. `redator.boletim(tenant, json)` escreve o roteiro ≤ 150 palavras: começa com "Bom dia, {nome}" e diz em uma frase até que dia vão os dados do Google; `gemini.crosscheck(roteiro, json)` bloqueia se houver número fora do JSON; corte por contagem de palavras antes de sintetizar.
4. `tts.synthesize` com o `voice_id` da casa e SSML para números, datas e pausas → OGG/Opus ≤ 60 s; `render.card` → PNG com os cinco números da semana, a posição e a data de referência.
5. 07h: `delivery.send(tenant, 'boletim', [audio, card])` com o modelo `boletim_segunda`; status `sent`, `delivered`, `read` em `deliveries`; reenvio uma vez após 2 h sem `delivered`.
6. Chave `tenant + boletim + semana ISO`; envio só entre 7h e 8h: se a janela passa, abre incidente e um `aviso_radar` de uma linha diz que o Boletim atrasa (runbook do Capítulo VIII), em vez de mandar tarde sem avisar.

> **Critério de pronto** — Áudio ≤ 60 s chega às 7h ± 5 min com card; nenhum número fora do JSON; a primeira frase diz até que dia vão os dados; a semana típica da padaria sai como 31 ligações pelo perfil, 22 rotas, 8 cliques no site, 3 avaliações novas todas respondidas, 1º lugar em 7 dos 9 pontos, 1 post publicado, horário de feriado ajustado.

### 05 Mapa de Domínio

- **Agente:** Cartógrafo
- **Cérebro:** Gemini + Grounding com Google Maps · Gemini Flash para normalizar
- **Conectores:** Places API (New) · GBP keywords · Render (SVG do BigQuery, PNG) · Delivery (modelo `entrega_radar`)

1. Dia 1, 02h: `cartografo.measure(tenant, modo='completa')` gera a grade sobre o raio do cliente (3×3 a 5×5 pontos; passo = raio na 3×3, raio ÷ 2 na 5×5) e roda `places.search_text` por termo (até 25) e ponto, com `locationBias` circular no ponto, `rankPreference` padrão e máscara mínima de campos.
2. Posição = índice do `place_id` do tenant no resultado; fora do top 20 = "não encontrado". Grava `rank_measurements(tenant_id, data, termo, grid_point, lat, lng, posicao)`. Nada de outros lugares: nem `place_id`, nem nota, nem contagem.
3. `gemini.analyze_territory(tenant, mes)` (Gemini Pro, JSON com esquema) classifica cada ponto (verde = top 3, cinza = 4º a 10º, vermelho = fora do top 10 ou não encontrado no top 20), calcula a variação contra o mês anterior e lista oportunidades; `gbp.get_keywords` traz as palavras-chave de descoberta do mês para propor só termos com impressões.
4. `render.map_svg(tenant, mes)` desenha a grade sobre o raio, um painel por termo, legenda das três cores e rodapé com o método: "Busca por texto na Places API como proxy da lista local do Maps; validação mensal com 20 buscas manuais". PNG para o WhatsApp, SVG interativo no dashboard. Não há comparação nominal com concorrentes: o mapa mostra a posição da casa, e só ela.
5. Termos vermelhos com impressões e campos da auditoria entram no tópico `editor.tasks`; sugestão de categoria vai ao Guardião.
6. Card enviado às 08h; edição reduzida do mesmo mapa (grade 3×3, termos-chave) no Dia 0 e no Dia 7.
7. Validação mensal: a operação faz 20 buscas manuais em termos e pontos sorteados e registra em `qa_samples`; concordância abaixo de 85% no top 3 abre incidente e revisa o método antes do próximo dia 1.
8. Custo: chamadas à Places API por tenant e mês = termos × pontos, limitadas em `limites_json`; acima do teto, a grade cai antes dos termos; cada chamada entra em `cost.per_tenant`.

> **Critério de pronto** — Mapa mensal com legenda das três cores, rodapé de método e concordância ≥ 85% com a amostra manual; nenhum nome ou dado de outro perfil no arquivo; nada além de `place_id` guardado por mais de 30 dias; a padaria de exemplo mostra 7 de 9 pontos verdes em "padaria perto de mim".

### 06 Diário de Bordo do Perfil

- **Agente:** Editor (o Cartógrafo diz o que otimizar; o Anfitrião registra ali as respostas a perguntas)
- **Cérebro:** Linguagem para texto · Gemini para fotos e campos
- **Conectores:** GBP v4 (posts, mídia) · Business Information API · calendário de feriados · Guardião · Delivery (`aviso_radar`, `pergunta_sim_nao`)

1. Segunda, 04h: `editor.weekly_post(tenant)` escolhe uma foto real entre as existentes (`vision.assess_photo`: nitidez, rosto, adequação à categoria; nunca gera foto do estabelecimento), escreve o post de até 300 caracteres no tom da casa, envia ao Guardião (P0/P1) ou publica (P2) com `gbp.create_post`. Chave `tenant + post + semana ISO`.
2. Diário, 05h: `editor.hours_check(tenant)` cruza os horários do perfil com `calendar.holidays(cidade, hoje, hoje + 10 dias)` (tabela própria: feriados nacionais e municipais por cidade, mantida pela operação). Feriado a 72 h: aplica o horário do padrão da casa em `limites_json` com `gbp.update_hours` e publica o post de aviso com o horário. Sem padrão: pergunta de sim ou não ao dono (`pergunta_sim_nao`) com o horário proposto; sem resposta até 24 h antes, o horário normal fica e o Diário registra. Chave `tenant + feriado + data`.
3. Eventos `editor.tasks` (do Cartógrafo no Dia 0, no Dia 7 e no dia 1; da Voz do Cliente quando um atrito é resolvível no próprio perfil): descrição, serviços (lista, sem preço), atributos, categoria secundária. Cada campo passa por `gbp.patch_location` com diff antes e depois em `profile_audits`; categoria principal, nome e endereço só via Guardião.
4. Fotos novas: `gbp.upload_media` das fotos avaliadas e aprovadas, uma linha por foto; foto com rosto sem termo nunca sobe.
5. Toda ação: `diario.log` com print da tela pública do perfil (Chrome headless) depois de publicar, `prompt_versao`, `modelo`, `custo`, `entrada_uri`, `saida_uri`. Linha em `actions_log`, append-only. Sem linha, a ação não aconteceu; a verificação automática diária confere que toda ação externa tem print.
6. Dia 1: `editor.audit_profile(tenant)` refaz a auditoria de completude (a mesma do Diagnóstico) e enfileira o que ainda falta; a auditoria vale 60 min nas Horas Devolvidas.
7. A seção do dashboard lista `actions_log` do tenant com print; linha curta pelo número da casa (`aviso_radar`) quando há ação relevante (feriado ajustado, categoria aprovada, descrição nova); o resumo entra no Boletim.

> **Critério de pronto** — Uma semana produz ≥ 1 post, 100% das ações com print, um feriado de teste tratado 72 h antes com horário e post, e nenhum campo sensível alterado sem aprovação; a linha do Diário nasce antes de a ação ser considerada feita.

### 07 Motor de Reputação

- **Agente:** Anfitrião
- **Cérebro:** Gemini Flash (classificar) · linguagem (responder) · Gemini (violação de política)
- **Conectores:** GBP v4 reviews · My Business Q&A API · Render (QR, PDF, card) · Delivery (modelo `entrega_radar`)

1. Primeira semana, assim que o tenant está `gbp_linked`: `gbp.get_review_link(tenant)` traz o link curto oficial "Receber mais avaliações" do perfil; `render.qr(tenant)` gera o QR e `render.pdf(material_qr)` monta o material do balcão (uma página: cartão de mesa e etiqueta de comanda, com o nome da casa); `delivery.send` manda o PDF pelo número da casa. O cliente imprime, ou a máquina manda o arquivo de novo quando ele pedir. Nenhum convite por mensagem a ninguém.
2. Polling a cada 30 min: `gbp.list_reviews(tenant, desde)` e `gbp.list_questions(tenant, desde)`; novidade publica `gbp.review.new` ou `gbp.question.new`; o texto vai para a tabela só como `texto_hash`, temas e sentimento.
3. Avaliação nova → `classify.review` → `anfitriao.reply_review(tenant, review_id)`: redige no tom da casa; nota ≤ 2 vai ao Guardião mesmo no P2; as demais vão ao lote no P0/P1 ou publicam direto no P2; `gbp.reply_review`; `diario.log` com print; `reviews.respondida_em` e `resposta_id`. Chave por `review_id`: nunca duas respostas à mesma avaliação; edição da avaliação pelo autor reabre o item.
4. Pergunta nova → `anfitriao.answer_question(tenant, question_id)`: responde só com o que está no perfil ou nos fatos da casa do Dia 0 ("vocês têm estacionamento?" sai em minutos, com o dado do perfil); dúvida vira `exige_humano` e o Guardião responde dentro das 4 h; `gbp.answer_question`; `questions.respondida_em`; linha no Diário.
5. Sinal de violação (avaliação falsa, spam, dado pessoal exposto, conteúdo proibido) → item no Guardião com o motivo; a denúncia é feita por gente, no fluxo do Google, nunca automática.
6. Lote noturno: `anfitriao.classify_batch(tenant)` classifica o dia (temas e sentimento) com cache de contexto, alimentando o Boletim de Reputação e a Voz do Cliente.
7. Dia 1: `anfitriao.reputation_report(tenant)` gera o card do Boletim de Reputação: nota, avaliações novas do mês, respondidas, tempo mediano de resposta, perguntas respondidas, temas elogiados e temas de atenção; sem comparação com outros perfis; enviado às 08h. Chave `tenant + reputacao + AAAA-MM`.

> **Critério de pronto** — Resposta mediana < 2 h e 100% em 24 h; pergunta respondida em < 4 h; o QR de teste abre a tela oficial de avaliação do perfil; Boletim de Reputação no dia 1; nenhuma mensagem enviada a nenhum número que não seja o do dono.

### 08 Extrato de Demanda

- **Agente:** Tesoureiro
- **Cérebro:** Gemini Pro só para as três frases; números só de SQL
- **Conectores:** BigQuery · Render (PDF) · Delivery (modelo `entrega_radar`)

1. Dia 1, 05h: SQL consolida o mês em `metrics_daily` até a `data_referencia` disponível: contatos = ligações pelo perfil (`call_clicks`) + pedidos de rota (`directions`) + cliques no site (`website_clicks`) + mensagens pelo perfil (`conversations`); impressões (Busca + Maps) e palavras-chave de descoberta só como contexto; nota e avaliações (`reviews`); termos no top 3 como pontos verdes ÷ pontos medidos (`rank_measurements` do dia 1); custo por contato = R$ 499 ÷ contatos do mês.
2. Os dias que o Google ainda não publicou entram na coleta seguinte (a linha de `metrics_daily` é substituída, não somada) e a série do dashboard se corrige sozinha; o PDF diz "dados até {data_referencia}".
3. Série de 6 meses (ou desde o Dia 0), com setas contra o mês anterior; a página explica uma vez que "ligações pelo perfil" são toques no botão Ligar contados pelo Google, não ligações atendidas.
4. Três frases redigidas pelo Gemini Pro e validadas contra o JSON: destaque da maior variação e do custo por contato; nenhuma estimativa de conversão, receita ou "novos clientes"; o dono põe o valor dele por cima.
5. `render.pdf(extrato_demanda)`: uma página, marca do Radar Urbano e nome do cliente, URL assinada de 30 dias, cópia permanente no dashboard; `delivery.send` às 08h.
6. Chave `tenant + extrato + AAAA-MM`; reprocessar substitui o PDF e não reenvia se já há `enviado_em`.

> **Critério de pronto** — 100% dos números vêm de SQL; nenhum campo de conversão, receita ou "novos clientes" existe no template; a padaria de exemplo fecha em 118 + 97 + 31 + 14 = 260 contatos e R$ 1,92 por contato, a oficina em 168 e R$ 2,97, a clínica em 160 e R$ 3,12; o PDF declara a data de referência.

### 09 Horas Devolvidas

- **Agente:** Tesoureiro, a partir do Diário de Bordo
- **Cérebro:** Nenhum (SQL)
- **Conectores:** BigQuery (`actions_log`, `hours_equivalence`, `deliveries`) · Render (card) · Delivery (modelo `entrega_radar`)

1. Tabela `hours_equivalence(acao, minutos)` mantida pela operação e publicada no rodapé do card: post 20 · foto selecionada e publicada 10 · resposta a avaliação 6 · resposta a pergunta 4 · ajuste de campo ou horário 10 · medição de posição 0,5 por termo-ponto · auditoria mensal do perfil 60 · Boletim 30 · extrato ou PDF 45 · Mapa de Domínio 60.
2. Dia 1, 05h: SQL soma por tenant as linhas de `actions_log` do mês, cada ação contada uma vez pela chave de idempotência e só se tem `print_uri` ou `saida_uri`, multiplicadas pelos minutos da tabela; agrupa por tipo.
3. Tempo do dono = soma dos minutos entre cada pergunta de sim ou não e o toque de resposta (`deliveries` e `wa.inbound`), arredondados para cima. Não há outro tempo do dono para contar.
4. `render.card(horas_devolvidas)`: total em horas e minutos, detalhamento por tipo, tempo do dono e a tabela de equivalência no rodapé. Exemplo da clínica em um mês: 8 posts (2h40) · 6 fotos (1h) · 27 avaliações respondidas (2h42) · 5 perguntas respondidas (20 min) · 4 ajustes de perfil (40 min) · 240 medições de posição (2h) · auditoria mensal (1h) · Boletins, extratos, mapa e fechamento (3h45) = 14h07. Tempo da Dra. Lívia: 2 minutos, em uma resposta de sim ou não.
5. `delivery.send` às 08h; chave `tenant + horas + AAAA-MM`.

> **Critério de pronto** — Card reconcilia com `actions_log` linha a linha; equivalências públicas no rodapé; a clínica de exemplo dá 14h07 e 2 minutos do dono; a frase de balcão fecha: "catorze horas por R$ 499".

### 10 Voz do Cliente

- **Agente:** Anfitrião classifica; Redator-chefe sintetiza
- **Cérebro:** Gemini Flash (classificar) · linguagem (síntese) · Gemini (validar frequências)
- **Conectores:** BigQuery (`reviews`, `questions`) · Render (card) · Delivery (`entrega_radar`, `aviso_radar`) · Editor (`editor.tasks`)

1. Lote noturno: `anfitriao.classify_batch(tenant)` classifica as avaliações e perguntas públicas do dia em temas (lista fechada por segmento mais temas emergentes) e sentimento, com cache de contexto; grava `temas[]` e `sentimento`; o texto fica só como hash. Nenhuma conversa privada entra: só o que é público no perfil.
2. Dia 1, 06h: `redator.voz_do_cliente(tenant)` recebe o JSON do mês: top 3 elogios e top 3 atritos por frequência (menções no mês e variação contra o mês anterior), cada um com uma frase real, lida da API na hora e anonimizada (sem nome, sem nada que identifique quem escreveu). Gemini valida que cada frequência existe no JSON.
3. Atrito resolvível no próprio perfil (horário confuso, informação faltando, serviço não listado, pergunta que se repete) → tarefa no tópico `editor.tasks` no mesmo dia e a linha "corrigi: {o que}" no próprio card. Atrito da operação (fila, produto acabando, tempo de espera) fica no card e a decisão fica com o dono.
4. Alerta quando um tema dispara: tema de atenção acima do limiar do tenant em `limites_json` (padrão: 3 menções em 7 dias) sai como aviso de uma linha (`aviso_radar`) fora do dia 1, no máximo um por semana.
5. `render.card` com 6 itens (3 + 3), frequência e evidência; `delivery.send` às 08h; chave `tenant + voz + AAAA-MM`.

> **Critério de pronto** — Card com 6 itens, cada um com frequência e evidência anonimizada; só de avaliações e perguntas públicas; sem identificação de autor; atrito resolvível vira tarefa do Editor no mesmo dia.

### 11 Fechamento Executivo

- **Agente:** Redator-chefe, com Tesoureiro e Cartógrafo
- **Cérebro:** Linguagem + Gemini para validar
- **Conectores:** BigQuery · Render (PDF) · Delivery (modelo `entrega_radar`) · dashboard (arquivo permanente)

1. Dia 1, 06h, depois da ordem do dia 1 (Cartógrafo → Editor → Tesoureiro → Anfitrião → Redator-chefe): `tesoureiro.month_summary(tenant)` monta o JSON do mês: cinco números com variação (contatos no mês, custo por contato, nota · avaliações, pontos verdes nos termos-chave, impressões na Busca e no Maps como contexto), o Extrato de Demanda em três linhas (contatos por tipo, custo por contato, data de referência), as horas devolvidas, o Mapa de Domínio em miniatura, as ações do Diário contadas por tipo e o que vem (fila do Editor, termos que o Cartógrafo vai testar).
2. `redator.fechamento(tenant, json)` escreve a página; `gemini.crosscheck` bloqueia número fora do JSON.
3. `render.pdf(fechamento)`: uma página, marca do Radar Urbano, nome do cliente, data de referência dos dados do Google; URL assinada de 30 dias; arquivo permanente no dashboard (`deliveries`).
4. `delivery.send` até as 08h; o dono encaminha ao contador com "segue o mês".
5. Trimestral, dia 1, a cada três meses desde o Dia 0: `redator.fechamento(tenant, periodo='trimestre')` com a série desde o Dia 0: contatos por mês, custo por contato, pontos verdes por mês, nota. Mesma página, mesma validação.
6. Chave `tenant + fechamento + AAAA-MM` (e `+ trimestre`); regenerar substitui o arquivo e não reenvia.

> **Critério de pronto** — PDF de uma página no dia 1 até 8h; nenhum número fora do JSON; versão trimestral a cada 3 meses com a curva desde o Dia 0; o Marcão de exemplo lê 168 contatos, R$ 2,97 por contato, nota 4,8 com 214 avaliações e 7 de 9 pontos verdes em "oficina mecânica".

*Capítulo VII · O onboarding técnico*

## O QUE ACONTECE NOS QUINZE MINUTOS, DO LADO DE DENTRO

O que acontece do lado da máquina durante os únicos 15 minutos do Dia 0. O roteiro real fecha em cerca de dez; os cinco restantes são folga para quem trava no perfil. Cada toque do cliente dispara um passo automático e um estado no documento do tenant, publicado em `tenant.state.changed`. Antes do primeiro toque existe um passo que não é do cliente: o comercial verifica a zona. Sem vaga, nada do que vem abaixo acontece.

| Toque do cliente | O que a máquina faz | Estado do tenant |
|---|---|---|
| Comercial verifica a zona (antes de tudo) | `zone.check(segmento, zona)` lê `zones` em transação: se `tenants_ativos < limite` (2), reserva a vaga em nome da proposta e devolve "disponível"; se não, devolve "lotada", grava o pedido na lista de espera da zona e o comercial não manda contrato. A reserva cai sozinha se o contrato não for assinado no prazo da proposta. | Nenhum. O tenant ainda não existe; só a reserva em `zones` |
| Assina o contrato (link) | Cria `tenants/{id}` com `segmento`, `zona`, os `termos[]` iniciais e `limites_json` extraídos do mandato de operação do contrato (o que faz sem perguntar, o que exige um sim, o que nunca); confirma a vaga (`zones.tenants_ativos` sobe um, evento `zone.changed`); cria o prefixo do tenant no bucket, os segredos vazios e as permissões das contas de serviço. | `created` |
| Cadastra o cartão (provedor) | Webhook de assinatura ativa do provedor de pagamento: grava o identificador da assinatura, agenda a primeira fatura, libera a cadência mensal. Se o webhook atrasar, a conversa do Dia 0 não espera por ele. | `billing_active` |
| Responde as 5 perguntas por áudio, no WhatsApp | O dono manda os áudios ao número da casa; a primeira mensagem dele abre a janela de 24 h. **Gemini** transcreve e extrai JSON: o que vende e como procuram viram `termos[]`; bairros ou raio viram `raio_m` e a grade; o jeito de falar vira `tom_json`; o que pode sem perguntar vira `limites_json`; número e nome viram `dono_nome` e `dono_wa_hash`. A máquina confirma por escrito, pergunta "É aqui que chegam as entregas?" com `pergunta_sim_nao`, e o Sim vira o opt-in registrado (data, hora, texto) no documento do tenant e no Diário. | `profiled` |
| Adiciona o e-mail operacional como Gerente no perfil | Job `gbp.discover(tenant)` lista os locais que a conta operacional enxerga, casa por nome e endereço, grava `gbp_location_id` e `place_id` em `locations` e lê o estado do local. Na sequência, na mesma conversa: `cartografo.measure(tenant, modo='reduzida')`, `editor.audit_profile(tenant)`, as três frases do Redator-chefe e `render.pdf(diagnostico)`. O Diagnóstico de Posição sai em minutos. Se o local está `PENDING_VERIFICATION`, o passo a passo de verificação vai pelo WhatsApp e o resto não espera. | `gbp_linked` (ou `gbp_pending_verification`) |
| Abre o link do dashboard | Token emitido; `deliveries` registra `lido_em`; opção de criar senha (Identity Platform), que nunca passa por nós. O Diagnóstico já está lá em PDF. Fim dos únicos 15 minutos. | `live` |
| Nenhum toque: dia 7 | `onboarding.day7(tenant)` gera o Antes e Depois do Perfil: diff de `profile_audits` mais a segunda medição reduzida. Card lado a lado no WhatsApp, arquivo no dashboard. | `live` (sem mudança; `deliveries` registra a entrega 02) |

> *Na vida real · Dra. Lívia, Clínica Lívia Odonto*
> Às 9h58 a Dra. Lívia manda o primeiro áudio, entre dois pacientes. Às 10h03, o quinto. Às 10h04 a máquina confirma por escrito o que entendeu e pergunta se é ali que chegam as entregas. Sim. Às 10h06 ela adiciona o e-mail operacional como Gerente, um toque. Às 10h08 o Diagnóstico está na conversa: verde em 4 dos 9 pontos para "dentista perto de mim", descrição vazia, três fotos, nenhum horário de feriado preenchido. Às 10h09 ela abre o dashboard. Onze minutos. Ninguém do Radar Urbano digitou nada.

**Regras do onboarding**

1. **Zona antes de tudo** — A trava territorial não é regra de vendas: é código. `MAX_TENANTS_PER_ZONE_SEGMENT=2` na configuração, `limite=2` em `zones`, e `zone.check` roda como transação (conta e reserva no mesmo passo), para duas propostas simultâneas não passarem juntas. A zona é o bairro, ou um raio equivalente onde bairro não faz sentido; o segmento é a família da categoria principal do perfil (padaria e confeitaria são alimentação; oficina e funilaria são automotivo; dentista e fisioterapeuta são saúde). Os dois campos ficam gravados no tenant e no contrato. Sem vaga, o tenant não nasce: o pedido vai para a lista de espera da zona e o comercial recebe a resposta na hora, no painel. Na assinatura, a reserva vira vaga; se a reserva tiver expirado, `zone.check` roda de novo antes de criar o tenant.
2. **Nada bloqueia nada** — Cada sistema vira um estado independente, e a máquina começa com o que tem. Perfil pendente de verificação não impede o dashboard de abrir, o Cartógrafo de medir (a medição usa o `place_id` público, não o acesso ao perfil) nem o Editor de preparar a fila (auditoria feita, post pronto; publica quando o estado vira `gbp_linked`). O Anfitrião e o Tesoureiro esperam o vínculo: avaliações e métricas só existem com o perfil verificado e o Gerente concedido. Webhook do cartão atrasado não segura a conversa do Dia 0. Nenhum passo exige o anterior; o único pré-requisito de tudo é a zona.
3. **Dia 7 é automático** — Sete dias depois de `created`, o job `onboarding.day7(tenant)` gera o Antes e Depois do Perfil. O Editor monta o diff a partir de `profile_audits` (o "antes" é a foto do perfil tirada em `gbp_linked`; o "depois" é o perfil daquele dia: campos preenchidos, fotos, horários, serviços, atributos, primeiro post) e o Cartógrafo roda a segunda medição reduzida nos mesmos termos e pontos do Dia 0. Card lado a lado pelo número da casa, arquivo no dashboard, linha em `deliveries`. Roda independentemente do que ainda está pendente: se o perfil segue `gbp_pending_verification`, o card sai com a medição e a lista de auditoria, e diz o que falta. Chave idempotente `tenant + onboarding + day7`: rodar duas vezes não manda duas vezes.
4. **Pendências viram uma pergunta** — Se um estado fica pendente por 72 h (cartão sem webhook, Gerente não concedido, perfil não verificado, número sem Sim), o Redator-chefe manda uma mensagem de uma linha pelo número da casa, com o link do passo, pelo modelo `aviso_radar`, no máximo uma vez por semana, e nunca pede senha nem código. A mesma pendência aparece para o comercial no painel, para o onboarding assistido de quem trava. Se continua pendente, vira exceção do Guardião, não mais mensagem. SAIR interrompe também os lembretes.

> **Do lado de fora** — Cinco áudios, um toque no perfil e um link. Do lado de dentro, cinco estados, uma transação na tabela de zonas e o primeiro Diagnóstico antes de o cliente guardar o celular.

*Capítulo VIII · A operação*

## COMO A MÁQUINA RODA TODO DIA

Cadências, papéis, runbooks, custo e escala. É o executivo da máquina: como ela roda todo dia sem depender de heróis. Neste produto não há atendimento em tempo real: tudo que é contato vem do Google com atraso, e o que é próprio é atualizado de hora em hora. Isso muda o dimensionamento: menos gente por cliente, mais clientes por operador, e nenhum plantão de madrugada.

**Tabela de cadências (horário de Brasília)**

| Quando | Job | Agente |
|---|---|---|
| Contínuo | Webhooks do número da casa (respostas do dono, status de entrega) | Delivery / Guardião |
| A cada 30 min | Polling de avaliações e perguntas; respostas | Anfitrião |
| A cada hora | Visões do dashboard | Tesoureiro |
| Diário 03h | Coleta Performance API (D-3..D-1) | Tesoureiro |
| Diário 05h | Checagem de horários e feriados (72 h antes) | Editor |
| Segunda 04h / 06h / 07h | Post semanal / Boletim gerado / Boletim enviado | Editor / Redator-chefe |
| Sábado 03h | Medição reduzida dos termos-chave | Cartógrafo |
| Dia 1, 02h → 08h | Medição completa → auditoria do perfil → extratos → cards → PDFs → envios (na ordem: Cartógrafo, Editor, Tesoureiro, Anfitrião, Redator-chefe) | Todos |
| Dia 7 do tenant | Antes e Depois | Editor + Cartógrafo |
| Trimestral, dia 1 | Fechamento Trimestral | Redator-chefe |

O dia 1 é uma fila, não uma corrida. Às 02h o Cartógrafo mede a grade completa e desenha o Mapa de Domínio; com a lista dele, o Editor faz a auditoria mensal do perfil e enfileira o que muda; às 05h o Tesoureiro fecha o Extrato de Demanda, as Horas Devolvidas e o custo por tenant; o Anfitrião fecha o Boletim de Reputação e entrega os temas classificados; às 06h o Redator-chefe escreve a Voz do Cliente e o Fechamento Executivo e passa tudo pela verificação cruzada; às 08h o Delivery manda os cards e PDFs em sequência, um de cada vez, para não virar enxurrada no celular do dono. O lote noturno de classificação do Anfitrião (temas e sentimento) roda de madrugada, fora da tabela, porque não entrega nada: prepara a Voz do Cliente e o Boletim de Reputação. Todo job tem chave idempotente `tenant_id + agente + entrega + período`; rodar de novo depois de uma falha só completa o que faltou.

**Papéis humanos (o executivo)**

| Papel | Responsabilidade | Dimensionamento |
|---|---|---|
| Head de Operação | Dono do SLA, dos runbooks e da avaliação cega mensal dos prompts; Guardião-chefe; dono da tabela de zonas | 1 desde o P0 |
| Engenheiro de automação | Conectores, agentes, deploy, custo por tenant; a contratação de maior retorno | 1 |
| Operadores (Guardiões) | Aprovação em lote, QA por amostragem (10% no P2), exceções, respostas a notas ≤ 2, pendências de onboarding | 30 → 80 → 150 clientes por operador; sobe porque não há atendimento em tempo real |
| Comercial / SDR | Verificação de zona antes de vender, contrato e cartão por link, onboarding assistido quando o cliente trava no perfil | Conforme aquisição |
| Jurídico externo | Contrato com mandato de operação, LGPD, políticas do Google e da Meta, cláusula de zona; revisão trimestral | Sob demanda |

**Runbooks (o que fazer quando)**

1. **Perfil suspenso ou pendente de verificação** — O GBP Connector detecta `SUSPENDED` ou `PENDING_VERIFICATION` em `locations.status` e abre incidente. Alerta imediato ao Head; congelar o Editor para o tenant (fila pausada, nada publica); o Anfitrião continua lendo, mas não responde; abrir a apelação pelo fluxo do Google com o cliente, com o passo a passo pelo número da casa; auditoria de conformidade em 100% dos tenants nas 48 h seguintes (nome sem termos de busca, categoria certa, endereço real); comunicação ao cliente com o que aconteceu, o que estamos fazendo e a data de referência dos dados que continuam no dashboard. As entregas que não dependem do perfil continuam. A linha no Diário registra o incidente do início ao fim.
2. **Cota ou erro de API do Google** — Retentativa exponencial com espera aleatória, por tenant, no Cloud Tasks. Degradação: o dashboard mostra a última data boa, com a data de referência explícita; medições em andamento param no ponto e retomam pela chave idempotente; se a cota da Places acabar no meio do dia 1, o Cartógrafo termina no dia seguinte e o Mapa sai com a data real da medição no rodapé. Se passar de 24 h, aviso interno e ao cliente, com a data de referência. Nunca trocar a API por raspagem para "compensar".
3. **Custo por tenant acima de R$ 25** — `cost.per_tenant` fecha o mês parcial todo dia; acima do alerta, o Tesoureiro publica `cost.alert` e o Head recebe. Diagnóstico pelos itens de `llm_calls`: reduzir a grade de medição (5×5 para 3×3) e os termos, renovar o cache de contexto, mover tarefas de volume para o modelo Flash, procurar loop de retentativa. Revisar em 48 h; se persistir, entra na avaliação mensal com o Head, com o custo aberto por agente.
4. **Modelo de IA fora do ar** — O LLMGateway usa o fallback por política para tarefas de linguagem (`LLM_LANGUAGE_FALLBACK`); tarefas Gemini-obrigatórias (extração, medição, classificação, decisão de Google, áudio, fotos) esperam na fila em vez de mudar de cérebro; alerta se a fila passa de 2 h. Se o Boletim de segunda não puder passar pela verificação cruzada, não sai: sai um `aviso_radar` de uma linha dizendo que o Boletim atrasa, e o job retoma quando o modelo volta.
5. **Número da casa com qualidade baixa (opt-outs dos donos)** — A Meta rebaixa a qualidade do número quando donos bloqueiam ou saem. Ler a qualidade do número e os SAIR da semana; se caiu: pausar tudo que não é Boletim, revisar os modelos (mensagem demais, horário errado, Sim/Não demais), reduzir a frequência de avisos, checar se algum dono está recebendo lembretes de pendência em excesso; se bloqueado, abrir contestação na Meta e avisar os clientes pelo dashboard, a outra porta; número reserva só com aprovação do Head e só depois de corrigir a causa. Regra permanente: só modelos de utilidade, nunca marketing, nunca clientes finais.
6. **Zona lotada com pedido de venda** — `zone.check` devolveu "lotada". O comercial não vende, não promete e não cria tenant "provisório". Registra o pedido na lista de espera com data e contato; oferece zona vizinha se fizer sentido para o negócio (o dono decide, não o comercial); quando uma vaga abre (offboarding ou mudança de zona), `zone.changed` avisa e o primeiro da lista é procurado. A zona não se redefine para caber um cliente a mais: a definição dela está no contrato dos dois que já estão lá.
7. **Offboarding** — Job `offboarding(tenant)`, disparado pelo cancelamento, que o cliente faz sozinho: remove a conta operacional do papel de Gerente no perfil; desliga a cadência do tenant; exporta o histórico (ZIP com PDFs, Diário de Bordo completo, prints, fotos que ele mandou, série de métricas em CSV) e entrega o link pelo número da casa e no dashboard; apaga os dados no prazo do contrato, exceto `actions_log` e prints, que ficam como prova pelo prazo da retenção; encerra segredos; marca o opt-out do número; libera a vaga da zona (`zones.tenants_ativos` cai um, `zone.changed`, lista de espera avisada). O perfil fica com o dono, inteiro, com tudo que a máquina publicou.

> **A regra dos runbooks** — Todo runbook termina com uma linha no Diário e uma frase para o cliente. O que não está escrito aqui é incidente, e incidente é o Head.

**Custo de tecnologia por cliente (referência de projeto)**

| Item | Base | Custo/cliente/mês |
|---|---|---|
| Gemini (Flash em volume, Pro na análise e no grounding) | ~100k tokens in, 30k out, com cache de contexto | R$ 3–5 |
| Cérebro de linguagem (posts, respostas a avaliações e perguntas, roteiros) | ~40k in, 10k out | R$ 2–4 |
| Places API (New) | medição completa no dia 1 mais quatro reduzidas, máscara só de `id`; sem snapshots | R$ 3–8 (cota gratuita cobre os primeiros clientes) |
| WhatsApp da casa (modelos de utilidade, só para o dono) | ≈ 25 mensagens/mês | R$ 1–2 |
| Cloud TTS, Cloud Run, BigQuery, Storage | rateio em escala | R$ 3–6 |
| **Total** | com folga para repricing; alerta em R$ 25 | **≈ R$ 12–25** |

A conta é pequena porque a máquina fala com uma pessoa só, o dono, e mede com uma API só, a Places. Por isso o alerta é R$ 25 por cliente por mês, e o custo por tenant é a segunda métrica da margem, depois da mensalidade. Cada chamada de modelo e de API grava custo estimado em `llm_calls` e em `actions_log`; `cost.per_tenant` soma; o painel interno mostra por tenant e por agente.

**SLOs**

1. **Entregas no horário** — ≥ 99% das entregas agendadas enviadas na janela; medido em `deliveries` (`enviado_em` contra a janela da entrega). Reenvio após 2 h sem `delivered` conta como atraso, não como falha.
2. **Resposta a avaliações** — Mediana < 2 h; 100% em 24 h; medido em `reviews` (`respondida_em` menos `data`). Notas ≤ 2 contam com o tempo do Guardião dentro.
3. **Perguntas do perfil** — Respondidas em < 4 h; medido em `questions`.
4. **Frescor** — Dados próprios (medições, respostas, ações) < 1 h no dashboard; dados do Google ≤ D-3, sempre com a data de referência na tela.
5. **Diário de Bordo** — 100% das ações externas com linha e print; verificação automática diária cruza `actions_log` com o que a API devolve (posts, respostas, campos).
6. **Dia 0** — Em até 15 minutos cronometrados, do primeiro áudio ao Diagnóstico na tela; medido a cada onboarding e revisto no piloto.

*Capítulo IX · Segurança e LGPD técnico*

## O QUE O CONTRATO PROMETE, O CÓDIGO CUMPRE

O que o contrato promete, o sistema cumpre por construção. Cada item da pauta jurídica do Mapa de Acessos tem um mecanismo técnico correspondente. Se o mecanismo não existe, a cláusula não deveria existir.

1. **Nenhuma senha de cliente** — O único acesso ao Google é o papel de Gerente no Perfil da Empresa, concedido pelo cliente à conta operacional do Radar Urbano; o token OAuth é da nossa conta, não da dele. Código de verificação do perfil nunca passa por nós: o cliente faz a verificação no fluxo do Google. A senha do dashboard é criada pelo cliente no Identity Platform e guardada como hash; nenhuma tela nossa a exibe. A prova é uma consulta: nenhuma tabela, segredo ou log tem campo para credencial de cliente.
2. **Segredos** — Secret Manager. O refresh token da conta operacional (`GBP_OPERATOR_REFRESH_TOKEN`) e o token do usuário de sistema da Meta (`META_SYSTEM_USER_TOKEN`) vivem fora de qualquer tenant; um segredo por tenant (`tenant-{id}-gbp-oauth`) guarda o vínculo do local e o token de acesso de curta duração em uso, para que revogar um cliente não toque nos outros. Acesso por conta de serviço do conector: o Editor não lê segredo da Meta, o Delivery não lê o do Google. Rotação a cada 90 dias; revogação automática no offboarding; auditoria de acesso ativada.
3. **Dados pessoais** — Do dono: nome e número. O número entra nas tabelas analíticas como `dono_wa_hash` (hash com sal por tenant); o claro fica só no documento do tenant no Firestore, e só o serviço Delivery lê. De terceiros (quem avalia ou pergunta no perfil): textos públicos lidos da API, tratados apenas para responder em nome da empresa, armazenados como `texto_hash`, temas e sentimento; o texto original é lido de novo da API quando é preciso responder; o nome do avaliador nunca vai para tabela, e para o prompt vai só o primeiro nome, quando a resposta pede. Camada de anonimização antes do LLMGateway, com exceção declarada por tarefa. Não existe canal com cliente final: nenhuma mensagem ativa, nenhum número de terceiro guardado.
4. **Zona** — Cláusula de exclusividade limitada, cumprida em código. `zones(segmento, zona, cidade, tenants_ativos, limite=2)` e `MAX_TENANTS_PER_ZONE_SEGMENT=2`; `zone.check` conta e reserva na mesma transação; `tenants.segmento` e `tenants.zona` não mudam sem o Guardião (mudar de zona é um novo `zone.check`); toda mudança publica `zone.changed`. Auditoria diária: a consulta em `tenants` agrupada por segmento e zona com mais de dois ativos tem de devolver zero linhas. A definição da zona (bairro ou raio) fica gravada no contrato e no tenant, para que a cláusula e o código falem da mesma coisa.
5. **Número da casa** — Opt-in do dono registrado: data, hora, texto da confirmação e hash do número, no documento do tenant e em `actions_log`. Só modelos de utilidade aprovados (`boletim_segunda`, `entrega_radar`, `pergunta_sim_nao`, `aviso_radar`); nunca marketing; nunca outro destinatário. SAIR imediato: o webhook `messages` reconhece SAIR em qualquer grafia e marca o opt-out na mesma transação; o Delivery recusa qualquer envio com a marca; o Guardião é avisado; o dashboard segue funcionando; a volta exige novo Sim por escrito. Texto livre do dono vai para transbordo humano, nunca para um modelo responder.
6. **Retenção** — Política por tabela, aplicada por ciclo de vida, não por lembrete. `metrics_daily`, `keywords_monthly` e `rank_measurements`: enquanto durar o contrato mais 90 dias (é a série do dashboard). `reviews` e `questions`: só hash e temas, pelo mesmo prazo. `actions_log` e os prints: 5 anos (prova). `llm_calls`: 12 meses. PDFs, cards e áudios das entregas: contrato mais 90 dias. Áudio do Dia 0: apagado depois da confirmação por escrito; fica a transcrição. Conteúdo da Places: nunca além de 30 dias; como só guardamos `place_id`, data, termo, ponto e posição, nada precisa expirar.
7. **Direitos do titular** — Endpoint interno `dsr(tenant, hash)` localiza, exporta ou apaga em até 15 dias os dados de um titular: o dono (nome, número, transcrição, entregas), um avaliador ou autor de pergunta (hash, temas e a resposta pública, que pode ser removida pela API). Canal público informado no contrato e na página de privacidade; o pedido vira linha no Diário.
8. **Suboperadores** — Lista mantida em página pública versionada: Google Cloud e APIs (Vertex AI, Places, Business Profile, Text-to-Speech), Meta (só para o número da casa), provedor do cérebro de linguagem, provedor de pagamento. Mudou a lista, muda a versão e o cliente é avisado.
9. **Logs e auditoria** — Cloud Audit Logs ativos nos dois projetos; acesso ao painel do Guardião com identidade nominal e 2FA; toda aprovação carrega quem aprovou; exportação de logs para bucket com retenção travada; o Diário de Bordo é append-only por permissão de tabela, não por convenção.

> **A prova** — Cada item acima tem uma consulta ou um log que o demonstra. A auditoria da semana 6 roda os nove e guarda o resultado com o Diário.

*Capítulo X · O plano de montagem*

## SEIS SEMANAS ATÉ O PRIMEIRO CLIENTE

Seis semanas para um engenheiro sênior e um Head de Operação, com o jurídico entrando na semana 6. O caminho crítico não é código: são a aprovação de acesso às Business Profile APIs (uma a duas semanas) e a verificação da empresa Radar Urbano na Meta para o número da casa. Por isso as duas começam no dia 1.

#### Semana 1 — Fundação e pedidos de acesso

Projetos `radar-hml` e `radar-prd` em `southamerica-east1`, Terraform, GitHub e Cloud Build para Cloud Run, BigQuery e Firestore com o modelo de dados (inclusive `zones`), Secret Manager, Identity Platform, Logging e Monitoring. Conta operacional Google com 2FA. Chave restrita da Places API (New). **No dia 1:** formulário de acesso às Business Profile APIs; verificação da empresa Radar Urbano na Meta, app com produto WhatsApp e o número da casa; os quatro modelos de mensagem submetidos. Esses prazos são o caminho crítico.

**Prova da semana:** `terraform apply` sobe os dois ambientes do zero; um job vazio roda no Scheduler e escreve uma linha em `actions_log`.

#### Semana 2 — Conectores e o chão da máquina

GBP Connector (leitura completa e edição em homologação sobre o perfil de teste, assim que a aprovação chegar; até lá, contratos e respostas gravadas), Places Connector com grade, máscara mínima e limites, LLMGateway com Gemini e um cérebro de linguagem atrás da mesma interface, Diário de Bordo com `diario.log` e print, telemetria de custo em `llm_calls` e `cost.per_tenant`.

**Prova da semana:** uma busca por termo e ponto devolve a posição do `place_id` de teste; uma edição de horário no perfil de teste gera diff antes e depois e print no Diário.

#### Semana 3 — Cartógrafo, Tesoureiro, Dashboard, Diagnóstico

Medição reduzida e completa, Mapa de Domínio em SVG a partir do BigQuery, coleta do Performance API com data de referência, visões de hora em hora, dashboard por tenant com link único e senha opcional. Diagnóstico de Posição de ponta a ponta: medição reduzida, auditoria de completude do perfil (a função do Editor que nasce aqui, antes do resto dele) e as três frases (a primeira tarefa do Redator-chefe, ainda sem voz), em PDF de uma página.

**Prova da semana:** teste de aceitação do Cartógrafo com 20 buscas manuais; o dashboard abre no celular com os números e a data de referência.

#### Semana 4 — Editor, Anfitrião, Guardião, Antes e Depois

Posts com foto real, fotos julgadas por `vision.assess_photo`, descrição, horários com o calendário de feriados nacional e municipal (ação 72 h antes), serviços e atributos, categoria só com Guardião. Polling de avaliações e perguntas a cada 30 min, respostas em até 2 h, classificação noturna, sinal de avaliação suspeita, material do QR com `render.qr`. Guardião em planilha primeiro, painel depois. `onboarding.day7` com o card Antes e Depois.

**Prova da semana:** primeiro tenant interno operando de ponta a ponta no perfil de teste; uma semana com um post aprovado, um feriado ajustado, uma avaliação de teste respondida, tudo com print.

#### Semana 5 — Redator-chefe, voz, entrega e onboarding

Boletim de Segunda com TTS (Chirp 3 HD, ≤ 60 s) e verificação cruzada; Delivery pelo número da casa com os modelos aprovados (`boletim_segunda`, `entrega_radar`, `pergunta_sim_nao`, `aviso_radar`), status e reenvio após 2 h; webhooks `messages` e `statuses` com Sim, Não, SAIR e transbordo; Extrato de Demanda, Horas Devolvidas, Voz do Cliente e Fechamento Executivo em PDF de uma página; onboarding automático (os estados do Dia 0, o Diagnóstico na conversa, o dia 7); verificação de zona com `zone.check`, `zones` e lista de espera.

**Prova da semana:** o Boletim de dados sintéticos chega às 7h no celular do Head; um Dia 0 completo, cronometrado, com o tenant interno; a terceira empresa do mesmo segmento na mesma zona é recusada.

#### Semana 6 — Endurecimento e piloto

Runbooks, SLOs e alertas, offboarding automático com liberação da vaga na zona, revisão de LGPD e das políticas do Google e da Meta com o jurídico, carga de custo por tenant com alerta em R$ 25. Piloto com 3 clientes reais (uma padaria, uma oficina, uma clínica) por 30 dias, com Guardião em P0 e o Dia 0 cronometrado em cada um.

**Prova da semana:** os três Dias 0 fecham em até 15 minutos; o primeiro Boletim real sai na segunda às 7h.

**Definição de "montei"**

1. **Os 11 testes de aceitação passam** — Um por entrega, listados no Capítulo VI, rodando em homologação com dados sintéticos e em produção com o tenant interno.
2. **O Dia 0 leva até 15 minutos cronometrados** — Com três pessoas que nunca viram o produto. O roteiro fecha em cerca de dez; os cinco restantes são a folga de quem trava no perfil.
3. **O piloto fecha um mês** — Três clientes reais recebem as 11 entregas no calendário, com Diário de Bordo completo e custo por tenant abaixo de R$ 25.
4. **Ninguém tem senha de ninguém** — Auditoria confirma: zero credenciais de cliente armazenadas, todos os acessos por papel.
5. **Nenhuma zona com mais de 2 tenants do mesmo segmento** — A consulta em `tenants` e em `zones` devolve zero violações; `zone.check` recusa a terceira em teste.

*Apêndice*

## O QUE O TECNÓLOGO VAI QUERER NA MÃO

Listas que o tecnólogo vai querer na mão. Nomes fixos: são os mesmos no código, no Diário e neste manual.

**Variáveis de ambiente e segredos (por ambiente)**

```
GCP_PROJECT, GCP_REGION=southamerica-east1
GEMINI_MODEL_PRO=gemini-2.5-pro  GEMINI_MODEL_FLASH=gemini-2.5-flash   (ou a geração vigente)
LLM_LANGUAGE_PRIMARY=claude-sonnet|gemini-2.5-pro   LLM_LANGUAGE_FALLBACK=gemini-2.5-pro
PLACES_API_KEY (restrita)   GBP_OAUTH_CLIENT_ID / SECRET   GBP_OPERATOR_REFRESH_TOKEN (Secret Manager)
META_APP_ID / META_APP_SECRET / META_SYSTEM_USER_TOKEN   WA_WEBHOOK_VERIFY_TOKEN   DELIVERY_SENDER_PHONE_ID
TTS_VOICE_ID (Chirp 3 HD pt-BR)
GUARDIAO_BASE_URL   DASHBOARD_BASE_URL
COST_ALERT_PER_TENANT_BRL=25   MAX_TENANTS_PER_ZONE_SEGMENT=2
```

**Tópicos Pub/Sub**

```
wa.inbound · wa.status · gbp.review.new · gbp.question.new · editor.tasks
approvals.decided · deliveries.send · tenant.state.changed · cost.alert · zone.changed
```

| Tópico | Quem publica | Quem consome |
|---|---|---|
| `wa.inbound` | Webhook `messages` do número da casa | Delivery (Sim e Não), onboarding (áudios do Dia 0), opt-out (SAIR), Guardião (texto livre, transbordo) |
| `wa.status` | Webhook `statuses` (sent, delivered, read) | Delivery (reenvio após 2 h sem `delivered`); `deliveries` |
| `gbp.review.new` | Polling do Anfitrião | Anfitrião (responder); Guardião (nota ≤ 2) |
| `gbp.question.new` | Polling do Anfitrião | Anfitrião (responder) |
| `editor.tasks` | Cartógrafo (otimizações); auditoria mensal | Editor |
| `approvals.decided` | Painel do Guardião | Editor e Anfitrião (publicam o que foi aprovado) |
| `deliveries.send` | Todos os agentes, via `delivery.send` | Delivery |
| `tenant.state.changed` | Onboarding, offboarding, runbooks | Cadências por tenant, dashboard, painel |
| `cost.alert` | Tesoureiro | Head; painel |
| `zone.changed` | `zone.check`, criação e offboarding de tenant | Painel do comercial; lista de espera |

**Ferramentas expostas aos agentes (ADK tools, assinatura resumida)**

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

| Família | Conector por trás | Quem chama |
|---|---|---|
| `gbp.get_location` · `gbp.patch_location` · `gbp.update_hours` · `gbp.update_services` · `gbp.create_post` · `gbp.upload_media` | GBP Connector (Business Information API v1; API v4 para posts e mídia) | Editor; o Cartógrafo só lê |
| `gbp.list_reviews` · `gbp.reply_review` · `gbp.list_questions` · `gbp.answer_question` · `gbp.get_review_link` | GBP Connector (API v4 para avaliações; My Business Q&A API) | Anfitrião |
| `gbp.get_daily_metrics` · `gbp.get_keywords` | GBP Connector (Business Profile Performance API v1) | Tesoureiro; o Cartógrafo lê as palavras-chave |
| `places.search_text` | Places Connector (Places API (New)) | Cartógrafo |
| `wa.send_template` · `wa.send_media` · `wa.send_interactive` | WA Connector (número da casa); o destinatário sai do tenant, nunca do parâmetro | Delivery e o onboarding do Dia 0; nenhum agente fala com o dono por conta própria |
| `tts.synthesize` · `render.card` · `render.pdf` · `render.map_svg` · `render.qr` | TTS Connector e Render | Redator-chefe, Cartógrafo, Tesoureiro, Anfitrião |
| `guardiao.submit` · `diario.log` · `delivery.send` | Painel do Guardião, Diário de Bordo, Delivery | Todos |
| `cost.per_tenant` · `vision.assess_photo` · `classify.review` · `zone.check` · `calendar.holidays` | `llm_calls` e `actions_log`; Gemini multimodal; Gemini Flash; `zones` no Firestore; tabela de feriados nacional e municipal | Tesoureiro; Editor; Anfitrião; comercial e onboarding; Editor |

**Contas e cadastros que precisam existir antes da semana 2**

1. **Google Cloud** — Organização, faturamento, projetos `radar-hml` e `radar-prd`, APIs habilitadas: Vertex AI, Places API (New), Business Profile APIs (após aprovação), Cloud Text-to-Speech, Cloud Run, Cloud Build, BigQuery, Firestore, Secret Manager, Scheduler, Pub/Sub, Identity Toolkit.
2. **Conta operacional Google** — Conta do Radar Urbano que será Gerente nos perfis dos clientes; 2FA; usada só pelo GBP Connector via OAuth; é ela que assina o formulário de acesso às Business Profile APIs e que o cliente vê na lista de usuários do perfil dele.
3. **Meta, só para o número da casa** — Portfólio de negócios do Radar Urbano verificado; app com produto WhatsApp; um número da empresa registrado na Cloud API (o número da casa, com nome de exibição Radar Urbano); usuário de sistema com token; os quatro modelos de utilidade submetidos e aprovados; webhook com `WA_WEBHOOK_VERIFY_TOKEN`. Nenhum cadastro em nome de cliente.
4. **Provedor de pagamento** — Assinatura recorrente por cartão (R$ 499/mês), webhook de status (é ele que vira `billing_active`), emissão de nota fiscal integrada, cancelamento pelo próprio cliente sem ligar para ninguém.

*Encerramento*

## A MÁQUINA ESTÁ DESENHADA {.fecho}

*Cinco camadas, cinco agentes, um humano com painel, quatro conectores e um serviço de entrega, um cérebro obrigatório para tudo que é dado e Google, onze receitas com critério de pronto e uma trava de duas casas por segmento por zona. O que resta é montar, na ordem, começando pelos pedidos de acesso no dia 1. Em seis semanas, o primeiro Boletim de Segunda sai às 7h. Depois disso, a máquina só precisa de cadência.*

Radar Urbano
