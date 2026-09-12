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
