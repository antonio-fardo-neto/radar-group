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

Do original ficam o TAM e o SAM; o SOM é recalculado pela trava territorial.

| Camada | Número | Origem |
|---|---|---|
| TAM | 15 milhões de CNPJs ativos em comércio, alimentação, saúde de bairro, serviços locais e oficinas | Dossiê original |
| SAM | 3,5 milhões de estabelecimentos em capitais e cidades médias com dependência de fluxo físico | Dossiê original |
| SOM | Vagas = zonas × segmentos × 2, por praça | Recalculado abaixo |

### A conta do SOM

O Radar Urbano atende no máximo duas empresas por segmento (categoria principal do Google) por zona (bairro do Maps ou raio equivalente). O mercado obtível não é uma fração do SAM; é a soma das vagas.

| Variável | Hipótese por praça | Nota |
|---|---|---|
| Zonas com densidade comercial | 40 a 80 bairros | Cidade grande ou região metropolitana; cidade média tem 15 a 30 |
| Segmentos com demanda de busca | 25 a 40 | Padaria, pizzaria, oficina, dentista, pet shop, salão, etc. Segmentos diferentes não competem entre si |
| Vagas por zona e segmento | 2 | Trava fixa |
| Vagas teóricas por praça | 2.000 a 6.400 | 40×25×2 a 80×40×2 |
| Ocupação realista | 15% a 25% | Nem todo segmento existe em todo bairro; nem toda empresa compra |
| **Clientes obtíveis por praça** | **300 a 1.600** | Projeção |

Consequências: 2.000 clientes exigem de 2 a 6 praças abertas; 10.000 clientes exigiriam 8 a 30 praças e não são um estágio deste dossiê. O crescimento é por abertura de praça, não por saturação de uma só. A trava também é argumento de venda: o cliente sabe que o vizinho do mesmo segmento não entra.

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
| Contrato | Mensal, cancelável, sem fidelidade abusiva |
| Trava territorial | Máximo 2 empresas por segmento por zona. Cláusula de exclusividade limitada no contrato |
| Reserva de vaga | Conversa não reserva; proposta escrita reserva por 5 dias úteis; a vaga ocupa na assinatura (transação em `zones`) |
| Fila | Ordem de chegada, sem exceção. Zona lotada vai para lista de espera |
| Dia 0 | Até 15 minutos cronometrados: cinco perguntas por áudio, Gerente no Perfil da Empresa, link do dashboard, Diagnóstico na mesma conversa. O roteiro real fecha em cerca de dez; os cinco restantes são folga |
| Acessos | Papel Gerente no perfil; nunca a senha do cliente; WhatsApp do dono só recebe; SAIR interrompe |
| Cobrança | Cartão recorrente no provedor de pagamento antes do Dia 0 |

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
| Custo de tecnologia | R$ 12 a 25 | Gemini R$ 3–5 · linguagem R$ 2–4 · Places R$ 3–8 · WhatsApp da casa R$ 1–2 · TTS, Cloud Run, BigQuery, Storage R$ 3–6. Alerta em R$ 25 |
| Meio de pagamento | R$ 15 | 3% de cartão recorrente (hipótese) |
| Custo de operação (Guardião) | R$ 200 → R$ 75 → R$ 43 | Operador a R$ 6.500/mês all-in dividido por 30, 80 e 150 clientes (hipótese de salário) |
| Impostos sobre receita | R$ 30 a 70 | Simples Nacional ou Lucro Presumido, 6% a 14% (hipótese) |
| **Margem de contribuição** | **R$ 190 a 340** | **38% a 68%, subindo com o patamar do Guardião** |

Hipóteses de aquisição e retenção (não são metas; são premissas de cenário):

| Indicador | Valor | Conta |
|---|---|---|
| Churn | 5% ao mês | Retenção média de 20 meses |
| LTV bruto | R$ 9.980 | 20 × 499 |
| LTV de contribuição | R$ 3.800 a 6.800 | 20 × margem de contribuição |
| CAC | R$ 1.000 a 1.500 | SDR por praça, comissão de canal, proposta com diagnóstico; sem tráfego pago |
| LTV bruto / CAC | 6,7× a 10× | |
| Payback do CAC | 3 a 8 meses de contribuição | Depende do patamar do Guardião |

Manter uma base estável de N clientes com churn de 5% exige vender 0,05 × N por mês só para repor: 5 vendas/mês em 100 clientes, 100 vendas/mês em 2.000.

## 8. Estágios (cenários, não metas)

MRR = clientes × R$ 499. Custos fixos e salários são hipóteses. Valuation e múltiplo de ARR do original: removidos; se algum dia for preciso, a única linha aceitável é "SaaS B2B de ticket fixo com churn medido; múltiplo a definir com base auditada".

| | 100 clientes | 500 clientes | 2.000 clientes |
|---|---|---|---|
| Praças | 1 | 1 a 2 | 3 a 6 |
| MRR | R$ 49.900 | R$ 249.500 | R$ 998.000 |
| Patamar do Guardião | P0/P1 · 30 por operador | P2 · 80 por operador | P2 · 150 por operador |
| Equipe | Head de Operação (também Guardião) · 1 engenheiro · 2 Guardiões · 1 SDR · jurídico e contabilidade externos | Head de Operação · 2 engenheiros · 7 Guardiões · 3 SDR · admin · jurídico e contabilidade externos | Head de Operação · 2 coordenadores · 4 engenheiros · 14 Guardiões · 8 comerciais · 3 admin/financeiro · jurídico externo |
| Custos fixos (folha, pró-labore, externos, ferramentas) | R$ 47.500 | R$ 120.000 | R$ 346.000 |
| Tecnologia (R$ 25/cliente, teto) | R$ 2.500 | R$ 12.500 | R$ 50.000 |
| Meio de pagamento (3%) | R$ 1.500 | R$ 7.500 | R$ 30.000 |
| Impostos | R$ 5.000 (Simples, ~10%) | R$ 35.000 (Presumido, ~14%) | R$ 140.000 (~14%) |
| **Resultado operacional** | **− R$ 6.600** | **R$ 74.500** | **R$ 432.000** |
| **Margem** | **negativa** | **~30%** | **~43%** |
| Vendas/mês para repor churn | 5 | 25 | 100 |

Leitura:

- **100 clientes** valida a operação, não paga a equipe. Ponto de equilíbrio com essa estrutura fica em torno de 115 a 130 clientes (custos fixos ÷ contribuição de ~R$ 409 por cliente). Até lá é investimento dos sócios.
- **500 clientes** é a primeira estrutura que se sustenta com folga; a margem depende de o Guardião estar no P2 (80 por operador) e do custo de tecnologia abaixo de R$ 25.
- **2.000 clientes** exige de 3 a 6 praças abertas e um time comercial que reponha 100 clientes por mês. A margem sobe porque o Guardião chega a 150 por operador e a engenharia não cresce na proporção da base.
- Um estágio de 10.000 clientes não cabe neste dossiê: seriam 8 a 30 praças e um modelo de expansão geográfica que não está desenhado.

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
| GBP Connector | Business Information, Performance, avaliações, posts, mídia, Q&A | OAuth 2.0, conta operacional com papel Gerente, `business.manage` |
| Places Connector | `places:searchText` com `locationBias` por ponto da grade | Chave restrita; cache 30 dias; só `place_id` fica |
| WA Connector | Número da casa, só para falar com o dono | Cloud API; modelos `boletim_segunda`, `entrega_radar`, `pergunta_sim_nao`, `aviso_radar` |
| TTS Connector | Áudio do Boletim, ≤ 60 s | Cloud Text-to-Speech, Chirp 3 HD pt-BR |
| Render & Delivery | Cards PNG, Mapa SVG, PDFs, dashboard Next.js, envio com status e reenvio após 2 h | Cloud Run |

Contagem: "cinco agentes e um humano com painel"; "quatro conectores e um serviço de entrega". Sem Google Ads API, telefonia ou WhatsApp do cliente.

## 10. Retenção

O que segura o cliente:

- **Entrega toda semana e todo mês, sem pedir nada.** Boletim na segunda às 7h, cinco entregas no dia 1. O dono não precisa abrir nada para saber que a máquina trabalhou.
- **Custo por contato visível.** O Extrato mostra R$ 499 ÷ contatos do mês e diz de onde vem cada número. A conta de valor fica com o dono, com os números na mão.
- **Horas Devolvidas.** Catorze horas por R$ 499 é a comparação com contratar alguém.
- **Diário de Bordo com print.** Tudo que foi feito no perfil está registrado; a dúvida "o que vocês fazem?" tem resposta em uma tela.
- **Cancelar custa mais que ficar.** Ao sair, o perfil volta a ficar parado (avaliações sem resposta, feriado errado), a vaga da zona libera para o concorrente da fila, e a reentrada depende de a vaga existir.
- **Sinais de risco tratados antes do cancelamento:** perfil sem avaliação nova por 30 dias, dono que não abre o Boletim, queda de posição em termo-chave, custo por contato subindo dois meses seguidos. O Head de Operação recebe a lista mensal.

Win-back do original reduzido a uma regra: ex-cliente volta pela fila da zona, sem condição especial.

## 11. Riscos e mitigação

| Risco | Efeito | Mitigação |
|---|---|---|
| Mudança do Google (algoritmo, políticas, APIs) | Medição perde validade; ações do Editor deixam de valer | Só diretrizes oficiais; validação mensal da grade com 20 buscas manuais; método declarado no rodapé do Mapa; nenhuma promessa de posição |
| Suspensão ou verificação pendente do perfil | Nenhuma ação possível; entregas param | Detecção de `SUSPENDED`/`PENDING_VERIFICATION` no conector; runbook de recurso; onboarding não bloqueia (`gbp_pending_verification`); aviso ao dono em uma linha |
| Cota, erro ou preço da API do Google (Places, GBP, Vertex) | Medição incompleta; custo por tenant acima de R$ 25 | Máscara mínima de campos; grade reduzida na semana e completa só no dia 1; alerta `cost.alert` a R$ 25; runbook de API parada; retry idempotente |
| Dependência da aprovação das Business Profile APIs | Sem aprovação, não há Editor, Anfitrião nem Tesoureiro | Pedido no dia 1 da montagem (1–2 semanas); enquanto espera, Cartógrafo e Places funcionam; conta operacional com papel Gerente, nunca senha |
| LGPD | Reclamação de titular; incidente com dados do dono | Dados do dono: nome e número (hash com sal); textos de terceiros como hash e temas; nenhuma mensagem ativa a clientes finais; retenção definida; pedido de titular com runbook |
| Número da casa com qualidade baixa na Meta | Modelos bloqueados; entregas não chegam | Só modelos de Utilidade; SAIR respeitado na hora; horário comercial para avisos; monitor de opt-out; reenvio pelo dashboard |
| Modelo de IA fora do ar ou degradado | Respostas atrasam; Boletim não sai | `LLMGateway` com fallback de linguagem; avaliações têm fila de 24 h; números nunca dependem de modelo |
| Erro público (resposta errada a avaliação, categoria errada) | Dano à reputação do cliente | Dois olhos para notas ≤ 2, categoria, nome e endereço em qualquer patamar; QA de 10%; Diário com print para corrigir e provar |
| Zona lotada com pedido de venda | Comercial vende o que não pode entregar | `zone.check` antes de qualquer proposta; lista de espera por ordem de chegada; cláusula de zona no contrato |
| Concentração em uma praça | Um evento local derruba a base | Abertura de segunda praça a partir de 300 a 500 clientes |

## 12. Jurídico e LGPD

Pauta para o advogado externo, oito itens do contrato:

1. **Mandato de operação.** O que a máquina faz sem perguntar (posts, fotos, horários, respostas a avaliações e perguntas, ajustes de campos); o que exige um Sim (categoria principal, nome, endereço, ofertas); o que nunca faz (prometer posição ou resultado, incentivo por avaliação).
2. **LGPD.** Dados do dono: nome e número. Textos públicos de avaliações e perguntas tratados apenas para responder em nome da empresa, armazenados como hash e temas. Nenhuma mensagem ativa a clientes finais. Suboperadores: Google Cloud e APIs, Meta (só o número da casa), provedor do cérebro de linguagem, provedor de pagamento. Retenção: `actions_log` 5 anos; `llm_calls` 12 meses; dados do tenant durante o contrato + 90 dias; áudio do Dia 0 apagado 7 dias após a confirmação por escrito.
3. **Política de avaliações e conteúdo do Google.** Sem incentivo, sem seleção, respostas verdadeiras, sem dados do avaliador.
4. **Marca, fotos e imagem.** O cliente autoriza uso das fotos reais; nunca se gera foto do estabelecimento.
5. **Preços, horários e informações comerciais.** Responsabilidade do cliente; origem de cada dado registrada no Diário.
6. **Exclusividade limitada por zona.** No máximo dois do mesmo segmento na mesma zona; como a zona é definida (bairro do Maps ou raio, com cidade e segmento no contrato); o que acontece se o cliente muda de endereço ou categoria (mantém até o fim do ciclo pago, entra na fila da zona nova).
7. **Limitação de responsabilidade.** A promessa é a operação medida e registrada, não o resultado.
8. **Reversibilidade e encerramento.** Remoção do Gerente, entrega do histórico, exclusão de dados no prazo, liberação da vaga na zona.

Tributário: Simples Nacional no início; Lucro Presumido quando a receita exigir. Sem holding internacional neste dossiê.

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
| 1 | Fundação Google Cloud; pedido de acesso às Business Profile APIs; verificação da empresa na Meta e número da casa; contrato com o advogado (8 itens) | Pedidos protocolados; projetos `radar-hml` e `radar-prd` no ar |
| 2 | Conectores GBP e Places; `LLMGateway`; Diário de Bordo; custo por tenant | Uma medição de grade e um `locations.get` gravados com print |
| 3 | Cartógrafo, Tesoureiro, Dashboard, Diagnóstico de Posição | Diagnóstico gerado para um perfil de teste em minutos |
| 4 | Editor, Anfitrião, Guardião (planilha → painel), Antes e Depois | Avaliação de teste respondida em < 2 h com aprovação no painel |
| 5 | Redator-chefe, TTS, Delivery pelo número da casa, Boletim, extratos e PDFs, onboarding automático, `zone.check` | Boletim de segunda entregue no WhatsApp com áudio ≤ 60 s |
| 6 | Endurecimento: runbooks, SLOs, offboarding, alerta de custo; cronometrar o Dia 0 | Os 11 testes de aceitação passam; Dia 0 em até 15 minutos |
| 7 a 10 | Piloto com 3 clientes (padaria, oficina, clínica) por 30 dias; primeira praça definida; lista de alvos por zona e segmento com `zone.check` | Um mês fechado com as 11 entregas; custo por tenant < R$ 25; nenhuma zona com mais de 2 do mesmo segmento |
| 11 a 13 | Abertura comercial na primeira praça: SDR, canal de contabilidades, proposta com diagnóstico reduzido; meta de ritmo, não de volume | 20 a 30 clientes ativos; churn e CAC medidos de verdade pela primeira vez; economia unitária da seção 7 revisada com dado real |

Definição de "montei": os 11 testes de aceitação passam; o Dia 0 leva até 15 minutos cronometrados; o piloto fecha um mês com as 11 entregas e custo por tenant abaixo de R$ 25; ninguém tem senha de ninguém; nenhuma zona com mais de 2 tenants do mesmo segmento.
