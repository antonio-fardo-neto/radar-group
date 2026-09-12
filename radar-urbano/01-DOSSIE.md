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
2. **LGPD.** Dados do dono: nome e número. Textos públicos de terceiros tratados só para responder em nome da empresa, guardados como hash e temas. Nenhuma mensagem a clientes finais. Suboperadores: Google Cloud e APIs, Meta (número da casa), provedor do cérebro de linguagem, provedor de pagamento. Retenção: `actions_log` 5 anos; `llm_calls` 12 meses; dados do tenant durante o contrato + 90 dias; áudio do Dia 0 apagado 7 dias após confirmação por escrito.
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
