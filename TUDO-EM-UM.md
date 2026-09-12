<!-- Radar Urbano · TUDO-EM-UM: todos os arquivos do pacote concatenados, na ordem, para colar de uma vez numa IA ou ler de ponta a ponta. Gerado por src/assemble.py; não editar à mão. -->


<!-- ======================================================================
     ARQUIVO: README.md
     ====================================================================== -->

# Radar Urbano

Pacote de documentos do **Radar Urbano**: serviço B2B de captura de intenção no Google Maps e na Busca local para pequenos negócios, por assinatura de **R$ 499/mês**, entregue por agentes de IA, com zero tempo do dono. Só o produto inicial (o que a versão antiga da holding chamava "Radar Maps"); os outros módulos aparecem apenas no arquivo de expansão.

## Os oito arquivos (em `radar-urbano/`)

| Arquivo | O que é |
|---|---|
| `01-DOSSIE.md` | A tese do negócio com as variáveis de um produto só: mercado, produto, modelo comercial, economia unitária, estágios, riscos |
| `02-POV-CLIENTE.md` | O que o cliente vê, contrata, recebe e nunca faz; preço; trava territorial; o que medimos e o que não prometemos |
| `03-POV-PLAYER.md` | O memorando para investidor/player: economia unitária, fases de escala, capacidade, riscos, uso de capital |
| `04-EXPANSAO.md` | Como cresce: por zonas e praças (produto único) e por módulos (fases 1 a 5) |
| `05-MAPA-DE-ENTREGAS.md` | As onze entregas, calendário, a máquina, a conta na mesa, a trava |
| `06-MAPA-DE-ACESSOS.md` | Contas, papéis, base legal, mapa por entrega, roteiro do Dia 0, a zona |
| `07-MAPA-MUNDI.md` | Manual de montagem da máquina: camadas, cérebros, conectores, fundação, agentes, receitas, operação, LGPD, seis semanas |
| `08-BIBLIA.md` | Livro de consulta: 57 verbetes passo a passo na numeração do Mapa Mundi, com glossário |

`TUDO-EM-UM.md` concatena os oito para colar de uma vez numa IA.

## Regras que valem em todos os arquivos

1. Nenhuma métrica de conversão, receita atribuída ou "novos clientes" prometida ao cliente. Só contagens (ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil, impressões, posição, avaliações) e custo por contato.
2. Gemini é o cérebro obrigatório para dados, medição e tudo que toca o Google.
3. Nunca a senha do cliente. Um único acesso: papel Gerente no Perfil da Empresa.
4. Zero tempo do dono: até 15 minutos no Dia 0.
5. No máximo duas empresas por segmento por zona, verificado antes da venda e em código.
6. Dados do Google com data de referência; sem tempo real neste produto.
7. Alerta de custo de tecnologia em R$ 25 por cliente por mês.

## Outras pastas

- `referencia/` — `01-DOSSIE-HOLDING-VERBATIM.md` (o dossiê original da holding, 52 seções, intocado) e `BRIEF-DE-ESCOPO.md` (as decisões de recorte que governaram a reescrita; inclui o adendo de alinhamento).
- `detalhado/` — as versões longas e aprofundadas (entregas, acessos, mapa mundi, roadmap, contexto, decisões, backlog, design, como gerar). São rascunhos em revisão; ver `detalhado/README.md`.
- `src/` — gerador de apresentações web (edição branca) e PDF a partir do Markdown: `python3 src/build.py --all`, `python3 src/make_pdf.py --all`, `python3 src/assemble.py tudo`. Ver `detalhado/07-COMO-GERAR.md`.
- `dist/` — HTML e PDF gerados.


<!-- ======================================================================
     ARQUIVO: radar-urbano/01-DOSSIE.md
     ====================================================================== -->

# Radar Urbano · Dossiê

Reescrita do dossiê da holding (52 seções, seis produtos) com as variáveis de um produto só: R$ 499/mês, trava de duas empresas por segmento por zona, onze entregas, cinco agentes e um humano com painel. Valuations, múltiplos de ARR, IPO, M&A e expansão internacional do original foram removidos; o que restou está em uma linha de hipótese na seção 8. Todo número financeiro aqui é projeção, salvo preço e custo de tecnologia, que vêm do brief.

## 1. O problema

- A busca por comércio local começa e termina no Google Maps e na Busca local. Quem está no top 3 recebe o toque em Ligar, o pedido de rota e o clique no site; quem está fora do top 10 não é visto.
- O dono não tem tempo para o Perfil da Empresa: horário errado em feriado, fotos velhas, avaliações sem resposta, perguntas públicas abertas, categorias e atributos incompletos.
- A alternativa (agência ou freelancer) cobra mensalidade por métrica de vaidade em rede social e exige tempo e senha do dono. O dono cancela em três meses.
- O Google entrega os números do perfil, mas ninguém os lê nem transforma em decisão.

## 2. A solução e a promessa

O Radar Urbano opera o Perfil da Empresa no Google do cliente, mede a posição dele no mapa e entrega, toda semana e todo mês, o que aconteceu, em números que o Google conta. Agentes de IA fazem tudo; o dono gasta zero tempo depois do Dia 0.

Promessa oficial: **captura de intenção otimizada, lucrativa e eficiente.**

Fora da promessa, por decisão (D5): conversão, receita atribuída, "novos clientes", ROI projetado, posição garantida. A única conta feita para o cliente é **custo por contato** (R$ 499 ÷ contatos do mês); o dono coloca o valor dele por cima.

## 3. Mercado

| Camada | Número | Origem |
|---|---|---|
| TAM | 15 milhões de CNPJs ativos em comércio, alimentação, saúde de bairro, serviços locais e oficinas | Dossiê original |
| SAM | 3,5 milhões de estabelecimentos em capitais e cidades médias com dependência de fluxo físico | Dossiê original |
| SOM | Vagas = zonas × segmentos × 2, por praça | Recalculado abaixo |

### A conta do SOM

Máximo de duas empresas por segmento (categoria principal do Google) por zona (bairro do Maps ou raio equivalente). O mercado obtível é a soma das vagas, não uma fração do SAM.

| Variável | Hipótese por praça |
|---|---|
| Zonas com densidade comercial | 40 a 80 bairros (cidade grande); 15 a 30 (cidade média) |
| Segmentos com demanda de busca | 25 a 40 (padaria, pizzaria, oficina, dentista, pet shop, salão...) |
| Vagas teóricas | 2.000 a 6.400 (zonas × segmentos × 2) |
| Ocupação realista | 15% a 25% (nem todo segmento existe em todo bairro; nem toda empresa compra) |
| **Clientes obtíveis por praça** | **300 a 1.600 (projeção)** |

Consequências: 2.000 clientes exigem 2 a 6 praças; 10.000 exigiriam 8 a 30 e não são estágio deste dossiê. O crescimento é por abertura de praça. A trava é também argumento de venda: o vizinho do mesmo segmento não entra.

## 4. O produto

Onze entregas: duas de entrada e nove recorrentes. Detalhe no Mapa de Entregas.

| Nº | Entrega | Quando | O que o dono recebe |
|---|---|---|---|
| 01 | Diagnóstico de Posição | Dia 0 | Card e PDF: posição hoje, o que falta no perfil, três frases |
| 02 | Antes e Depois do Perfil | Dia 7 | Card lado a lado: perfil e posição |
| 03 | Dashboard Radar | A cada hora | Link fixo no celular; dados do Google com data de referência |
| 04 | Boletim de Segunda | Segunda, 7h | Áudio ≤ 60 s e card da semana fechada |
| 05 | Mapa de Domínio | Mensal, dia 1 | Grade 3×3 a 5×5 por termo: verde top 3, cinza 4º–10º, vermelho fora |
| 06 | Diário de Bordo do Perfil | Contínuo | Registro append-only com print de tudo feito no perfil |
| 07 | Motor de Reputação | Contínuo e mensal | Avaliações respondidas em ≤ 2 h, perguntas, QR do balcão, Boletim de Reputação |
| 08 | Extrato de Demanda | Mensal, dia 1 | Ligações pelo perfil, rotas, cliques no site, mensagens, impressões, custo por contato |
| 09 | Horas Devolvidas | Mensal, dia 1 | Horas executadas pela máquina, com tabela de equivalência |
| 10 | Voz do Cliente | Mensal, dia 1 | Temas elogiados e de atenção (só avaliações e perguntas) |
| 11 | Fechamento Executivo | Mensal e trimestral | PDF de uma página para encaminhar ao contador ou sócio |

"Contato" é o que o Google conta no perfil: toques em Ligar, rotas, cliques no site e mensagens pelo perfil. Impressões e palavras-chave são contexto. Não há dado em tempo real: o Google atrasa 2 a 3 dias e tudo sai com data de referência.

Exemplo (brief): padaria 260 contatos, R$ 1,92 por contato; oficina 168, R$ 2,97; clínica 160, R$ 3,12. Horas Devolvidas da clínica: 14h07 no mês contra 2 minutos da dona. Frase de balcão: "catorze horas por R$ 499".

## 5. Modelo comercial

| Item | Regra |
|---|---|
| Preço | R$ 499/mês, fixo (R$ 16,63 por dia). Sem verba de mídia, sem plano maior |
| Contrato | Mensal, cancelável, sem fidelidade abusiva; cartão recorrente antes do Dia 0 |
| Trava territorial | 2 por segmento por zona; cláusula de exclusividade limitada |
| Reserva de vaga | Conversa não reserva; proposta escrita reserva por 5 dias úteis; a vaga ocupa na assinatura (transação em `zones`); fila por ordem de chegada |
| Dia 0 | Até 15 minutos cronometrados: cinco perguntas por áudio, Gerente no Perfil da Empresa, link do dashboard, Diagnóstico na mesma conversa. O roteiro real fecha em cerca de dez; o resto é folga |
| Acessos | Papel Gerente no perfil; nunca a senha do cliente; WhatsApp do dono só recebe; SAIR interrompe |

## 6. Aquisição

Outbound geolocalizado por dados públicos, sem raspagem do Google.

- **Alvos:** perfis fracos (poucas avaliações, nota baixa, horários incompletos, sem fotos recentes, avaliações sem resposta), levantados dentro dos termos da Places API (New) ou à mão. Sem extração em massa; só `place_id` fica além de 30 dias.
- **Zona antes de vender:** o comercial roda `zone.check` (segmento + zona) antes da primeira conversa. Zona lotada não recebe proposta; recebe lista de espera.
- **Abordagem:** Diagnóstico de Posição reduzido do perfil público (três termos, campos faltantes) e a conta de custo por contato com os números que o Google já mostra ao dono. Sem simulador de retorno.
- **Canais:** contabilidades (comissão recorrente por indicação), associações comerciais e de bairro, SDR por praça, indicação de cliente para segmento vizinho (a padaria indica o pet shop, não outra padaria).
- **Praça:** só abre com comercial dedicado e Guardião com capacidade.

## 7. Economia unitária (projeção)

| Linha | Valor por cliente/mês | Base |
|---|---|---|
| Receita | R$ 499 | Preço |
| Custo de tecnologia | R$ 12 a 25 | Gemini 3–5 · linguagem 2–4 · Places 3–8 · WhatsApp da casa 1–2 · TTS, Cloud Run, BigQuery, Storage 3–6. Alerta em R$ 25 |
| Meio de pagamento | R$ 15 | 3% de cartão recorrente (hipótese) |
| Operação (Guardião) | R$ 200 → 75 → 43 | Operador a R$ 6.500/mês all-in ÷ 30, 80 e 150 clientes (hipótese) |
| Impostos sobre receita | R$ 30 a 70 | Simples ou Presumido, 6% a 14% (hipótese) |
| **Margem de contribuição** | **R$ 190 a 340 (38% a 68%)** | Sobe com o patamar do Guardião |

Premissas de aquisição e retenção (não são metas):

| Indicador | Valor | Conta |
|---|---|---|
| Churn | 5% ao mês | Retenção média de 20 meses |
| LTV bruto | R$ 9.980 | 20 × 499 |
| LTV de contribuição | R$ 3.800 a 6.800 | 20 × margem |
| CAC | R$ 1.000 a 1.500 | SDR, comissão de canal, proposta com diagnóstico; sem tráfego pago |
| LTV bruto / CAC | 6,7× a 10× | |
| Payback do CAC | 3 a 8 meses | Depende do patamar do Guardião |

Com churn de 5%, manter N clientes exige vender 0,05 × N por mês só para repor.

## 8. Estágios (cenários, não metas)

MRR = clientes × R$ 499. Salários e custos fixos são hipóteses. Valuation e múltiplo de ARR do original: removidos; a única linha aceitável é "SaaS B2B de ticket fixo com churn medido; múltiplo a definir com base auditada".

| | 100 clientes | 500 clientes | 2.000 clientes |
|---|---|---|---|
| Praças | 1 | 1 a 2 | 3 a 6 |
| MRR | R$ 49.900 | R$ 249.500 | R$ 998.000 |
| Guardião | P0/P1 · 30 por operador | P2 · 80 por operador | P2 · 150 por operador |
| Equipe | Head de Operação (também Guardião) · 1 engenheiro · 2 Guardiões · 1 SDR · jurídico e contabilidade externos | Head · 2 engenheiros · 7 Guardiões · 3 SDR · admin · externos | Head · 2 coordenadores · 4 engenheiros · 14 Guardiões · 8 comerciais · 3 admin/financeiro · jurídico externo |
| Custos fixos | R$ 47.500 | R$ 120.000 | R$ 346.000 |
| Tecnologia (teto R$ 25) | R$ 2.500 | R$ 12.500 | R$ 50.000 |
| Meio de pagamento (3%) | R$ 1.500 | R$ 7.500 | R$ 30.000 |
| Impostos | R$ 5.000 (Simples) | R$ 35.000 (Presumido) | R$ 140.000 |
| **Resultado operacional** | **− R$ 6.600** | **R$ 74.500 (~30%)** | **R$ 432.000 (~43%)** |
| Vendas/mês para repor churn | 5 | 25 | 100 |

- **100 clientes** valida a operação, não paga a equipe. Equilíbrio em torno de 115 a 130 clientes (fixos ÷ contribuição de ~R$ 409). Até lá é investimento dos sócios.
- **500 clientes** é a primeira estrutura que se sustenta; a margem depende do Guardião no P2 e da tecnologia abaixo de R$ 25.
- **2.000 clientes** exige 3 a 6 praças e um comercial que reponha 100 clientes por mês. A margem sobe porque o Guardião chega a 150 por operador e a engenharia não cresce com a base.
## 9. Tecnologia

Google Cloud (`radar-hml`, `radar-prd`, `southamerica-east1`): Cloud Run e Jobs, ADK em Python, Scheduler → Pub/Sub, Firestore, BigQuery, Storage, Secret Manager, Identity Platform, GitHub → Cloud Build, Terraform. Gemini é obrigatório para dados, medição e tudo que toca API ou superfície do Google; outros modelos só para linguagem, atrás do `LLMGateway`.

| Peça | Função | Cérebro ou serviço |
|---|---|---|
| Cartógrafo | Posição por termo e ponto; Mapa de Domínio; Diagnóstico; tarefas para o Editor | Gemini Pro com Grounding com Google Maps; Flash para normalizar |
| Editor | Posts, fotos, descrição, horários e feriados (72 h antes), serviços, atributos, auditoria; categoria só com Guardião | Linguagem para texto; Gemini multimodal para fotos; Gemini para campos do perfil |
| Anfitrião | Avaliações em ≤ 2 h, perguntas do perfil, temas, avaliação suspeita, material do QR | Gemini Flash para classificar; linguagem para responder; Gemini para política |
| Tesoureiro | Performance API, dashboard, Extrato, Horas Devolvidas, custo por tenant | Números só de SQL; Gemini Pro só para três frases |
| Redator-chefe | Boletim, Voz do Cliente, Fechamento; checagem cruzada de números | Gemini para checagem; linguagem para texto |
| Guardião (humano) | Aprova em lote, QA de 10% no P2, exceções; dois olhos para categoria, nome, endereço e notas ≤ 2 | Painel próprio |

Conectores: **GBP** (Business Information, Performance, avaliações, posts, mídia, Q&A; OAuth 2.0 com conta operacional no papel Gerente) · **Places** (`places:searchText` por ponto da grade; chave restrita; cache 30 dias, só `place_id` fica) · **WA da casa** (Cloud API, só para falar com o dono; quatro modelos de Utilidade) · **TTS** (Chirp 3 HD pt-BR, ≤ 60 s) · **Render & Delivery** (cards PNG, Mapa SVG, PDFs, dashboard Next.js, reenvio após 2 h). Sem Google Ads API, telefonia ou WhatsApp do cliente.

## 10. Retenção

- **Entrega contínua sem pedir nada:** Boletim na segunda às 7h, cinco entregas no dia 1. O dono vê a máquina trabalhar sem abrir nada.
- **Custo por contato visível:** o Extrato mostra R$ 499 ÷ contatos e a origem de cada número.
- **Horas Devolvidas:** catorze horas por R$ 499 é a comparação com contratar alguém.
- **Diário de Bordo com print:** "o que vocês fazem?" tem resposta em uma tela.
- **Cancelar custa mais que ficar:** o perfil volta a parar, a vaga da zona vai para o próximo da fila e a reentrada depende de haver vaga.
- **Sinais de risco antes do cancelamento:** 30 dias sem avaliação nova, Boletim não lido, queda em termo-chave, custo por contato subindo dois meses seguidos. Lista mensal para o Head de Operação.

Win-back: ex-cliente volta pela fila da zona, sem condição especial.

## 11. Riscos e mitigação

| Risco | Efeito | Mitigação |
|---|---|---|
| Mudança do Google (algoritmo, políticas, APIs) | Medição perde validade; ações do Editor deixam de valer | Só diretrizes oficiais; validação mensal da grade com 20 buscas manuais; método no rodapé do Mapa; nenhuma promessa de posição |
| Perfil suspenso ou verificação pendente | Entregas param | Detecção de `SUSPENDED`/`PENDING_VERIFICATION`; runbook de recurso; onboarding não bloqueia; aviso ao dono em uma linha |
| Cota, erro ou preço de API (Places, GBP, Vertex) | Medição incompleta; custo acima de R$ 25 | Máscara mínima; grade reduzida na semana, completa só no dia 1; `cost.alert` a R$ 25; retry idempotente; runbook |
| Aprovação das Business Profile APIs | Sem ela não há Editor, Anfitrião nem Tesoureiro | Pedido no dia 1 da montagem (1–2 semanas); Cartógrafo e Places funcionam enquanto espera |
| LGPD | Reclamação de titular; incidente | Dados do dono: nome e número (hash com sal); textos de terceiros como hash e temas; nenhuma mensagem a clientes finais; runbook de pedido de titular |
| Número da casa com qualidade baixa na Meta | Modelos bloqueados | Só modelos de Utilidade; SAIR na hora; avisos em horário comercial; monitor de opt-out; reenvio pelo dashboard |
| Modelo de IA fora do ar | Respostas atrasam | `LLMGateway` com fallback; fila de 24 h para avaliações; números nunca dependem de modelo |
| Erro público (resposta ou categoria errada) | Dano à reputação do cliente | Dois olhos para notas ≤ 2, categoria, nome e endereço; QA de 10%; Diário com print |
| Zona lotada com pedido de venda | Vender o que não se entrega | `zone.check` antes da proposta; fila por ordem de chegada; cláusula de zona |
| Concentração em uma praça | Evento local derruba a base | Segunda praça entre 300 e 500 clientes |

## 12. Jurídico e LGPD

Pauta para o advogado externo, oito itens do contrato:

1. **Mandato de operação.** Sem perguntar: posts, fotos, horários, respostas a avaliações e perguntas, ajustes de campos. Com um Sim: categoria principal, nome, endereço, ofertas. Nunca: prometer posição ou resultado, incentivo por avaliação.
2. **LGPD.** Dados do dono: nome e número. Textos públicos de terceiros tratados só para responder em nome da empresa, guardados como hash e temas. Nenhuma mensagem a clientes finais. Suboperadores: Google Cloud e APIs, Meta (número da casa), provedor do cérebro de linguagem, provedor de pagamento. Retenção: `actions_log` 5 anos; `llm_calls` 12 meses; dados do tenant até 90 dias após o contrato.
3. **Política de avaliações e conteúdo do Google.** Sem incentivo, sem seleção, respostas verdadeiras, sem dados do avaliador.
4. **Marca, fotos e imagem.** Uso das fotos reais autorizado; nunca se gera foto do estabelecimento.
5. **Preços, horários e informações comerciais.** Responsabilidade do cliente; origem registrada no Diário.
6. **Exclusividade limitada por zona.** Dois por segmento por zona; zona = bairro do Maps ou raio, com cidade e segmento no contrato; mudança de endereço ou categoria mantém a operação até o fim do ciclo pago e entra na fila da zona nova.
7. **Limitação de responsabilidade.** A promessa é a operação medida e registrada, não o resultado.
8. **Reversibilidade e encerramento.** Remoção do Gerente, entrega do histórico, exclusão no prazo, liberação da vaga.

Tributário: Simples Nacional no início; Lucro Presumido quando a receita exigir.

## 13. Roadmap resumido

Detalhe, pré-requisitos e critérios de pronto estão no arquivo de expansão.

| Fase | Módulo | Em uma linha |
|---|---|---|
| 0 | Radar Urbano | Este dossiê. Seis semanas de montagem e piloto de 30 dias |
| 1 | Radar Concorrência + Radar Menu | Só Google, sem acesso novo do cliente |
| 2 | Radar Stars | Fundação Meta para o cliente e convite de avaliação |
| 3 | Radar Chat | Recepcionista, telefonia e contatos em tempo real |
| 4 | Radar Ads | Mídia paga com corte por custo por contato |
| 5 | Suíte | Bundle e cross-sell por dado |

## 14. Próximos 90 dias

| Semana | O que acontece | Pronto quando |
|---|---|---|
| 1 | Fundação Google Cloud; pedido das Business Profile APIs; verificação na Meta e número da casa; contrato com o advogado | Pedidos protocolados; projetos no ar |
| 2–5 | Conectores, `LLMGateway`, Diário e custo; depois Cartógrafo e Tesoureiro; Editor, Anfitrião e Guardião; Redator-chefe, TTS, Delivery, onboarding automático e `zone.check` | Cada entrega roda de ponta a ponta com print no Diário |
| 6 | Runbooks, SLOs, offboarding, alerta de custo; cronometrar o Dia 0 | 11 testes de aceitação passam; Dia 0 em até 15 min |
| 7–10 | Piloto com 3 clientes (padaria, oficina, clínica) por 30 dias; primeira praça e lista de alvos por zona e segmento | Mês fechado com as 11 entregas; custo por tenant < R$ 25; nenhuma zona acima de 2 |
| 11–13 | Abertura comercial na primeira praça: SDR, contabilidades, proposta com diagnóstico reduzido | 20 a 30 clientes ativos; churn e CAC medidos; seção 7 revisada com dado real |

Definição de "montei": os 11 testes de aceitação passam; Dia 0 em até 15 minutos cronometrados; piloto fecha um mês com as 11 entregas e custo por tenant abaixo de R$ 25; ninguém tem senha de ninguém; nenhuma zona com mais de 2 tenants do mesmo segmento.


<!-- ======================================================================
     ARQUIVO: radar-urbano/02-POV-CLIENTE.md
     ====================================================================== -->

# Radar Urbano · Ponto de vista do cliente

## 1. A oferta em uma frase

Por R$ 499 por mês, o Radar Urbano opera o Perfil da Empresa no Google (Maps e Busca local) com agentes de IA, mede a posição da empresa ponto a ponto, responde toda avaliação em até 2 horas e entrega tudo no WhatsApp do dono, sem que ele gaste um minuto depois do Dia 0.

Promessa oficial: captura de intenção otimizada, lucrativa e eficiente. Não se promete venda, conversão nem "novos clientes".

## 2. Por que Google Maps e não redes sociais

| | Tráfego de atenção (redes sociais) | Tráfego de intenção (Google Maps) |
|---|---|---|
| Demanda | Latente: precisa ser criada antes de converter | Existente: a busca antecede a decisão |
| Ciclo | Longo, dependente de frequência paga | Curto: contato no mesmo dia da busca |
| Indicadores | Alcance, curtidas, salvamentos | Ligações pelo perfil, rotas, cliques no site, mensagens |
| Custo | Cresce com a frequência de impacto | Mensalidade fixa, sem verba de mídia |

Objetivo operacional: busca relevante, posição no top 3 da primeira tela, ação direta a partir do perfil.

## 3. O que o cliente recebe

Duas entregas de entrada (uma vez) e nove recorrentes. Tudo chega pelo número da casa (o WhatsApp do Radar Urbano) e fica no dashboard.

| Nº | Entrega | Quando | Por onde | O que é |
|---|---|---|---|---|
| 01 | Diagnóstico de Posição | Dia 0, minutos depois do acesso | Card no WhatsApp; PDF no dashboard | Onde a empresa aparece hoje (termos-chave em 9 pontos), o que falta no perfil, o que a máquina faz primeiro |
| 02 | Antes e Depois do Perfil | Dia 7, automático | Card lado a lado no WhatsApp; arquivo no dashboard | Perfil do Dia 0 e do dia 7, campo a campo, com a segunda medição |
| 03 | Dashboard Radar | A cada hora; dados do Google com data de referência | Link fixo, ícone no celular; senha opcional | Contatos, impressões, posição, reputação, Diário e custo por contato em uma tela |
| 04 | Boletim de Segunda | Segunda, 7h | Áudio de até 60 s + card no WhatsApp | A semana fechada pelo Google, o que a máquina fez, o que vem |
| 05 | Mapa de Domínio | Dia 1 de cada mês | Imagem no WhatsApp; versão interativa no dashboard | Posição por termo em cada ponto da grade: verde (top 3), cinza (4º a 10º), vermelho (fora do top 10) |
| 06 | Diário de Bordo do Perfil | Contínuo | Seção do dashboard; uma linha no WhatsApp quando há ação relevante | Toda ação no perfil com data, hora, campo, antes, depois e print |
| 07 | Motor de Reputação | Respostas em até 2 h; boletim mensal dia 1 | Respostas no próprio Google; card no WhatsApp; QR em PDF | Toda avaliação e pergunta pública respondida; link curto e QR de avaliação para o balcão; Boletim de Reputação |
| 08 | Extrato de Demanda | Dia 1 | PDF de uma página no WhatsApp; série no dashboard | Contatos do mês por tipo e custo por contato |
| 09 | Horas Devolvidas | Dia 1 | Card no WhatsApp | Horas de trabalho executadas pela máquina, por tabela de equivalência publicada |
| 10 | Voz do Cliente | Dia 1; alerta quando um tema repete | Card no WhatsApp | Três elogios e três atritos das avaliações e perguntas, com uma evidência cada |
| 11 | Fechamento Executivo | Dia 1; trimestral a cada 3 meses | PDF no WhatsApp; arquivo permanente no dashboard | O mês em uma página: contatos, custo por contato, mapa, reputação, horas, o que foi feito e o que vem |

Nenhuma entrega passa de 60 segundos de áudio ou uma página. Números do Google chegam com data de referência (atraso de 2 a 3 dias, sem tempo real); os da própria máquina, de hora em hora.

## 4. O que o cliente nunca faz

1. Zero reuniões: não existe call de alinhamento, de resultado, de nada.
2. Zero login obrigatório: quem nunca abrir o dashboard recebe tudo pelo WhatsApp; SAIR interrompe os envios.
3. Zero aprovação: posts, fotos, horários, descrição, serviços, atributos e respostas foram pré-autorizados no Dia 0; categoria principal, nome, endereço e ofertas chegam como pergunta de Sim/Não.
4. Zero relatório longo: áudio de até 60 segundos ou uma página.
5. Zero surpresa: toda ação fica no Diário de Bordo com print antes de qualquer resumo; um humano (o Guardião) revisa por amostragem.
6. Zero cobrança de esforço: a máquina nunca pede foto, texto, tabela ou senha; entra como Gerente convidada pelo dono e sai quando ele quiser.

## 5. Os únicos 15 minutos (Dia 0)

Antes da conversa, fora dos quinze: verificação da zona pelo comercial, contrato por link, cartão no provedor de pagamento (5 minutos no celular).

| Minuto | Passo | O que o dono faz |
|---|---|---|
| 0 a 5 | Cinco perguntas por áudio no WhatsApp | Responde: o que mais vende e como o cliente procura; bairros ou raio que importam; o jeito da casa de falar; o que a máquina pode fazer sem perguntar; em que número recebe e como quer ser chamado |
| 5 a 8 | Gerente no Perfil da Empresa | Um toque: adiciona o e-mail operacional do Radar Urbano como Gerente. Se o perfil não está verificado, recebe o passo a passo; o resto não espera |
| 8 a 10 | Dashboard e Diagnóstico | Recebe o link fixo, cria senha se quiser, recebe o Diagnóstico de Posição na mesma conversa |
| 10 a 15 | Folga | Reservada para quem trava no perfil. Quinze é o teto, não a meta |

O Sim ao fim das cinco perguntas confirma o número e registra o consentimento para receber as entregas.

## 6. Preço e condições

| Item | Valor |
|---|---|
| Mensalidade | R$ 499, fixa |
| Equivalente por dia | R$ 16,63 |
| Contrato | Mensal, cancelável, sem fidelidade |
| Verba de mídia | Não existe neste produto |
| Setup ou taxa de entrada | Não existe |
| Cobrança | Cartão no provedor de pagamento; nota fiscal mensal |

Compromisso do Radar Urbano: perfil estruturado por completo na primeira semana (prova no Antes e Depois do dia 7) e operação medida e registrada todo mês.

## 7. Trava territorial

Regra: no máximo 2 empresas do mesmo segmento (categoria principal do perfil) na mesma zona (bairro do Google Maps ou raio equivalente, escrito no contrato com a cidade).

- Motivo técnico: perfis concorrentes na mesma malha de busca disputam as mesmas três posições e degradam o resultado de todos.
- O que o cliente ganha: no máximo um outro do mesmo ramo na mesma zona dentro do Radar Urbano, como cláusula de exclusividade limitada no contrato.
- Como verifica: antes de vender, o comercial consulta segmento + zona; resposta em uma linha (livre, 0 ou 1 de 2; ou lotada, 2 de 2 com fila). A consulta repete na assinatura. O cliente pode perguntar quantos há na zona dele e ouve o número.
- Reserva: a proposta escrita reserva a vaga por 5 dias úteis; a vaga só se ocupa na assinatura. Fila por ordem de chegada, sem exceção.
- Se a zona muda (endereço, categoria principal, raio maior): nova consulta antes de mudar; com vaga, aditivo e liberação da vaga antiga no mesmo dia; sem vaga, opera até o fim do ciclo pago e entra na fila da zona nova. A mensalidade não muda.

## 8. O que medimos e o que não prometemos

Contato é o que o Google conta a partir do perfil:

| Linha | O que conta |
|---|---|
| Ligações pelo perfil | Toques no botão Ligar contados pelo Google (não são ligações atendidas) |
| Pedidos de rota | Toques em Rotas ou Como chegar |
| Cliques no site | Toques no link do site publicado no perfil |
| Mensagens pelo perfil | Conversas iniciadas pelo chat do próprio perfil, quando o dono o mantém ligado |

Impressões (Busca e Maps) e palavras-chave de descoberta são contexto; não entram na soma.

Custo por contato = R$ 499 ÷ contatos do mês. Exemplo (padaria, mês típico): 118 ligações + 97 rotas + 31 cliques + 14 mensagens = 260 contatos; custo por contato R$ 1,92. Oficina: 168 contatos, R$ 2,97. Clínica: 160 contatos, R$ 3,12. Números de exemplo; os do cliente são conferíveis no dashboard e na tela de desempenho do próprio Google.

O que não existe: taxa de conversão, receita atribuída, "novos clientes gerados", simulador de retorno, promessa de posição. O dono põe o valor de um contato no balcão dele por cima do custo por contato e faz a conta em um segundo.

## 9. Comparação

| Critério | Equipe interna | Agência tradicional | Radar Urbano |
|---|---|---|---|
| Custo mensal direto | R$ 3.500 a R$ 6.000 (CLT + encargos) | R$ 1.800 a R$ 4.500 + taxas | R$ 499 fixos |
| Foco de execução | Diluído em várias demandas | Redes sociais e branding | Só Perfil da Empresa no Google |
| Métrica de controle | Entregáveis internos | Alcance e engajamento | Ligações pelo perfil, rotas, cliques no site, mensagens |
| Tempo de implantação | 30 a 90 dias (contratação) | 15 a 45 dias (onboarding) | Diagnóstico no Dia 0; perfil a limpo em 7 dias |
| Tempo do dono | Gestão da pessoa | Reuniões e aprovações | Até 15 minutos, uma vez |
| Vínculo | Rescisão onerosa | Fidelidade de 12 meses | Mensal, sem fidelidade |

Nenhuma coluna promete resultado.

## 10. Acessos que o cliente concede

| Acesso | O que é | O que nunca acontece |
|---|---|---|
| Gerente no Perfil da Empresa | Um toque no Dia 0: adiciona o e-mail operacional do Radar Urbano com papel Gerente | Senha do Google do cliente; propriedade do perfil |
| Número de WhatsApp | Só para receber entregas e perguntas de Sim/Não do número da casa | Mensagens a clientes finais; WhatsApp da empresa do cliente |
| Cartão no provedor de pagamento | Cadastro direto no provedor | Dados do cartão no Radar Urbano |
| Dashboard | Conta criada pelo Radar Urbano; senha opcional, criada pelo cliente | Ninguém do Radar Urbano vê a senha |

O que a máquina faz sem perguntar (mandato no contrato): posts, fotos, horários e feriados, descrição, serviços, atributos, respostas a avaliações e perguntas. O que exige um Sim: categoria principal, nome, endereço, ofertas. O que nunca faz: prometer posição ou resultado, incentivar ou selecionar avaliações, publicar foto gerada do estabelecimento.

Dados guardados: nome e número do dono; avaliações e perguntas públicas só como tema, sentimento e hash.

## 11. Como sair

- Cancela quando quiser, pelo WhatsApp ou pelo dashboard; vale a partir do fim do ciclo pago.
- SAIR a qualquer momento interrompe os envios sem cancelar o serviço; o trabalho no perfil continua.
- No encerramento: o Radar Urbano é removido como Gerente, o perfil fica com tudo que foi publicado, o histórico (Diário, extratos, fechamentos, mapas) é entregue ao dono, os dados são apagados no prazo do contrato (90 dias) e a vaga na zona é liberada para a fila.
- O que se perde: o perfil vivo, as respostas em 2 horas, a medição, o extrato e a vaga na zona.


<!-- ======================================================================
     ARQUIVO: radar-urbano/03-POV-PLAYER.md
     ====================================================================== -->

# Radar Urbano · 03-POV-PLAYER

Memorando de investimento do Radar Urbano como produto único. Tudo que é número de escala, CAC, LTV, imposto e múltiplo está marcado como hipótese ou projeção. Os únicos números fechados são os do produto: preço, custo de tecnologia, trava territorial, dimensionamento de operador e prazo de montagem.

## 1. Tese em cinco linhas

1. Comércio local é encontrado pelo Google Maps e pela Busca local; o perfil da empresa é o canal, e quase ninguém o opera direito.
2. O Radar Urbano opera esse perfil por assinatura fixa de R$ 499/mês, com cinco agentes de IA e um humano com painel, e zero tempo do dono depois dos 15 minutos do Dia 0.
3. A promessa é operação medida e registrada (posição, contatos contados pelo Google, custo por contato); nunca conversão, receita ou "novos clientes".
4. A trava de 2 empresas por segmento por zona cria escassez vendável e um teto de crescimento por praça; crescer é abrir zonas e praças.
5. O custo marginal por cliente é pequeno (tecnologia R$ 12–25, operador para 30 → 80 → 150 clientes), então a margem de contribuição sobe com a escala sem inchar a folha.

## 2. O produto e o preço

| Item | Valor |
|---|---|
| Preço | R$ 499/mês, fixo, mensal, cancelável; sem verba de mídia |
| Onze entregas | 2 de entrada (Diagnóstico de Posição no Dia 0, Antes e Depois no Dia 7) e 9 recorrentes (Dashboard, Boletim de Segunda, Mapa de Domínio, Diário de Bordo, Motor de Reputação, Extrato de Demanda, Horas Devolvidas, Voz do Cliente, Fechamento Executivo) |
| Quem faz | Cartógrafo, Editor, Anfitrião, Tesoureiro, Redator-chefe; Guardião humano por amostragem |
| Tempo do dono | Até 15 minutos no Dia 0; depois, respostas de Sim ou Não |
| Acesso | Papel de Gerente no Perfil da Empresa; nunca senha do cliente |
| Métrica ao cliente | Contagens do Google (ligações pelo perfil, rotas, cliques no site, mensagens) com data de referência; custo por contato = R$ 499 ÷ contatos |
| Exclusividade | No máximo 2 do mesmo segmento na mesma zona, em contrato |

Exemplo do brief (padaria, mês típico): 260 contatos, custo por contato R$ 1,92; 14h07 de trabalho devolvidas por mês na clínica. O argumento de venda é "catorze horas por R$ 499", não retorno projetado.

## 3. Economia unitária (por cliente, por mês)

| Linha | Valor | Base |
|---|---|---|
| Receita | R$ 499 | Preço fixo |
| Impostos | R$ 30 (6%) | Hipótese: Simples Nacional no início; em Lucro Presumido a linha vai a ~14% (R$ 70) |
| Cobrança (cartão) | R$ 15 (3%) | Hipótese |
| Tecnologia | R$ 12–25 | Gemini R$ 3–5, linguagem R$ 2–4, Places R$ 3–8, WhatsApp da casa R$ 1–2, TTS/Cloud Run/BigQuery/Storage R$ 3–6; alerta em R$ 25 |
| Operação (Guardião) | R$ 200 → R$ 75 → R$ 40 | Operador a R$ 6.000/mês (hipótese, com encargos) para 30 → 80 → 150 clientes |
| Margem de contribuição | R$ 234 → R$ 359 → R$ 394 | 47% → 72% → 79%, com tecnologia em R$ 20 e Simples |
| Churn | 5%/mês | Hipótese conservadora; vida média 20 meses |
| LTV (receita) | R$ 9.980 | 499 × 20 |
| LTV (contribuição) | R$ 7.200 | R$ 359 × 20, no patamar de 80 clientes por operador |
| CAC | R$ 1.000–1.500 | Hipótese: SDR, verificação de zona, contrato por link, Dia 0 assistido; sem mídia paga no início |
| Payback do CAC | 3–4 meses | CAC ÷ contribuição de R$ 359 |
| LTV/CAC | 5–7x | Contribuição sobre CAC |

O que move a tabela: o número de clientes por operador (a única linha grande) e o custo por tenant (a métrica de primeira classe da operação). Sem telefonia, sem WhatsApp da empresa e sem atendimento em tempo real, não há plantão: por isso o operador escala de 30 para 150.

## 4. Fases de escala (projeção)

MRR = clientes × R$ 499. Custos fixos com faixas salariais de mercado como hipótese; imposto no Simples até 100 clientes e Lucro Presumido (14%) a partir de 500.

| | 20 clientes | 100 clientes | 500 clientes | 2.000 clientes |
|---|---|---|---|---|
| MRR | R$ 9.980 | R$ 49.900 | R$ 249.500 | R$ 998.000 |
| Equipe | Head + 1 engenheiro; Head é o Guardião e o comercial | Head, 1 engenheiro, 2 operadores, 1 SDR | Head, 2 engenheiros, 7 operadores, 3 SDR, 1 admin/financeiro | Head + 2 coordenadores, 4 engenheiros, 14 operadores, 8 SDR, 3 admin/financeiro/RH |
| Custo fixo estimado | R$ 32 mil | R$ 51 mil | R$ 119 mil | R$ 285 mil |
| Custo variável (impostos, cobrança, tecnologia) | R$ 1,3 mil | R$ 6,5 mil | R$ 52 mil | R$ 210 mil |
| Resultado mensal | −R$ 23 mil | −R$ 8 mil | +R$ 78 mil (31%) | +R$ 503 mil (50%) |
| Praças | 1 | 1 | 2–3 | 6–8 |
| Guardião | P0 (tudo aprovado antes) | P1 (lote) | P2 (10% de amostragem) | P2 |

Leitura: o ponto de equilíbrio fica perto de 120 clientes com esta equipe. A margem só aparece de verdade quando o operador passa de 80 clientes e o imposto é o único custo variável relevante. Nada aqui é a margem de 83,5% do memorando antigo; aquela conta não tinha operação.

## 5. Capacidade e trava

- Regra: 2 empresas por segmento por zona (bairro do Google Maps ou raio equivalente, escrito no contrato com cidade e segmento). Segmento é a categoria principal do perfil.
- Motivo técnico: dois perfis concorrentes na mesma malha de busca disputam as mesmas posições e degradam o resultado dos dois.
- Como escassez: a vaga é vendida como exclusividade limitada; proposta escrita reserva por 5 dias úteis; a vaga só se ocupa na assinatura; fila por ordem de chegada, sem exceção.
- Como limite: capacidade de uma praça = zonas × segmentos vendáveis × 2. Hipótese para uma cidade média: 40 zonas × 30 segmentos × 2 = 2.400 vagas teóricas; com ocupação realista de 10–15%, 240–360 clientes por praça. Isso dita o número de praças da tabela da seção 4.
- Como se expande: novas zonas (carga na tabela `zones`), novas praças (tabela de zonas e de feriados municipais da cidade, um comercial local); o núcleo da máquina não muda. Redesenho de zona não expulsa quem já está.
- Consequência para o investidor: crescimento é geográfico e previsível; não existe "vender mais para o mesmo bairro".

## 6. Por que a operação escala sem inchar

- Cinco agentes fazem a execução (medição, perfil, reputação, números, texto e voz); o humano só aprova, audita por amostragem e trata exceção.
- Guardião em patamares: P0 tudo aprovado antes; P1 lote com meta de > 85% sem edição; P2 publicação direta com QA de 10%. Categoria, nome, endereço e notas 1 e 2 sempre com dois olhos.
- Sem atendimento em tempo real: nenhum plantão, nenhum SLA de minutos, todas as cadências são jobs (30 min, hora, dia, semana, dia 1).
- Custo por tenant é métrica de primeira classe: cada chamada grava custo em `llm_calls` e `actions_log`; alerta em R$ 25; runbook de redução (grade menor, Flash, cache).
- Um Head de Operação desde o P0, um engenheiro; o resto cresce por clientes por operador, não por cliente.

## 7. Retenção e lock-in honesto

O que segura:
- Entregas no celular do dono toda segunda às 7h e todo dia 1; o cancelamento tem uma data e um rosto (o Boletim que para de chegar).
- Diário de Bordo com print: histórico de tudo que a máquina fez no perfil, com prova.
- Série própria de medição de posição (por termo, ponto e data), que não se compra depois.
- A vaga na zona: quem cancela libera a vaga para a fila; voltar depende de ter vaga.
- Custo por contato visível, calculado do que o Google conta.

Churn alvo: 5%/mês na hipótese base; abaixo de 3% no piloto seria sinal, não plano.

O que derruba:
- Um mês sem melhora visível de posição em um perfil já bem posicionado (o produto entrega manutenção, não ganho infinito).
- Perfil suspenso pelo Google no meio do contrato.
- Dono que não lê o Boletim e não entende custo por contato; a venda precisou do "catorze horas por R$ 499".
- Agência local que oferece o mesmo por menos, sem prova e sem trava.

Sem fidelidade abusiva: o lock-in é dado, prova e vaga, não contrato.

## 8. Riscos

| Risco | Efeito | Mitigação |
|---|---|---|
| Dependência do Google e das Business Profile APIs | Aprovação de acesso (1–2 semanas) é caminho crítico; mudança de termos ou cotas para o produto | Pedido no dia 1; conector isolado; Places API dentro dos termos (cache 30 dias, só `place_id`); nunca raspagem |
| Suspensão de perfis | Tenant sem operação por dias ou semanas | Runbook: congelar Editor, apelação com o cliente, auditoria de conformidade em 100% dos tenants em 48 h; nome sem termos de busca, categoria só com humano |
| Cotas de API e custo | Medição do dia 1 incompleta; custo por tenant acima de R$ 25 | Retentativa idempotente; grade reduzida; alerta e runbook de custo |
| LGPD | Dados de terceiros (avaliadores) e do dono | Hash e temas, sem texto guardado; suboperadores nomeados; nenhuma mensagem a clientes finais; canal de titular em 15 dias |
| Meta (número da casa) | Qualidade do número cai com opt-outs; entrega para o dono para | Só modelos de utilidade; SAIR respeitado; dashboard como segunda porta |
| Execução | Seis semanas com dois profissionais; um engenheiro é ponto único de falha | Terraform, deploy automático, Diário de Bordo; plano de segundo engenheiro em 100 clientes |
| Concorrência de agências | Oferta parecida, mais barata, sem prova | Trava de zona, Diário com print, série de posição, custo por contato; nunca prometer posição |
| Promessa mal vendida | Comercial promete conversão e o contrato não sustenta | Cláusula de limitação; treinamento; proibição explícita de "novos clientes" e ROI |
| Churn acima da hipótese | LTV cai, payback estica | Medir no piloto antes de contratar SDR; alavanca é Guardião P1/P2 e Boletim |

## 9. Uso de capital

Montagem (6 semanas, 1 engenheiro sênior + 1 Head de Operação):

| Item | Valor (hipótese) |
|---|---|
| Engenheiro sênior, 1,5 mês | R$ 25–30 mil |
| Head de Operação, 1,5 mês | R$ 18–22 mil |
| Jurídico (contrato com mandato, LGPD, cláusula de zona) | R$ 5–10 mil |
| Google Cloud, Meta, Places, ferramentas, domínio | R$ 3–5 mil |
| Total da montagem | R$ 50–65 mil |

Piloto (semana 6 em diante, 3 clientes, 30 dias): mesma equipe, tecnologia ≤ R$ 75 total, Guardião em P0. Critério de pronto: 11 testes de aceitação, Dia 0 em até 15 minutos, custo por tenant abaixo de R$ 25, zero senha de cliente, zero zona com 3 tenants.

Primeiros 90 dias depois do piloto: equipe de 2 (R$ 30–35 mil/mês) + 1 SDR a partir do mês 2 (R$ 6 mil/mês) + tecnologia; meta de 20 clientes no fim do período (MRR R$ 9.980). Queima acumulada até o mês 5: R$ 180–250 mil. Esse é o capital do primeiro ciclo; o segundo (100 → 500) só se justifica com churn e CAC medidos no piloto.

## 10. Saída

Hipótese: receita recorrente de serviço com operação humana negocia a 3–6x ARR em aquisição por agência, consolidador ou plataforma de SaaS local; o múltiplo depende de churn medido e margem por praça, não de projeção. Sem valuation neste documento.


<!-- ======================================================================
     ARQUIVO: radar-urbano/04-EXPANSAO.md
     ====================================================================== -->

# Radar Urbano · Expansão

Duas dimensões independentes: (A) mais zonas, praças e clientes do produto único; (B) mais módulos ligados por tenant. A trava de 2 empresas por segmento por zona vale nas duas.

## Parte A · Expansão geográfica e comercial

### A1. A unidade de expansão

- Unidade: **zona × segmento**, com **2 vagas**.
- Zona = bairro do Google Maps ou raio equivalente, gravado no contrato com cidade e segmento. Não é a sobreposição de grades de medição.
- Segmento = categoria principal do perfil no Google (padaria e pizzaria são segmentos diferentes).
- Vaga se reserva pela proposta escrita (5 dias úteis) e se ocupa na assinatura, em transação na tabela `zones`. Fila por ordem de chegada, sem exceção.
- Consequência: a receita máxima de uma praça é finita e conhecida antes de vender. Crescer é abrir zonas e segmentos novos.

### A2. Capacidade por praça

Fórmula: **vagas = zonas × segmentos relevantes × 2**. Segmento relevante: tem demanda por busca local e ao menos 2 perfis fracos na zona (levantado por dados públicos antes de abrir a praça).

Exemplo (números redondos, só para ilustrar):

| Variável | Valor de exemplo |
|---|---|
| Zonas na cidade (bairros com busca local relevante) | 40 |
| Segmentos relevantes por zona | 12 |
| Vagas teóricas (40 × 12 × 2) | 960 |
| Ocupação realista (nem toda zona tem 2 candidatos em cada segmento) | 30–50% |
| Clientes alcançáveis na praça | 300–480 |
| Receita mensal no teto realista (× R$ 499) | R$ 150 mil – R$ 240 mil |

Regras: contar bairros pelo Maps, não pelo IBGE; bairro sem volume de busca local não conta; segmento é categoria principal (padaria, pizzaria, oficina, dentista são quatro segmentos); refazer a estimativa a cada 100 clientes com os dados reais de `zones`.

### A3. Sequência de crescimento

| Estágio | Clientes | Onde | O que prova | Gatilho para o próximo |
|---|---|---|---|---|
| Piloto | 3 (padaria, oficina, clínica) | Praça piloto | 11 entregas por 30 dias; Dia 0 em até 15 min; custo por tenant < R$ 25; Guardião em P0 | 11 testes de aceitação passando |
| Tração | 20 | Mesma praça | Onboarding sem engenheiro; Guardião em P1; custo de aquisição por canal conhecido | 20 clientes vivos por 60 dias |
| Praça | 100 | Mesma cidade | 1 operador para 80 clientes; P2 com QA de 10%; runbooks usados | Critérios de abertura (abaixo) |
| Segunda praça | 100 → 200+ | Cidade nova | O roteiro repetido sem o fundador; tabelas por cidade funcionando | Repetir |

Critérios para abrir praça nova (todos):

1. Zonas lotadas acima de 40% nos segmentos-alvo da praça atual, ou fila de espera maior que 10.
2. Ao menos 1 Guardião abaixo de 60% da capacidade do estágio.
3. Custo de tecnologia por tenant abaixo de R$ 25 por 3 meses; churn mensal abaixo de 5% no mesmo período.
4. Levantamento de capacidade da cidade nova (A2) com ao menos 200 vagas realistas.
5. Calendário municipal, fuso e `zones` da cidade nova carregados antes da primeira proposta.

### A4. Equipe por estágio

| Papel | Piloto (3) | 20 | 100 | 500 (várias praças) |
|---|---|---|---|---|
| Head de Operação | 1 | 1 | 1 | 1 |
| Engenheiro de automação | 1 | 1 | 1 | 2 |
| Guardiões / operadores | 1 (o Head) | 1 | 2 (80 clientes/operador) | 4 (150 clientes/operador) |
| Comercial / SDR | fundador | 1 | 2 | 1 por praça |
| Jurídico | externo | externo | externo | externo |

A razão clientes/operador sobe 30 → 80 → 150 porque não há atendimento em tempo real. O SDR verifica a zona antes de qualquer proposta e assiste o Dia 0. Praça nova exige SDR ou parceiro local; operação e engenharia ficam centralizadas.

### A5. Canais de aquisição por praça

| Canal | Como funciona | Custo e observações |
|---|---|---|
| Outbound por dados públicos | Perfis fracos por zona e segmento (categoria errada, sem fotos, sem horário de feriado, avaliações sem resposta) via Places API dentro dos termos e consulta manual; abordagem com Diagnóstico de Posição reduzido | Só `place_id` fica além de 30 dias; sem raspagem |
| Contabilidades | Escritórios contábeis da praça indicam clientes por segmento | Comissão de indicação |
| Associações de segmento | Material com a trava de 2 por zona como argumento (escassez real) | Custo baixo; funciona por segmento, não por bairro |
| Indicação de cliente | Vaga da zona vizinha oferecida a quem indica | Só se a zona estiver livre; sem desconto no preço fixo |
| Material do balcão | QR e link curto levam a marca | Passivo |

Argumento de venda em todos os canais: contagens, custo por contato e o Diário de Bordo. Nunca conversão, receita ou "novos clientes".

### A6. O que muda na máquina ao crescer

| Peça | Hoje (uma praça) | Com várias praças |
|---|---|---|
| `zones` | `zones(segmento, zona, cidade, tenants_ativos, limite=2)` | Mesma tabela; `cidade` vira chave obrigatória; auditoria diária por cidade (zero linhas com mais de 2 ativos) |
| Tabela de cidades | Implícita | `cities(cidade, uf, fuso, ativa, aberta_em)`; `tenants` ganha `cidade`; `zone.check(segmento, zona, cidade)` |
| Calendário de feriados | Nacional + municipal da praça piloto | Uma linha por cidade e data, carregada antes de abrir a praça; `calendar.holidays(cidade, de, ate)` já recebe cidade |
| Fuso horário | Horário de Brasília | `cities.fuso`; Boletim às 7h locais; avisos e perguntas das 8h às 19h locais; jobs internos (03h, 05h) seguem em Brasília |
| Guardião | Uma fila | Fila com filtro por cidade e por operador; cada operador tem praças atribuídas |
| Custo por tenant | Média geral | `cost.per_tenant` também por cidade; praça acima de R$ 25 entra no runbook antes de crescer |
| Cotas de API | Uma chave Places, um OAuth GBP | Mesmas credenciais; pedir aumento de cota a cada 100 clientes |
| Número da casa | Um | Um serve todas as praças; segundo só se a qualidade cair (runbook) |
| Comercial | Verificação de zona manual pelo SDR | Painel de disponibilidade por cidade/zona/segmento, lido de `zones`, com fila |

Nada disso altera agentes, entregas ou preço. É configuração e tabela.

## Parte B · Expansão por módulos

### B1. As fases

| Fase | Módulo | O que devolve ao cliente | Acesso novo do cliente | Pré-requisito / caminho crítico | Preço | Montagem | O que muda nos documentos |
|---|---|---|---|---|---|---|---|
| 0 | Radar Urbano (núcleo) | 11 entregas, 5 agentes + Guardião, 4 conectores | Gerente no perfil, WhatsApp do dono, cartão | Business Profile APIs (1–2 semanas); Meta para o número da casa | R$ 499 | 6 semanas + piloto 30 dias | Nenhum: são os documentos atuais |
| 1 | Radar Concorrência + Radar Menu | "Quem ganhou a semana" (sábado 9h); Sentinela como agente (feriado, clima, pico de busca, concorrente); comparação nominal no Mapa de Domínio; catálogo com preço; "O que te procuram" no dia 1 | Nenhum (3 concorrentes e a lista de itens, por áudio) | Núcleo vivo com Cartógrafo aprovado (85% nas 20 buscas); lista de ações autorizadas por tenant; jurídico em 3 frases | R$ 399 + R$ 399 | 3 semanas + piloto | Entregas: 2 seções; 05 e 07 ganham comparação. Acessos: 3 frases, 2 perguntas. Mundi: Sentinela, `places.get_details`, clima. Bíblia: cap. XI e XII |
| 2 | Radar Stars | Convite de avaliação após atendimento pelo WhatsApp da empresa; Boletim de Reputação com contagem de convites | Sistema E: WhatsApp da empresa (Meta, Embedded Signup, número dedicado) | Tech Provider na Meta (dias a semanas, pedido no dia 1); verificação da empresa do cliente; jurídico item 3 | R$ 299 | 3 semanas + piloto | Acessos: Sistema E, itens 2, 3 e 8, passo "minuto 10 a 14". Mundi: WA Connector com 2 metades, `wa_linked`. Bíblia: cap. XIII |
| 3 | Radar Chat | Recepcionista 24/7, Agenda das 7h, número de rastreamento, Resgate de Ligações Perdidas; dashboard em tempo real; "pediu preço" e "horários marcados" no Extrato | Sistema F: telefonia + Sistema E | Fase 2; provedor de telefonia (cadastro regulatório, números por DDD); teste em 3 operadoras; jurídico itens 1, 2, 3, 8 | R$ 499 | 4 semanas + piloto | Entregas: 3 seções; 03 e 08 redefinidos. Acessos: Sistema F. Mundi: Recepcionista, Voice Connector, SLO de latência; Guardiões 20→60→120. Bíblia: cap. XIV |
| 4 | Radar Ads | Micro-campanhas de busca com raio e teto; Extrato de Mídia com custo por contato por campanha; corte automático | Sistema G: Google Ads (conta do cliente vinculada à MCC) | Fundação Telefonia da Fase 3 (atribuição); developer token (dias a semanas); limiares por segmento; verificação de anunciante | R$ 699 (verba do cliente à parte) | 3 semanas + simulação 31 dias + piloto | Entregas: Extrato de Mídia; 11 ganha linha. Acessos: Sistema G, itens 1 e 7. Mundi: Estrategista, Ads Connector. Bíblia: cap. XV |
| 5 | Suíte | Os 5 módulos num contrato; proposta de expansão no 3º Fechamento (conta de equilíbrio, não previsão); custo por módulo | Sistemas A a G, contrato com anexos | Os 5 pilotos fechados; provedor de pagamento com bundle; 1 trimestre de um tenant com tudo | R$ 1.500–2.200 | 2 semanas + piloto de 1 trimestre | Acessos: anexos, encerramento por módulo. Mundi: 8 agentes, custo por módulo. Bíblia: VII.4, VIII.7, VIII.8 |

Sequencial com 1 engenheiro: 44 semanas depois do núcleo (cerca de 1 ano do dia 1). Com 2 engenheiros e montagem da fase seguinte durante o piloto da anterior: cerca de 9 meses. Venda de módulo só com piloto fechado.

Alerta de custo por tenant: R$ 25 no núcleo + Concorrência 2 + Menu 1 + Stars 2 + Chat 5 + Ads 5 = R$ 40 na suíte.

### B2. Regra da modularidade

```
tenants.modules_json = {
  "concorrencia": {"ativo": false},
  "menu":         {"ativo": false},
  "stars":        {"ativo": false},
  "chat":         {"ativo": false},
  "ads":          {"ativo": false},
  "suite":        false
}
todo job de módulo:  if not tenant.modules[MODULO].ativo: return   (uma linha, sem custo)
alerta de custo:     COST_ALERT_PER_TENANT_BRL = 25 + soma dos acréscimos dos módulos ativos
```

1. Liga e desliga por tenant, pela flag. Nenhum agente, conector ou tabela do núcleo muda.
2. Cada módulo traz as próprias peças com o próprio nome (`competitor_snapshots`, `invites`, `calls`, `campaigns`).
3. Cada módulo traz os próprios acessos (sistemas E, F, G) e cláusulas (anexos); o Dia 0 ganha um passo dentro dos mesmos 15 minutos.
4. As 11 entregas do núcleo não são renumeradas; entregas de módulo têm nome e aparecem no Dashboard, Boletim e Fechamento só com o módulo ligado.
5. Compartilhado: LLMGateway, Diário de Bordo (coluna `modulo`), Guardião (uma fila), número da casa, Dashboard, Tesoureiro (custo por módulo), Cartógrafo (uma medição serve Mapa, Concorrência e Ads), trava de zona.
6. Cada fase fecha com piloto de 30 dias nos 3 clientes do núcleo, Guardião em P0 para o módulo novo.
7. Desligar um módulo remove só acessos, segredos e cadências dele e exporta o histórico. Não existe módulo sem núcleo.

### B3. Dependências

| Módulo | Depende de | Deixa pronto para | Pode inverter com |
|---|---|---|---|
| Concorrência | Núcleo (Cartógrafo, Places, Editor, Delivery) | `top_place_ids` no Mapa; sinais para o Editor | Qualquer um |
| Menu | Núcleo (Editor, GBP Connector, Guardião) | Itens de catálogo para cross-sell e termos do Ads | Qualquer um |
| Stars | Núcleo (Anfitrião) + Fundação Meta | A Fundação Meta, que o Chat usa inteira | Chat (depois dele, Stars cai para 1 semana) |
| Chat | Núcleo + Fundação Meta + Fundação Telefonia | `calls`, número de rastreamento (Ads), evento `atendimento.concluido` (Stars) | Stars; nunca depois do Ads |
| Ads | Núcleo (Cartógrafo) + Fundação Telefonia | Extrato de Mídia para o Fechamento | Nada; Recepcionista recomendada, não obrigatória |
| Suíte | Os cinco | Bundle, proposta de expansão, custo por módulo | Nada |

### B4. Ordem alternativa

| Caminho | Ordem | Quando usar | Efeito no prazo |
|---|---|---|---|
| A · Padrão | 1, 2, 3, 4, 5 | Menor acesso novo primeiro; 1 engenheiro | 44 semanas |
| B · Atendimento primeiro | 3 (com Fundação Meta dentro), 2, 1, 4, 5 | Praças de oficina e clínica (ligação perdida dói mais que posição) | Chat 5 semanas; Stars 1 semana |
| C · Reputação primeiro | 2, 1, 3, 4, 5 | Praças com nota baixa ou poucas avaliações | Igual ao padrão; Chat herda a fundação |
| Menu sozinho | Menu (2 semanas), depois Concorrência (2 semanas) | Piloto de alimentação | Fase 1 vira 4 semanas em duas partes |
| Ads sem Chat | Só Fundação Telefonia (número, encaminhamento, `calls`) + Ads | Cliente quer verba, não quer atendimento automático | +R$ 5 telefonia +R$ 5 Ads no alerta |

Nunca inverte: Ads antes da telefonia (sem atribuição); qualquer módulo antes do núcleo com piloto fechado; suíte antes dos 5 pilotos; venda antes do piloto.

### B5. O que não muda em nenhuma fase

1. Nenhuma métrica de conversão, receita atribuída, "novos clientes" ou ROI. Só contagens e custo por contato.
2. Gemini para dados, medição e tudo que toca API do Google (Sentinela, Recepcionista e Estrategista incluídos); outros cérebros só para linguagem, atrás da LLMGateway.
3. Nunca a senha do cliente: Gerente no perfil, Embedded Signup com código do cliente, convite na MCC, cartão no provedor.
4. Zero tempo do dono; os únicos minutos são no Dia 0 (15, inteiros, com a suíte).
5. Diário de Bordo append-only com print, uma tabela, coluna `modulo`.
6. Custo por tenant: alerta R$ 25 + acréscimos declarados, até R$ 40.
7. Trava de 2 por segmento por zona, em código, para a suíte inteira; nenhum módulo compra exceção.
8. Sem raspagem do Google: Places API dentro dos termos, snapshots de 30 dias, só `place_id` fica.
9. Só avaliações reais: convite após atendimento real, com consentimento, sem incentivo, sem seleção.
10. Frescor honesto: Google com data de referência; dado próprio em até 1 hora; tempo real só onde existe (a partir do Chat).


<!-- ======================================================================
     ARQUIVO: radar-urbano/05-MAPA-DE-ENTREGAS.md
     ====================================================================== -->

# Radar Urbano · Mapa de Entregas

Onze entregas: dois objetos de entrada (uma vez) e nove recorrentes. R$ 499/mês (R$ 16,63/dia), mensal, cancelável, sem verba de mídia. Promessa: captura de intenção otimizada, lucrativa e eficiente. Nunca conversão, receita atribuída ou "novos clientes".

## 1. Regra do zero

1. **Zero reuniões**: o único tempo do dono são até 15 minutos do Dia 0 (roteiro real fecha em cerca de dez).
2. **Zero login obrigatório**: tudo chega pelo WhatsApp do dono, pelo número da casa; dashboard opcional; SAIR interrompe os envios, não o trabalho.
3. **Zero aprovação**: posts, fotos, horários, descrição, serviços, atributos e respostas são pré-autorizados no Dia 0; categoria principal, nome, endereço e ofertas exigem um Sim.
4. **Zero relatório longo**: nada passa de 60 s de áudio ou uma página; Google com data de referência, dados próprios de hora em hora.
5. **Zero surpresa**: toda ação entra no Diário de Bordo (append-only, com print) antes de qualquer resumo; o Guardião audita por amostragem.
6. **Zero cobrança de esforço**: nunca pede foto, texto, tabela ou senha; entra como Gerente do Perfil da Empresa e sai quando o dono quiser.

## 2. Tabela-mestre

| Nº | Entrega | Grupo | Quando | Por onde chega | Quem faz |
|---|---|---|---|---|---|
| 01 | Diagnóstico de Posição | Entrada | Dia 0, minutos depois do acesso | Card no WhatsApp; PDF no dashboard | Cartógrafo + Editor + Redator-chefe |
| 02 | Antes e Depois do Perfil | Entrada | Dia 7 (a partir de `created`) | Card lado a lado; arquivo no dashboard | Editor + Cartógrafo |
| 03 | Dashboard Radar | Vendas & Performance | A cada hora; Google com data de referência | Link fixo no WhatsApp, ícone no celular | Tesoureiro |
| 04 | Boletim de Segunda | Vendas & Performance | Segunda, 7h | Áudio ≤ 60 s + card | Redator-chefe |
| 05 | Mapa de Domínio | Vendas & Performance | Dia 1 (reduzido no Dia 0 e dia 7) | Imagem; interativo no dashboard | Cartógrafo |
| 06 | Diário de Bordo do Perfil | Vendas & Performance | Contínuo | Dashboard; linha no WhatsApp quando relevante | Editor |
| 07 | Motor de Reputação | Vendas & Performance | Respostas ≤ 2 h; boletim dia 1 | Respostas no Google; card; QR em PDF | Anfitrião |
| 08 | Extrato de Demanda | Controladoria & Eficiência | Dia 1 | PDF; série no dashboard | Tesoureiro |
| 09 | Horas Devolvidas | Controladoria & Eficiência | Dia 1 | Card | Tesoureiro |
| 10 | Voz do Cliente | Controladoria & Eficiência | Dia 1; alerta quando um tema dispara | Card | Anfitrião + Redator-chefe |
| 11 | Fechamento Executivo | Controladoria & Eficiência | Dia 1; trimestral | PDF; arquivo no dashboard | Redator-chefe |

Envios: Boletim 7h; dia 1 e dia 7 até as 8h; avisos e perguntas Sim/Não das 8h às 19h; reenvio após 2 h sem confirmação, sem duplicar.

## 3. As entregas

### 01 Diagnóstico de Posição

Assim que o dono adiciona o Radar Urbano como Gerente, a máquina mede 2–3 termos-chave em nove pontos e audita a completude do perfil. O card chega na mesma conversa.

- Contém: mapa reduzido (verde, cinza, vermelho); auditoria campo a campo; três frases (onde está, o que falta, o que a máquina faz primeiro); data e hora.
- Único toque do dono: adicionar o e-mail operacional como Gerente. Nunca senha. Perfil não verificado: passo a passo, o resto não espera.

### 02 Antes e Depois do Perfil

Perfil do Dia 0 e do dia 7 lado a lado, campo a campo (diff de `profile_audits`), com a segunda medição reduzida nos mesmos termos e pontos e as duas datas.

- Pendência do Dia 0, se houver, vem como uma única pergunta Sim/Não.
- O card diz que uma semana raramente mexe posição; o que mudou foi o perfil.

### 03 Dashboard Radar

Link fixo com token, que vira ícone no celular. Sem menu nem filtro: contatos, impressões e palavras-chave, posição, reputação, Diário com prints, custo por contato.

- Dois relógios ditos na tela: Google com data de referência, coleta diária 3h (D-3..D-1); dados próprios de hora em hora. Sem tempo real.
- Rodapé: ligações pelo perfil são toques em Ligar, não ligações atendidas.
- Senha opcional, criada pelo dono, que ninguém do Radar Urbano vê; link mágico entra sem senha.

### 04 Boletim de Segunda

Áudio de até 60 s com a voz da casa e card de uma tela, toda segunda às 7h, inclusive feriado. Cobre a semana fechada pelo Google (data de referência, em geral quinta ou sexta) e diz isso: contatos, avaliações, posição (sábado 3h), ações do Diário, o que vem.

- 6h: Redator-chefe confere cada número contra o banco e escreve no tom do Dia 0; TTS com `voice_id` fixo; 7h envio.
- Janela de 24 h fechada: modelo `boletim_segunda` (card + voz em MP4); aberta: PNG e OGG livres. Semana incompleta: o Boletim diz quantos dias cobre.

### 05 Mapa de Domínio

Posição por termo, ponto a ponto, em grade 3×3 (bairro) a 5×5 (região). Um mapa por termo e um resumo: pontos verdes de pontos medidos, contra o mês anterior. Só a posição do cliente; sem comparação nominal com concorrentes.

- Cores: verde = top 3; cinza = 4º a 10º; vermelho = fora do top 10 ou não encontrado no top 20.
- Rodapé de método: `places:searchText` com `locationBias` por ponto, proxy da lista local; validação mensal com 20 buscas manuais.
- Sem raspagem; da Places API só `place_id` fica além de 30 dias. A medição própria fica na série.
- Sábado 3h reduzido (termos-chave, 9 pontos); dia 1 2h completo. Vermelhos viram `editor.tasks`.

### 06 Diário de Bordo do Perfil

Registro append-only de toda ação no perfil (data, hora, agente, campo, antes, depois, print). Nada entra sem linha; nada some.

- Post semanal segunda 4h, com foto real do perfil ou enviada pelo dono; nunca gerar nem pedir foto. Fotos existentes avaliadas (nitidez, luz, atualidade) para capa e destaques.
- Descrição (limite 750 caracteres), serviços (lista, sem preço) e atributos escritos para os termos que trazem cliente; revistos por `editor.tasks` e na auditoria do dia 1.
- Feriados: checagem diária 5h; tabela própria de feriados nacionais e municipais por cidade; 72 h antes, horário especial e post de aviso, pela regra do dono; na dúvida, pergunta Sim/Não.
- Categorias com dois olhos; principal só com Sim. Nunca termos de busca no nome.
- Linha no WhatsApp só para ação relevante, em horário comercial.

### 07 Motor de Reputação

Polling a cada 30 min. Resposta humanizada e específica a toda avaliação em até 2 h (100% em 24 h); perguntas públicas em menos de 4 h. Boletim de Reputação no dia 1: nota, novas, respondidas, temas elogiados e de atenção.

- Balcão: link curto oficial "Receber mais avaliações" e QR em PDF, na segunda semana. Só avaliações reais: sem incentivo, sem seleção, sem convite ativo por mensagem.
- Notas 1 e 2 passam pelo Guardião em qualquer patamar, ainda dentro das 2 h.
- Sem dado do avaliador; texto não armazenado (hash, temas, sentimento). Política de conteúdo do Google verificada antes.
- Avaliação suspeita: o Guardião denuncia pelo canal oficial; a máquina não discute em público.

### 08 Extrato de Demanda

Uma página por mês: quatro linhas e a soma, custo por contato (R$ 499 ÷ contatos), contexto fora da soma (impressões, dez palavras-chave), série de seis meses. O dono coloca o valor dele por cima.

- Explicar uma vez: ligações pelo perfil são toques em Ligar, não ligações atendidas; mensagens pelo perfil só existem com o chat do perfil ligado.
- Data de referência na página; correção posterior do Google corrige a série e diz quando.

### 09 Horas Devolvidas

Linhas do Diário (nenhuma sem print) convertidas em tempo humano pela tabela abaixo, publicada no rodapé do card e fixa no mês. Tempo do dono = minutos das respostas Sim/Não.

| Ação | Tempo |
|---|---|
| Post criado e publicado | 20 min |
| Foto selecionada e publicada | 10 min |
| Resposta a avaliação | 6 min |
| Resposta a pergunta do perfil | 4 min |
| Ajuste de campo ou horário | 10 min |
| Medição de posição | 0,5 min por termo-ponto |
| Auditoria mensal do perfil | 60 min |
| Boletim de Segunda | 30 min |
| Extrato ou PDF | 45 min |
| Mapa de Domínio | 60 min |

Exemplo (clínica, um mês): 14h07 devolvidas, 2 min do dono. Frase de balcão: "catorze horas por R$ 499".

### 10 Voz do Cliente

Avaliações e perguntas públicas do mês classificadas por tema e sentimento: três elogios e três atritos mais recorrentes, com frequência e uma frase real sem nome.

- Atrito resolvível no perfil (horário, informação faltando, serviço não listado): corrigido e avisado no card. Atrito de operação: só mostrado.
- Alerta de uma linha quando o mesmo atrito aparece 3 vezes em 7 dias.

### 11 Fechamento Executivo

Uma página em PDF, último envio do dia 1: contatos contra o mês anterior, impressões, custo por contato, nota e avaliações, Mapa de Domínio em miniatura, horas devolvidas, o que a máquina fez e vai fazer, data de referência no rodapé.

- Trimestral, junto com o mensal: três meses lado a lado e a curva desde o Dia 0.
- Sem cópia automática a terceiros: o dono encaminha o PDF a quem quiser.

## 4. Calendário

| Período | O que acontece |
|---|---|
| Dia 0 | Antes, fora dos 15 min: `zone.check`, contrato, cartão. Min 0–5 cinco perguntas por áudio; 5–8 Gerente no perfil; 8–10 dashboard e Diagnóstico. O Sim final registra o opt-in com hora. |
| Semana 1 | Perfil auditado e corrigido, feriados na agenda. Dashboard no ar. Pendências de reputação respondidas. Sábado 3h: medição. Dia 7: Antes e Depois. |
| Semana 2 | Primeiro Boletim com semana fechada. Post em ritmo. QR em PDF. |
| Semana 3 | Série de posição com 4–5 pontos; vermelhos viram tarefas do Editor. Primeiro feriado 72 h antes, se houver. |
| Semana 4 | Dia 1, 2h–8h: medição completa, auditoria, extratos, cards, PDFs, envios. Chegam as seis entregas mensais. |
| Mês 2 | Termos novos; esforço movido para o vermelho. Segunda auditoria. |
| Mês 3 | Primeiro Fechamento Trimestral. Proposta de novos termos e raio (raio maior passa por `zone.check`). |
| Permanente | 30 min: avaliações e perguntas. Hora: dashboard. Diário 3h coleta, 5h feriados. Segunda 4h post, 7h Boletim. Sábado 3h medição. Dia 1: seis entregas. Domingo: nada chega. |

## 5. A máquina

Cinco agentes e um humano com painel. Gemini obrigatório para tudo que toca o Google; linguagem pode vir de outro modelo, atrás do `LLMGateway`.

| Nome | Missão |
|---|---|
| Cartógrafo | Mede posição por termo e ponto (Places API), desenha o Mapa de Domínio, diz ao Editor o que otimizar |
| Editor | Mantém o perfil vivo: post, fotos, descrição, horários, serviços, atributos, auditoria; categoria só com Guardião |
| Anfitrião | Responde avaliações e perguntas, classifica tema e sentimento, sinaliza suspeitas, gera QR e o Boletim de Reputação |
| Tesoureiro | Consolida em número: coleta do Performance API, dashboard, Extrato, Horas Devolvidas, custo por contato e por tenant; só SQL |
| Redator-chefe | Dado em 60 s de áudio e uma página: Diagnóstico, Boletim, Voz do Cliente, Fechamento; confere números antes |
| Guardião (humano) | Aprova em lote, audita por amostragem, trata exceções; dois olhos para categoria, nome, endereço e notas ≤ 2; denuncia avaliação falsa. Patamares: P0 tudo antes, P1 lote > 85% sem edição, P2 QA de 10% |

## 6. A conta na mesa

Contato = o que o Google conta a partir do perfil: ligações pelo perfil (toques em Ligar), pedidos de rota, cliques no site, mensagens pelo perfil. Impressões e palavras-chave são contexto, fora da soma. Custo por contato = R$ 499 ÷ contatos do mês. Números de exemplo:

| | Padaria (Seu Jorge) | Oficina (Marcão) | Clínica (Dra. Lívia) |
|---|---|---|---|
| Ligações pelo perfil | 118 | 96 | 58 |
| Pedidos de rota | 97 | 41 | 37 |
| Cliques no site | 31 | 22 | 44 |
| Mensagens pelo perfil | 14 | 9 | 21 |
| **Contatos no mês** | **260** | **168** | **160** |
| Impressões (Busca + Maps) | 9.400 | 6.100 | 5.300 |
| Nota · avaliações | 4,7 · 128 | 4,8 · 214 | 4,9 · 96 |
| Pontos verdes no termo principal | 7 de 9 ("padaria perto de mim") | 7 de 9 ("oficina mecânica") | 6 de 9 ("dentista perto de mim") |
| **Custo por contato** | **R$ 1,92** | **R$ 2,97** | **R$ 3,12** |

## 7. Trava territorial

- No máximo 2 empresas do mesmo segmento por zona. Segmento = categoria principal do perfil. Zona = bairro do Google Maps ou raio equivalente, escrita no contrato com cidade e segmento.
- Motivo: a busca local tem três posições na primeira tela; concorrentes na mesma malha degradam o resultado de ambos.
- `zone.check` antes da proposta e de novo na assinatura: livre (0 ou 1 de 2) ou lotada (2 de 2, fila).
- Conversa não reserva; proposta escrita reserva por 5 dias úteis; a vaga só se ocupa na assinatura (transação em `zones`). Fila por ordem de chegada; ninguém fura. Quem sai libera a vaga.
- Mudança de endereço, categoria principal ou raio roda a verificação. Com vaga: aditivo, vaga antiga liberada. Sem vaga: opera até o fim do ciclo pago e entra na fila da zona nova; o endereço muda mesmo assim. Zona redesenhada: quem está, fica.
- Cláusula de exclusividade limitada no contrato; o cliente pode perguntar quantos há na zona dele. Não muda a mensalidade.

## 8. Por que fecha

1. O valor chega antes da fatura: Diagnóstico no Dia 0, Antes e Depois no dia 7, conta completa no dia 1.
2. Toda entrega é tangível (áudio, card, mapa, extrato, PDF), com a data do dado impressa.
3. Tempo do dono é zero por arquitetura: nunca insumo, reunião, relatório ou senha; só perguntas Sim/Não.
4. A promessa é só o que se conta e se confere no Google: contatos e custo por contato, nunca conversão ou venda.
5. Cancelar custa mais do que ficar: perfil parado, avaliações sem resposta, mapa e extrato somem, e a vaga na zona abre para o vizinho.


<!-- ======================================================================
     ARQUIVO: radar-urbano/06-MAPA-DE-ACESSOS.md
     ====================================================================== -->

# Radar Urbano · Mapa de Acessos

## 1. Princípios

1. **Senha do cliente, nunca.** Acesso por convite e papel, dentro da conta dele; código de verificação é digitado por ele na tela do Google.
2. **O cliente é o dono.** Perfil, avaliações, fotos, posts e histórico ficam em nome dele; o Radar Urbano é operador convidado.
3. **Revogável em um toque.** O Gerente sai na mesma tela em que entrou; as mensagens param com SAIR; no encerramento a máquina se remove.
4. **Mínimo necessário.** Único acesso concedido: papel Gerente no Perfil da Empresa. Dashboard é conta criada para ele; cartão vai direto ao provedor.
5. **Pré-autorizado por escrito, com limite.** O que faz sem perguntar está no contrato; categoria principal, nome, endereço e ofertas exigem um Sim por botão no WhatsApp, registrado com hora; sem resposta, não faz.
6. **Tudo registrado.** Cada ação no Diário de Bordo, append-only, com antes, depois e print.

## 2. Sistemas A–D

| Sistema | Conta necessária | Papel concedido | Como concede | Senha | Revogação |
|---|---|---|---|---|---|
| **A · Perfil da Empresa no Google** | Conta Google do cliente, perfil verificado, ele como Proprietário. Perfil de terceiro: Solicitar acesso (3 dias). Não verificado: vídeo, telefone, e-mail ou carta | Gerente para o e-mail operacional (conta única, 2FA, só pelo conector via OAuth `business.manage`). Edita, publica, responde, lê desempenho. Não gerencia usuários, não transfere nem exclui. Categoria principal, nome e endereço: só com Sim e dois olhos | Maps > Seu perfil comercial > Configurações > Gerentes/Usuários > Adicionar > Gerente > Convidar (ou business.google.com > Usuários). A conta operacional aceita e localiza o perfil por nome e endereço | Nunca | Cliente remove o usuário na mesma tela. A máquina percebe na chamada seguinte, congela Editor e Anfitrião e avisa o Head de Operação |
| **B · WhatsApp do dono** | Nenhuma conta nova: o número do dono, informado no contrato e confirmado na quinta pergunta do Dia 0. Do lado do Radar Urbano, uma conta na WhatsApp Business Platform com o número da casa | Nenhum. Só recebe. Responde Sim, Não, SAIR ou texto livre (vai a uma pessoa) | Aceite marcado no contrato; abre a conversa pelo link da página (se não abrir em 1 h, o número da casa manda `pergunta_sim_nao`); o Sim ao fim das cinco perguntas é o opt-in, com hora | Nunca | SAIR interrompe na hora, com registro. Não cancela o contrato: entregas ficam no dashboard. Trocar número: quinta pergunta de novo |
| **C · Dashboard Radar** | Criada pelo Radar Urbano no Identity Platform, na ativação | Cliente: leitura de tudo o que é dele. Radar Urbano: nenhum papel na conta dele | Recebe o link fixo com token pelo WhatsApp no minuto 8 do Dia 0 | Nova e opcional, criada pelo cliente por link único (morre após uso), em hash; a operação não lê nem redefine. Sem senha, entra pelo link fixo (mágico) | Cliente pede link novo ou desativa. No encerramento vira arquivo entregue e a conta fecha |
| **D · Contrato, pagamento e nota fiscal** | Cartão na página do provedor; dados fiscais; número e aceite do número da casa marcados no contrato; assinatura digital | Cobrança recorrente de R$ 499/mês, cancelável, sem fidelidade abusiva. O Radar Urbano recebe só o estado da assinatura e os últimos dígitos | Link do contrato (só após o comercial confirmar a vaga na zona) e link do provedor. Cinco minutos, antes da conversa | Nunca | Cancelamento por mensagem ao número da casa ou pelo dashboard, sem multa; encerramento no mesmo dia |

Dados gerados: A, métricas com data de referência (atraso de 2–3 dias), diff com print, avaliações e perguntas só como hash e temas. B, número do dono (hash com sal), nome de tratamento, aceite, status de entrega (reenvio após 2 h). C, aberturas do link, senha em hash. D, assinatura, notas fiscais, contrato, zona e segmento.

Regras de uso: A, só API oficial; nunca termo de busca no nome, categoria principal sem humano ou foto gerada; `SUSPENDED`/`PENDING_VERIFICATION` congela edição e abre incidente. B, só modelos de utilidade (`boletim_segunda`, `entrega_radar`, `entrega_radar_pdf`, `pergunta_sim_nao`, `aviso_radar`), rodapé "Responda SAIR para parar", cerca de 25 mensagens/mês; Boletim segunda 7h; dia 1 e dia 7 até 8h; avisos e perguntas Sim/Não só das 8h às 19h; lembrete de pendência no máximo semanal.

## 3. Base legal (pauta para o advogado)

Pauta, não parecer. Nenhum cliente entra antes da revisão do jurídico externo.

1. **Mandato de operação.** Publicar, editar e responder em nome da empresa no Perfil da Empresa. Sem perguntar: posts com foto real, fotos existentes, descrição (750 caracteres), horários e feriados (72 h antes), serviços sem preço, atributos, respostas a avaliações e perguntas. Com Sim registrado: categoria principal, nome, endereço, ofertas. Nunca: prometer posição ou resultado, incentivo por avaliação, termo de busca no nome, imagem gerada. Sem mandato de atendimento, anúncio ou mensagem a clientes finais.
2. **LGPD.** Cliente controlador do que a máquina trata em nome dele; Radar Urbano operador, e controlador dos dados cadastrais do dono (nome e número, hash na base analítica). Avaliações e perguntas: só para responder e classificar, guardadas como hash e temas; nome do avaliador nunca em resposta ou card. Nenhum dado de cliente final. Suboperadores: Google Cloud e APIs do Google; Meta (só número da casa); provedor do cérebro de linguagem; provedor de pagamento. Hospedagem em São Paulo; Meta e linguagem podem tratar fora do Brasil: prever transferência internacional. Retenção: `actions_log` 5 anos; `llm_calls` 12 meses; dados do tenant contrato + 90 dias; Places API 30 dias (só `place_id` fica); áudio do Dia 0 apagado 7 dias após confirmação escrita. Pedidos de titular em 15 dias. Sigilo.
3. **Política de avaliações e conteúdo do Google.** Só avaliações reais; sem incentivo, sem seleção (link curto e QR à vista de todos), sem pedir nota. Respostas verdadeiras, sem dados do avaliador; notas 1 e 2 com dois olhos. Suspeita: Guardião denuncia pelo canal oficial; ninguém pede remoção de avaliação legítima.
4. **Marca, fotos e imagem.** Uso autorizado de marca, nome e fotos existentes e enviadas. Rosto só com termo de imagem; sem termo, fotos sem pessoas. Nenhuma imagem gerada por IA. Voz dos áudios é a voz sintética da casa, nunca imitação do dono. O publicado é do cliente.
5. **Preços, horários e informações.** O cliente responde pela veracidade de horários, serviços, atributos, endereço, telefone e do que disse no Dia 0; a máquina registra a origem de cada dado. Feriados: calendário nacional e municipal, regra do Dia 0, na dúvida pergunta 72 h antes. Sem preço publicado; pergunta sobre preço é respondida sem valor.
6. **Exclusividade limitada por zona.** Máximo de duas empresas do mesmo segmento (categoria principal) na mesma zona (bairro ou raio equivalente), escrita no contrato com cidade e segmento. Não é exclusividade de mercado nem promessa de posição; motivo técnico: mais de dois perfis na mesma malha degradam todos. Reserva, fila e mudança de zona conforme a seção 6; cancelamento sem multa se a zona nova estiver lotada.
7. **Limitação de responsabilidade.** Sem promessa de posição, conversão, receita ou clientes novos. Promete a operação medida e registrada e a captura de intenção otimizada, lucrativa e eficiente, demonstrada por contagens do Google com data de referência (ligações pelo perfil = toques no botão Ligar). O que o Google muda ou suspende está fora do controle; o Diário prova a diligência. Custo por contato = mensalidade ÷ contatos.
8. **Reversibilidade.** Os passos da seção 7, com prazos: link do histórico por 30 dias; exclusão em contrato + 90 dias, salvo nota fiscal, contrato e Diário como prova. Nada sai do perfil. Quem volta passa pela verificação de zona de novo.

## 4. Mapa por entrega

A Perfil da Empresa · B WhatsApp do dono · C Dashboard. D sustenta todas. Senha: sempre nunca (em 03, senha nova criada pelo cliente).

| Nº | Entrega | Sist. | Acesso necessário | Ação do cliente | Dados que informa |
|---|---|---|---|---|---|
| 01 | Diagnóstico de Posição | A B C | Gerente para auditoria de completude; medição por Places API sem conta do cliente; número; dashboard | Cinco perguntas; conceder Gerente. Sem Gerente, sai com medição pública e auditoria do visível | O que vende e como procuram; bairros ou raio; nome e número |
| 02 | Antes e Depois | A B C | Gerente para o diff Dia 0 → 7; segunda medição; número; dashboard | Nenhuma; dia 7 desde `created`, mesmo com pendência | Nenhum |
| 03 | Dashboard Radar | A B C | Performance API com data de referência; conta do dashboard; número | Abrir o link fixo; senha opcional | Número |
| 04 | Boletim de Segunda | A B C | Desempenho da semana fechada; avaliações; medição de sábado; número; dashboard | Aceite no Dia 0 | Número; nome; jeito da casa de falar |
| 05 | Mapa de Domínio | A B C | Nenhum acesso à conta para medir (Places API, grade 3×3 a 5×5); Gerente só para ler o `place_id`; número; dashboard | Confirmar raio e termos sugeridos | Raio; termos |
| 06 | Diário de Bordo do Perfil | A B C | Gerente: campos, descrição, horários, serviços, atributos, posts, fotos; categoria só com humano. Número para linha curta e Sim/Não; dashboard | Conceder Gerente; foto real opcional; responder Sim/Não | Jeito de falar; o que nunca publicar; horários e regra de feriado; serviços sem preço; cidade |
| 07 | Motor de Reputação | A B | Gerente: ler e responder avaliações e perguntas; link curto oficial de avaliação. Número para Boletim de Reputação e PDF do QR | Conceder Gerente; QR no balcão | Frases proibidas; assinatura das respostas; onde fica o QR |
| 08 | Extrato de Demanda | A B C | Performance API (ligações pelo perfil, rotas, cliques no site, mensagens somam; impressões e palavras-chave são contexto); número; dashboard | Nenhuma | Nenhum |
| 09 | Horas Devolvidas | B C | Nenhum acesso à conta: Diário + tabela de equivalência; número; dashboard | Nenhuma | Nenhum |
| 10 | Voz do Cliente | A B C | Leitura de avaliações e perguntas; número; dashboard | Nenhuma | Nenhum |
| 11 | Fechamento Executivo | A B C | Todas as leituras acima; número; dashboard | Nenhuma; encaminha o PDF a quem quiser | Nenhum |

## 5. Roteiro do Dia 0

Teto de 15 minutos cronometrados; o roteiro real fecha em cerca de dez.

| Momento | O que acontece | Toque do cliente | Estado |
|---|---|---|---|
| Antes | Comercial roda `zone.check`. Só com vaga: contrato por link (número, aceite, assinatura) e cartão no provedor. A página termina no link que abre a conversa com o número da casa | Assina; cartão; primeira mensagem | `created` → `billing_active` |
| 0–5 min | Cinco perguntas por áudio: o que vende e como procuram; bairros ou raio; jeito de falar; o que pode fazer sem perguntar; número e nome. Gemini transcreve; confirmação por escrito | Áudios; Sim (opt-in com hora) | `profiled` |
| 5–8 min | Adiciona o e-mail operacional como Gerente, passo a passo na tela. Não verificado: recebe o roteiro de verificação; o resto não espera | Um toque | `gbp_linked` ou `gbp_pending_verification` |
| 8–10 min | Link fixo do dashboard; senha opcional; Diagnóstico de Posição na mesma conversa. Última mensagem: "A partir de agora você só recebe. Segunda, 7h, o primeiro Boletim. Dia 7, o Antes e Depois." | Abre o link | `live` |
| 10–15 min (folga) | Só para quem trava no perfil: não acha o menu; não verificado (vídeo: fachada, placa, interior); perfil de terceiro (Solicitar acesso, 3 dias); inexistente (criar e verificar). Nada segura Diagnóstico nem dashboard. Passou de 15: comercial encerra; lembrete semanal até resolver | Conforme o caso | mantém |
| Encerramento | Seção 7 | Nenhum | encerrado |

## 6. A zona

- **Definições:** segmento = categoria principal do perfil (padaria e pizzaria são segmentos diferentes); zona = bairro do Google Maps ou raio equivalente, no contrato com cidade e segmento. Limite 2 por segmento por zona (`MAX_TENANTS_PER_ZONE_SEGMENT=2`, tabela `zones`).
- **Verificação antes da venda:** comercial roda `zone.check` com segmento e zona (planilha na versão de bicicleta): 0/2 ou 1/2 livre, 2/2 lotada. Livre: contrato com zona e segmento escritos. Lotada: dito na primeira conversa, antes de qualquer link; lista de espera sem cobrança e sem prazo. Cada unidade é um tenant e uma vaga.
- **Reserva:** conversa não reserva. Proposta escrita reserva por 5 dias úteis. A vaga se ocupa na assinatura (transação em `zones`; `zone.changed` avisa). Contador acima de dois: tenant não nasce, Head de Operação decide.
- **Fila:** ordem de chegada, sempre; ninguém fura, nem cliente antigo. Vaga liberada vai ao primeiro da lista; comercial confirma interesse antes do contrato.
- **Mudança de endereço:** nova verificação antes. Com vaga: aditivo, vaga antiga liberada. Sem vaga: operação até o fim do ciclo pago; lista de espera da zona nova; vaga antiga libera no dia da mudança confirmada; o endereço no perfil muda mesmo assim (Guardião aprova); cancelamento sem multa.
- **Mudança de categoria principal:** Sim do dono e dois olhos; Guardião roda `zone.check` no segmento novo antes. Sem vaga, regra do endereço.
- **Redesenho de zona:** quem está fica; aviso escrito aos clientes da zona.
- **Liberação:** no offboarding, no mesmo dia, pela máquina.

## 7. Encerramento (offboarding)

1. Cancelamento registrado; provedor interrompe a cobrança; sem multa.
2. A máquina remove o e-mail operacional do papel Gerente.
3. Fim dos envios do número da casa, com aviso final de uma linha.
4. Histórico exportado (Diário com prints, extratos, Fechamentos, cards, Mapas, fotos, posts, respostas); link por 30 dias.
5. Dashboard encerrado após a exportação.
6. Exclusão dos dados em contrato + 90 dias, salvo nota fiscal, contrato e `actions_log` (5 anos).
7. Vaga da zona liberada; comercial avisa o primeiro da lista.
8. Nada sai do perfil. Retorno: novos acessos e nova verificação de zona.


<!-- ======================================================================
     ARQUIVO: radar-urbano/07-MAPA-MUNDI.md
     ====================================================================== -->

# Radar Urbano · 07-MAPA-MUNDI

Manual de montagem da máquina. Régua: BRIEF (seções 6–9 e 15). Nomes de tabelas, tópicos, ferramentas e variáveis são os mesmos no código, no Diário e aqui.

## 1. Arquitetura

Camadas:

1. Interfaces: Perfil da Empresa no Google (Busca e Maps), Places API (New), WhatsApp do dono (número da casa), Dashboard Radar. Nenhuma outra.
2. Conectores: GBP, Places, WA, TTS; ao lado, Render & Delivery (cards, mapa, PDFs, QR, dashboard, envio com status). Conector executa, registra custo, devolve JSON; nunca decide.
3. Agentes, orquestrador e Guardião: Cartógrafo, Editor, Anfitrião, Tesoureiro, Redator-chefe. Cloud Scheduler → Pub/Sub → Cloud Run Jobs; Cloud Tasks por tenant. Guardião: humano com painel.
4. Cérebros: Gemini na Vertex AI (obrigatório para dado, medição, áudio, foto e decisão que toca o Google); linguagem intercambiável atrás do `LLMGateway`; Cloud TTS. Nenhum agente chama modelo direto.
5. Memória e prova: Firestore (estado por tenant), BigQuery (métricas, medições, Diário, custo, zonas), Cloud Storage (fotos, prints, PDFs, áudios), Secret Manager (nunca senha de cliente).

Regras:

1. Camadas estritas: cada camada fala só com a de baixo; trocar modelo, voz ou template não toca agente; trocar endpoint toca só o conector.
2. Gemini é o cérebro de dados e de Google: extração, aferição, classificação e toda decisão sobre API ou superfície do Google, com saída estruturada.
3. Um cliente é um tenant com zona: todo dado carrega `tenant_id`; o tenant só nasce se `zone.check` confirmar vaga (máximo 2 por segmento por zona, em transação).
4. Tudo é job idempotente: chave `tenant_id + agente + entrega + período`, verificada antes da ação externa.
5. Humano aprova, IA executa: P0 tudo antes; P1 lote (meta > 85% sem edição); P2 direto com QA de 10%; categoria principal, nome, endereço e notas 1 e 2 sempre com dois olhos.
6. Diário de Bordo é a verdade: toda ação externa grava linha imutável em `actions_log` com print; sem linha, não aconteceu.
7. Custo por cliente é métrica de primeira classe: alerta em R$ 25/cliente/mês. Sem tempo real: dados do Google com data de referência; a máquina não fala com cliente final.

## 2. Cérebros

| Função | Modelo | Como |
|---|---|---|
| Extração e normalização (perfil, métricas, avaliações, perguntas, palavras-chave) | Gemini Flash (volume) · Pro (análise mensal) | `generateContent` + `responseSchema` |
| Aferição de posição e leitura de superfícies Google | Gemini + Grounding com Google Maps | Medição é `places.search_text`; o Gemini interpreta e propõe termos |
| Decisões que tocam API do Google | Gemini Pro | Function calling com ferramentas do GBP |
| Transcrição dos áudios do Dia 0 | Gemini multimodal | OGG + `responseSchema`: termos, raio, tom, limites, nome |
| Classificar avaliações e perguntas | Gemini Flash | Polling 30 min; lote noturno; cache de contexto |
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

Regras: (1) saída estruturada sempre; sem JSON válido, retry com temperatura menor e, na terceira falha, exceção no Guardião; (2) prompts versionados no repositório, versão em `actions_log` e `llm_calls`; (3) avaliação cega mensal: 100 amostras por agente, dois humanos, sem saber o modelo; (4) cache de contexto renovado a cada 24 h; (5) nenhum dado pessoal no prompt sem necessidade; o modelo nunca vê número da casa nem token.

## 3. Conectores

Termos comuns ao Google: nome real sem termo de busca; categoria descreve o negócio; horários e fotos reais; avaliações sem incentivo, seleção ou dado do avaliador; suspeita denunciada pelo fluxo oficial; sem raspagem.

### GBP

| | |
|---|---|
| APIs | Business Information v1: `accounts.locations.list`, `locations.get`, `locations.patch` (`updateMask`, `validateOnly`), atributos, `categories.list`; campos `regularHours`, `specialHours`, `profile.description`, `serviceItems`, `metadata.newReviewUri`, `metadata.mapsUri` · Performance v1: `fetchMultiDailyMetricsTimeSeries` (`CALL_CLICKS`, `BUSINESS_DIRECTION_REQUESTS`, `WEBSITE_CLICKS`, `BUSINESS_CONVERSATIONS`, `BUSINESS_IMPRESSIONS_{DESKTOP,MOBILE}_{SEARCH,MAPS}`), `searchkeywords/impressions/monthly` · v4: `reviews.list/reply`, `localPosts.create`, `media.create` · Q&A: `questions.list`, `answers.upsert` · `locations.admins.list` · `getVoiceOfMerchantState` |
| Acesso | Formulário oficial das Business Profile APIs (1–2 semanas; dia 1 da semana 1). OAuth 2.0 com a conta operacional (2FA), Gerente em cada perfil, escopo `business.manage`; `GBP_OPERATOR_REFRESH_TOKEN`; `tenant-{id}-gbp-oauth` aponta por padrão para o token da casa |
| Cotas | Baixas para edição; pedir aumento com o acesso. Desempenho em lote 03h (D-3..D-1); edições por Cloud Tasks, uma por tenant, retry em 429/5xx; polling 30 min, `pageSize` 50. Palavras-chave abaixo do limiar chegam como faixa |
| Armadilhas | Categoria principal só com humano; `patch` sem `updateMask` apaga o resto (conector recusa); `SUSPENDED`/`PENDING_VERIFICATION` abre incidente; `hasGoogleUpdated` = revisar antes de sobrescrever; nota chega como enum `ONE..FIVE`; foto e post exigem URL assinada curta; v4 pode migrar; descrição ≤ 750 caracteres |

### Places

| | |
|---|---|
| Endpoints | `places:searchText` com `textQuery`, `locationBias` circular no ponto (raio = passo), `rankPreference` padrão, `languageCode=pt-BR`, `regionCode=BR`, `pageSize=20`, máscara `places.id` · `places/{place_id}` só no Dia 0 |
| Acesso e cotas | Chave restrita à API e ao IP de saída (Cloud NAT); `PLACES_API_KEY`; nunca no navegador. Uma chamada por termo por ponto; grade 3×3 a 5×5; ≤ 25 termos; ≈ 240 chamadas/tenant/mês; teto em `limites_json`; R$ 3–8 |
| Termos | Nada além de 30 dias exceto `place_id`: guardamos só `place_id` do cliente, data, termo, ponto, lat/lng, posição |
| Método | Centro no endereço; passo = raio (3×3) ou raio ÷ 2 (5×5); posição = índice do `place_id` (1–20) ou "não encontrado". Verde top 3, cinza 4º–10º, vermelho fora do top 10. Mesmo horário sempre. Validação mensal: 20 buscas manuais, ≥ 85% no top 3, em `qa_samples` |
| Armadilhas | `locationBias` é viés, não cerca; `rankPreference=DISTANCE` mede outra coisa; sem `languageCode`/`regionCode` a lista muda; não paginar além de 20; `place_id` pode mudar em fusão (reconfirmar por `metadata.mapsUri`); alerta de orçamento |

### WA (número da casa)

| | |
|---|---|
| Endpoints | `POST /{phone_number_id}/messages` (`template`, `audio`, `image`, `document`, `interactive`) · `POST /{phone_number_id}/media` · `GET /{media_id}` · webhooks `messages` e `statuses` · `/{waba_id}/message_templates` · `/{waba_id}/phone_numbers` (`quality_rating`) |
| Acesso | Portfólio do Radar Urbano verificado (dia 1); app com WhatsApp; número dedicado "Radar Urbano"; usuário de sistema → `META_SYSTEM_USER_TOKEN`; `META_APP_ID/SECRET`; `WA_WEBHOOK_VERIFY_TOKEN`; `DELIVERY_SENDER_PHONE_ID`. Sem Tech Provider, sem Embedded Signup, sem conta do cliente |
| Modelos (Utilidade; rodapé "Responda SAIR para parar") | `boletim_segunda`: cabeçalho de vídeo (card + voz em MP4), números e data de referência, botão do dashboard; só com a janela de 24 h fechada · `entrega_radar`: cabeçalho de imagem · `entrega_radar_pdf`: cabeçalho de documento (nome lógico `entrega_radar` no código) · `pergunta_sim_nao`: botões · `aviso_radar`: {{1}} nome, {{2}} linha |
| Janela e horários | Livre só na janela de 24 h aberta pelo dono (botão conta). Dia 0: o dono abre pelo link da página do contrato; sem mensagem em 1 h, sai `pergunta_sim_nao` ("Podemos começar?"). Segunda: janela aberta → PNG + OGG livres; fechada → `boletim_segunda`. ≈ 25 mensagens/dono/mês. Boletim 7h; dia 1 e Dia 7 até 8h; `aviso_radar` e perguntas 8h–19h. R$ 1–2 |
| Armadilhas | Modelo com cara de marketing = rejeição; `quality_rating` cai com bloqueios (SAIR honrado na hora em `wa_optout`); nunca celular de alguém; `audio/ogg` Opus, PNG ≤ 5 MB, MP4 ≤ 16 MB; número do dono só como hash; texto livre vai a humano; token rotacionado a cada 90 dias |

### TTS + Render & Delivery

| | |
|---|---|
| TTS | Chirp 3 HD pt-BR, `TTS_VOICE_ID` fixo; `OGG_OPUS` 48 kHz; ≤ 60 s (corte por ≤ 150 palavras; conector mede e recusa); números por extenso; card + OGG viram MP4 para o modelo |
| Render | HTML → PNG/PDF (Chrome headless), templates versionados; Mapa em SVG de `rank_measurements`; PDFs de uma página em `radar-{amb}-artefatos/{tenant_id}/{entrega}/{periodo}.pdf`, URL assinada 30 dias, cópia no dashboard; QR: `gbp.get_review_link` → `render.qr` → PDF de balcão e comanda, sem prêmio; todo card traz cliente, período, data de referência |
| Dashboard | Next.js no Cloud Run; link fixo `DASHBOARD_BASE_URL/t/{token}`; senha opcional criada pelo cliente (Identity Platform; link mágico = sem senha; link único = criar/redefinir); visões de hora em hora; números, Mapa, Diário com prints, Voz do Cliente, Reputação, arquivos, Horas, custo por contato; abertura grava `lido_em` |
| Delivery | Recebe (tenant, entrega, período, artefatos); decide janela × modelo; sobe mídia; envia; grava `enviado_em`, `entregue_em`, `lido_em`; chave `tenant + entrega + período`; reenvio único após 2 h, depois incidente; respeita `wa_optout` e horários; fila `deliveries.send` |

## 4. Fundação

| Peça | Escolha |
|---|---|
| Projetos e APIs | `radar-hml`, `radar-prd`, `southamerica-east1`. Vertex AI, Places API (New), Business Profile APIs, Cloud TTS, Cloud Run, Cloud Build, BigQuery, Firestore, Secret Manager, Scheduler, Pub/Sub, Identity Toolkit. Sem Google Ads API |
| Execução | Cloud Run (webhooks, dashboard, painel, render); Cloud Run Jobs (um container por agente); ADK em Python; opção Agent Engine. Scheduler → Pub/Sub → Jobs; Cloud Tasks por tenant |
| Dados | Firestore (documento por tenant); BigQuery particionado por data, clusterizado por `tenant_id`; Cloud Storage (bucket por ambiente, prefixo por tenant); tabela de feriados nacionais e municipais lida por `calendar.holidays` |
| Segredos, identidade, observabilidade | Secret Manager (um por uso); Identity Platform (cliente; painel com 2FA); Logging, Error Reporting, Monitoring; `llm_calls` |
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

Contatos = `call_clicks + directions + website_clicks + conversations`; impressões e palavras-chave são contexto. `posicao` nula = não encontrado. `profile_audits` com `origem='diagnostico'` é o "antes" do Dia 7.

Tenancy: (1) documento `tenants/{id}` com configuração, `limites_json`, tom, termos, raio, segmento, zona, estado, consentimento, subcoleções `approvals` e `queue`; nasce só após `zone.check`; (2) segredos por tenant (`tenant-{id}-gbp-oauth`), segredos da casa lidos só pelo conector dono, rotação 90 dias; (3) contas de serviço mínimas (só WA lê token da Meta; só Delivery lê o número claro; ninguém tem `UPDATE`/`DELETE` em `actions_log`); (4) `dono_wa_hash` com sal por tenant; textos de terceiros só como hash, temas e sentimento.

Estados: `zone.check` (antes de existir) → `created` → `billing_active` → `profiled` → `gbp_linked` ou `gbp_pending_verification` → `live`.

## 5. Agentes

Todos em ADK; nenhum chama API direto; nenhum fala com o dono senão via `delivery.send`; todos usam `diario.log` e `guardiao.submit`. Sentinela de calendário é rotina do Editor. Convite de avaliação não existe. Entradas de cada agente: as tabelas da seção 4 que ele lê, mais `tom_json`, `limites_json` e fatos da casa do Dia 0.

### Cartógrafo

| | |
|---|---|
| Gatilho | Dia 0 após `gbp_linked`, Dia 7 e sábado 03h (reduzida: 3×3, até 5 termos); dia 1 02h (completa) |
| Ferramentas / cérebro | `places.search_text` · `gbp.get_keywords` · `gbp.get_location` · `render.map_svg` · `render.card` · `cost.per_tenant`. Gemini Pro + Grounding com Google Maps; Flash normaliza; sem linguagem |
| Saídas / guardrails | `rank_measurements`; Mapa; JSON do Diagnóstico; `editor.tasks`; categoria ao Guardião. ≤ 25 termos; grade ≤ 5×5; teto em `limites_json`; só o `place_id` do cliente; nunca cita outro perfil; mede mesmo com perfil pendente |
| Métricas / teste | Custo de medição; cobertura da grade; variação de verdes. Teste: ≥ 85% no top 3 vs 20 buscas manuais; reduzida < 2 min; nenhum `place_id` de terceiros |

```
Cartógrafo. Verde = top 3, cinza = 4–10, vermelho = fora do top 10 ou não encontrado. Sem termos sem impressões, sem citar outro perfil, sem termos no nome, sem promessa de posição.
JSON: {territorio:[{termo,pontos_verde,pontos_cinza,pontos_vermelho,variacao_mes}], diagnostico:{termos_no_top3,termos_fora,maior_lacuna}, oportunidades:[{termo,motivo,acao_sugerida}], auditoria_perfil:[{campo,atual,sugerido,impacto}], nap_consistente:bool}
```

### Editor

| | |
|---|---|
| Gatilho | Segunda 04h (post); diário 05h (feriados 72 h antes); `editor.tasks`; Dia 0 (auditoria); Dia 7 (diff); dia 1 (auditoria mensal); `approvals.decided` |
| Ferramentas / cérebro | `gbp.get_location` · `gbp.create_post` · `gbp.upload_media` · `gbp.patch_location` · `gbp.update_hours` · `gbp.update_services` · `calendar.holidays` · `vision.assess_photo` · `render.card` · `delivery.send`. Linguagem (texto); Gemini (fotos e qualquer campo do perfil) |
| Saídas / guardrails | Guardião (P0/P1) ou publicação (P2), com print; `posts`; `profile_audits`; horários de feriado; auditoria de completude; diff do Dia 7; `aviso_radar`. Só fotos com `assess_photo.ok`; categoria principal, nome, endereço via Guardião; ≤ 1 post/dia; descrição ≤ 750 caracteres; serviços sem preço; feriado sem padrão vira `pergunta_sim_nao` (sem resposta até 24 h antes, horário normal fica); nada publica em perfil suspenso ou pendente |
| Métricas / teste | Aprovação sem edição (> 85% no P1); feriados com ≥ 72 h (100%); completude. Teste: uma semana gera 1 post aprovado; feriado de teste vira horário + post 72 h antes com aviso; 100% com print; nenhum campo sensível sem aprovação |

```
Editor da {casa}, tom {tom}. Nunca prometa resultado, posição ou desconto; nunca termos de busca no nome; só {fatos_da_casa} e {limites}. Post ≤ 300 caracteres com foto entre as disponíveis (nunca gerar). Feriado a 72 h: horário pelo padrão da casa e post ≤ 200 caracteres.
JSON: {post, foto_uri, justificativa, horario_feriado, publicar_em, requer_guardiao:bool}
```

### Anfitrião

| | |
|---|---|
| Gatilho | Polling 30 min (→ `gbp.review.new`, `gbp.question.new`); lote noturno; dia 1 (Reputação, Voz do Cliente); primeira semana (QR); `approvals.decided` |
| Ferramentas / cérebro | `gbp.list_reviews` · `gbp.reply_review` · `gbp.list_questions` · `gbp.answer_question` · `gbp.get_review_link` · `render.qr` · `render.pdf` · `render.card` · `classify.review`. Gemini Flash (classificar); linguagem (responder); Gemini (violação de política) |
| Saídas / guardrails | Respostas no Google; `reviews`, `questions`; Boletim de Reputação; classificação do mês; sinal de suspeita; QR em PDF. Nunca mensagem a cliente final; link oficial sem encurtador próprio; responde todas; notas 1 e 2 via Guardião em qualquer patamar; nunca dado do avaliador, compensação ou pedido de nota; texto só como hash; dúvida = `exige_humano`; chave por `review_id` |
| Métricas / teste | Mediana < 2 h e 100% em 24 h; perguntas < 4 h; edição pelo Guardião; sinalizadas/mês. Teste: avaliação de teste respondida em < 2 h; "vocês têm estacionamento?" em < 4 h com dado do perfil; QR abre a tela oficial; nenhuma mensagem a outro número |

```
Responde avaliações e perguntas públicas em nome da {casa}. Sem chavão; ao ponto; nunca compensação, dado do avaliador, discussão ou pedido de nota. Nota ≤ 3: desculpa, explicação, convite a falar com {responsavel} pelo {canal}. Pergunta: só perfil ou {fatos_da_casa}; sem certeza, exige_humano. ≤ 400 caracteres.
JSON: {resposta, tom_detectado, temas[], sentimento, suspeita_de_violacao:bool, exige_humano:bool}
```

### Tesoureiro

| | |
|---|---|
| Gatilho | Hourly (visões); diário 03h (coleta D-3..D-1); dia 1 05h (Extrato, Horas, custo, JSON do mês); segunda 06h (JSON da semana); `cost.alert` |
| Ferramentas / cérebro | `gbp.get_daily_metrics` · `gbp.get_keywords` · `render.pdf` · `render.card` · `cost.per_tenant`. Gemini Flash (normalizar); Pro só para três frases; números só de SQL |
| Saídas / guardrails | Visões do dashboard; `metrics_daily`; Extrato (PDF); Horas Devolvidas (card); custo por tenant e alerta; JSONs para o Redator-chefe. Nenhum número de modelo; reconciliação < 2%; sempre `data_referencia`; contato = 4 métricas; custo por contato = R$ 499 ÷ contatos; nenhum campo de conversão, receita ou "novos clientes"; coleta por (tenant, data) substitui, nunca soma |
| Métricas / teste | Frescor (próprio < 1 h; Google ≤ D-3); reconciliação; custo vs R$ 25. Teste: extrato sintético bate 100%; padaria (118 + 97 + 31 + 14) = 260 contatos e R$ 1,92; nenhuma visão sem `data_referencia` |

```
Três frases sobre este extrato, sem número fora do JSON, sem conversão, receita ou "novos clientes". Toques em Ligar = "ligações pelo perfil". Destaque a maior variação e o custo por contato. Diga até que data vão os dados.
```

### Redator-chefe

| | |
|---|---|
| Gatilho | Dia 0 (três frases); segunda 06h (Boletim; envio 07h); dia 1 06h (Voz do Cliente, Fechamento); trimestral; pendência há 72 h (≤ 1 lembrete/semana) |
| Ferramentas / cérebro | `tts.synthesize` · `render.card` · `render.pdf` · `delivery.send`. Linguagem; Gemini (verificação cruzada); Cloud TTS |
| Saídas / guardrails | OGG ≤ 60 s + card; PDFs (Diagnóstico, Fechamento mensal e trimestral); card Voz do Cliente; `aviso_radar` de pendência. Número fora dos dados bloqueia; ≤ 60 s; Boletim só 7h–8h; lembrete nunca após SAIR; nunca "novos clientes", conversão, receita, ROI, outro perfil; nenhum texto sem `prompt_versao` |
| Métricas / teste | Leitura/escuta (`read`); correções manuais; bloqueios da verificação; pendências resolvidas em 7 dias. Teste: Boletim sintético passa na verificação com áudio ≤ 60 s; Diagnóstico em três frases só com números da medição; número plantado bloqueia |

```
Boletim para {nome}, ≤ 150 palavras, falado, começa com "Bom dia, {nome}"; primeira frase diz até que dia vão os dados ({data_referencia}). O que mudou; contatos por tipo; avaliações; posição nos termos-chave; o que a máquina fez; o que vem. Só números do JSON. Termine com uma ação da semana.
Diagnóstico: três frases: onde a casa está; a maior lacuna do perfil; o que a máquina faz primeiro. Sem promessa de posição.
```

### Guardião (humano com painel)

| | |
|---|---|
| Gatilho | Fila contínua; SLA 4 h úteis em P0/P1; amostragem diária de 10% no P2; texto livre do dono (`wa.inbound`); suspeita de avaliação; `cost.alert`; estado do perfil |
| Ferramentas / cérebro | Painel (Cloud Run + Identity Platform, 2FA): aprovar, editar, rejeitar em lote; incidente; denúncia pelo fluxo do Google; `qa_samples`; resposta humana ao dono. Sem cérebro; Gemini Flash só ordena a fila |
| Saídas / guardrails | `approvals.decided`; edições devolvidas com motivo; feedback para a avaliação cega; incidentes; denúncias; `qa_samples`. ≤ 60 itens/hora por operador; categoria, nome, endereço e notas 1 e 2 com dois olhos em qualquer patamar; sem senha de cliente em tela; dono por nome e hash |
| Métricas / teste | Itens/hora; taxa de edição; tempo de fila; clientes por operador (30 → 80 → 150). Teste: 100 itens sintéticos em < 90 min por um operador; categoria só com duas aprovações; texto livre na fila em < 1 min |

```
Ordene por risco (categoria, nome, endereço e notas ≤ 2 primeiro; depois prazo), agrupe parecidos do mesmo tenant. JSON: {ordem:[item_id], grupos:[[item_id]]}. Não altere nenhum item.
```

## 6. Receitas

Chave em todo job: `tenant_id + agente + entrega + período`. Toda entrega passa pelo Delivery. Todo dado do Google com data de referência.

### 01 Diagnóstico de Posição

1. `gbp_linked` (ou pendente com `place_id` casado) → `cartografo.measure(modo='reduzida')`; em paralelo `editor.audit_profile` → `profile_audits` com `origem='diagnostico'`.
2. `redator.diagnostico` + `crosscheck`; `render.card` e `render.pdf`; `delivery.send` na mesma conversa (janela aberta); chave `tenant + diagnostico + dia0`. Lacunas e termos vermelhos → `editor.tasks`.

Pronto: card e PDF em ≤ 2 min após `gbp_linked`; três frases sem número fora da medição; `profile_audits` guarda o "antes".

### 02 Antes e Depois do Perfil

1. Scheduler diário 06h → `onboarding.day7` para `created` + 7, com ou sem pendências.
2. `editor.profile_diff` (`profile_audits` do Dia 0 vs hoje) + medição reduzida nos mesmos termos e pontos; `render.card` lado a lado; `delivery.send` até 8h; pendência aberta termina o card como uma `pergunta_sim_nao`. Chave `tenant + onboarding + day7`.

Pronto: sai no Dia 7 até 8h; toda diferença existe em `profile_audits`, `actions_log` ou `rank_measurements`.

### 03 Dashboard Radar

1. Hourly → `tesoureiro.refresh_views`. Diário 03h → `tesoureiro.collect_gbp` D-3..D-1 → `metrics_daily` (impressões = desktop + mobile); `data_referencia` = último dia publicado; chave (tenant, data). Dia 1 → `keywords_monthly`.
2. Seis números com setas vs 7 dias anteriores; linha fixa: "Dados do Google até {data_referencia}. O Google publica com 2 a 3 dias de atraso. 'Ligações pelo perfil' são toques no botão Ligar contados pelo Google, não ligações atendidas." Link fixo com token; senha opcional; abertura grava `lido_em`.

Pronto: abre em < 2 s; seis números com data de referência; sem campo de conversão; padaria = 260 contatos e R$ 1,92.

### 04 Boletim de Segunda

1. Sábado 03h: medição reduzida. Segunda 06h: `tesoureiro.week_summary` (4 métricas até a `data_referencia`, tipicamente quinta ou sexta; avaliações; posição; ações; o que vem); `redator.boletim` ≤ 150 palavras + `crosscheck`; `tts.synthesize` → OGG ≤ 60 s; `render.card`.
2. 07h: `delivery.send`: janela aberta → livres; fechada → `boletim_segunda`. Chave `tenant + boletim + semana ISO`; janela 7h–8h perdida → incidente + `aviso_radar`.

Pronto: áudio ≤ 60 s às 7h ± 5 min; nenhum número fora do JSON; padaria = 31 ligações pelo perfil, 22 rotas, 8 cliques, 3 avaliações respondidas, 1º em 7 de 9 pontos, 1 post, feriado ajustado.

### 05 Mapa de Domínio

1. Dia 1 02h: `cartografo.measure(modo='completa')`; `gemini.analyze_territory` (Pro): cores, variação mensal, oportunidades só com termos que têm impressões.
2. `render.map_svg` com legenda e rodapé "Busca por texto na Places API como proxy da lista local do Maps; validação mensal com 20 buscas manuais"; envio até 8h; reduzido no Dia 0 e Dia 7. Termos vermelhos → `editor.tasks`; categoria → Guardião; validação em `qa_samples` (< 85% = incidente); chamadas = termos × pontos, teto em `limites_json`.

Pronto: legenda, rodapé, ≥ 85%; nenhum dado de outro perfil; padaria = 7 de 9 verdes em "padaria perto de mim".

### 06 Diário de Bordo do Perfil

1. Segunda 04h: `editor.weekly_post` (foto real via `vision.assess_photo`, ≤ 300 caracteres); chave `tenant + post + semana ISO`. Diário 05h: `editor.hours_check` com `calendar.holidays(cidade, hoje, hoje + 10)`; a 72 h → `gbp.update_hours` + post; sem padrão → `pergunta_sim_nao`; chave `tenant + feriado + data`.
2. `editor.tasks` → `gbp.patch_location` com diff em `profile_audits`; fotos via `gbp.upload_media`. Toda ação: `diario.log` com print da tela pública; verificação diária confere 100%. Dia 1: `editor.audit_profile`. `aviso_radar` (8h–19h) em ação relevante.

Pronto: uma semana produz ≥ 1 post, 100% com print, feriado tratado 72 h antes, nenhum campo sensível sem aprovação.

### 07 Motor de Reputação

1. Primeira semana: `gbp.get_review_link` → `render.qr` → PDF → `delivery.send`.
2. Polling 30 min → `classify.review` → `anfitriao.reply_review`; notas 1 e 2 via Guardião; `gbp.reply_review`; chave por `review_id`. Pergunta → `anfitriao.answer_question` só com perfil e fatos da casa; dúvida = `exige_humano` (4 h). Violação → Guardião denuncia no fluxo do Google. Lote noturno `classify_batch`; dia 1 `reputation_report` (nota, novas, respondidas, mediana, perguntas, temas); chave `tenant + reputacao + AAAA-MM`.

Pronto: mediana < 2 h e 100% em 24 h; pergunta < 4 h; QR abre a tela oficial; nenhuma mensagem a outro número.

### 08 Extrato de Demanda

1. Dia 1 05h: SQL do mês até a `data_referencia`: contatos = 4 métricas; impressões e palavras-chave como contexto; nota; verdes ÷ medidos; custo por contato = R$ 499 ÷ contatos. Dias não publicados entram na coleta seguinte.
2. Série de 6 meses com setas; explica "ligações pelo perfil"; três frases (Gemini Pro) validadas; `render.pdf`; `delivery.send` até 8h; chave `tenant + extrato + AAAA-MM`.

Pronto: 100% dos números de SQL; sem campo de conversão; padaria 260 e R$ 1,92; oficina 168 e R$ 2,97; clínica 160 e R$ 3,12.

### 09 Horas Devolvidas

1. `hours_equivalence`: post 20 · foto 10 · resposta a avaliação 6 · resposta a pergunta 4 · ajuste de campo/horário 10 · medição 0,5 por termo-ponto · auditoria mensal 60 · Boletim 30 · extrato/PDF 45 · Mapa 60.
2. Dia 1 05h: SQL soma `actions_log` do mês (uma vez por chave, só com print ou saída) × minutos; tempo do dono = minutos entre cada `pergunta_sim_nao` e a resposta. `render.card` com total, detalhamento, tempo do dono e tabela no rodapé; `delivery.send` até 8h; chave `tenant + horas + AAAA-MM`.

Pronto: reconcilia com `actions_log` linha a linha; clínica de exemplo = 14h07 e 2 min do dono.

### 10 Voz do Cliente

1. Lote noturno: `classify_batch` (temas por segmento + emergentes; sentimento); só avaliações e perguntas públicas.
2. Dia 1 06h: `redator.voz_do_cliente`: top 3 elogios e top 3 atritos com frequência, variação e frase anonimizada; Gemini valida frequências. Atrito resolvível no perfil → `editor.tasks` no mesmo dia + "corrigi: {o que}" no card; tema acima do limiar (padrão 3 menções em 7 dias) → `aviso_radar`, ≤ 1/semana. `render.card` com 6 itens; `delivery.send` até 8h; chave `tenant + voz + AAAA-MM`.

Pronto: 6 itens com frequência e evidência anonimizada; atrito resolvível vira tarefa no mesmo dia.

### 11 Fechamento Executivo

1. Dia 1 06h, após Cartógrafo → Editor → Tesoureiro → Anfitrião: `tesoureiro.month_summary` (cinco números com variação, extrato em três linhas, horas, mapa em miniatura, ações por tipo, o que vem); `redator.fechamento` + `crosscheck`; `render.pdf`; `delivery.send` até 8h; o dono encaminha a quem quiser.
2. Trimestral desde o Dia 0: série de contatos, custo por contato, verdes, nota. Chave `tenant + fechamento + AAAA-MM` (e `+ trimestre`).

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
8. Suboperadores em página pública versionada: Google Cloud e APIs, Meta (número da casa), provedor do cérebro de linguagem, provedor de pagamento. Cloud Audit Logs nos dois projetos; painel com identidade nominal e 2FA; `actions_log` append-only por permissão de tabela.

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
wa.inbound            webhook messages          -> Delivery (Sim/Não), onboarding (áudios), opt-out (SAIR), Guardião (texto livre)
wa.status             webhook statuses          -> Delivery (reenvio 2 h); deliveries
gbp.review.new / gbp.question.new   polling     -> Anfitrião; Guardião (notas 1 e 2)
editor.tasks          Cartógrafo; Voz do Cliente -> Editor
approvals.decided     painel do Guardião        -> Editor, Anfitrião
deliveries.send       todos, via delivery.send  -> Delivery
tenant.state.changed  onboarding, offboarding   -> cadências, dashboard, painel
cost.alert            Tesoureiro                -> Head; painel
zone.changed          zone.check, offboarding   -> painel do comercial; lista de espera
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

Contas antes da semana 2: (1) Google Cloud: organização, faturamento, `radar-hml` e `radar-prd`, APIs da seção 4; (2) conta operacional Google com 2FA, Gerente nos perfis, usada só pelo GBP Connector, assina o formulário das Business Profile APIs; (3) Meta, só para o número da casa: portfólio verificado, app com WhatsApp, número dedicado "Radar Urbano", usuário de sistema com token, os cinco modelos aprovados, webhook; nenhum cadastro em nome de cliente; (4) provedor de pagamento: assinatura R$ 499/mês, webhook de status (vira `billing_active`), nota fiscal, cancelamento pelo próprio cliente.


<!-- ======================================================================
     ARQUIVO: radar-urbano/08-BIBLIA.md
     ====================================================================== -->

# Radar Urbano · Bíblia

Consulta na numeração do Mapa Mundi: travou no capítulo III de lá, procure III.x aqui. 57 verbetes, cinco partes fixas. Glossário no fim. Seguiu e não deu certo: o verbete está incompleto; anote o que faltou.

## Capítulo I · Visão e organograma

### I.1 O que é "a máquina"
**O que é:** Cinco agentes (Cartógrafo, Editor, Anfitrião, Tesoureiro, Redator-chefe), um Guardião humano, quatro conectores e o Render & Delivery; onze entregas; o dono só recebe.
**Antes:** Nada.
**Passos:** 1) Entregas 01 a 11, numeração fixa; 01 e 02 uma vez. 2) Cinco camadas; cada uma fala só com a de baixo; Gemini obrigatório para dado e Google. 3) Tenant = apartamento do cliente (I.4); zona = bairro com duas vagas por segmento (VII.2).
**Deu certo quando:** Você explica tudo com "onze pratos, cinco cozinheiros, um chefe que prova, duas mesas por ramo por bairro".
**Se deu errado:** Mais de cinco agentes ou onze entregas, ou o dono dentro da cozinha: desenho errado.

### I.2 O que é um conector
**O que é:** Programa que só fala com um sistema de fora; não pensa; devolve comprovante (id + print) e custo.
**Antes:** Nada; para ligar, capítulo III.
**Passos:** 1) Agente nunca chama `googleapis.com` ou `graph.facebook.com`; só o verbo. 2) Verbos: `gbp.*`, `places.search_text`, `wa.send_*`, `tts.synthesize`, `render.*`, `delivery.send`. 3) Falha lá fora: erro claro e retentativa (I.5). Todo conector tem sandbox (V.3).
**Deu certo quando:** Todo código que toca sistema de fora está em `connectors/`.
**Se deu errado:** Verbo com dados de outros estabelecimentos: recuse. API mudou: conserto só em `connectors/`.

### I.3 O que é um agente (e o ADK)
**O que é:** Programa com missão, cérebro via LLMGateway e ferramentas, rodando como job.
**Antes:** V.1; esqueletos no capítulo V do Mapa Mundi.
**Passos:** 1) Pasta por agente: prompt versionado, ferramentas, cérebro pelo LLMGateway. 2) Gatilhos: Cartógrafo Dia 0, Dia 7, sábado 03h, dia 1 02h · Editor segunda 04h, diário 05h · Anfitrião 30 min · Tesoureiro hora, 03h · Redator-chefe segunda 06h, dia 1 06h. 3) Uma missão por agente; até o P1 nada sai sem `guardiao.submit`; última ação, `diario.log`.
**Deu certo quando:** Existem `agents/cartografo`, `editor`, `anfitriao`, `tesoureiro`, `redator_chefe`.
**Se deu errado:** Agente que faz tudo, fica esperando ou chama Google direto: erro. Sexto agente: cabe num dos cinco.

### I.4 O que é "tenant"
**O que é:** O apartamento de cada cliente: todo dado tem `tenant_id`; a ficha tem `segmento` e `zona`, que fazem a trava territorial ser código.
**Antes:** Firestore (IV.3); zona verificada (VII.2).
**Passos:** 1) `tenant_id` em toda tabela, fila, segredo e pasta; nasce só após `zone.check`. 2) Ficha: `nome`, `segmento`, `zona`, `tom_json`, `limites_json`, `termos[]`, `raio_m`, `dono_wa_hash`; estados `created` → `billing_active` → `profiled` → `gbp_linked` → `live`. 3) `zones(segmento, zona, cidade, tenants_ativos, limite=2)`: `live` soma 1; offboarding subtrai.
**Deu certo quando:** `tenant_id` na primeira coluna de toda tabela; nenhuma linha de `zones` acima de 2.
**Se deu errado:** Três do mesmo segmento numa zona: congele o terceiro, avise o Head.

### I.5 O que é "job idempotente"
**O que é:** Rodar duas vezes dá o mesmo que uma.
**Antes:** `deliveries` e `actions_log`.
**Passos:** 1) Etiqueta única: cliente + agente + entrega + período (`padaria|redator|boletim|2026-09-14`). 2) Antes: "já feita?" Se sim, para; depois, grava em `deliveries` ou `actions_log`. 3) Ações no mundo conferem lá fora (avaliação já respondida?). Data de Brasília.
**Deu certo quando:** O mesmo job duas vezes gera uma entrega, uma linha, um custo.
**Se deu errado:** Duplicada: etiqueta não gravada. Data de domingo: UTC.

### I.6 O que é o Diário de Bordo
**O que é:** `actions_log`, append-only, com print: hora, agente, entrega, ação, alvo, print, versão do prompt, modelo, custo.
**Antes:** BigQuery; Storage para prints.
**Passos:** 1) Última ação de toda publicação, resposta, envio ou edição: `diario.log`. 2) Print da tela pública; texto de terceiros só como hash e temas; o Sim/Não do dono vira linha. 3) Só inserção; erro vira linha de correção; job diário acusa ação sem print. Retenção 5 anos.
**Deu certo quando:** Qualquer post tem a linha com print; qualquer avaliação mostra os minutos até a resposta.
**Se deu errado:** Sem `prompt_versao`: agente fora do LLMGateway. Custo em branco: o alerta de R$ 25 fica cego.

## Capítulo II · Os cérebros

### II.1 O que é um "cérebro" e como se contrata
**O que é:** Modelo de IA pago por token.
**Antes:** Cartão e e-mail da empresa; faturamento (III.1).
**Passos:** 1) Gemini pela Vertex AI (II.2), sem chave; Claude opcional (II.3). 2) `EXTRACT`, `MEASURE`, `CLASSIFY`, `GOOGLE_DECISION`, `AUDIO_IN`, `VISION` sempre Gemini; escrita usa `LLM_LANGUAGE_PRIMARY` e `FALLBACK`. 3) Modelos só em variáveis; Flash para volume, Pro para análise; Gemini R$ 3–5, linguagem R$ 2–4 por cliente/mês.
**Deu certo quando:** Studio responde "OK" e `llm_calls` tem a linha com custo.
**Se deu errado:** "billing not enabled": III.1. Claude medindo ou classificando: política furada.

### II.2 Como ligar o Gemini (Vertex AI)
**O que é:** Vertex AI (faturamento da empresa, região, Grounding com Google Maps, cache de contexto).
**Antes:** `radar-hml` com faturamento; papel de editor.
**Passos:** 1) Console → **Vertex AI → Ativar API → Model Garden → Gemini** Flash → **Vertex AI Studio** → "Responda só: OK". 2) **Grounding**: confira **Google Maps** como fonte; **IAM**: Vertex AI User à conta de serviço. 3) `gcloud auth application-default login`; `pip install google-genai`; `genai.Client(vertexai=True, project="radar-hml", location="southamerica-east1")`.
**Deu certo quando:** Studio "OK", grounding cita o Maps, script imprime "OK".
**Se deu errado:** "Permission denied": papel ou login. "Model not found in region": `us-central1` e registre.

### II.3 Como contratar o Claude (opcional)
**O que é:** Cérebro de linguagem só para escrever; nunca mede, classifica ou decide sobre o Google.
**Antes:** E-mail e cartão da empresa; Secret Manager (IV.4).
**Passos:** 1) `console.anthropic.com` → **Billing**: cartão e limite mensal (US$ 50). 2) **API Keys → Create Key** `radar-hml`; guarde como `llm-claude-key`; feche a aba. 3) Sonnet em `LLM_LANGUAGE_PRIMARY`, Gemini Pro em `FALLBACK` (ou o inverso, por II.6); teste "Responda só: OK".
**Deu certo quando:** Script imprime "OK"; o LLMGateway só o oferece para escrita.
**Se deu errado:** "Invalid API key": espaço no fim. Limite atingido: veja `llm_calls` antes de subir.

### II.4 Saída estruturada (JSON)
**O que é:** O cérebro preenche um formulário (`responseSchema`); "segundo" em vez de `2` quebraria o Mapa de Domínio.
**Antes:** Nada.
**Passos:** 1) Toda chamada leva `schema`; o LLMGateway o coloca no `generateContent`. 2) Cartógrafo `{termo, ponto, posicao|null}`; Anfitrião `{resposta, tema, sentimento, risco, suspeita}`; Editor `{campo, situacao, sugestao}`. 3) Fora do formulário: repete com temperatura menor; duas recusas, falha alto; dados com temperatura zero.
**Deu certo quando:** Em `llm_calls` a resposta é JSON válido só com os campos do esquema.
**Se deu errado:** Muitas recusas: simplifique. Número como texto: tipo não declarado.

### II.5 Prompt de sistema
**O que é:** Folha de instruções fixa de cada agente, versionada; uma frase muda todos os clientes.
**Antes:** Esqueletos do capítulo V do Mapa Mundi; ficha do tenant.
**Passos:** 1) Blocos: identidade, permissões, proibições, formato; chaves `{casa}`, `{segmento}`, `{zona}`, `{tom}`, `{servicos}`, `{horarios}`, `{limites}`. 2) Proibições: prometer posição; brinde por avaliação; inventar serviço, preço ou horário; termo de busca no nome; dado do avaliador; gerar foto. 3) `prompts/<agente>/v1.2.md`; mudou, `v1.3`; o Diário grava a versão; trocar em produção exige II.6 ou sandbox.
**Deu certo quando:** Versão na configuração igual à de uma linha recente do Diário.
**Se deu errado:** Mudou "do nada": volte pelo Git. Nome de outro cliente: bug de tenant, congele.

### II.6 Avaliação cega mensal
**O que é:** 100 exemplos reais por agente que escreve, gerados pelos dois cérebros, embaralhados, notados por duas pessoas às cegas.
**Antes:** Planilha (entrada, A, B, nota 1, nota 2; gabarito escondido); sandbox; régua 5 "publicaria sem tocar" a 1 "não pode sair".
**Passos:** 1) Entradas do Diário do mês anterior: Anfitrião 100 avaliações e perguntas; Editor 100 posts; Redator-chefe Boletins e três frases. 2) Gere em sandbox com a mesma versão de prompt; embaralhe; notas sem conversa. 3) Maior média vira `LLM_LANGUAGE_PRIMARY`; registre em `avaliacoes/AAAA-MM.md`; notas 1–2 viram casos de teste.
**Deu certo quando:** Arquivo por mês em `avaliacoes/` e a variável em produção bate com ele.
**Se deu errado:** Diferença < 0,2: empate, custo decide. Discordância ≥ 2 pontos: régua ruim.

## Capítulo III · Os conectores

### III.1 Google Cloud: conta, projeto, faturamento
**O que é:** Onde a máquina mora; projeto é a pasta do ambiente, faturamento é o cartão.
**Antes:** Conta Google da empresa com 2FA; cartão, CNPJ; e-mail do engenheiro.
**Passos:** 1) `console.cloud.google.com` → **Novo projeto** `radar-hml` e `radar-prd`; anote o **Número do projeto**; **Faturamento**: ligue os dois; **IAM**: engenheiro como Editor. 2) **Biblioteca**: Vertex AI, Places API (New), Cloud Run Admin, Cloud Build, BigQuery, Firestore, Secret Manager, Scheduler, Pub/Sub, Text-to-Speech, Identity Toolkit. 3) `gcloud init`; `gcloud config set run/region southamerica-east1`; **Orçamentos** R$ 500/mês; exportação de faturamento ao BigQuery.
**Deu certo quando:** Dois projetos com faturamento; onze APIs "Ativada".
**Se deu errado:** "Sem permissão": conta pessoal. Cartão recusado: banco.

### III.2 Pedir acesso às Business Profile APIs
**O que é:** Formulário do Google, 1–2 semanas; pedido do dia 1.
**Antes:** Número do projeto; site com nome, atividade e e-mail no domínio; texto de uso (gestão de Perfis da Empresa de PMEs; acesso por papel de Gerente; sem senha, sem extração em massa).
**Passos:** 1) `developers.google.com/my-business` → **Prerequisites / Request access**; preencha; data em `acessos.md`. 2) Enquanto espera: III.3, III.4, III.6, III.7. 3) Aprovado: ativar Account Management, Business Information, Performance, Q&A e Google My Business API (v4); **Cotas** > 0; teste `accounts.list`.
**Deu certo quando:** Cinco APIs ativas, cotas > 0, `accounts.list` sem 403.
**Se deu errado:** 15 dias sem resposta: reenvie e escreva no fórum oficial. Cota 0: outro projeto.

### III.3 Conta operacional e OAuth
**O que é:** `operacao@radarurbano.com.br` é o funcionário que o cliente adiciona como Gerente; OAuth deixa o programa agir por ela sem senha.
**Antes:** `radar-prd`; conta no domínio; cofre de senhas para gente.
**Passos:** 1) Crie a conta, 2FA, senha no cofre; **Tela de permissão OAuth**: Interno, ou Externo publicado (em Teste o token morre em 7 dias). 2) **Credenciais → ID do cliente OAuth → Aplicativo da Web** `radar-gbp`; redirecionamento `http://localhost:8080/callback`; segredo `gbp-oauth-client`. 3) `scripts/gbp_login.py` (`access_type=offline`, `prompt=consent`, escopo `business.manage`) só com a conta operacional; refresh token em `gbp-operator-refresh-token`; rotação 90 dias.
**Deu certo quando:** `accounts.list` devolve a conta e o token segue válido após 8 dias.
**Se deu errado:** `redirect_uri_mismatch`: URL não idêntica. `access_denied`: conta errada.

### III.4 Ser adicionado como Gerente no perfil do cliente
**O que é:** O cliente adiciona a conta operacional como Gerente: um minuto, minuto 5 a 8 do Dia 0.
**Antes:** Cliente Proprietário, logado no celular com a conta dona (senão III.5).
**Passos:** 1) Texto ao cliente: "Abra o *Google Maps* com a conta dona do perfil e pesquise o nome da empresa. *Três pontinhos* → *Configurações do Perfil da Empresa* → *Pessoas e acesso* (ou *Gerentes*) → *Adicionar* → operacao@radarurbano.com.br → *Gerente* → *Convidar*." 2) Computador: `business.google.com` → **Configurações do Perfil da Empresa → Pessoas e acesso → Adicionar**. 3) `gbp.discover` aceita o convite, casa nome e endereço, grava `gbp_location_id` e `place_id`; `gbp_linked` dispara a entrega 01.
**Deu certo quando:** `locations` preenchido, `gbp_linked`, Diagnóstico na conversa.
**Se deu errado:** Não acha o menu: peça print. Não é proprietário: III.5.

### III.5 Perfil não reivindicado ou não verificado
**O que é:** Sem reivindicar e verificar, ninguém edita.
**Antes:** Cliente no estabelecimento, com e-mail e telefone da empresa.
**Passos:** 1) Cliente pesquisa a empresa logado: "É proprietário desta empresa?" = A; "já foi reivindicado" = B; não aparece = C. 2) A: **Gerenciar agora** → verificação; B: **Solicitar acesso**, o dono atual tem 3 dias; C: `google.com/business` → **Adicionar sua empresa**, categoria principal com o Guardião. 3) Verificação: vídeo sem cortes (fachada com placa e número, interior, prova de que trabalha ali), até 5 dias úteis; verificado, III.4.
**Deu certo quando:** `locations.status` sai de `PENDING_VERIFICATION`; `gbp_linked`; Dia 7 conta do vínculo.
**Se deu errado:** Vídeo recusado: placa, número, loja aberta. Sem resposta: `support.google.com/business` com CNPJ.

### III.6 Places API e chave restrita
**O que é:** Serviço pago que lista lugares para um termo perto de um ponto; o Cartógrafo mede posição com `places:searchText`.
**Antes:** Faturamento; `curl`.
**Passos:** 1) **Biblioteca → Places API (New) → Ativar**; **Chave de API** `places-prd` → **Restringir** → só Places API (New); depois IPs do Cloud NAT; segredo `places-api-key`. 2) Teste: `POST .../v1/places:searchText`, cabeçalhos `X-Goog-Api-Key` e `X-Goog-FieldMask: places.id`, corpo `textQuery`, `pt-BR`, `BR`, `pageSize 20`, `locationBias.circle`. 3) Posição = índice do `place_id` (1–20) ou fora do top 20; **Maps Platform → Cotas**: 5.000/dia.
**Deu certo quando:** O teste devolve lugares; Métricas mostra "Text Search"; chave restrita.
**Se deu errado:** "API key not valid": IP ou projeto. "REQUEST_DENIED": ativou a antiga.

### III.7 Meta: portfólio, verificação, app e número da casa
**O que é:** Uma vez só: Portfólio de negócios, verificação da empresa, App com WhatsApp e um número da empresa: o número da casa.
**Antes:** CNPJ em PDF, comprovante de endereço no nome legal, site, e-mail no domínio; conta pessoal de um sócio com 2FA; número novo que nunca teve WhatsApp; página de privacidade; cartão.
**Passos:** 1) `business.facebook.com` → **Criar conta** "Radar Urbano" → **Central de Segurança → Verificação da empresa**. 2) `developers.facebook.com` → **Criar app** (Empresa) → **WhatsApp** → **Adicionar número**: nome "Radar Urbano", código por SMS ou ligação; anote `phone_number_id` (`DELIVERY_SENDER_PHONE_ID`) e `waba_id`; **Básico**: `META_APP_ID/SECRET`; modo **Ativo**. 3) **Usuários do sistema** `radar-system` com app e WABA; **Gerar token** (nunca expira) → `meta-system-user-token`; **Webhooks**: URL `https://<wa-inbound>/webhooks/wa`, assine `messages` e `message_template_status_update`; **Pagamento**: cartão.
**Deu certo quando:** `hello_world` sai do número da casa como "Radar Urbano"; webhook recebe `sent/delivered/read`; empresa verificada.
**Se deu errado:** Verificação recusada: nomes não batem. "Número em uso": apague a conta no celular.

### III.8 Modelos de mensagem para o dono (e o SAIR)
**O que é:** Fora da janela de 24 h só sai modelo aprovado.
**Antes:** III.7; amostras de card, PDF e MP4; consentimento do Dia 0 registrado.
**Passos:** 1) Gerenciador → **Modelos de mensagem → Criar**, Utilidade, pt_BR; corpos literais na seção 15 do brief ({{1}} nome, {{2}} conteúdo, {{3}} referência). 2) Janela aberta: card e áudio livres; fechada: modelo com MP4; só status Aprovado. 3) SAIR: `wa_optout = true`, uma resposta, nada mais até novo Sim escrito; outro texto: transbordo humano.
**Deu certo quando:** Cinco modelos Aprovados; o Sim volta pelo webhook; SAIR desliga na hora.
**Se deu errado:** Rejeitado ou Marketing: tire tom de promoção. Vídeo recusado: MP4 H.264/AAC ≤ 16 MB.

### III.9 Cloud Text-to-Speech: a voz da casa
**O que é:** Texto vira voz para o Boletim (≤ 60 s).
**Antes:** Faturamento; roteiro de teste com números por extenso.
**Passos:** 1) **Biblioteca → Cloud Text-to-Speech API → Ativar**; painel: Português (Brasil), **Chirp 3: HD**; escolha e anote em `TTS_VOICE_ID`. 2) Script `google-cloud-texttospeech`: `OGG_OPUS`, 48000 Hz, mono; envie ao seu celular por `wa.send_media` tipo `audio`. 3) 60 s ≈ 150 palavras; o conector recusa acima; números por extenso, sem SSML.
**Deu certo quando:** Toca no WhatsApp como mensagem de voz, < 60 s.
**Se deu errado:** Robótica: voz Standard/WaveNet. Chega como documento: OGG/Opus mono, `audio/ogg`.

### III.10 Webhook: status e respostas do dono, e como testar
**O que é:** A Meta toca `wa-inbound` a cada evento: status (`sent`, `delivered`, `read`, `failed`) e respostas (Sim, Não, SAIR, texto, áudio).
**Antes:** `wa-inbound` no Cloud Run ou `ngrok`; `WA_WEBHOOK_VERIFY_TOKEN`, `META_APP_SECRET`.
**Passos:** 1) Validação: `GET /webhooks/wa?hub.mode=subscribe&hub.verify_token=...&hub.challenge=N` → 200 com `N` em texto puro. 2) Recados: `POST` com `X-Hub-Signature-256` (HMAC do corpo bruto); publique em `wa.status`/`wa.inbound`; 200 em < 2 s; idempotência pelo `wamid`. 3) Local: `ngrok http 8080`, cadastre a URL, **Verificar e salvar**, `hello_world`; status → `deliveries`; Sim/Não → `approvals.decided`; "sair" → opt-out; outro texto → transbordo.
**Deu certo quando:** Recados no log com 200 em < 2 s; `deliveries` com `lido_em`; um Sim em `approvals.decided`.
**Se deu errado:** "Não foi possível validar": challenge com aspas. Nada no POST: WABA não assinada.

### III.11 Link curto e QR de avaliação (o material do balcão)
**O que é:** Link oficial do perfil que abre a tela "escreva sua avaliação", virado em QR e PDF de balcão e comanda.
**Antes:** Tenant `gbp_linked` e verificado; logotipo e tom; política do Google (sem brinde, sem "gostou?", sem tablet).
**Passos:** 1) Dono: painel do perfil → **Receber mais avaliações**; máquina: `gbp.get_review_link` lê `metadata.newReviewUri`. 2) `render.qr` (correção de erro alta); `render.pdf`: cartão A6 e tira de comanda, "Avalie a sua experiência. Aponte a câmera para o código." 3) `entrega_radar` (documento) na primeira semana; em "Arquivos" no dashboard; linha ao dono: "não peça nota, não ofereça nada, não escolha para quem mostrar".
**Deu certo quando:** QR lido fora da rede da loja abre a tela certa; a primeira avaliação por ele é respondida em < 2 h.
**Se deu errado:** `newReviewUri` vazio: não verificado ou suspenso. "Página não encontrada": novo `place_id`.

## Capítulo IV · A fundação

### IV.1 Cloud Run
**O que é:** Programas sem servidor.
**Antes:** `gcloud`; repositório com `Dockerfile`.
**Passos:** 1) `gcloud run deploy wa-inbound --source . --region southamerica-east1 --allow-unauthenticated`. 2) `gcloud run jobs create cartografo --source . --region southamerica-east1 --command python --args -m,agents.cartografo`; execute com `--args --tenant=padaria`. 3) Conta de serviço por agente: Vertex AI User, BigQuery Data Editor, Firestore User, Secret Accessor só nos segredos dele.
**Deu certo quando:** A URL responde e o job termina "Succeeded".
**Se deu errado:** "Permission denied": falta papel. Build falhou: log do Cloud Build.

### IV.2 BigQuery
**O que é:** Armazém de números; todo extrato, card e dashboard nasce de SQL aqui.
**Antes:** Faturamento.
**Passos:** 1) **Criar conjunto de dados** `radar`, `southamerica-east1`; as 15 tabelas da seção 8 do brief via `sql/create_tables.sql`; partição por data, cluster `tenant_id`; expiração conforme IX.2. 2) `hours_equivalence`: post 20 · foto 10 · resposta a avaliação 6 · pergunta 4 · ajuste 10 · medição 0,5 por termo-ponto · auditoria 60 · Boletim 30 · extrato/PDF 45 · Mapa 60. 3) `SELECT COUNT(*) FROM radar.metrics_daily` → 0; cota diária de consulta (50 GB).
**Deu certo quando:** 15 tabelas particionadas, com cluster e expiração visíveis.
**Se deu errado:** "Not found: Dataset": região. Expiração "Nunca": console e Terraform.

### IV.3 Firestore
**O que é:** Banco de fichas: um documento por tenant (configuração, estado, `wa_optout`, `editor_frozen`) e a fila `approvals`.
**Antes:** Projeto criado.
**Passos:** 1) **Firestore → Criar banco** → Nativo → `southamerica-east1`. 2) Coleção `tenants`, documento `padaria-teste` com os campos de I.4; coleção `approvals`. 3) Regras: só contas de serviço; índices pelo link que o console sugere.
**Deu certo quando:** O documento aparece e o programa o lê.
**Se deu errado:** "Insufficient permissions": Firestore User. Ficha sem `segmento`/`zona`: não passa de `created`.

### IV.4 Secret Manager
**O que é:** Cofre de senhas de sistema; só contas autorizadas leem; troca sem tocar em código.
**Antes:** API ativada.
**Passos:** 1) **Criar segredo**: `places-api-key`, `gbp-oauth-client`, `gbp-operator-refresh-token`, `meta-app-secret`, `meta-system-user-token`, `wa-webhook-verify-token`; por tenant `tenant-{id}-gbp-oauth`. 2) Segredo → **Permissões** → conta de serviço → Secret Accessor. 3) Código lê `versions/latest`; nunca em variável em claro; trocar: **Nova versão**; rotação de 90 dias.
**Deu certo quando:** O programa lê e **Registros** mostra o acesso.
**Se deu errado:** "Permission denied": Accessor faltando. Vazou: revogue na origem, versão nova.

### IV.5 Cloud Scheduler e Pub/Sub
**O que é:** Relógio e quadro de recados; juntos, a cadência da seção 9 do brief.
**Antes:** Jobs no Cloud Run.
**Passos:** 1) Tópicos: `wa.inbound`, `wa.status`, `gbp.review.new`, `gbp.question.new`, `editor.tasks`, `approvals.decided`, `deliveries.send`, `tenant.state.changed`, `cost.alert`, `zone.changed`, `agents.run`. 2) Scheduler, fuso `America/Sao_Paulo`: anfitrião `*/30 * * * *` · visões `0 * * * *` · coleta `0 3 * * *` · horários `0 5 * * *` · post `0 4 * * 1` · Boletim `0 6 * * 1`, envio `0 7 * * 1` · reduzida `0 3 * * 6` · dia 1 `0 2 1 * *`. 3) Serviço `dispatcher` assina `agents.run` e dispara o job por tenant ativo.
**Deu certo quando:** Na segunda seguinte o Boletim sai sozinho com `enviado_em` às 7h.
**Se deu errado:** Horário errado: fuso UTC. Recado duplicado: normal (I.5).

### IV.6 GitHub e deploy automático
**O que é:** PR aprovado em `main` vira revisão nova no Cloud Run pelo Cloud Build.
**Antes:** Repositório privado `radar-urbano`.
**Passos:** 1) Ramificações `main` (produção) e `hml`. 2) **Cloud Build → Gatilhos → Conectar repositório**; `^main$` com `cloudbuild.yaml` para `radar-prd`; `^hml$` para `radar-hml`. 3) Ninguém envia direto para `main`; PR revisado por outra pessoa.
**Deu certo quando:** PR aprovado aparece em **Revisões** em minutos.
**Se deu errado:** Build falhou: log do gatilho. Revisão ruim: volte à anterior.

### IV.7 Terraform
**O que é:** Infraestrutura como texto (projetos, tabelas, tópicos, permissões, expirações).
**Antes:** Engenheiro.
**Passos:** 1) S1: `terraform apply` sobe os dois ambientes; se atrasar, console e `terraform import` até a S3. 2) Depois, todo recurso nasce no Terraform, inclusive retenção (IX.2).
**Deu certo quando:** `terraform plan` em `radar-hml` sem diferença.
**Se deu errado:** Diferença: alguém clicou no console; corrija no código.

## Capítulo V · Os agentes

### V.1 ADK: primeiro agente em 20 minutos
**O que é:** Instalar o kit e rodar um agente de teste, molde dos cinco.
**Antes:** Python 3.11+; login ADC; Vertex AI (II.2).
**Passos:** 1) `python -m venv .venv && source .venv/bin/activate && pip install google-adk google-genai`. 2) `agents/ola/agent.py`: `Agent(name="ola", model=os.environ["GEMINI_MODEL_FLASH"], instruction="Responda em uma frase.", tools=[])`. 3) `GOOGLE_GENAI_USE_VERTEXAI=TRUE`, `GOOGLE_CLOUD_PROJECT=radar-hml`, `GOOGLE_CLOUD_LOCATION=southamerica-east1`; `adk web` em `agents/`, digite "oi".
**Deu certo quando:** Responde no `adk web` e o log mostra a chamada ao Gemini.
**Se deu errado:** `ModuleNotFoundError`: venv inativo. Região: troque a variável.

### V.2 Dar uma ferramenta a um agente
**O que é:** Função do conector com nome e docstring clara; o ADK mostra ao cérebro, que decide quando chamar.
**Antes:** V.1; GBP Connector com `create_post` em homologação.
**Passos:** 1) `def create_post(tenant_id: str, texto: str, foto_uri: str) -> dict:` com docstring "Publica um post no perfil do cliente. Retorna id e print." 2) `tools=[create_post, diario_log, guardiao_submit]`; instrução: "monte o post, `guardiao_submit`; aprovado, `create_post` e `diario_log`". 3) `adk web`: "Publique o post da semana da padaria-teste".
**Deu certo quando:** Post no perfil de teste e linha com print no Diário.
**Se deu errado:** Não chama: docstring vaga. Argumentos errados: tipos e exemplos.

### V.3 Sandbox
**O que é:** `RADAR_SANDBOX=1` troca as ferramentas que tocam o mundo por versões que só anotam; o cérebro roda, o mundo não.
**Antes:** V.2.
**Passos:** 1) Conectores em `dry_run=True` gravam em `actions_log` com `sandbox=true`; obrigatório em `radar-hml`. 2) Perfil de teste no Google e número de teste da Meta para o que precisa tocar o mundo. 3) `scripts/seed_tenant.py padaria-teste`: um mês sintético; teste fixo: `zone.check` recusa a terceira na zona.
**Deu certo quando:** Ponta a ponta em homologação sem linha com `sandbox=false`.
**Se deu errado:** Ação real em homologação: rodou sem a variável; bloqueie por código.

### V.4 Painel do Guardião
**O que é:** Fila de aprovação em lote.
**Antes:** Google Sheets; depois Identity Platform.
**Passos:** 1) Planilha `Guardião`: `id`, `tenant`, `agente`, `tipo`, `conteúdo`, `foto`, `risco`, `decisão`, `texto editado`, `decidido por`, `hora`; job a cada 5 min executa; abas `QA` e `Zonas`. 2) Verdade: login, prioridade, atalhos A/E/R, Firestore `approvals`, custo por tenant ao lado, transbordo, `zone.check`. 3) P0 tudo antes; P1 lote com meta > 85%; P2 direto com QA de 10%; dois olhos sempre para categoria, nome, endereço, notas 1–2.
**Deu certo quando:** 100 itens sintéticos aprovados em < 90 min com registro.
**Se deu errado:** Fila crescendo (SLA 4 h úteis): taxa de rejeição alta é prompt ruim, não falta de gente.

### V.5 A grade de medição: raio, termos, pontos e a validação com 20 buscas
**O que é:** 3×3 a 5×5 pontos sobre o raio do cliente; por termo, uma `places.search_text` por ponto; posição = índice do `place_id`.
**Antes:** `place_id`; `termos[]` e `raio_m` do Dia 0; chave Places.
**Passos:** 1) Raio: o que o dono disse; padrão 1.500 m em cidade, 3.000 m onde bairro não serve; 3×3 no Dia 0, Dia 7 e sábado, até 5×5 no dia 1; espaçamento = 2 × raio ÷ (lado − 1), `radius` = espaçamento ÷ 2. 2) Até 25 termos; 3 a 5 termos-chave nas reduzidas; `rank_measurements(tenant_id, data, termo, grid_point, lat, lng, posicao)`, nulo = fora do top 20; verde top 3, cinza 4º–10º, vermelho fora do top 10. 3) Validação mensal: 20 buscas manuais no Maps do celular, conta neutra, localização no ponto; concordância ≥ 85%; rodapé do Mapa declara o método.
**Deu certo quando:** Posição para cada termo-ponto; SVG com três cores; validação ≥ 85%.
**Se deu errado:** < 85%: `radius` grande ou termo genérico. Sempre fora do top 20: `place_id` errado.

## Capítulo VI · As receitas (bicicletas das onze entregas)

Bicicleta e máquina produzem o mesmo objeto, com a mesma cara. Ferramentas: app do Perfil da Empresa (Google Maps → foto → **Seu perfil comercial**), planilha por cliente, Canva, Google Docs, My Maps, WhatsApp Business no celular da casa. Toda ação gera print e linha na aba `Diário`. Passou de 7 h por cliente por mês: automatize essa entrega primeiro.

### VI.01 Diagnóstico de Posição
**O que é:** Card + PDF do Dia 0: posição em um termo-chave nos 9 pontos, o que falta no perfil, três primeiras ações.
**Antes:** Termo-chave e raio do Dia 0; `place_id`.
**Passos:** 1) Enquanto o cliente adiciona o Gerente, busque o termo em 9 pontos do Maps (localização no ponto); anote. 2) App → **Editar perfil**: confira descrição, categorias, horários (e **Adicionar horário de feriado**), serviços, atributos, fotos. 3) Canva: 9 quadradinhos coloridos, lista do que falta, três frases; Docs → PDF; mande no minuto 8 a 10.
**Deu certo quando:** O card chega antes dos 15 minutos.
**Se deu errado:** Perfil pendente: só posição e o que é público; diga isso.

### VI.02 Antes e Depois do Perfil
**O que é:** Card lado a lado no Dia 7 (desde `created`): cada campo antes e depois, mais a segunda medição.
**Antes:** Prints do Dia 0; lista do VI.01.
**Passos:** 1) Refaça a busca nos 9 pontos. 2) **Editar perfil**: print de cada campo alterado (descrição, horários, serviços, fotos, posts). 3) Canva em duas colunas com a linha de posição e a frase do QR; WhatsApp até as 8h; arquivo no dashboard.
**Deu certo quando:** Cada linha do card tem linha no Diário com print.
**Se deu errado:** Perfil ligou depois: conte 7 dias do vínculo.

### VI.03 Dashboard Radar
**O que é:** Link fixo com números do Google (com data de referência) e o que é próprio; hora em hora na máquina, diário na bicicleta.
**Antes:** Planilha por cliente, "qualquer pessoa com o link".
**Passos:** 1) Primeira linha: ligações pelo perfil, rotas, cliques no site, mensagens, impressões, data de referência; uma linha por dia. 2) Todo dia 7h: app → **Desempenho** → copie o último dia disponível (2–3 dias atrás) com a data. 3) Nota fixa: "ligações pelo perfil são toques no botão Ligar contados pelo Google"; peça para salvar na tela inicial.
**Deu certo quando:** O cliente abre no celular e vê números com data.
**Se deu errado:** Número sem data de referência: não publique.

### VI.04 Boletim de Segunda
**O que é:** Áudio ≤ 60 s + card às 7h, cobrindo a semana fechada disponível.
**Antes:** Planilha do VI.03; posição de sábado nos termos-chave; aba `Diário`.
**Passos:** 1) Domingo: some a semana até a data de referência; avaliações novas e respondidas em **Avaliações**. 2) Segunda 6h: áudio ("Bom dia, {nome}", números por extenso, "dados do Google até quinta", ações, o que vem, "nada a fazer do seu lado"). 3) Card no Canva; 7h, áudio e card.
**Deu certo quando:** 7h, ≤ 60 s, data de referência dita.
**Se deu errado:** Google atrasado: diga "o Google ainda não liberou os números"; o resto sai.

### VI.05 Mapa de Domínio
**O que é:** Imagem do dia 1 com a grade colorida por termo; sem concorrentes nomeados; rodapé com o método.
**Antes:** Termos (na bicicleta, 5); Google My Maps.
**Passos:** 1) 9 pontos do bairro, cada termo buscado no Maps com a localização no ponto; anote. 2) My Maps: marcador por ponto (verde/cinza/vermelho), camada por termo; exporte; rodapé "posição vista na busca do Maps em cada ponto; validação com 20 buscas". 3) Dia 1 até as 8h; link no dashboard.
**Deu certo quando:** Todo ponto tem cor e o rodapé diz o método.
**Se deu errado:** Não dá para ir aos pontos: modo anônimo com o endereço do ponto; anote.

### VI.06 Diário de Bordo do Perfil
**O que é:** Tudo que foi feito no perfil, em português de gente, com print; linha no WhatsApp quando há ação relevante.
**Antes:** Aba `Diário`; calendário de feriados nacionais e municipais.
**Passos:** 1) Segunda: app → **Adicionar atualização** → foto real + texto; print. 2) 72 h antes de feriado: **Editar perfil → Horário de funcionamento → Adicionar horário de feriado** + post; print. 3) **Fotos**; **Descrição** (≤ 750 caracteres); serviços e atributos; categoria só com aprovação humana; linha no WhatsApp por ação relevante, 8h–19h.
**Deu certo quando:** Toda ação tem linha com print; o resumo entra no Boletim.
**Se deu errado:** Foto gerada ou de banco: nunca.

### VI.07 Motor de Reputação
**O que é:** Toda avaliação respondida em ≤ 2 h; perguntas respondidas; QR; Boletim de Reputação mensal.
**Antes:** Notificações do app; tom; planilha `Avaliações` (data, nota, temas, sentimento, respondida em).
**Passos:** 1) **Avaliações → Responder**, específica e humanizada; notas ≤ 2 por segunda pessoa antes; **Perguntas e respostas**: < 4 h. 2) **Receber mais avaliações** → link → QR + PDF (III.11) na primeira semana; suspeita: **Denunciar avaliação**. 3) Dia 1: card com nota, novas, respondidas, temas elogiados e de atenção.
**Deu certo quando:** Nenhuma avaliação passa de 2 h (100% em 24 h); QR no balcão.
**Se deu errado:** Dono quer convite por mensagem ou brinde: não existe neste produto.

### VI.08 Extrato de Demanda
**O que é:** PDF do dia 1: contatos do mês e custo por contato (R$ 499 ÷ contatos).
**Antes:** **Desempenho** do mês fechado.
**Passos:** 1) Contatos = ligações pelo perfil + rotas + cliques no site + mensagens pelo perfil; impressões e palavras-chave só como contexto. 2) R$ 499 ÷ contatos (exemplo padaria: 260, R$ 1,92). 3) Docs → PDF de uma página com data de referência e a nota sobre "ligações pelo perfil"; WhatsApp até as 8h.
**Deu certo quando:** Quatro linhas, soma, custo por contato, data.
**Se deu errado:** Pediram "novos clientes" ou "receita": não entra; o dono coloca o valor dele por cima.

### VI.09 Horas Devolvidas
**O que é:** Card do dia 1: ações do Diário × tabela de equivalência; tempo do dono = minutos dos Sim/Não.
**Antes:** Aba `Diário`; tabela do IV.2.
**Passos:** 1) Conte por tipo e multiplique (clínica: 8 posts, 6 fotos, 27 avaliações, 5 perguntas, 4 ajustes, 240 medições, auditoria, Boletins e extratos = 14h07). 2) Card com a soma, a tabela no rodapé e o tempo do dono ("2 minutos, em uma resposta de sim ou não").
**Deu certo quando:** Cada linha do card bate com o Diário.
**Se deu errado:** Minuto sem linha no Diário: não conta.

### VI.10 Voz do Cliente
**O que é:** Card do dia 1 com temas de avaliações e perguntas: três elogios, três atritos, uma frase real de cada, sem nome; alerta quando um tema dispara.
**Antes:** Planilha `Avaliações` com temas.
**Passos:** 1) Leia tudo do mês; marque tema e sentimento; conte. 2) Card: três mais elogiados, três de atenção, frase anônima, variação contra o mês anterior. 3) Tema que triplica na semana: linha no WhatsApp em horário comercial.
**Deu certo quando:** Nenhum nome; cada tema com contagem.
**Se deu errado:** Só avaliações e perguntas; conversas não existem aqui.

### VI.11 Fechamento Executivo
**O que é:** PDF de uma página no dia 1 (e trimestral): cinco números com variação, três linhas do Extrato, horas, mapa em miniatura, o que fizemos, o que vem.
**Antes:** VI.03, VI.05, VI.08, VI.09 prontos.
**Passos:** 1) Modelo no Docs; números do mês e variação; mapa em miniatura; ações; próximo mês. 2) Trimestre: três meses lado a lado; PDF até as 8h; arquivo permanente no dashboard.
**Deu certo quando:** Uma página, números conferidos contra o Extrato, sem promessa de resultado.
**Se deu errado:** Cópia automática a terceiros: não existe.

## Capítulo VII · Onboarding

### VII.1 O roteiro literal do Dia 0
**O que é:** Quatro mensagens, cada uma com um toque que vira estado.
**Antes:** Zona verificada (VII.2); contrato por link (número do dono e aceite do canal) e pagamento; conta operacional; número da casa com modelos; relógio.
**Passos:** 1) Antes (5 min dele): contrato assinado → `zone.check` ocupa a vaga e cria o tenant (`created`); cartão → `billing_active`; o dono abre a conversa pelo link do contrato (janela de 24 h); sem mensagem em 1 h, `pergunta_sim_nao` "Podemos começar?". 2) Minuto 0–5: cinco perguntas por áudio (o que mais vende e como o cliente procura; bairros ou raio; jeito de falar; o que pode fazer sem perguntar; número e como quer ser chamado); Gemini transcreve; confirmação por `pergunta_sim_nao`; o Sim grava tudo (`profiled`) e vale como opt-in. 3) Minuto 5–8: texto do Gerente (III.4); `gbp.discover` liga; medição 3×3, auditoria, três frases, PDF. 4) Minuto 8–10: "Seu painel: {link}. Salve na tela inicial. Senha, se quiser, lá dentro; ninguém aqui vê. Seu Diagnóstico de Posição: {card}. A partir de agora você só recebe: segunda 7h o Boletim; Dia 7 o Antes e Depois; dia 1 o Mapa e os extratos."; abrir o link registra a entrega 01 (`live`); pare o relógio.
**Deu certo quando:** `live` (ou pendente registrada); Diagnóstico com `lido_em`; consentimento com data, hora e texto; ≤ 15 min.
**Se deu errado:** Some: após 72 h, `aviso_radar` com o passo pendente, um por semana. Sem a pergunta 4: Editor em P0.

### VII.2 Verificar a disponibilidade da zona (a trava territorial)
**O que é:** Antes de vender: nesta zona, neste segmento, já há dois? Zona = bairro do Google Maps (ou raio equivalente), no contrato com cidade e segmento.
**Antes:** Endereço do perfil; categoria principal; `zones` e **Consultar zona** (ou planilha `Zonas`: `cidade`, `zona`, `segmento`, `tenants_ativos`, `limite`, `nomes`, `reserva`, `lista_de_espera`).
**Passos:** 1) Zona: endereço no Maps, leia o bairro ("São Paulo · Jardim América"); onde bairro não serve, círculo com o raio da grade; segmento: categoria principal, teste "apareceriam na mesma busca?". 2) Livre: proposta com cidade, zona e segmento na cláusula; reserva por 5 dias úteis (conversa não reserva); assinado: `zone.check` em transação soma 1, publica `zone.changed`; só então `created`. 3) Lotada: não venda, sem tenant provisório; lista de espera (nome, contato, data; ordem de chegada, ninguém fura); vaga abriu: comercial chama o primeiro em 2 dias úteis. 4) Mudou endereço ou categoria: nova verificação; sem vaga, mantém até o fim do ciclo pago e entra na lista da zona nova; zona redesenhada: quem está fica.
**Deu certo quando:** Nenhuma linha de `zones` acima de 2, todo dia; todo `live` com zona e segmento do contrato; `zone.check` recusa a terceira em teste.
**Se deu errado:** Vendeu em zona lotada: o tenant não nasce; Head devolve com a frente da lista. Bairro em disputa: vale o Maps.

## Capítulo VIII · Operação

### VIII.1 QA por amostragem
**O que é:** Todo dia útil, 10% das ações publicadas ontem, lidas pelo print: `ok`, `editaria`, `errado`.
**Antes:** Aba `QA`; `actions_log` de ontem; `qa_samples`; 20 min no início do turno.
**Passos:** 1) `sql/qa_amostra.sql`: ontem, `sandbox = false`, só o que tocou o mundo; 10%, mínimo 20, máximo 60. 2) Leia como o cliente do cliente; `errado` com motivo; corrige no mesmo dia, com print e origem `qa`. 3) Metas: `errado` < 2%, `editaria` < 15%; dois dias fora, o agente volta ao P1 até revisar o prompt; dia 2, taxas por `prompt_versao` para II.6.
**Deu certo quando:** ≥ 20 linhas por dia útil; taxas na meta; cada `errado` com correção.
**Se deu errado:** Só `ok` por semanas: plante três erros num tenant de teste. Erros num tenant só: `tom_json`.

### VIII.2 Custo por cliente (e o que fazer acima de R$ 25)
**O que é:** Custo de tecnologia por tenant por mês; alerta em R$ 25.
**Antes:** `llm_calls`, `actions_log`, `rank_measurements`, `deliveries`; `sql/custo_por_tenant.sql`; `precos_unitarios`; faturas.
**Passos:** 1) Dia 1 (Tesoureiro 05h): `llm_calls.custo` + buscas × preço Places + mensagens × preço utilidade + TTS + rateio de nuvem; confira com as faturas (10% de folga). 2) Referência: Gemini 3–5 · linguagem 2–4 · Places 3–8 · WhatsApp da casa 1–2 · TTS, Cloud Run, BigQuery, Storage 3–6 · total R$ 12–25. 3) Acima: `cost.alert`; causas: grade ou termos demais (5×5 × 25 termos = 625 buscas), Pro onde Flash bastava, auditoria sem cache, job em dobro, loop; corrija na ordem barata; revise em 48 h.
**Deu certo quando:** Média < R$ 25; nenhum tenant acima por dois meses; tabela batendo com as faturas.
**Se deu errado:** Cartógrafo campeão: grade. Editor: sem cache.

### VIII.3 Runbook: perfil suspenso
**O que é:** `locations.status = SUSPENDED`; `tenant.state.changed` alerta o Head.
**Antes:** Acesso Gerente; Diário de 30 dias e `profile_audits`; comprovantes do cliente (CNPJ, fachada com placa, conta de luz).
**Passos:** 1) `editor_frozen = true`; Anfitrião lê, mas não responde; em até 1 h, pelo número da casa: o que houve, o que fizemos, o que vamos fazer, o que precisamos dele. 2) Audite 30 dias: termo de busca no nome, categoria trocada, endereço divergente, post fora da política; corrija com print; **Restabelecer perfil suspenso** com o Proprietário; número do caso na ficha. 3) Enquanto espera: Cartógrafo mede; Boletim diz "perfil suspenso desde {data}"; em 48 h, auditoria em 100% dos tenants; causa nossa vira prompt novo; restabelecido: descongele; `incidentes/AAAA-MM-DD-tenant.md`.
**Deu certo quando:** Status ativo; causa registrada; auditoria dos 100% em 48 h; cliente avisado no início, a cada passo e no fim.
**Se deu errado:** Recusado: comprovante fraco; reenvie. 14 dias sem resposta: Head assume. Quer cancelar: pode; ofereça congelar sem cobrar.

### VIII.4 Runbook: API do Google parou
**O que é:** 429 (cota) ou 5xx em Business Profile, Places, Vertex AI ou TTS.
**Antes:** **Logging** com `status >= 429`; páginas de status; **Cotas**; conta operacional.
**Passos:** 1) Qual API, qual código: 401/403 é credencial (III.3) ou Gerente removido (III.4); Google fora: 30 min sem mexer, não reinicie; 429: peça aumento, reduza cadência. 2) Avaliações fora > 90 min: Guardião responde à mão em `business.google.com`, Diário com origem `manual VIII.4`; o Anfitrião reconhece depois; perguntas: meta 4 h; Performance API > 72 h: o Boletim diz. 3) Gemini fora: tarefas obrigatórias esperam (fila > 2 h alerta); linguagem usa fallback; Boletim sem verificação cruzada não sai: `aviso_radar` de atraso.
**Deu certo quando:** Fila esvaziou sozinha; nada duplicado; nenhuma avaliação > 24 h nem pergunta > 4 h; `incidentes/AAAA-MM-DD-api.md`.
**Se deu errado:** Fila não esvazia: 400 (API mudou) ou 401/403. Cota estoura todo dia 1: lotes (02h, 02h30, 03h).

### VIII.5 Runbook: número da casa com qualidade baixa
**O que é:** A Meta rebaixou qualidade ou limite do número da casa.
**Antes:** Gerenciador → **Números de telefone**; `deliveries`; `wa.inbound` com SAIR.
**Passos:** 1) Anote qualidade e limite; opt-outs em 30 dias ÷ donos ativos, > 2% é nosso; `deliveries` por modelo, dono e hora: `aviso_radar` > 1/semana, fora de horário (Boletim 7h segunda; dia 1 até 8h; o resto 8h–19h). 2) Pause `aviso_radar` por 7 dias; corrija hora e texto; SAIR respeitado na hora; cliente segue pelo dashboard. 3) Vermelho: **Solicitar revisão** (número único, só clientes pagantes, só serviço contratado, opt-out por uma palavra); faixa no dashboard; religue 25/50/100% em três dias.
**Deu certo quando:** Verde; opt-outs < 2%; Boletim seguinte com `lido_em` na maioria; `incidentes/AAAA-MM-DD-numero-da-casa.md`.
**Se deu errado:** Bloqueio permanente: segundo número na mesma WABA, modelos de novo, `DELIVERY_SENDER_PHONE_ID` novo; só com o Head. Queda sem opt-out: spam na primeira mensagem; confira nome de exibição.

### VIII.6 Runbook: offboarding
**O que é:** O cliente cancelou; a máquina se retira, devolve tudo, apaga no prazo e libera a vaga.
**Antes:** Cancelamento registrado e data de fim do ciclo; ficha, segredos, Storage, BigQuery.
**Passos:** 1) `closing` com a data; até lá tudo continua; no dia, `offboarding(tenant)`: Fechamento de encerramento com a série desde o Dia 0. 2) `business.google.com` → perfil → **Usuários** → conta operacional → **Remover**; `deliveries` fecha; ZIP com link assinado de 30 dias (Diário em CSV com prints, PDFs, cards, mapas, fotos, posts, respostas, métricas). 3) Desative `tenant-{id}-gbp-oauth`; `zones.tenants_ativos` − 1 no mesmo dia; `zone.changed`; comercial chama o primeiro da lista; `closed` com data; `offboarding/AAAA-MM-DD-tenant.md`.
**Deu certo quando:** Fechamento e ZIP entregues; conta fora de **Usuários**; segredos desativados; vaga livre e publicada; `closed`; perfil intacto.
**Se deu errado:** Quer voltar: `reopen(tenant)` dentro da retenção; acessos e vaga de novo. Conta não sai do perfil: registre, avise por escrito, desative o segredo.

## Capítulo IX · Segurança e LGPD

### IX.1 Pedido de titular
**O que é:** Avaliador, autor de pergunta ou dono pede para ver ou apagar dados; 15 dias.
**Antes:** Pedido por escrito (`radarurbano.com.br/privacidade`); link ou texto exato; do dono, mensagem do número cadastrado; `dsr(tenant, hash)`.
**Passos:** 1) Identidade com o mínimo; `dsr` procura em `reviews.texto_hash`, `questions.texto_hash`, `tenants.dono_wa_hash`, `actions_log.alvo`; ver: `modo='exportar'` → PDF. 2) Apagar terceiro: hash vira marcador, temas e sentimento limpos; ficam data, nota, `respondida_em`; resposta pública apagável por `reviews.reply`, com aviso à empresa; prints ficam. 3) Apagar dono: offboarding; apague `dono_nome`, `dono_wa_hash`, `tom_json`, transcrição, áudios; `actions_log` fica; registre em `lgpd/pedidos/AAAA-MM-DD-tenant.md`; avise o cliente (controlador).
**Deu certo quando:** < 15 dias com registro; consulta pelo hash vazia; cliente avisado.
**Se deu errado:** Não aponta a avaliação: sem texto não há hash. Quer apagar a resposta e a empresa não: decisão dela.

### IX.2 Suboperadores e retenção
**O que é:** Quatro suboperadores: Google Cloud e APIs; Meta (só o número da casa); provedor do cérebro de linguagem; provedor de pagamento.
**Antes:** `radarurbano.com.br/suboperadores` e `/privacidade` com data; BigQuery, Storage, Firestore; Terraform; jurídico trimestral.
**Passos:** 1) Página com nome, país, finalidade e o que cada um recebe; data a cada mudança; uma linha aos clientes na entrega seguinte. 2) Retenção: `actions_log` e prints 5 anos · dados do tenant (`reviews`, `questions`, `rank_measurements`, métricas, `posts`, `deliveries`, arquivos) e do dono: contrato + 90 dias · respostas brutas da Places 30 dias · áudios do Dia 0 apagados após a confirmação por escrito · `llm_calls` e `qa_samples` 12 meses · ZIP 30 dias · contrato e nota fiscal pelo prazo da lei. 3) Expiração de partição no BigQuery; ciclo de vida por prefixo no Storage; job dos 90 dias após `closed`; revisão trimestral em `lgpd/revisoes/AAAA-Tn.md`.
**Deu certo quando:** Página com data; expiração em cada tabela; ciclo de vida em cada bucket; job dos 90 dias com log diário.
**Se deu errado:** Tabela "Nunca": console e Terraform. Ferramenta nova recebendo texto sem passar por aqui: incidente; pare.

## Capítulo X · O plano de montagem

### X.1 O quadro das seis semanas
**O que é:** Seis colunas com "pronto quando" e uma linha vermelha no topo com as aprovações de terceiros (Business Profile APIs; Meta e número da casa; modelos): o caminho crítico.
**Antes:** Quadro; capítulo X do Mapa Mundi; III.2 e III.7 lidos; engenheiro, Head, jurídico na S6.
**Passos:** 1) Linha vermelha com data de envio e de resposta de cada pedido; reunião de 15 min em pé toda segunda, com evidência. 2) Sem Google: sandbox e bicicletas (S3 não depende); sem Meta: número de teste, 250 donos/dia bastam; S5: `zones` é a verdade antes de qualquer venda. 3) Quadro: S1 fundação e pedidos (`terraform apply` sobe os dois ambientes; três pedidos com data) · S2 conectores, LLMGateway, Diário, custo (busca devolve posição; toda chamada em `llm_calls`) · S3 Cartógrafo, Tesoureiro, dashboard, Diagnóstico (validação ≥ 85%; Diagnóstico em minutos após `gbp_linked`) · S4 Editor, Anfitrião, Guardião em planilha, Antes e Depois (tenant interno uma semana com print; 100 itens em < 90 min) · S5 Redator-chefe, TTS, Delivery, webhooks, extratos, Dia 0 e Dia 7 automáticos, `zone.check` (Boletim sintético às 7h; Dia 0 cronometrado; terceira empresa recusada) · S6 runbooks, SLOs, offboarding, jurídico, alerta de R$ 25, piloto com 3 clientes por 30 dias em P0.
**Deu certo quando:** 11 testes de aceitação passam; Dia 0 ≤ 15 min com três pessoas novas; piloto fecha um mês com as 11 entregas e custo < R$ 25; ninguém tem senha de ninguém; nenhuma zona com mais de 2.
**Se deu errado:** S4 sem Google: siga em sandbox. S5 sem Meta: 250 donos/dia.

## Glossário

| Termo | Definição |
|---|---|
| ADK | Kit do Google, em Python, para montar agentes. |
| Agente | Programa com missão que pensa com IA e usa ferramentas; cinco, mais um humano com painel. |
| Cache de contexto | Guardar no Gemini o que não muda para não pagar de novo. |
| Cérebro | Modelo de IA; Gemini para dado e Google, outro só para linguagem. |
| Conector | Programa que fala com um sistema de fora; quatro, mais o Render & Delivery. |
| Contato | Toque em Ligar, rota, clique no site ou mensagem pelo perfil, contados pelo Google. Nunca ligação atendida. |
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
