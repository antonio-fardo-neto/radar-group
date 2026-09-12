# Radar Urbano · Bíblia

Livro de consulta, na numeração do Mapa Mundi: travou no capítulo III do Mapa Mundi, procure III.x aqui. 57 verbetes, cinco partes fixas cada: O que é · Antes · Passos · Deu certo quando · Se deu errado. Glossário no fim. Regra: se seguiu e não deu certo, o verbete está incompleto; anote o que faltou.

## Capítulo I · Visão e organograma

### I.1 O que é "a máquina"
**O que é:** Cinco agentes (Cartógrafo, Editor, Anfitrião, Tesoureiro, Redator-chefe), um humano com painel (Guardião), quatro conectores (GBP, Places, WA da casa, TTS) e o Render & Delivery, produzindo onze entregas para um dono que só recebe. Cinco camadas (interfaces, conectores, agentes com orquestrador e Guardião, cérebros, memória e prova); cada uma fala só com a de baixo.
**Antes:** Nada.
**Passos:**
1. Entregas 01 a 11, numeração fixa; 01 e 02 uma vez, o resto recorrente.
2. Gemini obrigatório para dado e Google; memória = Firestore, BigQuery, Storage; relógio = Scheduler e Pub/Sub.
3. Tenant = apartamento do cliente (I.4); zona = bairro com duas cadeiras por segmento (VII.2).
**Deu certo quando:** Você explica tudo com "onze pratos, cinco cozinheiros, um chefe que prova, um caderno que não se apaga, duas mesas por ramo em cada bairro".
**Se deu errado:** Mais de cinco agentes ou onze entregas, ou o dono dentro da cozinha (login, reunião, aprovação semanal): desenho errado.

### I.2 O que é um conector
**O que é:** Programa que só sabe falar com um sistema de fora (Google, Meta, TTS). Não pensa, não decide, não chama cérebro; expõe verbos, devolve comprovante (id + print) e custo por tenant.
**Antes:** Nada; para ligar, capítulo III.
**Passos:**
1. Agente nunca chama `googleapis.com` ou `graph.facebook.com`; só o verbo.
2. Verbos: `gbp.*` (get/patch_location, update_hours, create_post, upload_media, list/reply_review, list/answer_question, get_daily_metrics, get_keywords, update_services, get_review_link); `places.search_text`; `wa.send_template/media/interactive`; `tts.synthesize`; `render.card/pdf/map_svg/qr`; `delivery.send`.
3. Falha lá fora: erro claro e retentativa (I.5). Todo conector tem sandbox (V.3).
**Deu certo quando:** Todo código que toca sistema de fora está em `connectors/` (`gbp`, `places`, `wa`, `tts`, `render_delivery`).
**Se deu errado:** Verbo que devolve dados de outros estabelecimentos: recuse (só `place_id`, data, termo, ponto, posição). API mudou: conserto só em `connectors/`.

### I.3 O que é um agente (e o ADK)
**O que é:** Programa com missão, cérebro via LLMGateway e ferramentas, rodando como job (começa, faz, termina). ADK é o kit do Google, em Python, que deixa os cinco iguais por dentro.
**Antes:** V.1; esqueletos no capítulo V do Mapa Mundi.
**Passos:**
1. Pasta por agente: prompt versionado (II.5), ferramentas (V.2), cérebro pelo LLMGateway (II.1).
2. Gatilhos: Cartógrafo Dia 0, Dia 7, sábado 03h, dia 1 02h · Editor segunda 04h, diário 05h, `editor.tasks`, dia 1 · Anfitrião 30 min, lote noturno, dia 1 · Tesoureiro hora, 03h, dia 1 05h · Redator-chefe segunda 06h, dia 1 06h, trimestral.
3. Um agente, uma missão. Até o P1 nada sai sem `guardiao.submit`; categoria, nome, endereço e notas 1–2 sempre com Guardião. Última ação: `diario.log`.
**Deu certo quando:** Existem `agents/cartografo`, `editor`, `anfitriao`, `tesoureiro`, `redator_chefe`, cada um com prompt, ferramentas e cérebro.
**Se deu errado:** Agente que faz tudo, fica ligado esperando ou chama Google direto: erro. Sexto agente: a missão cabe num dos cinco.

### I.4 O que é "tenant"
**O que é:** O apartamento de cada cliente: todo dado tem `tenant_id`; a ficha tem `segmento` e `zona`, que fazem a trava territorial ser código.
**Antes:** Firestore (IV.3); zona verificada (VII.2).
**Passos:**
1. `tenant_id` em toda tabela, fila, segredo (`tenant-{id}-gbp-oauth`) e pasta do Storage.
2. Nasce só após `zone.check`; zona lotada vai para lista de espera.
3. Ficha: `nome`, `segmento`, `zona`, `tom_json`, `limites_json`, `termos[]`, `raio_m`, `dono_nome`, `dono_wa_hash`; estado `created` → `billing_active` → `profiled` → `gbp_linked` (ou `gbp_pending_verification`) → `live`, cada mudança em `tenant.state.changed`.
4. `zones(segmento, zona, cidade, tenants_ativos, limite=2)`: `live` soma 1; offboarding subtrai e publica `zone.changed`.
**Deu certo quando:** `tenant_id` é a primeira coluna de toda tabela; nenhuma linha de `zones` passa de 2.
**Se deu errado:** Três do mesmo segmento numa zona: congele o terceiro, avise comercial e Head no dia. Dono com duas casas: dois tenants; o número repete, o id nunca.

### I.5 O que é "job idempotente"
**O que é:** Rodar duas vezes dá o mesmo que uma. Pub/Sub entrega "pelo menos uma vez"; sem isso o dono recebe dois Boletins.
**Antes:** `deliveries` e `actions_log` (IV.2).
**Passos:**
1. Etiqueta única: cliente + agente + entrega + período (`padaria|redator|boletim|2026-09-14`; `padaria|cartografo|diagnostico|dia0`).
2. Antes: "já feita?" Se sim, para sem erro. Depois: grava em `deliveries` ou `actions_log`.
3. Ações no mundo conferem lá fora (avaliação já respondida? post com a data já existe?). Etapas têm etiqueta própria (`...|audio`, `...|envio`). Data sempre de Brasília.
**Deu certo quando:** O mesmo job duas vezes gera uma entrega, uma linha no Diário, um custo.
**Se deu errado:** Duplicada: etiqueta não gravada. Boletim com data de domingo: UTC. Dois cards com 2 h: o `delivered` não chegou pelo webhook (III.10).

### I.6 O que é o Diário de Bordo
**O que é:** `actions_log`, append-only, com print: hora, agente, entrega, ação, alvo, entrada, saída, print, versão do prompt, modelo, custo. Sem linha, não aconteceu. Dele saem as entregas 06 e 09 e as amostras de II.6 e VIII.1.
**Antes:** BigQuery; Storage para prints.
**Passos:**
1. Última ação de toda publicação, resposta, envio ou edição: `diario.log`.
2. Print da tela pública na pasta do tenant; texto de avaliação de terceiros só como hash e temas.
3. Conta de serviço só insere; erro vira linha de correção. O Sim/Não do dono também vira linha.
4. Job diário acusa ação sem print, sem `prompt_versao` e entrega sem linha. Retenção 5 anos.
**Deu certo quando:** Qualquer post do perfil tem a linha com print; qualquer avaliação mostra os minutos até a resposta.
**Se deu errado:** Sem `prompt_versao`: agente fora do LLMGateway. Custo em branco: o alerta de R$ 25 fica cego. Pedido para apagar linha: nunca.

## Capítulo II · Os cérebros

### II.1 O que é um "cérebro" e como se contrata
**O que é:** Modelo de IA pago por token. Ninguém fala direto: tudo passa pelo `LLMGateway`, que escolhe pela política, mede e grava em `llm_calls`.
**Antes:** Cartão e e-mail da empresa; projeto com faturamento (III.1).
**Passos:**
1. Gemini pela Vertex AI (II.2), sem chave; Claude opcional (II.3).
2. Política: `EXTRACT`, `MEASURE`, `CLASSIFY`, `GOOGLE_DECISION`, `AUDIO_IN`, `VISION` sempre Gemini; escrita usa `LLM_LANGUAGE_PRIMARY` com `LLM_LANGUAGE_FALLBACK`.
3. `LLMGateway.generate(task, tenant, input, schema)` grava tenant, agente, tarefa, modelo, tokens, custo, latência, versão do prompt.
4. Modelos só em variáveis (`GEMINI_MODEL_PRO/FLASH`, `LLM_LANGUAGE_*`). Flash para volume, Pro para análise. Referência: Gemini R$ 3–5, linguagem R$ 2–4 por cliente/mês.
**Deu certo quando:** Vertex AI Studio responde "OK" e `llm_calls` tem a linha com custo.
**Se deu errado:** "billing not enabled": III.1. Claude medindo ou classificando: política furada. Gemini fora: tarefas dele esperam; fila > 2 h alerta (VIII.4).

### II.2 Como ligar o Gemini (Vertex AI)
**O que é:** A máquina usa a Vertex AI (faturamento da empresa, região, Grounding com Google Maps, cache de contexto). AI Studio é só para brincar.
**Antes:** `radar-hml` com faturamento; conta da empresa com papel de dono ou editor.
**Passos:**
1. Console → projeto `radar-hml` → busca "Vertex AI" → **Ativar API**.
2. **Model Garden → Gemini** → Flash → **Abrir no Vertex AI Studio** → "Responda só: OK".
3. Em **Grounding**, confira **Google Maps** como fonte; teste com um lugar real (se não houver, `us-central1`).
4. **IAM → Conceder acesso**: papel **Vertex AI User** para a conta de serviço do Cloud Run.
5. Do computador: `gcloud auth application-default login`, `pip install google-genai`, `genai.Client(vertexai=True, project="radar-hml", location="southamerica-east1")` e `generate_content(model=GEMINI_MODEL_FLASH, contents="Responda só: OK")`.
6. Nomes em `GEMINI_MODEL_FLASH/PRO`; cache de contexto (perfil, tom, regras por 24 h) quando os agentes rodarem.
**Deu certo quando:** Studio "OK", grounding cita o Maps, script imprime "OK".
**Se deu errado:** "Permission denied": papel ou login ADC. "Model not found in region": troque e registre a exceção. Grounding sem Maps: não avance o Cartógrafo (raspar é proibido).

### II.3 Como contratar o Claude (opcional)
**O que é:** Cérebro de linguagem só para escrever; nunca mede, classifica ou decide sobre o Google. Escolha por avaliação cega (II.6).
**Antes:** E-mail e cartão da empresa; Secret Manager (IV.4).
**Passos:**
1. `console.anthropic.com` → conta da empresa → **Billing**: cartão e limite mensal (US$ 50).
2. **API Keys → Create Key** `radar-hml` (depois `radar-prd`); guarde como `llm-claude-key`; feche a aba.
3. Família Sonnet (ou vigente) em `LLM_LANGUAGE_PRIMARY`; Gemini Pro em `LLM_LANGUAGE_FALLBACK` (ou o inverso, pelo teste cego).
4. `pip install anthropic`, `ANTHROPIC_API_KEY` só no terminal, `messages.create(..., "Responda só: OK")`.
5. Confirme que o LLMGateway só oferece Claude para escrita.
**Deu certo quando:** Script imprime "OK", Billing mostra centavos, segredo com versão ativa.
**Se deu errado:** "Invalid API key": espaço no fim. Limite atingido: olhe `llm_calls` antes de subir (loop). Chave no repositório: revogue e crie outra.

### II.4 Saída estruturada (JSON)
**O que é:** O cérebro preenche um formulário (`responseSchema`), não texto solto; "segundo" em vez de `2` quebraria o Mapa de Domínio.
**Antes:** Nada.
**Passos:**
1. Toda chamada leva `schema`; o LLMGateway o coloca no `generateContent`.
2. Cartógrafo `{termo, ponto:int, posicao:int|null, place_id_encontrado}`; Anfitrião `{resposta, tema, sentimento, risco, suspeita:bool}`; Editor `{campo, situacao: ok|faltando|desatualizado, sugestao}`.
3. Fora do formulário: repete com temperatura menor; duas recusas, o job falha alto. Dados com temperatura zero; números como número.
**Deu certo quando:** Em `llm_calls` a resposta é JSON válido só com os campos do esquema.
**Se deu errado:** Muitas recusas: simplifique. Número como texto: tipo não declarado. Campo extra aceito: validação desligada. Texto cortado: mais tokens de saída.

### II.5 Prompt de sistema
**O que é:** Folha de instruções fixa de cada agente, versionada no repositório; uma frase muda todos os clientes.
**Antes:** Esqueletos do capítulo V do Mapa Mundi; ficha do tenant.
**Passos:**
1. Quatro blocos: identidade, permissões, proibições, formato.
2. Chaves da ficha: `{casa}`, `{segmento}`, `{zona}`, `{tom}`, `{servicos}`, `{horarios}`, `{limites}`.
3. Proibições: prometer posição ou resultado; desconto ou brinde por avaliação; inventar serviço, preço ou horário; termo de busca no nome; dado pessoal do avaliador; gerar foto do estabelecimento.
4. `prompts/<agente>/v1.2.md`; mudou, `v1.3`; o Diário grava a versão. Trocar em produção exige II.6 ou sandbox (V.3); é deploy (IV.6).
**Deu certo quando:** Versão na configuração igual à de uma linha recente do Diário.
**Se deu errado:** Mudou "do nada": volte a versão pelo Git. Nome de outro cliente: bug de tenant, congele o agente. Folha cara: o fixo vai para o cache de contexto.

### II.6 Avaliação cega mensal
**O que é:** 100 exemplos reais por agente que escreve, gerados pelos dois cérebros, embaralhados, notados por duas pessoas sem saber qual é qual. Só linguagem.
**Antes:** Planilha (entrada, A, B, nota 1, nota 2; gabarito escondido); sandbox; dois avaliadores por 2 h; régua 5 "publicaria sem tocar" a 1 "não pode sair".
**Passos:**
1. Entradas do Diário do mês anterior: Anfitrião 100 avaliações e perguntas (20 de notas 1–3, 10 perguntas); Editor 100 posts; Redator-chefe Boletins e três frases. Sem nome de avaliador.
2. Gere em sandbox com a mesma versão de prompt; embaralhe; notas em colunas separadas.
3. Maior média vira `LLM_LANGUAGE_PRIMARY`; deploy de variável no primeiro dia útil. Registre em `avaliacoes/AAAA-MM.md`; notas 1–2 viram casos de teste.
**Deu certo quando:** Arquivo por mês em `avaliacoes/` e a variável em produção bate com ele.
**Se deu errado:** Diferença < 0,2: empate, custo decide. Discordância ≥ 2 pontos: régua ruim. Cérebro caiu no meio: refaça tudo no dia seguinte.

## Capítulo III · Os conectores

### III.1 Google Cloud: conta, projeto, faturamento
**O que é:** Onde a máquina mora; projeto é a pasta do ambiente, faturamento é o cartão.
**Antes:** Conta Google da empresa com 2FA (Workspace se houver); cartão, CNPJ, endereço fiscal; e-mail do engenheiro.
**Passos:**
1. `console.cloud.google.com` → **Novo projeto** `radar-hml` e `radar-prd`; anote ID e **Número do projeto**.
2. **Faturamento → Criar conta**; ligue os dois projetos. **IAM**: engenheiro como Editor.
3. **APIs e serviços → Biblioteca**: Vertex AI, Places API (New), Cloud Run Admin, Cloud Build, BigQuery, Firestore, Secret Manager, Scheduler, Pub/Sub, Text-to-Speech, Identity Toolkit (onze). Business Profile só após III.2.
4. `gcloud init`; `gcloud config set run/region southamerica-east1`.
5. **Orçamentos e alertas**: R$ 500/mês, 50/90/100% para o Head. **Exportação de faturamento** diária para o BigQuery (`billing`).
**Deu certo quando:** Dois projetos com faturamento; `gcloud config list` certo; onze APIs "Ativada".
**Se deu errado:** "Sem permissão": conta pessoal. Cartão recusado: banco. "(New)" não aparece: digite junto. Projeto fora da organização: migre em **Gerenciar recursos**.

### III.2 Pedir acesso às Business Profile APIs
**O que é:** Formulário do Google, 1–2 semanas; pedido do dia 1. Sem ele, Editor, Anfitrião e Tesoureiro não tocam perfil real.
**Antes:** Número do projeto de `radar-prd` (e `radar-hml`); site do Radar Urbano com nome, atividade e e-mail no domínio; texto de uso: gestão de Perfis da Empresa de PMEs por assinatura, leitura e atualização, posts, respostas a avaliações e perguntas, métricas; acesso por papel de Gerente concedido pelo cliente; sem senha, sem extração em massa; um projeto, uma conta operacional.
**Passos:**
1. `developers.google.com/my-business` → **Prerequisites / Request access**; preencha e envie; data em `acessos.md`.
2. Enquanto espera: III.3, III.4, III.6, III.7.
3. Aprovado: ativar Account Management, Business Information, Business Profile Performance, Q&A e Google My Business API (v4). **Cotas** > 0. Teste `accounts.list` (III.3).
**Deu certo quando:** Cinco APIs ativas, cotas > 0, `accounts.list` sem 403.
**Se deu errado:** 15 dias sem resposta: reenvie e escreva no fórum oficial. "Uso não claro" ou "site não representa": texto acima; página em construção não passa. Cota 0: aprovação em outro projeto.

### III.3 Conta operacional e OAuth
**O que é:** `operacao@radarurbano.com.br` é o funcionário que o cliente adiciona como Gerente; OAuth deixa o programa agir por ela sem senha, com refresh token revogável.
**Antes:** `radar-prd`; Workspace ou conta no domínio; cofre de senhas para gente.
**Passos:**
1. Crie a conta ("Radar Urbano · Operação"), 2FA, senha no cofre; não abre e-mail.
2. **Tela de permissão OAuth** (ou **Google Auth Platform → Branding**): Interno (Workspace) ou Externo; se Externo, **Publicar** (em Teste o token morre em 7 dias).
3. **Credenciais → ID do cliente OAuth → Aplicativo da Web** `radar-gbp`; redirecionamento `http://localhost:8080/callback`.
4. `client_id/secret` em `gbp-oauth-client`. `scripts/gbp_login.py` (`google-auth-oauthlib`, `access_type=offline`, `prompt=consent`), escopo `business.manage`, só com a conta operacional; refresh token em `gbp-operator-refresh-token`.
5. Teste `GET .../v1/accounts`: 403 antes da aprovação, a conta depois. Rotação a cada 90 dias.
**Deu certo quando:** `accounts.list` devolve a conta e o token segue válido após 8 dias.
**Se deu errado:** `redirect_uri_mismatch`: URL não idêntica. `access_denied`: conta errada. `invalid_grant` depois de uma semana: app em Teste. Só access token: faltou `prompt=consent`.

### III.4 Ser adicionado como Gerente no perfil do cliente
**O que é:** O cliente adiciona a conta operacional como Gerente: um minuto, minuto 5 a 8 do Dia 0. Gerente edita, publica, responde; não remove dono nem transfere.
**Antes:** Cliente Proprietário, logado no celular com a conta dona (senão III.5).
**Passos:**
1. Mande em texto: "Abra o *Google* ou o *Google Maps* com a conta dona do perfil e pesquise o nome da empresa. Toque nos *três pontinhos* (ou *Editar perfil*) → *Configurações do Perfil da Empresa* → *Pessoas e acesso* (ou *Gerentes*/*Usuários*) → *Adicionar* → operacao@radarurbano.com.br → *Gerente* → *Convidar*."
2. Computador: `business.google.com` → empresa → **Configurações do Perfil da Empresa → Pessoas e acesso → Adicionar**.
3. `gbp.discover` aceita o convite (`accounts.invitations.list/accept`), lista locais, casa nome e endereço, grava `gbp_location_id` e `place_id` em `locations`; `gbp_linked` dispara a entrega 01. Bicicleta: aceite pelo e-mail.
**Deu certo quando:** `locations` preenchido, estado `gbp_linked`, Diagnóstico na conversa.
**Se deu errado:** Não acha o menu: peça print, oriente por "Pessoas e acesso". "E-mail não pode ser adicionado": digitação ou aviso de segurança na conta. Não é proprietário: III.5; o resto não espera. Dois perfis da loja: Guardião confere `place_id`. Escolheu Proprietário: troque para Gerente.

### III.5 Perfil não reivindicado ou não verificado
**O que é:** Sem reivindicar (dizer "é meu") e verificar (provar), ninguém edita. Tenant em `gbp_pending_verification`; Cartógrafo mede pelo `place_id` público, Diagnóstico e dashboard saem; Editor, Anfitrião e Tesoureiro esperam.
**Antes:** Cliente no estabelecimento, com e-mail e telefone da empresa.
**Passos:**
1. Cliente pesquisa a empresa logado: painel do perfil = já é dono (III.4); "É proprietário desta empresa?" = caso A; "já foi reivindicado" = caso B; não aparece = caso C.
2. A: **Gerenciar agora** → confirma dados → verificação. B: **Solicitar acesso**; o dono atual tem 3 dias. C: `google.com/business` → **Adicionar sua empresa**; categoria principal combinada com o Guardião.
3. Verificação: em geral vídeo sem cortes (fachada com placa e número, interior, prova de que trabalha ali), até 5 dias úteis.
4. Verificado: III.4; `gbp.discover` roda diariamente para pendentes; pendência > 72 h, uma linha ao dono por semana. Ao ligar, Editor audita, Anfitrião responde o acumulado; o Dia 7 conta do vínculo.
**Deu certo quando:** `locations.status` sai de `PENDING_VERIFICATION`; tenant `gbp_linked`.
**Se deu errado:** Vídeo recusado: placa, número, loja aberta, sem cortes. Sem resposta e sem opção: `support.google.com/business` com CNPJ e comprovante. "Suspenso": VIII.3.

### III.6 Places API e chave restrita
**O que é:** Serviço pago que lista lugares para um termo perto de um ponto; o Cartógrafo mede posição com `places:searchText`. Chave restrita = só essa API. Guardamos só `place_id`, data, termo, ponto, posição; nada além de 30 dias.
**Antes:** Faturamento; `curl`.
**Passos:**
1. **Biblioteca → Places API (New) → Ativar** (a antiga não serve).
2. **Credenciais → Chave de API** `places-prd`/`places-hml` → **Restringir chave** → só Places API (New); depois, IPs do Cloud NAT. Segredo `places-api-key`.
3. Teste: `POST https://places.googleapis.com/v1/places:searchText`, cabeçalhos `X-Goog-Api-Key` e `X-Goog-FieldMask: places.id`, corpo com `textQuery`, `languageCode: pt-BR`, `regionCode: BR`, `pageSize: 20`, `locationBias.circle` (centro e `radius`).
4. Uma chamada por termo e ponto (V.5); posição = índice do `place_id` do cliente (1–20) ou fora do top 20.
5. **Google Maps Platform → Cotas**: 5.000/dia (sobe após 50 clientes); **Métricas** aberto na primeira semana.
**Deu certo quando:** O teste devolve lugares, Métricas mostra "Text Search", a chave aparece restrita.
**Se deu errado:** "API key not valid": restrição de IP ou projeto. "REQUEST_DENIED": ativou a antiga. Máscara inválida: vai no cabeçalho com `places.`. Mesmos resultados em todo ponto: `radius` grande ou `locationRestriction`. Conta subiu: campos caros ou 5×5 com 25 termos (guardrail).

### III.7 Meta: portfólio, verificação, app e número da casa
**O que é:** Uma vez só: Portfólio de negócios, verificação da empresa, App com WhatsApp e um número da empresa registrado: o número da casa. O cliente não faz nada na Meta.
**Antes:** CNPJ em PDF, comprovante de endereço no nome legal, site, e-mail no domínio (tudo batendo); conta pessoal do Facebook de um sócio com 2FA; número novo no CNPJ que nunca teve WhatsApp; página de privacidade; cartão.
**Passos:**
1. `business.facebook.com` → **Criar conta** "Radar Urbano" → **Central de Segurança → Verificação da empresa → Iniciar** (não é o Meta Verified pago).
2. `developers.facebook.com` → **Criar app** → Outro → Empresa → `Radar Urbano` → **Adicionar produto → WhatsApp**; teste `hello_world` com o número de teste.
3. **Configuração da API → Adicionar número**: nome de exibição "Radar Urbano", código por SMS ou ligação, PIN de 2FA no cofre; anote `phone_number_id` (`DELIVERY_SENDER_PHONE_ID`) e `waba_id`.
4. **Configurações → Básico**: `META_APP_ID/SECRET` (segredo `meta-app-secret`); URL de privacidade; modo **Ativo**.
5. **Usuários do sistema → Adicionar** `radar-system` (Administrador), atribua app e WABA, **Gerar token** (nunca expira; `whatsapp_business_messaging`, `whatsapp_business_management`) → `meta-system-user-token`; rotação 90 dias.
6. **Webhooks**: URL `https://<wa-inbound>/webhooks/wa`, token de verificação (`wa-webhook-verify-token`); assine `messages` e `message_template_status_update`; confira a WABA assinada (`POST /{waba_id}/subscribed_apps`).
7. Gerenciador do WhatsApp → **Configurações de pagamento**: cartão. **Números de telefone**: limite (250 sem verificação, 1.000 com) e qualidade verde.
**Deu certo quando:** `hello_world` sai do número da casa com o nome "Radar Urbano"; webhook recebe `sent/delivered/read`; empresa verificada.
**Se deu errado:** Verificação recusada: nome, site ou e-mail não batem, comprovante velho. "Número em uso": apague a conta no app do celular. SMS não chega: ligação. Nome rejeitado: sem "oficial", emoji ou genérico. Sem status: WABA não assinada ou app em Desenvolvimento.

### III.8 Modelos de mensagem para o dono (e o SAIR)
**O que é:** Fora da janela de 24 h só sai modelo aprovado. Quatro nomes lógicos, categoria Utilidade, rodapé "Responda SAIR para não receber mais mensagens.": `boletim_segunda` (cabeçalho vídeo), `entrega_radar` (imagem; versão `entrega_radar_pdf` documento), `pergunta_sim_nao` (botões Sim/Não), `aviso_radar`.
**Antes:** III.7; amostras de card, PDF e MP4 (card + voz, 60 s); consentimento do Dia 0 registrado.
**Passos:**
1. Gerenciador do WhatsApp → **Modelos de mensagem → Criar modelo**, Utilidade, nome em minúsculas, pt_BR.
2. Corpos: `boletim_segunda` "Bom dia, {{1}}. Seu Boletim de Segunda do Radar Urbano: {{2}}. Dados do Google até {{3}}. O áudio de um minuto está acima; o painel, no botão." (botão URL "Abrir o painel") · `entrega_radar` "Olá, {{1}}. Chegou {{2}} do Radar Urbano, referente a {{3}}. Está no seu painel também." · `pergunta_sim_nao` "Olá, {{1}}. O Radar Urbano precisa de um sim ou não: {{2}}. Se não responder, nada é feito." · `aviso_radar` "Aviso do Radar Urbano para {{1}}: {{2}}. Detalhes no painel."
3. Exemplo de amostra: "Seu Jorge" / "31 ligações pelo perfil, 22 rotas, 8 cliques no site, 3 avaliações novas respondidas, 1º lugar em 7 dos 9 pontos" / "quinta, 10 de setembro".
4. Só status Aprovado é usado (webhook `message_template_status_update`). Janela aberta: card PNG e áudio OGG livres (`wa.send_media`); fechada: modelo com MP4.
5. SAIR: `wa_optout = true`, uma resposta ("suas entregas continuam no painel"), nada mais até novo Sim por escrito. Outro texto livre: transbordo humano.
6. Teste em homologação: quatro modelos, Sim, Não, SAIR, texto livre; linhas no Diário com `read`.
**Deu certo quando:** Cinco modelos Aprovados; chegam com o nome "Radar Urbano"; o Sim volta pelo webhook; SAIR desliga na hora.
**Se deu errado:** Rejeitado ou virou Marketing: tire tom de promoção e reenvie. Vídeo recusado: MP4 H.264/AAC ≤ 16 MB. Enviada e não entregue: reenvio após 2 h e pendência. Pausado: novo nome.

### III.9 Cloud Text-to-Speech: a voz da casa
**O que é:** Texto vira voz para o Boletim (≤ 60 s). Uma voz fixa do Radar Urbano, Chirp 3 HD pt-BR, igual para todos.
**Antes:** Faturamento; roteiro de teste com números por extenso (semana típica da padaria).
**Passos:**
1. **Biblioteca → Cloud Text-to-Speech API → Ativar**.
2. Painel **Text-to-Speech**: Português (Brasil), **Chirp 3: HD**; ouça com duas ou três pessoas; escolha e não volte; `pt-BR-Chirp3-HD-<nome>` em `TTS_VOICE_ID`.
3. Script `google-cloud-texttospeech`: `OGG_OPUS`, 48000 Hz, mono; mande ao seu celular por `wa.send_media` tipo `audio`.
4. 60 s ≈ 150 palavras; Redator-chefe corta; TTS Connector recusa acima. Roteiro: números e horas por extenso, sem SSML.
**Deu certo quando:** Toca no WhatsApp como mensagem de voz, < 60 s, números certos.
**Se deu errado:** Robótica: voz Standard/WaveNet. Chega como documento: precisa OGG/Opus mono, `Content-Type: audio/ogg`. Voz "não encontrada": `voices.list` e atualize a variável.

### III.10 Webhook: status e respostas do dono, e como testar
**O que é:** A Meta toca `wa-inbound` a cada evento: status (`sent`, `delivered`, `read`, `failed`) e respostas (Sim, Não, SAIR, texto, áudio do Dia 0). Sem ele a máquina fala e não ouve.
**Antes:** `wa-inbound` no Cloud Run ou `ngrok`; `WA_WEBHOOK_VERIFY_TOKEN`, `META_APP_SECRET`.
**Passos:**
1. Validação: `GET /webhooks/wa?hub.mode=subscribe&hub.verify_token=...&hub.challenge=N` → token bate: 200 com `N` em texto puro; senão 403.
2. Recados: `POST /webhooks/wa`; confira `X-Hub-Signature-256` (HMAC-SHA256 do corpo bruto); publique em `wa.status`/`wa.inbound`; 200 em < 2 s. Status em `value.statuses[0]`; resposta em `value.messages[0]` (`button`, `interactive`, `text`, `audio`).
3. Local: `ngrok http 8080`, cadastre a URL no painel, **Verificar e salvar**, `hello_world`, responda "oi".
4. Idempotência pelo `wamid`. Efeitos: status → `deliveries`; Sim/Não → `approvals.decided` com o id da pergunta no `payload`; "sair" → opt-out; outro texto/áudio fora do Dia 0 → transbordo.
5. Produção: URL do Cloud Run, assinatura obrigatória, sem login; refaça o teste.
**Deu certo quando:** Cada recado no log com 200 em < 2 s; `deliveries` com `lido_em`; um Sim em `approvals.decided`.
**Se deu errado:** "Não foi possível validar": challenge com aspas/JSON. Nada no POST: WABA não assinada. "Assinatura inválida": HMAC sobre JSON convertido. Lento e desativado: trabalho pesado dentro do webhook. Parou no Cloud Run: variáveis não montadas ou serviço com autenticação.

### III.11 Link curto e QR de avaliação (o material do balcão)
**O que é:** Todo perfil verificado tem um link oficial que abre a tela "escreva sua avaliação"; a máquina vira QR e PDF de balcão e comanda. Único pedido de avaliação do produto: passivo, sem incentivo, sem seleção.
**Antes:** Tenant `gbp_linked` e verificado; logotipo e tom; política do Google (sem brinde, sem "gostou?" antes, sem tablet na loja, sem avaliação de funcionário).
**Passos:**
1. Dono: painel do perfil → **Receber mais avaliações** → link `g.page/r/<código>/review`.
2. Máquina: `gbp.get_review_link` lê `metadata.newReviewUri` em `locations.get` com `readMask=metadata`.
3. `render.qr` (correção de erro alta; teste em Android e iPhone); `render.pdf`: cartão A6 e tira de comanda, texto "Avalie a sua experiência. Aponte a câmera para o código.", nome, logotipo, link por extenso.
4. `entrega_radar` (documento) na primeira semana; fica em "Arquivos" no dashboard; linha no Diário.
5. Linha ao dono no Antes e Depois ou no Boletim de Reputação: "não peça nota, não ofereça nada, não escolha para quem mostrar".
**Deu certo quando:** QR lido fora da rede da loja abre a tela certa; a primeira avaliação por ele é respondida em < 2 h.
**Se deu errado:** `newReviewUri` vazio: não verificado ou suspenso. "Página não encontrada": novo `place_id`, gere pela API. Não lê no plástico: papel fosco, ≥ 2,5 cm. Avaliações somem: filtro de spam (mesmo wi-fi, contas novas). Dono quer brinde ou filtro: não; Head conversa.

## Capítulo IV · A fundação

### IV.1 Cloud Run
**O que é:** Programas sem servidor. Serviço ouve (`wa-inbound`, dashboard, painel); job roda e termina (agentes).
**Antes:** `gcloud`; repositório com `Dockerfile`.
**Passos:**
1. `gcloud run deploy wa-inbound --source . --region southamerica-east1 --allow-unauthenticated` (só webhooks públicos).
2. `gcloud run jobs create cartografo --source . --region southamerica-east1 --command python --args -m,agents.cartografo`; executar com `--args --tenant=padaria`. Um job por agente, mais `gbp.discover`, `onboarding.day7`, `offboarding`.
3. Conta de serviço por agente (`sa-cartografo`): Vertex AI User, BigQuery Data Editor, Firestore User, Secret Accessor só nos segredos dele.
4. Variáveis do Apêndice no deploy; segredos montados do Secret Manager. Logs em **Cloud Run → Logs**.
**Deu certo quando:** A URL responde e o job termina "Succeeded".
**Se deu errado:** "Permission denied": falta papel; a mensagem diz qual. Build falhou: log do Cloud Build. Custo subindo: instância mínima ligada.

### IV.2 BigQuery
**O que é:** Armazém de números; todo extrato, card e dashboard nasce de SQL aqui.
**Antes:** Faturamento.
**Passos:**
1. **BigQuery → Criar conjunto de dados** `radar`, `southamerica-east1`.
2. As 15 tabelas da seção 8 do brief (`tenants`, `zones`, `locations`, `metrics_daily`, `keywords_monthly`, `rank_measurements`, `reviews`, `questions`, `posts`, `profile_audits`, `actions_log`, `deliveries`, `llm_calls`, `hours_equivalence`, `qa_samples`) via `sql/create_tables.sql`; partição por data, cluster por `tenant_id`; expiração conforme IX.2.
3. Carregue `hours_equivalence`: post 20 · foto 10 · resposta a avaliação 6 · resposta a pergunta 4 · ajuste 10 · medição 0,5 por termo-ponto · auditoria 60 · Boletim 30 · extrato/PDF 45 · Mapa 60.
4. `SELECT COUNT(*) FROM radar.metrics_daily` → 0. Cota diária de consulta (50 GB).
**Deu certo quando:** 15 tabelas particionadas, com cluster e expiração visíveis.
**Se deu errado:** "Not found: Dataset": região diferente. Expiração "Nunca": corrija no console e no Terraform.

### IV.3 Firestore
**O que é:** Banco de fichas: um documento por tenant (configuração, estado, `wa_optout`, `editor_frozen`) e a fila `approvals`.
**Antes:** Projeto criado.
**Passos:**
1. **Firestore → Criar banco** → Nativo → `southamerica-east1`.
2. Coleção `tenants`, documento `padaria-teste` com os campos de I.4; coleção `approvals` (V.4).
3. Regras: só contas de serviço. Índices pelo link que o console sugere.
**Deu certo quando:** O documento aparece e o programa o lê.
**Se deu errado:** "Insufficient permissions": falta Firestore User. Ficha sem `segmento`/`zona`: não passa de `created`.

### IV.4 Secret Manager
**O que é:** O cofre de senhas de sistema; só contas autorizadas leem; troca sem tocar em código.
**Antes:** API ativada.
**Passos:**
1. **Segurança → Secret Manager → Criar segredo**: `places-api-key`, `gbp-oauth-client`, `gbp-operator-refresh-token`, `meta-app-secret`, `meta-system-user-token`, `wa-webhook-verify-token`, `llm-claude-key`; por tenant `tenant-{id}-gbp-oauth`.
2. Segredo → **Permissões** → conta de serviço → Secret Manager Secret Accessor.
3. Código lê `.../secrets/<nome>/versions/latest`; nunca em variável em claro. Trocar: **Nova versão**; rotação de 90 dias para tokens.
**Deu certo quando:** O programa lê e **Registros** mostra o acesso.
**Se deu errado:** "Permission denied": Accessor faltando naquele segredo. Segredo vazado: revogue na origem, versão nova.

### IV.5 Cloud Scheduler e Pub/Sub
**O que é:** Relógio e quadro de recados; juntos, a cadência da seção 9 do brief.
**Antes:** Jobs no Cloud Run.
**Passos:**
1. **Pub/Sub → Criar tópico**: `wa.inbound`, `wa.status`, `gbp.review.new`, `gbp.question.new`, `editor.tasks`, `approvals.decided`, `deliveries.send`, `tenant.state.changed`, `cost.alert`, `zone.changed`, `agents.run`.
2. **Cloud Scheduler → Criar job**, fuso `America/Sao_Paulo`, destino `agents.run`: anfitrião `*/30 * * * *` · visões `0 * * * *` · coleta `0 3 * * *` · horários `0 5 * * *` · post `0 4 * * 1` · Boletim `0 6 * * 1` e envio `0 7 * * 1` · reduzida `0 3 * * 6` · dia 1 `0 2 1 * *` (Cartógrafo → Editor → Tesoureiro → Anfitrião → Redator-chefe, envios até 8h) · `gbp-discover` e `cost-check` diários.
3. Serviço `dispatcher` assina `agents.run` e dispara o job por tenant ativo.
**Deu certo quando:** Na segunda seguinte o Boletim sai sozinho com `enviado_em` às 7h.
**Se deu errado:** Horário errado: fuso em UTC. Recado duplicado: normal (I.5).

### IV.6 GitHub e deploy automático
**O que é:** PR aprovado em `main` vira revisão nova no Cloud Run pelo Cloud Build. Trocar prompt ou variável de modelo também é deploy.
**Antes:** Repositório privado `radar-urbano`.
**Passos:**
1. Ramificações `main` (produção) e `hml`.
2. **Cloud Build → Gatilhos → Conectar repositório**; gatilho `^main$` com `cloudbuild.yaml` para `radar-prd`; `^hml$` para `radar-hml`.
3. Ninguém envia direto para `main`; PR com revisão de outra pessoa.
**Deu certo quando:** PR aprovado aparece em **Revisões** em minutos.
**Se deu errado:** Build falhou: log do gatilho. Revisão ruim: volte para a anterior em **Revisões**.

### IV.7 Terraform
**O que é:** Infraestrutura como texto (projetos, tabelas, tópicos, permissões, expirações, ciclos de vida).
**Antes:** Engenheiro.
**Passos:**
1. S1: `terraform apply` sobe os dois ambientes (critério de pronto); se atrasar, console e `terraform import` até a S3.
2. Depois, todo recurso nasce no Terraform, inclusive retenção (IX.2).
**Deu certo quando:** `terraform plan` em `radar-hml` sem diferença.
**Se deu errado:** Diferença: alguém clicou no console; corrija no código.

## Capítulo V · Os agentes

### V.1 ADK: primeiro agente em 20 minutos
**O que é:** Instalar o kit e rodar um agente de teste, molde dos cinco.
**Antes:** Python 3.11+; login ADC; Vertex AI (II.2).
**Passos:**
1. `python -m venv .venv && source .venv/bin/activate && pip install google-adk google-genai`.
2. `agents/ola/agent.py`: `Agent(name="ola", model=os.environ["GEMINI_MODEL_FLASH"], instruction="Responda em uma frase.", tools=[])`.
3. `GOOGLE_GENAI_USE_VERTEXAI=TRUE`, `GOOGLE_CLOUD_PROJECT=radar-hml`, `GOOGLE_CLOUD_LOCATION=southamerica-east1`.
4. `adk web` em `agents/`, escolha `ola`, digite "oi". Como job: `adk run ola`.
**Deu certo quando:** Responde no `adk web` e o log mostra a chamada ao Gemini.
**Se deu errado:** `ModuleNotFoundError`: venv inativo. Região: troque a variável. Modelo no código: leia da variável.

### V.2 Dar uma ferramenta a um agente
**O que é:** Função do conector com nome e docstring clara; o ADK mostra ao cérebro, que decide quando chamar.
**Antes:** V.1; GBP Connector com `create_post` em homologação.
**Passos:**
1. `connectors/gbp/`: `def create_post(tenant_id: str, texto: str, foto_uri: str) -> dict:` com docstring "Publica um post no perfil do cliente. Retorna id e print."
2. `tools=[create_post, diario_log, guardiao_submit]`; instrução: "monte o post, `guardiao_submit`; aprovado, `create_post` e `diario_log`".
3. `adk web`: "Publique o post da semana da padaria-teste"; veja a chamada no painel.
**Deu certo quando:** Post no perfil de teste e linha com print no Diário.
**Se deu errado:** Não chama: docstring vaga. Argumentos errados: tipos e exemplos. Publicou sem Guardião: guardrail no código.

### V.3 Sandbox
**O que é:** `RADAR_SANDBOX=1` troca as ferramentas que tocam o mundo por versões que só anotam; o cérebro roda, o mundo não.
**Antes:** V.2.
**Passos:**
1. Conectores em `dry_run=True` gravam em `actions_log` com `sandbox=true`; em `radar-hml` obrigatório por código.
2. Perfil de teste no Google e número de teste da Meta para o que precisa tocar o mundo.
3. `scripts/seed_tenant.py padaria-teste`: um mês sintético. Teste fixo: `zone.check` recusa a terceira do segmento na zona.
**Deu certo quando:** Ponta a ponta em homologação sem linha com `sandbox=false`.
**Se deu errado:** Ação real em homologação: rodou sem a variável; bloqueie por código.

### V.4 Painel do Guardião
**O que é:** Fila de aprovação em lote. Bicicleta: planilha no dia 1. Verdade: app no Cloud Run na S4, com **Consultar zona**.
**Antes:** Google Sheets; depois Identity Platform.
**Passos:**
1. Planilha `Guardião`: `id`, `tenant`, `agente`, `tipo`, `conteúdo`, `foto`, `risco`, `decisão` (Aprovar/Editar/Rejeitar), `texto editado`, `decidido por`, `hora`; job a cada 5 min executa. Abas `QA` (VIII.1) e `Zonas` (VII.2). Vermelho para notas ≤ 2, categoria, nome, endereço.
2. Verdade: login, prioridade, atalhos A/E/R, Firestore `approvals`, custo por tenant ao lado, transbordo do `wa.inbound`, `zone.check`.
3. Patamares: P0 tudo antes; P1 lote com meta > 85% sem edição; P2 direto com QA de 10%. Dois olhos sempre para categoria, nome, endereço, notas 1–2.
**Deu certo quando:** 100 itens sintéticos aprovados em < 90 min com registro.
**Se deu errado:** Fila crescendo (SLA 4 h úteis): taxa de rejeição alta é prompt ruim, não falta de gente.

### V.5 A grade de medição: raio, termos, pontos e a validação com 20 buscas
**O que é:** 3×3 a 5×5 pontos sobre o raio do cliente; por termo, uma `places.search_text` por ponto; posição = índice do `place_id`. Base do Diagnóstico, do Mapa de Domínio e da linha de posição do Boletim.
**Antes:** `place_id`; `termos[]` e `raio_m` do Dia 0; chave Places.
**Passos:**
1. Raio: o que o dono disse; padrão 1.500 m em cidade, 3.000 m onde bairro não serve. 3×3 no Dia 0, Dia 7 e sábado; até 5×5 no dia 1 (5×5 só com justificativa em `limites_json`).
2. Espaçamento = 2 × raio ÷ (lado − 1); `radius` = espaçamento ÷ 2. Até 25 termos; 3 a 5 termos-chave nas reduzidas.
3. `rank_measurements(tenant_id, data, termo, grid_point, lat, lng, posicao)`; nulo = fora do top 20. Flash normaliza; Pro com grounding quando a lista diverge.
4. Verde top 3, cinza 4º–10º, vermelho fora do top 10; 0,5 min por termo-ponto nas Horas Devolvidas.
5. Validação mensal: 20 buscas manuais no Maps do celular, conta neutra, localização no ponto; concordância ≥ 85%; rodapé do Mapa declara o método.
**Deu certo quando:** Posição para cada termo-ponto, SVG com as três cores, validação ≥ 85%.
**Se deu errado:** < 85%: `radius` grande ou termo genérico. Sempre fora do top 20: `place_id` errado. Custo alto: grade ou termos demais (VIII.2).

## Capítulo VI · As receitas (bicicletas das onze entregas)

Regra comum: bicicleta e máquina produzem o mesmo objeto, com a mesma cara. Ferramentas: app do Perfil da Empresa (Google Maps → foto → **Seu perfil comercial**), planilha por cliente, Canva, Google Docs, My Maps, WhatsApp Business no celular da casa. Toda ação gera print e linha na aba `Diário`. Passou de 7 h por cliente por mês: automatize essa entrega primeiro.

### VI.01 Diagnóstico de Posição
**O que é:** Card + PDF do Dia 0: posição em um termo-chave nos 9 pontos, o que falta no perfil, três primeiras ações.
**Antes:** Termo-chave e raio do Dia 0; `place_id`.
**Passos:**
1. Enquanto o cliente adiciona o Gerente, busque o termo em 9 pontos do Maps (localização no ponto) e anote a posição.
2. App do Perfil → **Editar perfil**: confira descrição, categorias, horários (e **Adicionar horário de feriado**), serviços, atributos, fotos.
3. Canva: 9 quadradinhos coloridos, lista do que falta, três frases; Docs → PDF; mande no minuto 8 a 10.
**Deu certo quando:** O card chega antes dos 15 minutos.
**Se deu errado:** Perfil pendente: só posição e o que é público; diga isso.

### VI.02 Antes e Depois do Perfil
**O que é:** Card lado a lado no Dia 7 (desde `created`): cada campo antes e depois, mais a segunda medição.
**Antes:** Prints do Dia 0; lista do VI.01.
**Passos:**
1. Refaça a busca nos 9 pontos.
2. **Editar perfil**: print de cada campo alterado (descrição, horários, serviços, fotos, posts).
3. Canva em duas colunas com a linha de posição e a frase do QR; WhatsApp até as 8h; arquivo no dashboard.
**Deu certo quando:** Cada linha do card tem linha no Diário com print.
**Se deu errado:** Perfil ligou depois: conte 7 dias do vínculo.

### VI.03 Dashboard Radar
**O que é:** Link fixo com números do Google (com data de referência) e o que é próprio; hora em hora na máquina, diário na bicicleta.
**Antes:** Planilha por cliente, "qualquer pessoa com o link".
**Passos:**
1. Primeira linha: ligações pelo perfil, rotas, cliques no site, mensagens, impressões, data de referência; uma linha por dia embaixo.
2. Todo dia 7h: app do Perfil → **Desempenho** → copie o último dia disponível (2–3 dias atrás) com a data.
3. Nota fixa: "ligações pelo perfil são toques no botão Ligar contados pelo Google". Peça para salvar na tela inicial.
**Deu certo quando:** O cliente abre no celular e vê números com data.
**Se deu errado:** Número sem data de referência: não publique.

### VI.04 Boletim de Segunda
**O que é:** Áudio ≤ 60 s + card às 7h, cobrindo a semana fechada disponível.
**Antes:** Planilha do VI.03; posição de sábado nos termos-chave; aba `Diário`.
**Passos:**
1. Domingo: some a semana até a data de referência; avaliações novas e respondidas em **Avaliações**.
2. Segunda 6h: áudio no WhatsApp Business ("Bom dia, {nome}", números por extenso, "dados do Google até quinta", ações, o que vem, "nada a fazer do seu lado").
3. Card no Canva; 7h, áudio e card.
**Deu certo quando:** 7h, ≤ 60 s, data de referência dita.
**Se deu errado:** Google atrasado: diga "o Google ainda não liberou os números"; o resto sai.

### VI.05 Mapa de Domínio
**O que é:** Imagem do dia 1 com a grade colorida por termo; sem concorrentes nomeados; rodapé com o método.
**Antes:** Termos (na bicicleta, 5); Google My Maps.
**Passos:**
1. 9 pontos do bairro, cada termo buscado no Maps com a localização no ponto; anote.
2. My Maps: marcador por ponto (verde/cinza/vermelho), camada por termo; exporte imagem; rodapé "posição vista na busca do Maps em cada ponto; validação com 20 buscas".
3. Dia 1 até as 8h; link no dashboard.
**Deu certo quando:** Todo ponto tem cor e o rodapé diz o método.
**Se deu errado:** Não dá para ir aos pontos: modo anônimo com o endereço do ponto; anote.

### VI.06 Diário de Bordo do Perfil
**O que é:** Tudo que foi feito no perfil, em português de gente, com print; linha no WhatsApp quando há ação relevante.
**Antes:** Aba `Diário` (data, hora, ação, alvo, print); calendário de feriados nacionais e municipais.
**Passos:**
1. Segunda: app → **Adicionar atualização** → foto real + texto; print.
2. 72 h antes de feriado: **Editar perfil → Horário de funcionamento → Adicionar horário de feriado** + post; print.
3. **Fotos**; **Descrição** (≤ 750 caracteres); serviços e atributos nas abas. Categoria só com aprovação humana.
4. Uma linha no WhatsApp por ação relevante, 8h–19h: "horário do feriado ajustado e post agendado. Nada a fazer."
**Deu certo quando:** Toda ação tem linha com print; o resumo entra no Boletim.
**Se deu errado:** Foto gerada ou de banco: nunca.

### VI.07 Motor de Reputação
**O que é:** Toda avaliação respondida em ≤ 2 h; perguntas respondidas; QR; Boletim de Reputação mensal.
**Antes:** Notificações do app ligadas; tom; planilha `Avaliações` (data, nota, temas, sentimento, respondida em).
**Passos:**
1. **Avaliações → Responder**, específica e humanizada; notas ≤ 2 por segunda pessoa antes.
2. **Perguntas e respostas**: < 4 h, com fatos do perfil.
3. **Receber mais avaliações** → link → QR + PDF (III.11) na primeira semana. Suspeita: **Denunciar avaliação**.
4. Dia 1: card com nota, novas, respondidas, temas elogiados e de atenção.
**Deu certo quando:** Nenhuma avaliação passa de 2 h (100% em 24 h); QR no balcão.
**Se deu errado:** Dono quer convite por mensagem ou brinde: não existe neste produto.

### VI.08 Extrato de Demanda
**O que é:** PDF do dia 1: contatos do mês e custo por contato (R$ 499 ÷ contatos). Sem conversão, sem receita.
**Antes:** **Desempenho** do mês fechado.
**Passos:**
1. Contatos = ligações pelo perfil + rotas + cliques no site + mensagens pelo perfil; impressões e palavras-chave só como contexto.
2. R$ 499 ÷ contatos (exemplo padaria: 260, R$ 1,92).
3. Docs → PDF de uma página com data de referência e a nota sobre "ligações pelo perfil"; WhatsApp até as 8h.
**Deu certo quando:** Quatro linhas, soma, custo por contato, data.
**Se deu errado:** Pediram "novos clientes" ou "receita": não entra; o dono coloca o valor dele por cima.

### VI.09 Horas Devolvidas
**O que é:** Card do dia 1: ações do Diário × tabela de equivalência; tempo do dono = minutos dos Sim/Não.
**Antes:** Aba `Diário`; tabela do IV.2.
**Passos:**
1. Conte por tipo e multiplique (clínica: 8 posts, 6 fotos, 27 avaliações, 5 perguntas, 4 ajustes, 240 medições, auditoria, Boletins e extratos = 14h07).
2. Card com a soma, a tabela no rodapé e o tempo do dono ("2 minutos, em uma resposta de sim ou não").
**Deu certo quando:** Cada linha do card bate com o Diário.
**Se deu errado:** Minuto sem linha no Diário: não conta.

### VI.10 Voz do Cliente
**O que é:** Card do dia 1 com temas de avaliações e perguntas: três elogios, três atritos, uma frase real de cada, sem nome; alerta quando um tema dispara.
**Antes:** Planilha `Avaliações` com temas.
**Passos:**
1. Leia tudo do mês; marque tema e sentimento; conte.
2. Card: três mais elogiados, três de atenção, frase anônima, variação contra o mês anterior.
3. Tema que triplica na semana: linha no WhatsApp em horário comercial.
**Deu certo quando:** Nenhum nome; cada tema com contagem.
**Se deu errado:** Só avaliações e perguntas; conversas não existem aqui.

### VI.11 Fechamento Executivo
**O que é:** PDF de uma página no dia 1 (e trimestral): cinco números com variação, três linhas do Extrato, horas, mapa em miniatura, o que fizemos, o que vem. O dono encaminha a quem quiser.
**Antes:** VI.03, VI.05, VI.08, VI.09 prontos.
**Passos:**
1. Modelo no Docs; números do mês e variação; mapa em miniatura; ações; próximo mês.
2. Trimestre: três meses lado a lado. PDF até as 8h; arquivo permanente no dashboard.
**Deu certo quando:** Uma página, números conferidos contra o Extrato, sem promessa de resultado.
**Se deu errado:** Cópia automática a terceiros: não existe.

## Capítulo VII · Onboarding

### VII.1 O roteiro literal do Dia 0
**O que é:** Quatro mensagens, cada uma com um toque que vira estado: `created` → `billing_active` → `profiled` → `gbp_linked` → `live`. Real: cerca de dez minutos; teto: 15, cronometrados.
**Antes:** Zona verificada (VII.2); contrato por link (número do dono e aceite do canal marcados) e link de pagamento; conta operacional; número da casa com modelos; relógio.
**Passos:**
1. Antes (5 min dele): contrato assinado → `zone.check` ocupa a vaga e cria `tenants/{id}` (`created`); cartão → webhook (`billing_active`). O dono abre a conversa pelo link do contrato (janela de 24 h); sem mensagem em 1 h, `pergunta_sim_nao` "Podemos começar?".
2. Minuto 0–5: cinco perguntas por áudio (o que mais vende e como o cliente procura; bairros ou raio; jeito da casa de falar; o que pode fazer sem perguntar; número e como quer ser chamado). Gemini transcreve; a máquina confirma por escrito com `pergunta_sim_nao`; o Sim grava tudo (`profiled`) e vale como opt-in com hora.
3. Minuto 5–8: texto do Gerente (III.4); `gbp.discover` liga (`gbp_linked` ou pendente); medição 3×3, auditoria, três frases, PDF.
4. Minuto 8–10: "Seu painel: {link}. Salve na tela inicial. Senha, se quiser, lá dentro; ninguém aqui vê. Seu Diagnóstico de Posição: {card}. A partir de agora você só recebe: segunda 7h o Boletim; Dia 7 o Antes e Depois; dia 1 o Mapa e os extratos." Abrir o link registra a entrega 01 (`live`).
5. Pare o relógio; anote. Minuto 10–15 é folga para quem travou no perfil.
**Deu certo quando:** `live` (ou pendente com pendência registrada); Diagnóstico com `lido_em`; consentimento com data, hora e texto; ≤ 15 min.
**Se deu errado:** Some: após 72 h, `aviso_radar` com o passo pendente, um por semana; depois, exceção do Guardião e onboarding assistido. Respostas pela metade: aceite; sem a pergunta 4, Editor em P0. Número de outra pessoa: quem recebe consente. Passou de 15: mande a mensagem 4 mesmo assim.

### VII.2 Verificar a disponibilidade da zona (a trava territorial)
**O que é:** Antes de vender: nesta zona, neste segmento, já há dois? Zona = bairro do Google Maps (ou raio equivalente), no contrato com cidade e segmento. Segmento = categoria principal do perfil. Limite 2 no código (`MAX_TENANTS_PER_ZONE_SEGMENT=2`).
**Antes:** Endereço do perfil; categoria principal; `zones` e **Consultar zona** (ou planilha `Zonas`: `cidade`, `zona`, `segmento`, `tenants_ativos`, `limite`, `nomes`, `reserva`, `lista_de_espera`).
**Passos:**
1. Zona: cole o endereço no Maps e leia o bairro ("São Paulo · Jardim América"); onde bairro não serve, círculo com o raio da grade ("Atibaia · centro, 3 km").
2. Segmento: categoria principal; teste "apareceriam na mesma busca?" (padaria e pizzaria, não). Dúvida: Head decide e registra.
3. Consulte: zero, um ou dois de dois. Sem linha: crie com 0.
4. Livre: proposta com cidade, zona e segmento na cláusula; reserva por 5 dias úteis (conversa não reserva). Assinado: `zone.check` em transação soma 1, grava no tenant, publica `zone.changed`; só então `created`.
5. Lotada: não venda, não crie tenant provisório; lista de espera (nome, contato, data; ordem de chegada, ninguém fura) ou outra unidade. Vaga abriu: comercial chama o primeiro em até 2 dias úteis.
6. Mudou endereço ou categoria: nova verificação. Com vaga, aditivo e ajuste das linhas; sem vaga, mantém até o fim do ciclo pago e entra na lista da zona nova (o endereço no perfil muda mesmo assim). Zona redesenhada: quem está fica.
**Deu certo quando:** Nenhuma linha de `zones` acima de 2, todo dia; todo `live` com zona e segmento do contrato; `zone.check` recusa a terceira em teste.
**Se deu errado:** Vendeu em zona lotada: o tenant não nasce; Head devolve com a frente da lista ou oferece outra unidade. Bairro em disputa: vale o Google Maps. Segunda unidade da mesma empresa: ocupa vaga. Planilha e tabela discordam: a tabela manda a partir da S5.

## Capítulo VIII · Operação

### VIII.1 QA por amostragem
**O que é:** Todo dia útil, 10% das ações publicadas ontem, lidas pelo print: `ok`, `editaria`, `errado`. Categoria, nome, endereço e notas ≤ 2 nunca entram no P2.
**Antes:** Aba `QA`; `actions_log` de ontem; `qa_samples`; 20 min no início do turno, a mesma pessoa na semana.
**Passos:**
1. `sql/qa_amostra.sql`: ontem, `sandbox = false`, só o que tocou o mundo, ao acaso; 10%, mínimo 20, máximo 60.
2. Leia como o cliente do cliente, no celular. `errado` com motivo (tom, dado inventado, promessa, dado pessoal, foto, horário, resposta que não responde).
3. `errado` corrige no mesmo dia, com print e origem `qa`.
4. Metas: `errado` < 2%, `editaria` < 15%. Dois dias fora: o agente volta ao P1 até revisar o prompt e cinco dias na meta. Dia 2: taxas por `prompt_versao` para II.6.
**Deu certo quando:** ≥ 20 linhas por dia útil; taxas na meta; cada `errado` com correção.
**Se deu errado:** Só `ok` por semanas: plante três erros num tenant de teste. Erros num tenant só: `tom_json`; refaça a pergunta 3 por `pergunta_sim_nao`. Erros de um tipo: regra no prompt.

### VIII.2 Custo por cliente (e o que fazer acima de R$ 25)
**O que é:** Custo de tecnologia por tenant por mês; alerta em R$ 25. É o nosso custo, não o custo por contato do cliente.
**Antes:** `llm_calls`, `actions_log`, `rank_measurements`, `deliveries`; `sql/custo_por_tenant.sql`; `precos_unitarios`; faturas do Google e da Meta.
**Passos:**
1. Dia 1 (Tesoureiro 05h; parcial diária): `llm_calls.custo` + buscas × preço Places + mensagens × preço utilidade + TTS + rateio de nuvem pelos `live`.
2. Confira com **Faturamento → Relatórios** e **Faturamento** da Meta; folga de 10%.
3. Referência: Gemini 3–5 · linguagem 2–4 · Places 3–8 · WhatsApp da casa (≈ 25 mensagens) 1–2 · TTS, Cloud Run, BigQuery, Storage 3–6 · total R$ 12–25.
4. Acima: `cost.alert`, tenant marcado no painel. Causas: termos ou grade demais (5×5 × 25 termos = 625 buscas; 3×3 × 10 = 90); Pro onde Flash bastava; auditoria sem cache; job em dobro; loop de retentativa.
5. Corrija na ordem barata: grade e termos → cache → Flash → idempotência → loop; registre em `limites_json` e no Diário; revise em 48 h.
**Deu certo quando:** Média < R$ 25; nenhum tenant acima por dois meses; tabela batendo com as faturas.
**Se deu errado:** Cartógrafo campeão: grade. Editor: sem cache. Anfitrião: Pro em classificação. Places > R$ 8 em todos: completa rodando toda semana. Custo zero em `live`: a máquina parou; veja `actions_log`.

### VIII.3 Runbook: perfil suspenso
**O que é:** `locations.status = SUSPENDED`; `tenant.state.changed` alerta o Head. Duas metades: consertar este cliente e conferir os outros.
**Antes:** Acesso Gerente; Diário de 30 dias e `profile_audits`; comprovantes do cliente (CNPJ, fachada com placa, conta de luz); `aviso_radar`.
**Passos:**
1. `editor_frozen = true`; Anfitrião lê, mas não responde.
2. Em até 1 h, pelo número da casa: o que houve, o que já fizemos, o que vamos fazer, as três coisas que precisamos dele. Sem culpa.
3. Audite 30 dias: termo de busca no nome, categoria trocada, endereço ou telefone divergentes, post fora da política; corrija com print e origem `runbook VIII.3`.
4. **Restabelecer perfil suspenso** (formulário oficial) com o Proprietário; comprovantes; número do caso na ficha.
5. Enquanto espera: Cartógrafo mede; Boletim com "Perfil suspenso desde {data}; pedido aberto em {data}"; dashboard com a última data boa.
6. Em 48 h, auditoria de conformidade em 100% dos tenants; causa nossa vira prompt novo antes de publicar.
7. Restabelecido: descongele; Anfitrião responde o acumulado (notas ≤ 2 primeiro); medição extra; uma linha ao cliente. `incidentes/AAAA-MM-DD-tenant.md`; o Fechamento menciona em uma frase.
**Deu certo quando:** Status ativo; causa registrada; auditoria dos 100% em 48 h; cliente avisado no início, a cada passo e no fim.
**Se deu errado:** Recusado: comprovante fraco; reenvie. 14 dias sem resposta: Head assume; aviso a cada 7 dias. Quer cancelar: pode; ofereça congelar sem cobrar. Era `PENDING_VERIFICATION`: III.5.

### VIII.4 Runbook: API do Google parou
**O que é:** 429 (cota) ou 5xx em Business Profile, Places, Vertex AI ou TTS. Conectores retentam; jobs são idempotentes; o runbook cobre cota e a promessa de 2 h. Nunca raspar para compensar.
**Antes:** **Logging** com `status >= 429`; páginas de status; **Cotas**; conta operacional.
**Passos:**
1. Qual API, qual código: 401/403 é credencial (III.3) ou Gerente removido (III.4).
2. Google fora: 30 min sem mexer; não reinicie (duplica).
3. 429: peça aumento em **Cotas**; reduza cadência (polling 30 → 60 min; sábado espera).
4. Avaliações fora > 90 min: Guardião responde à mão em `business.google.com` (notas ≤ 2 com dois olhos), Diário com origem `manual VIII.4`; o Anfitrião reconhece depois. Perguntas: meta 4 h.
5. Performance API: > 24 h, última data boa; > 72 h, o Boletim diz. Places: retoma pela chave idempotente com a data real.
6. Gemini fora: tarefas obrigatórias esperam (fila > 2 h alerta); linguagem usa fallback, registrado em `llm_calls.modelo`. Boletim sem verificação cruzada não sai: `aviso_radar` de atraso.
7. Voltou: confira `deliveries` e `actions_log` sem duplicidade; `incidentes/AAAA-MM-DD-api.md`.
**Deu certo quando:** Fila esvaziou sozinha; nada duplicado; nenhuma avaliação > 24 h nem pergunta > 4 h; incidente registrado.
**Se deu errado:** Fila não esvazia: 400 (API mudou) ou 401/403. Cota estoura todo dia 1: lotes (02h, 02h30, 03h). Meta parou: retentativa, Delivery reenvia após 2 h; o Boletim já está no dashboard.

### VIII.5 Runbook: número da casa com qualidade baixa
**O que é:** A Meta rebaixou qualidade ou limite do número da casa. Causa única aqui: donos mandando SAIR, bloqueando ou denunciando. Um número para todos: poucos afetam todos.
**Antes:** Gerenciador do WhatsApp → **Números de telefone**; `deliveries`; `wa.inbound` com SAIR; textos dos modelos.
**Passos:**
1. Anote qualidade e limite com a data. Opt-outs em 30 dias ÷ donos ativos; > 2% é nosso.
2. `deliveries` por modelo, dono e hora: `aviso_radar` > 1/semana; fora de horário (Boletim 7h segunda; dia 1 até 8h; o resto 8h–19h; nada de madrugada ou domingo); `pergunta_sim_nao` sem necessidade; número trocado.
3. Pause `aviso_radar` por 7 dias; corrija hora e texto apontado. SAIR respeitado na hora; cliente segue pelo dashboard; volta só com Sim escrito.
4. Vermelho: **Solicitar revisão** com o caso de uso (número único, só clientes pagantes, só serviço contratado, opt-out por uma palavra). Faixa no dashboard.
5. Religue 25/50/100% em três dias, começando pelo Boletim. `incidentes/AAAA-MM-DD-numero-da-casa.md`.
**Deu certo quando:** Verde; opt-outs < 2%; Boletim seguinte com `entregue_em` e `lido_em` na maioria; nada fora do horário.
**Se deu errado:** Bloqueio permanente: segundo número na mesma WABA, modelos de novo, `DELIVERY_SENDER_PHONE_ID` novo, aviso a cada dono; só com o Head. Limite estourou na segunda: verifique a empresa; Boletim em duas ondas. Queda sem opt-out: spam na primeira mensagem; confira o nome de exibição e a mensagem 1.

### VIII.6 Runbook: offboarding
**O que é:** O cliente cancelou; a máquina se retira, devolve tudo, apaga no prazo e libera a vaga. O perfil dele fica inteiro no Google.
**Antes:** Cancelamento registrado e data de fim do ciclo; ficha, segredos, Storage, BigQuery; na bicicleta, planilha `Zonas`.
**Passos:**
1. `closing` com a data; até lá tudo continua. No dia, `offboarding(tenant)`.
2. Fechamento Executivo de encerramento com a série desde o Dia 0.
3. `business.google.com` → perfil → **Usuários** → conta operacional → **Remover**.
4. `deliveries` fecha; hash do número marcado; nada a desligar na Meta.
5. ZIP com link assinado de 30 dias (Diário em CSV com prints, PDFs, cards, mapas, fotos, posts, respostas, métricas) pelo número da casa e no dashboard.
6. Desative `tenant-{id}-gbp-oauth`; token do dashboard revogado após 30 dias.
7. `zones.tenants_ativos` − 1 no mesmo dia; `zone.changed`; comercial chama o primeiro da lista em 2 dias úteis.
8. `closed` com data; retenção (IX.2). `offboarding/AAAA-MM-DD-tenant.md`: motivo, tempo de casa, última série, custo por contato.
**Deu certo quando:** Fechamento e ZIP entregues; conta fora de **Usuários**; segredos desativados; vaga livre e publicada; tenant `closed`; perfil intacto.
**Se deu errado:** Quer voltar: `reopen(tenant)` dentro da retenção; acessos e vaga de novo. Conta não sai do perfil: registre, avise por escrito, desative o segredo. ZIP > 100 MB: só o link. Cancelou dia 28: entregas do dia 1 saem; Fechamento no fim do ciclo.

## Capítulo IX · Segurança e LGPD

### IX.1 Pedido de titular
**O que é:** Avaliador, autor de pergunta ou dono pede para ver ou apagar dados; 15 dias. De terceiros só há hash, temas, sentimento e a resposta pública; do dono, nome de tratamento, hash do número, transcrição, tom, autorizações, entregas.
**Antes:** Pedido por escrito (`radarurbano.com.br/privacidade`); link ou texto exato; do dono, mensagem do número cadastrado; `dsr(tenant, hash)`.
**Passos:**
1. Identidade com o mínimo. `dsr` procura em `reviews.texto_hash`, `questions.texto_hash`, `tenants.dono_wa_hash`, `actions_log.alvo`.
2. Responda o que há: "um código derivado do texto (não o texto), os temas, o sentimento e a resposta pública em nome da empresa; não temos seu nome, telefone ou e-mail".
3. Ver: `dsr(..., modo='exportar')` → PDF.
4. Apagar terceiro: hash vira marcador, temas e sentimento limpos; ficam data, nota, `respondida_em`. Resposta pública apagável por `reviews.reply`, com aviso à empresa; a avaliação é do Google. Prints ficam; `alvo` deixa de apontar.
5. Apagar dono: offboarding; apague `dono_nome`, `dono_wa_hash`, `tom_json`, transcrição, áudios. `actions_log` fica; contrato e nota pelo prazo da lei.
6. Registre em `lgpd/pedidos/AAAA-MM-DD-tenant.md` e no Diário; avise o cliente (controlador) sem identificar a pessoa além do necessário.
**Deu certo quando:** < 15 dias com registro; consulta pelo hash vazia; cliente avisado.
**Se deu errado:** Não aponta a avaliação: sem texto não há hash. Quer apagar a resposta e a empresa não: decisão dela; registre as duas. Pedido de número desconhecido: transbordo. Dados que nunca tivemos: responda por escrito.

### IX.2 Suboperadores e retenção
**O que é:** Quatro suboperadores: Google Cloud e APIs; Meta (só o número da casa); provedor do cérebro de linguagem; provedor de pagamento. Lista pública; retenção configurada na máquina.
**Antes:** `radarurbano.com.br/suboperadores` e `/privacidade` com data; BigQuery, Storage, Firestore; Terraform; jurídico trimestral.
**Passos:**
1. Página com nome, país, finalidade e o que cada um recebe; data a cada mudança; uma linha aos clientes na entrega seguinte.
2. Retenção: `actions_log` e prints 5 anos · `reviews`, `questions`, `rank_measurements`, `metrics_daily`, `keywords_monthly`, `posts`, `profile_audits`, `deliveries` e arquivos de entregas: contrato + 90 dias · respostas brutas da Places 30 dias (só `place_id` fica) · dados do dono contrato + 90 dias; áudios do Dia 0 apagados após a confirmação por escrito (rede de segurança 7 dias) · `llm_calls` e `qa_samples` 12 meses · ZIP 30 dias · contrato e nota fiscal pelo prazo da lei.
3. Expiração de partição no BigQuery; ciclo de vida por prefixo no Storage; job dos 90 dias após `closed` apaga dados do dono e deixa a casca (`tenant_id`, datas, zona, segmento).
4. Revisão trimestral com o jurídico em `lgpd/revisoes/AAAA-Tn.md`. Trocou de cérebro de linguagem: página antes da primeira chamada.
**Deu certo quando:** Página com data; expiração em cada tabela; ciclo de vida em cada bucket; job dos 90 dias com log diário.
**Se deu errado:** Tabela "Nunca": console e Terraform. Ferramenta nova recebendo texto sem passar por aqui: incidente; pare. Cliente voltou no dia 100: o ZIP era a cópia; está no contrato.

## Capítulo X · O plano de montagem

### X.1 O quadro das seis semanas
**O que é:** Seis colunas com "pronto quando" e uma linha vermelha no topo com as aprovações de terceiros (Business Profile APIs; verificação na Meta e número da casa; modelos): o caminho crítico.
**Antes:** Quadro; capítulo X do Mapa Mundi; III.2 e III.7 lidos; engenheiro, Head, jurídico na S6.
**Passos:**
1. Linha vermelha com data de envio e de resposta de cada pedido; vermelha enquanto faltar resposta.
2. Reunião de 15 min em pé toda segunda, com evidência.
3. Sem aprovação do Google: sandbox e bicicletas (S3 não depende). Sem verificação da Meta: número de teste; 250 donos/dia bastam para o piloto.
4. S5: `zones` é a verdade antes de qualquer venda. S6: "Definição de montei" com evidência.

| Semana | Monta | Pronto quando |
|---|---|---|
| 1 Fundação e pedidos | Projetos, Terraform, GitHub/Cloud Build, BigQuery e Firestore (com `zones`), Secret Manager, Identity Platform; conta operacional; chave Places; dia 1: formulário Google, Meta, modelos | `terraform apply` sobe os dois ambientes; job vazio escreve em `actions_log`; três pedidos com data |
| 2 Conectores | GBP, Places com grade, LLMGateway, Diário com print, custo | Busca por termo e ponto devolve posição; edição de horário com diff e print; toda chamada em `llm_calls` |
| 3 Cartógrafo, Tesoureiro, Dashboard, Diagnóstico | Medições, Mapa SVG, coleta com data de referência, visões por hora, dashboard, Diagnóstico de ponta a ponta | Validação ≥ 85%; dashboard no celular; Diagnóstico em minutos após `gbp_linked` |
| 4 Editor, Anfitrião, Guardião, Antes e Depois | Posts, fotos, horários e feriados, serviços, atributos; polling, respostas ≤ 2 h, QR; Guardião em planilha; `onboarding.day7` | Tenant interno uma semana com print; 100 itens em < 90 min; card do Dia 7 |
| 5 Redator-chefe, voz, entrega, onboarding, zona | Boletim com TTS; Delivery e webhooks; extratos e PDFs; Dia 0 e Dia 7 automáticos; `zone.check` e lista de espera | Boletim sintético às 7h com `lido_em`; Dia 0 cronometrado; terceira empresa recusada |
| 6 Endurecimento e piloto | Runbooks, SLOs, offboarding, revisão jurídica, alerta de R$ 25; piloto com 3 clientes por 30 dias em P0 | Três Dias 0 ≤ 15 min; primeiro Boletim real; os cinco itens de "montei" |

**Deu certo quando:** 11 testes de aceitação passam; Dia 0 ≤ 15 min com três pessoas novas; piloto fecha um mês com as 11 entregas e custo < R$ 25; ninguém tem senha de ninguém; nenhuma zona com mais de 2.
**Se deu errado:** S4 sem Google: siga em sandbox. S5 sem Meta: 250 donos/dia. Semana estourou: corte o que não está em "montei" (painel em planilha, Terraform depois), não empurre a S6. Tenant do piloto > R$ 25: não é "montei".

## Glossário

| Termo | Definição |
|---|---|
| ADK | Kit do Google, em Python, para montar agentes. |
| Agente | Programa com missão que pensa com IA e usa ferramentas; cinco, mais um humano com painel. |
| Append-only | Só se acrescenta; nada se edita ou apaga. |
| Cache de contexto | Guardar no Gemini o que não muda para não pagar de novo. |
| Cérebro | Modelo de IA; Gemini para dado e Google, outro só para linguagem. |
| Conector | Programa que fala com um sistema de fora; quatro, mais o Render & Delivery. |
| Contato | Toque em Ligar, pedido de rota, clique no site ou mensagem pelo perfil, contados pelo Google. Nunca ligação atendida. |
| Custo por cliente | Gasto de tecnologia por tenant por mês; alerta em R$ 25. |
| Custo por contato | R$ 499 ÷ contatos do mês; a única conta feita para o cliente. |
| Data de referência | Último dia que os números do Google cobrem (2–3 dias atrás); acompanha todo número do Google. |
| Diagnóstico de Posição | Entrega 01: card e PDF do Dia 0 com posição atual, o que falta no perfil e as primeiras ações. |
| Diário de Bordo | `actions_log`: registro imutável de toda ação, com print. |
| Grade de medição | Pontos (3×3 a 5×5) sobre o raio do cliente onde se mede a posição por termo. |
| Grounding | Gemini consultando dados oficiais do Maps enquanto responde. |
| Guardião | Humano com painel: aprova em lote, audita por amostragem, dois olhos no que é de risco. |
| Idempotente | Fazer duas vezes dá o mesmo que uma. |
| Janela de 24 h | Após mensagem do dono, 24 h de resposta livre sem modelo. |
| Link curto de avaliação | Link oficial "Receber mais avaliações" do perfil, que vira QR e PDF de balcão. |
| Link fixo / mágico / único | Dashboard com token (vira ícone) / entrada sem senha / só para criar ou redefinir senha. |
| LLMGateway | Balcão único de cérebros: política, medição, `llm_calls`. |
| Número da casa | O único WhatsApp do Radar Urbano, na Meta, que fala só com o dono. SAIR interrompe. |
| Opt-in / Opt-out | Sim registrado no Dia 0 / SAIR, respeitado na hora. |
| Patamar (P0, P1, P2) | Tudo aprovado antes / lote com meta > 85% / publicação direta com QA de 10%. |
| Performance API | Porta do Perfil da Empresa que devolve métricas com atraso e data de referência. |
| Places API | Serviço pago do Google sobre lugares; busca por texto como proxy da lista local; só `place_id` além de 30 dias. |
| Ponto da grade | Coordenada onde se mede a posição: verde top 3, cinza 4º–10º, vermelho fora do top 10. |
| Prompt de sistema | Folha de instruções fixa e versionada de um agente. |
| Refresh token | Chave de longa duração do OAuth; o segredo mais importante do GBP Connector. |
| Sandbox | Modo de teste que não toca o mundo. |
| Segmento | Categoria principal do perfil e as buscas que ela disputa; com a zona, define a vaga. |
| Tenant | O apartamento de cada cliente: tudo que é dele, isolado. |
| Token (Meta) | Chave do usuário de sistema do Radar Urbano que autoriza o número da casa. Uma só. |
| WABA | Conta do WhatsApp Business do Radar Urbano na Meta, dona do número da casa. Uma só. |
| Webhook | Campainha: a Meta toca a URL da máquina quando algo acontece. |
| Zona | Bairro do endereço do cliente no Google Maps (ou raio equivalente); no máximo duas empresas do mesmo segmento. |
| zone.check | Conta e ocupa a vaga da zona em transação; recusa a terceira. |
