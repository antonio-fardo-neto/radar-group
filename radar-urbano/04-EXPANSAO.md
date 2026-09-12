# Radar Urbano · Expansão

Duas dimensões de crescimento, independentes: (A) mais zonas, praças e clientes do produto único; (B) mais módulos ligados por tenant. A primeira não depende da segunda. A trava de 2 empresas por segmento por zona vale nas duas.

## Parte A · Expansão geográfica e comercial

### A1. A unidade de expansão

- Unidade: **zona × segmento**, com **2 vagas**.
- Zona = bairro do Google Maps ou raio equivalente, gravado no contrato com cidade e segmento. Não é a sobreposição de grades de medição.
- Segmento = categoria principal do perfil no Google (padaria e pizzaria são segmentos diferentes).
- Vaga se reserva pela proposta escrita (5 dias úteis) e se ocupa na assinatura, em transação na tabela `zones`. Fila por ordem de chegada, sem exceção.
- Consequência: a receita máxima de uma praça é finita e conhecida antes de vender. Crescer é abrir zonas e segmentos novos, não vender mais na mesma vaga.

### A2. Capacidade por praça

Fórmula: **vagas = zonas × segmentos relevantes × 2**. Segmentos relevantes são os que têm demanda local por busca e ao menos 2 perfis fracos na zona (levantado por dados públicos antes de abrir a praça).

Exemplo (números redondos, só para ilustrar):

| Variável | Valor de exemplo |
|---|---|
| Zonas na cidade (bairros com busca local relevante) | 40 |
| Segmentos relevantes por zona | 12 |
| Vagas teóricas (40 × 12 × 2) | 960 |
| Ocupação realista (nem toda zona tem 2 candidatos em cada segmento) | 30–50% |
| Clientes alcançáveis na praça | 300–480 |
| Receita mensal no teto realista (× R$ 499) | R$ 150 mil – R$ 240 mil |

Regras da estimativa:

- Contar bairros pelo Maps, não pelo IBGE; bairro sem busca local ("perto de mim" sem volume) não conta.
- Segmentos por família de exemplo: alimentação (padaria, pizzaria, restaurante, açaí), automotivo (oficina, funilaria, borracharia, auto elétrica), saúde (dentista, fisioterapia, clínica médica, pet shop/veterinária). Cada um é uma categoria principal distinta.
- A estimativa é refeita a cada 100 clientes com os dados reais de `zones` (zonas lotadas, zonas vazias, fila).

### A3. Sequência de crescimento

| Estágio | Clientes | Onde | O que prova | Gatilho para o próximo |
|---|---|---|---|---|
| Piloto | 3 (padaria, oficina, clínica) | Praça piloto | 11 entregas por 30 dias; Dia 0 em até 15 min; custo por tenant < R$ 25; Guardião em P0 | 11 testes de aceitação passando |
| Tração | 20 | Mesma praça | Onboarding sem engenheiro; Guardião em P1 (> 85% aprovado sem edição); canais de aquisição com custo conhecido | 20 clientes vivos por 60 dias, churn conhecido |
| Praça | 100 | Mesma cidade | 1 operador para 80 clientes; P2 com QA de 10%; runbooks usados de verdade | Critérios de abertura de praça (abaixo) |
| Segunda praça | 100 → 200+ | Cidade nova | O mesmo roteiro repetido sem o fundador; tabelas por cidade funcionando | Repetir |

Critérios para abrir praça nova (todos, não um):

1. Taxa de zonas lotadas na praça atual acima de 40% nos segmentos-alvo, ou fila de espera maior que 10 tenants.
2. Operadores com folga: pelo menos 1 Guardião abaixo de 60% da capacidade do estágio.
3. Custo de tecnologia por tenant estável abaixo de R$ 25 por 3 meses.
4. Churn mensal abaixo de 5% nos últimos 3 meses.
5. Levantamento de capacidade da cidade nova feito (A2) com ao menos 200 vagas realistas.
6. Calendário municipal, fuso e `zones` da cidade nova carregados antes da primeira proposta.

### A4. Equipe por estágio

| Papel | Piloto (3) | 20 | 100 | 500 (várias praças) |
|---|---|---|---|---|
| Head de Operação | 1 | 1 | 1 | 1 |
| Engenheiro de automação | 1 | 1 | 1 | 2 |
| Guardiões / operadores | 1 (o Head) | 1 | 2 (80 clientes/operador) | 4 (150 clientes/operador) |
| Comercial / SDR | fundador | 1 | 2 | 1 por praça |
| Jurídico | externo | externo | externo | externo |

Notas:

- A razão clientes/operador sobe 30 → 80 → 150 porque não há atendimento em tempo real; o operador aprova lote, audita amostra e trata exceção.
- O SDR faz a verificação de zona antes de qualquer proposta e o onboarding assistido do Dia 0; não vende para zona lotada.
- Cada praça nova exige um SDR local ou parceiro local; operação e engenharia continuam centralizadas.

### A5. Canais de aquisição por praça

| Canal | Como funciona | Custo e observações |
|---|---|---|
| Outbound geolocalizado por dados públicos | Levantar perfis fracos por zona e segmento (categoria errada, sem fotos, sem horário de feriado, avaliações sem resposta, nota baixa) usando a Places API dentro dos termos e consulta manual; abordagem com um Diagnóstico de Posição reduzido | Só `place_id` armazenado por mais de 30 dias; nada de raspagem; lista de abordagem morre em 30 dias |
| Contabilidades | Parceria com escritórios contábeis da praça: indicação de clientes por segmento | Comissão de indicação; o contador recebe nada além do que o cliente encaminha ("segue o mês") |
| Associações e sindicatos de segmento | Palestra ou material com a trava de 2 por zona como argumento (escassez real) | Custo baixo; funciona por segmento, não por bairro |
| Indicação de cliente | Vaga da zona vizinha oferecida ao cliente que indica | Só se a zona indicada estiver livre; sem desconto que quebre o preço fixo |
| Material do balcão | QR e link curto de avaliação levam a marca; a página pública explica o produto | Passivo; mede-se por contatos, não por conversão |

Argumento de venda em todos os canais: contagens, custo por contato e o Diário de Bordo. Nunca conversão, receita ou "novos clientes".

### A6. O que muda na máquina ao crescer

| Peça | Hoje (uma praça) | Com várias praças |
|---|---|---|
| `zones` | `zones(segmento, zona, cidade, tenants_ativos, limite=2)` | Mesma tabela; `cidade` vira chave obrigatória; auditoria diária por cidade (zero linhas com mais de 2 ativos) |
| Tabela de cidades | Implícita | `cities(cidade, uf, fuso, ativa, aberta_em)`; `tenants` ganha `cidade`; `zone.check(segmento, zona, cidade)` |
| Calendário de feriados | Tabela nacional + municipal da praça piloto | Uma linha por cidade e data; carregar o calendário municipal antes de abrir a praça; `calendar.holidays(cidade, de, ate)` já recebe cidade |
| Fuso horário | Tudo em horário de Brasília | `cities.fuso`; Boletim às 7h locais; janela de `aviso_radar` e `pergunta_sim_nao` das 8h às 19h locais; jobs internos (03h coleta, 05h horários) continuam em Brasília |
| Grade de medição | Raio do cliente | Sem mudança; a grade é por tenant, não por cidade |
| Guardião | Uma fila | Fila com filtro por cidade e por operador; cada operador tem praças atribuídas |
| Custo por tenant | Média geral | `cost.per_tenant` agrupado também por cidade; praça com custo acima de R$ 25 entra no runbook antes de crescer |
| Cotas de API | Uma chave Places, um OAuth GBP | Mesmas credenciais; monitorar cota por dia; pedir aumento de cota ao Google a cada 100 clientes |
| Modelos da Meta | Um número da casa | Um número da casa serve todas as praças; segundo número só se a qualidade cair (runbook) |
| Comercial | Verificação de zona manual pelo SDR | Painel de disponibilidade por cidade/zona/segmento, lido de `zones`, com fila |

Nada disso altera agentes, entregas ou preço. É configuração e tabela.

## Parte B · Expansão por módulos

### B1. As fases

| Fase | Módulo | O que devolve ao cliente | Acesso novo do cliente | Pré-requisito / caminho crítico | Preço | Montagem | O que muda nos documentos |
|---|---|---|---|---|---|---|---|
| 0 | Radar Urbano (núcleo) | 11 entregas, 5 agentes + Guardião, 4 conectores | Gerente no perfil, WhatsApp do dono, cartão | Business Profile APIs (1–2 semanas); Meta para o número da casa | R$ 499 | 6 semanas + piloto 30 dias | Nenhum: são os documentos atuais |
| 1 | Radar Concorrência + Radar Menu | Card "Quem ganhou a semana" (sábado 9h); Sentinela como agente (feriado, clima, pico de busca, concorrente); comparação nominal no Mapa de Domínio; catálogo com preço publicado; "O que te procuram" no dia 1 | Nenhum (3 concorrentes e uma lista de itens, por áudio) | Núcleo vivo com Cartógrafo aprovado (85% com as 20 buscas); lista de ações autorizadas por tenant; jurídico em 3 frases | R$ 399 + R$ 399 | 3 semanas + piloto | Entregas: 2 seções novas; 05 e 07 ganham comparação. Acessos: 3 frases e 2 perguntas. Mundi: Sentinela, `places.get_details`, clima, 2 tabelas. Bíblia: capítulos XI e XII |
| 2 | Radar Stars | Convite de avaliação após atendimento pelo WhatsApp da empresa; Boletim de Reputação com convites (contagens) | Sistema E: WhatsApp da empresa (Meta, Embedded Signup, número dedicado) | Cadastro como Tech Provider na Meta (dias a semanas, pedido no dia 1); verificação da empresa do cliente; jurídico item 3 | R$ 299 | 3 semanas + piloto | Acessos: Sistema E, itens 2, 3 e 8, passo "minuto 10 a 14". Mundi: WA Connector com 2 metades, estados `wa_linked`. Bíblia: capítulo XIII |
| 3 | Radar Chat | Recepcionista 24/7, Agenda das 7h, número de rastreamento, Resgate de Ligações Perdidas; dashboard em tempo real; "pediu preço" e "horários marcados" no Extrato | Sistema F: telefonia (linha da empresa) + Sistema E | Fase 2; provedor de telefonia (cadastro regulatório, números por DDD); teste em 3 operadoras; jurídico itens 1, 2, 3, 8 | R$ 499 | 4 semanas + piloto | Entregas: 3 seções, 03 e 08 redefinidos. Acessos: Sistema F. Mundi: Recepcionista, Voice Connector, 3 tabelas, SLO de latência; Guardiões caem para 20→60→120. Bíblia: capítulo XIV |
| 4 | Radar Ads | Micro-campanhas de busca com raio e teto; Extrato de Mídia com custo por contato por campanha; corte automático | Sistema G: Google Ads (conta do cliente, vinculação à MCC) | Fundação Telefonia da Fase 3 (atribuição); developer token (dias a semanas); limiares por segmento; verificação de anunciante | R$ 699 (verba do cliente à parte) | 3 semanas + simulação 31 dias + piloto | Entregas: Extrato de Mídia, 11 ganha linha. Acessos: Sistema G, itens 1 e 7. Mundi: Estrategista, Ads Connector, Google Ads API. Bíblia: capítulo XV |
| 5 | Suíte | Os 5 módulos num contrato; proposta automática de expansão no 3º Fechamento (conta de equilíbrio, não previsão); custo por módulo | Sistemas A a G, contrato com anexos | Os 5 pilotos fechados; provedor de pagamento com bundle; 1 trimestre de um tenant com tudo | R$ 1.500–2.200 | 2 semanas + piloto de 1 trimestre | Acessos: contrato em anexos, encerramento por módulo. Mundi: 8 agentes, custo por módulo. Bíblia: VII.4, VIII.7, VIII.8 |

Calendário sequencial com 1 engenheiro: 44 semanas depois do núcleo (cerca de 1 ano do dia 1). Com 2 engenheiros e montagem da fase seguinte durante o piloto da anterior: cerca de 9 meses. Venda de módulo só com piloto fechado.

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
2. Cada módulo traz as próprias peças com o próprio nome (`competitor_snapshots`, `invites`, `calls`, `campaigns`, `tenant-{id}-waba-token`).
3. Cada módulo traz os próprios acessos (sistemas E, F, G) e cláusulas (anexos do contrato); o Dia 0 ganha um passo dentro dos mesmos 15 minutos.
4. As 11 entregas do núcleo não são renumeradas; entregas de módulo têm nome e aparecem no Dashboard, Boletim e Fechamento só quando o módulo está ligado.
5. Compartilhado: LLMGateway, Diário de Bordo (coluna `modulo`), Guardião (uma fila por risco), número da casa, Dashboard, Tesoureiro (`llm_calls.modulo`, custo por módulo), Cartógrafo (uma medição serve Mapa, Concorrência e Ads), trava de zona.
6. Cada fase fecha com piloto de 30 dias nos 3 clientes do núcleo, Guardião em P0 para o módulo novo.
7. Desligar um módulo remove só os acessos, segredos e cadências dele e exporta o histórico. Não existe módulo sem núcleo.

### B3. Dependências

| Módulo | Depende de | Deixa pronto para | Pode inverter com |
|---|---|---|---|
| Concorrência | Núcleo (Cartógrafo, Places, Editor, Delivery) | `top_place_ids` no Mapa; sinais para o Editor | Qualquer um |
| Menu | Núcleo (Editor, GBP Connector, Guardião) | Itens de catálogo para o cross-sell e termos do Ads | Qualquer um |
| Stars | Núcleo (Anfitrião) + Fundação Meta para clientes | A Fundação Meta, que o Chat usa inteira | Chat (se vier depois dele, cai para 1 semana) |
| Chat | Núcleo + Fundação Meta + Fundação Telefonia | `calls`, `conversations`, número de rastreamento (Ads), evento `atendimento.concluido` (Stars) | Stars; nunca depois do Ads |
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

1. Nenhuma métrica de conversão, receita atribuída, "novos clientes" ou ROI. Só contagens e custo por contato (por campanha, no Ads; conta de equilíbrio na proposta de expansão).
2. Gemini para dados, medição, classificação e tudo que toca API do Google (Sentinela, Recepcionista e Estrategista incluídos). Outros cérebros só para linguagem, atrás da LLMGateway.
3. Nunca a senha do cliente: Gerente no perfil, Embedded Signup com código digitado pelo cliente, vinculação por convite na MCC, cartão no provedor.
4. Zero tempo do dono; os únicos minutos são no Dia 0, que com a suíte usa os 15 inteiros.
5. Diário de Bordo append-only com print, uma tabela, coluna `modulo`.
6. Custo por tenant como métrica de primeira classe: alerta R$ 25 + acréscimos declarados, até R$ 40.
7. Trava de 2 por segmento por zona, verificada antes da venda e em código, para a suíte inteira; nenhum módulo compra exceção.
8. Sem raspagem do Google: Places API dentro dos termos, snapshots de 30 dias, só `place_id` fica.
9. Só avaliações reais: convite após atendimento real, com consentimento, sem incentivo, sem seleção.
10. Frescor honesto: dados do Google com data de referência; dado próprio em até 1 hora; tempo real só onde existe (chamadas e conversas, a partir do Chat).
