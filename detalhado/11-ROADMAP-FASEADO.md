<!-- Radar Urbano · O Roadmap Faseado: a regra da modularidade, o mapa das fases (0 a 5), uma seção por fase (Concorrência e Menu, Stars, Chat, Ads, a suíte), dependências e ordem alternativa, o que não muda em nenhuma fase. Menos profundo que os quatro documentos principais; completo o bastante para decidir a ordem e montar. Fonte: 11-ROADMAP-FASEADO.md, gerado por src/build.py -->

# RADAR URBANO: O ROADMAP FASEADO

*Os outros cinco pilares do dossiê, em fases e por módulo: o que cada um adiciona ao núcleo, o que pede do cliente, o que custa, em que ordem entra, quando está pronto e o que nunca muda.*

*Capítulo I · A regra da modularidade*

## UM NÚCLEO, CINCO MÓDULOS, UMA REGRA

O núcleo é o Radar Urbano: onze entregas, cinco agentes e um humano com painel, quatro conectores e um serviço de entrega, no máximo duas empresas por segmento por zona. Está desenhado inteiro nos quatro documentos (Mapa de Entregas, Mapa de Acessos, Mapa Mundi, Bíblia) e é o que se vende primeiro. Os outros cinco pilares do dossiê (seção 4) não são versões maiores do núcleo; são módulos: Radar Concorrência, Radar Menu, Radar Stars, Radar Chat e Radar Ads. Cada módulo é um conjunto de agentes, conectores, tabelas, acessos, cláusulas, verbetes e entregas que se liga por tenant, sem tocar no que já funciona. Este roadmap diz em que ordem eles entram, o que cada um pede, quanto custa e quando está pronto.

**O que é um módulo**

1. **Liga por tenant** — Cada tenant tem um campo `modules_json`, no documento do Firestore e na tabela `tenants`. Todo job começa lendo a flag do seu módulo; se está desligada, o job termina em uma linha, sem custo. Nenhum agente, conector ou tabela do núcleo muda quando um módulo é ligado ou desligado.
2. **Tem nome, preço e dono** — Um módulo é vendido separado, aparece separado na fatura e tem um agente ou um conector responsável. Ninguém compra "recursos"; compra Radar Stars.
3. **Traz as próprias peças, com o próprio nome** — Tabelas, tópicos, ferramentas, variáveis e segredos do módulo levam o nome dele (`competitor_snapshots`, `calls`, `ads_daily`, `tenant-{id}-waba-token`). O que é do núcleo continua com o nome de sempre.
4. **Traz os próprios acessos e cláusulas** — Se o módulo pede uma conta nova do cliente, o Mapa de Acessos ganha um sistema com letra nova (E, F, G) e a base legal ganha os itens correspondentes. O Dia 0 ganha um passo, dentro dos mesmos quinze minutos.
5. **Traz as próprias entregas, sem renumerar** — As onze entregas do núcleo mantêm o número. As entregas de módulo têm nome (Quem ganhou a semana, Agenda das 7h, Extrato de Mídia) e entram no Dashboard, no Boletim e no Fechamento como seções que só aparecem quando o módulo está ligado.
6. **Tem teste de aceitação e critério de pronto** — Cada fase fecha com um piloto de 30 dias nos mesmos três clientes do núcleo (uma padaria, uma oficina, uma clínica), com o Guardião em P0 para o módulo novo. Não se vende módulo antes de o piloto fechar.
7. **Desliga sem deixar rastro** — Desligar um módulo remove só os acessos, os segredos e as cadências daquele módulo e exporta o histórico dele. O núcleo continua. O contrário não existe: não há módulo sem núcleo.

```
tenants.modules_json = {
  "concorrencia": {"ativo": true,  "desde": "2027-02-01", "concorrentes": ["<place_id>", "<place_id>", "<place_id>"]},
  "menu":         {"ativo": true,  "desde": "2027-02-01"},
  "stars":        {"ativo": false},
  "chat":         {"ativo": false},
  "ads":          {"ativo": false},
  "suite":        false
}
regra de todo job:   if not tenant.modules[MODULO].ativo: return      (uma linha, sem custo, idempotente)
alerta de custo:     COST_ALERT_PER_TENANT_BRL = 25 + soma dos acréscimos dos módulos ativos
                     (Concorrência +2 · Menu +1 · Stars +2 · Chat +5 · Ads +5 · suíte completa = 40)
```

**O que é compartilhado**

- **LLMGateway**: Uma política por tarefa. A regra do núcleo continua valendo para Sentinela, Recepcionista e Estrategista: Gemini obrigatório para dado, medição e tudo que toca o Google; outros cérebros só para linguagem, atrás da camada. Um módulo acrescenta tarefas à política; não abre porta nova.
- **Diário de Bordo**: Uma tabela só, `actions_log`, que ganha a coluna `modulo`. Convite, mensagem de resgate, ajuste de campanha, oferta relâmpago: tudo com linha e print, como no núcleo.
- **Guardião**: Uma fila, ordenada por risco. O módulo novo entra em P0 no piloto e sobe de patamar por tenant, como qualquer agente.
- **Delivery e o número da casa**: Um canal com o dono. Os modelos novos para o dono (`agenda_7h`, `quem_ganhou`, `extrato_midia`) entram na mesma conta do Radar Urbano; o dono continua saindo com uma palavra.
- **Dashboard Radar**: Uma tela. Seções por módulo só existem quando o módulo está ligado. Dado em tempo real só chega com o Chat; até lá, tudo continua com data de referência.
- **Tesoureiro**: Uma conta. `llm_calls` e `cost.per_tenant` ganham `modulo`; o custo por contato passa a dividir a soma das mensalidades ativas pelos contatos do mês, com a conta aberta no Extrato.
- **Redator-chefe**: Um Boletim de 60 segundos, sempre. Com mais módulos, o roteiro prioriza; não cresce.
- **Cartógrafo**: Uma medição serve o Mapa de Domínio, a comparação da Concorrência e a escolha de termos do Ads.
- **Places Connector**: A mesma chave restrita e os mesmos termos (30 dias, só `place_id` fica). O módulo acrescenta endpoints, não regras.
- **Tenancy**: O mesmo desenho: um documento por tenant, segredos por tenant e por módulo, contas de serviço mínimas por agente.
- **A trava de zona**: É do núcleo e vale para a suíte inteira. Nenhum módulo compra exceção.

**O que é exclusivo de cada módulo**

| Módulo | Agente próprio | Conector ou fundação própria | Acesso novo do cliente | Entregas próprias |
|---|---|---|---|---|
| Radar Concorrência | Sentinela | Places (detalhes e vizinhança) e uma API de clima | Nenhum | Quem ganhou a semana · Sentinela de Oportunidades · comparação nominal no Mapa de Domínio e no Boletim de Reputação |
| Radar Menu | Nenhum (o Editor) | Nenhum (o GBP Connector ganha cardápio e serviços com preço) | Nenhum (uma autorização) | Vitrine Indexada · O que te procuram |
| Radar Stars | Nenhum (o Anfitrião) | Fundação Meta para clientes: Tech Provider, Embedded Signup, conta do WhatsApp Business do cliente | E · WhatsApp da empresa | Convite pós-atendimento · Boletim de Reputação com convites |
| Radar Chat | Recepcionista | Fundação Telefonia (Voice Connector) e o WA Connector em tempo real | E · WhatsApp da empresa; F · Telefonia | Recepcionista 24/7 e Agenda das 7h · Resgate de Ligações Perdidas · Extrato de Demanda com pedidos e horários marcados |
| Radar Ads | Estrategista | Ads Connector (Google Ads API) | G · Google Ads | Extrato de Mídia · micro-campanhas com corte por custo por contato |

**Os princípios da ordem**

1. **Menor acesso novo do cliente primeiro** — Fase 1 pede zero contas novas; Fase 2 pede uma conta na Meta; Fase 3 pede um número dedicado e uma linha; Fase 4 pede uma conta de anúncios com cartão. Cada acesso novo é atrito no Dia 0 e revisão no jurídico; quanto mais tarde, mais clientes já confiam.
2. **Fundações compartilhadas antes dos módulos que dependem delas** — A Fundação Meta para clientes serve Stars e Chat; a Fundação Telefonia serve o Resgate e a atribuição do Ads. Monta-se a fundação com o módulo menor em cima (Stars) e o maior (Chat) herda.
3. **Caminho crítico de aprovações de terceiros começa no dia 1 de cada fase** — Cadastro como Tech Provider na Meta, developer token do Google Ads, cadastro regulatório no provedor de telefonia: nada disso é código, tudo isso demora, e é pedido no primeiro dia da fase, como foi com as Business Profile APIs no núcleo.
4. **Custo por tenant e alerta sobem por módulo, e sobem antes** — Cada módulo tem um acréscimo declarado no alerta (R$ 2, 1, 2, 5 e 5). O piloto de cada fase mede o custo real e ajusta o acréscimo antes da venda, nunca depois.
5. **Piloto antes de venda, sempre** — Trinta dias com a padaria, a oficina e a clínica, Guardião em P0, teste de aceitação passando. A montagem da fase seguinte pode começar durante o piloto; a venda, não.
6. **Nenhum módulo muda as regras inegociáveis** — O capítulo IV lista o que não muda. Se um módulo precisar de uma exceção para funcionar, o módulo está errado.

*Capítulo II · O mapa das fases*

## AS SEIS FASES, EM UMA TELA

Fase 0 é o núcleo, já desenhado. As cinco seguintes ligam os módulos na ordem dos princípios do capítulo I: primeiro o que não pede acesso novo, depois as duas fundações (Meta, telefonia), depois a mídia, por fim a suíte. Cada fase tem uma seção própria neste documento, com o que entra, como se monta e o critério de pronto.

- **Fase 0 · Radar Urbano (o núcleo, já desenhado)** — Onze entregas, cinco agentes e o Guardião, quatro conectores, R$ 499 por mês, seis semanas de montagem e piloto de 30 dias. Tudo que vem depois liga em cima disto e nada do que vem depois mexe nisto.
- **Fase 1 · Radar Concorrência e Radar Menu** — Só Google, nenhum acesso novo do cliente. A Sentinela vira agente, os três concorrentes voltam ao mapa, o card de sábado volta, o catálogo com preço e "O que te procuram" entram. Três semanas.
- **Fase 2 · Radar Stars** — A Fundação Meta para clientes (Tech Provider, Embedded Signup, conta do WhatsApp Business de cada cliente, modelos, consentimento) com o módulo menor em cima: o convite de avaliação depois do atendimento. Três semanas, com a Meta no caminho crítico.
- **Fase 3 · Radar Chat** — Recepcionista 24/7, Agenda das 7h, Fundação Telefonia com número de rastreamento e Resgate de Ligações Perdidas. Contatos em tempo real; "pediu preço" e "horários marcados" voltam ao Extrato. Quatro semanas.
- **Fase 4 · Radar Ads** — Conta gerenciadora, developer token, o Estrategista e o Extrato de Mídia, com corte automático por custo por contato. Depende do número de rastreamento da Fase 3 para saber de onde veio cada ligação. Três semanas.
- **Fase 5 · A suíte** — Os cinco módulos em um contrato entre R$ 1.500 e R$ 2.200, a proposta automática de expansão no mês 3, o cross-sell por dado e o que a máquina compartilha. Duas semanas e um trimestre de piloto.

**Por vertical, o que vem primeiro**

| Vertical (dossiê, seção 22) | Persona | Primeiro módulo | Depois |
|---|---|---|---|
| Alimentação fora do lar | Seu Jorge, Padaria Pão da Praça | Radar Menu (cardápio e horários dentro da busca) | Stars (o convite logo depois do consumo), Concorrência |
| Saúde e bem-estar | Dra. Lívia, Clínica Lívia Odonto | Radar Stars (reputação, só com avaliações reais) | Chat (agendamento pelo WhatsApp), Concorrência |
| Serviços essenciais | Marcão, Oficina Marcão Auto Center | Radar Chat (a ligação na hora da pane, e o Resgate quando ninguém atende) | Ads (urgência no raio que importa), Concorrência |

**O calendário, sequencial**

| Fase | Montagem | Piloto | Acumulado depois do núcleo |
|---|---|---|---|
| 0 · Radar Urbano | 6 semanas | 30 dias | (10 semanas do dia 1) |
| 1 · Concorrência e Menu | 3 semanas | 30 dias | 7 semanas |
| 2 · Stars | 3 semanas (Meta no caminho crítico) | 30 dias | 14 semanas |
| 3 · Chat | 4 semanas | 30 dias | 22 semanas |
| 4 · Ads | 3 semanas | simulação de 31 dias mais 30 dias com clientes | 29 semanas |
| 5 · A suíte | 2 semanas | um trimestre | 44 semanas |

Sequencial, com um engenheiro e o Head de Operação: 44 semanas depois do núcleo; somando as dez do núcleo, cerca de um ano do dia 1 até a suíte fechar um trimestre. Com dois engenheiros e a montagem da fase seguinte começando durante o piloto da anterior, cerca de nove meses. Cabe na janela que o dossiê chama de meses 7 a 18 (seção 13). O que nunca se antecipa é a venda: módulo só se vende com piloto fechado.

*Fase 1 · Só Google, sem acesso novo*

## Radar Concorrência e Radar Menu

*O bairro inteiro no mapa, e a vitrine dentro da busca. Nenhuma conta nova do cliente.*

A primeira fase não pede nada ao cliente além de três nomes e uma lista. Os dois módulos vivem inteiros dentro do que o núcleo já acessa: a Places API e o Perfil da Empresa com papel Gerente. O Radar Concorrência devolve o que o núcleo tirou de propósito: os três concorrentes que o dono escolhe, medidos com método; o card de sábado; e a Sentinela como agente, que vigia feriado, clima, pico de busca e concorrente e age dentro do que foi pré-autorizado. O Radar Menu devolve o catálogo com preço e o card mensal "O que te procuram". É a fase mais barata de montar e a que mais muda a cara do Mapa de Domínio: ele passa a dizer contra quem.

> *Na vida real · Dra. Lívia, Clínica Lívia Odonto*
> Sábado, 9h. "Quem ganhou a semana: Clínica Lívia. Você está em 1º para 'dentista perto de mim' em 6 dos 9 pontos medidos. A Odonto Center publicou 4 fotos e ganhou 2 avaliações; você ganhou 5. Esta semana vou reforçar 'implante' nos três pontos onde eles ainda lideram." Ela lê no café, entre um paciente e outro, e mostra para a recepcionista.

> *Na vida real · Seu Jorge, Padaria Pão da Praça*
> Dia 1. "O que te procuram: 1º bolo de cenoura, 2º pão de fermentação, 3º café da manhã. 'Salgado assado' caiu 40% nas buscas. Sugestão: destacar o kit café da manhã na vitrine e no post de sábado." Seu Jorge monta o kit. Em duas semanas, "kit café da manhã" aparece entre as palavras de descoberta do perfil.

**O que entra**

- **O que o cliente passa a receber:** Radar de Concorrência: card "Quem ganhou a semana" todo sábado às 9h (um vencedor, um motivo, o que a máquina vai fazer), a partir da medição reduzida de sábado e dos sinais públicos dos três concorrentes (posição nos termos-chave, nota, avaliações novas, fotos publicadas, horários) · Sentinela de Oportunidades: aviso de uma linha (até 160 caracteres, no máximo dois por dia) quando um sinal aparece (feriado, pico de busca por um termo na região, concorrente fechado, com nota em queda ou horário mudado, clima que muda a compra), com a ação já executada quando era pré-autorizada e um card Sim/Não quando é oferta relâmpago · Mapa de Domínio ganha a comparação nominal: em cada ponto, quem ocupa o top 3 · Boletim de Reputação ganha a comparação de nota e de avaliações novas com os três · Fechamento Trimestral ganha o comparativo de território (quantos pontos ficaram verdes contra cada concorrente) · Vitrine Indexada: cardápio, catálogo ou lista de serviços com preço, foto e descrição, publicados no perfil · "O que te procuram" no dia 1: os dez itens mais procurados, os que subiram, os que ninguém procura e as sugestões de destaque do mês.
- **Agentes:** Sentinela (agente novo, o sexto): varredura a cada 6 h, sinais de feriado e clima às 06h, "Quem ganhou" no sábado às 08h; cérebro Gemini Pro, saída `{sinal, evidencia, acao, requer_sim, texto_aviso}`; só propõe ações da lista autorizada do tenant; nunca cita concorrente pelo nome em conteúdo público · Cartógrafo passa a gravar os três primeiros `place_id` de cada ponto e alimenta o card de sábado · Editor ganha o catálogo: estrutura com o Gemini o que o cliente mandou ou o que já é público no site e no cardápio digital, manda cada preço ao Guardião para um Sim, publica e revisa no dia 1 · Redator-chefe escreve o card de sábado e a página de "O que te procuram".
- **Conectores e APIs:** Places Connector ganha `places:searchNearby` e `places/{place_id}` com máscara mínima (nota, contagem de avaliações, horário atual, contagem de fotos), ferramenta `places.get_details(place_id, campos)`; o resto continua: sem extração em massa, nada além de 30 dias exceto `place_id` · Uma API de previsão do tempo atrás de um conector pequeno (`weather.forecast(lat, lng)`, chave `WEATHER_API_KEY`) · GBP Connector ganha cardápio pela API de Food Menus (v4, `accounts.locations.foodMenus`) e serviços com preço pela Business Information API (`serviceItems` com `price`), ferramenta `gbp.update_menu_or_services(tenant, itens)`. Armadilha: produtos de varejo não têm API pública; até existir, o Guardião publica pelo Editor de produtos do perfil, à mão, e o Diário registra a origem.
- **Acessos e cláusulas novas:** Nenhum acesso novo: os dois módulos usam o papel Gerente e a chave de Places do Radar Urbano. O Dia 0 (ou a ativação, para quem já é cliente) ganha duas perguntas por áudio: quem são os três concorrentes que te incomodam; que datas importam para o negócio. A base legal ganha três frases: no item 1, ofertas relâmpago e descontos só com um Sim; no item 3, nunca citar concorrente em conteúdo público e usar só sinais públicos dentro dos termos da Places API; no item 5, o cliente responde pela veracidade dos preços e autoriza a extração do que já é público nos canais dele, com cada preço confirmado por um Sim.
- **Tabelas e tópicos:** `competitors(tenant_id, place_id, nome)` · `competitor_snapshots(tenant_id, place_id, data, rating, reviews_count, fotos_count, aberto)`, com expiração de 30 dias · `rank_measurements` ganha `top_place_ids[3]` · `catalog_items(tenant_id, item_id, nome, preco, foto_uri, descricao, origem, confirmado_por, publicado_em)` · `limites_json` ganha `acoes_autorizadas` e `datas_do_negocio` · tópico `sentinela.signal` · cadências novas: a cada 6 h (varredura), diário 06h (feriados e clima), sábado 08h e 09h (Quem ganhou, envio), dia 1 (catálogo e "O que te procuram") · variável `WEATHER_API_KEY` · `hours_equivalence` ganha "item de catálogo publicado 5 min" e "sinal tratado 10 min".
- **Verbetes novos na Bíblia:** Capítulo XI · Radar Concorrência: XI.1 Escolher os três concorrentes e gravar os `place_id` · XI.2 A lista de ações autorizadas da Sentinela (e o que sempre pede Sim) · XI.3 Contratar a API de clima e restringir a chave · XI.4 Quem ganhou a semana: a versão de bicicleta · XI.5 Sentinela de Oportunidades: a versão de bicicleta. Capítulo XII · Radar Menu: XII.1 Estruturar o catálogo com o Gemini a partir do que já é público · XII.2 Publicar cardápio e serviços com preço (o que tem API e o que ainda é à mão) · XII.3 Vitrine Indexada: a versão de bicicleta · XII.4 O que te procuram: a versão de bicicleta. E, no capítulo VII: VII.3 Ligar um módulo em um tenant (`modules_json`). Glossário ganha Snapshot, Sinal, Oferta relâmpago, Food Menus.

**Como se monta**

- **Pré-requisitos e caminho crítico:** Núcleo vivo com os três clientes do piloto e o teste de aceitação do Cartógrafo passando (concordância de 85% ou mais com as 20 buscas manuais): a comparação nominal só vale se a medição própria vale. Não há aprovação de terceiro no caminho: a chave de clima é imediata e a Places já está aprovada. O caminho crítico é interno: a lista de ações autorizadas por tenant precisa existir antes de a Sentinela rodar, e o jurídico revisa as três frases novas antes do piloto.
- **Prazo de montagem estimado:** Três semanas: uma para `modules_json`, o faturamento por módulo e a leitura da flag em todos os jobs; uma e meia para Sentinela, snapshots, `top_place_ids` e o card de sábado; meia para o catálogo, o Sim de preços e "O que te procuram". Depois, piloto de 30 dias com os três clientes.
- **Preço e custo por tenant:** Radar Concorrência R$ 399/mês; Radar Menu R$ 399/mês. Custo de tecnologia: Concorrência acrescenta R$ 1–3 por cliente (detalhes na Places quatro vezes ao dia para três lugares, Gemini Pro a cada 6 h); Menu acrescenta menos de R$ 1 (as APIs de perfil são gratuitas; o Gemini estrutura o catálogo uma vez). Alerta por tenant: R$ 25 + 2 (Concorrência) + 1 (Menu) = R$ 28 para quem tem os dois. Custo por contato passa a dividir a soma das mensalidades ativas: a padaria do exemplo, com os dois módulos, paga R$ 1.297 (499 + 399 + 399) e, com os mesmos 260 contatos, o custo por contato vai a R$ 4,99; o Extrato mostra a conta aberta.
- **O que muda nos quatro documentos:** Mapa de Entregas: duas seções de módulo depois da 11 (Quem ganhou a semana e Sentinela; Vitrine Indexada e O que te procuram); a entrega 05 ganha a legenda "contra quem", a 07 ganha a comparação; o calendário ganha "Semana 3 · Os olhos" e "Todo sábado, 9h" no ritmo permanente. Mapa de Acessos: nenhum sistema novo; as três frases na base legal; duas perguntas a mais no roteiro; a Vitrine no mapa por entrega. Mapa Mundi: Sentinela no capítulo V, `places.get_details` e clima no III, duas tabelas e um tópico no IV, três receitas no VI, quatro linhas na tabela de cadências. Bíblia: capítulos XI e XII, o VII.3 e quatro palavras no glossário.

> **Critério de pronto** — Concorrente marcado como fechado no snapshot de teste gera aviso e post pré-autorizado em menos de 6 h; oferta relâmpago nunca sai sem Sim; card de sábado às 9h, com cinco minutos de folga, com vencedor, motivo e ação, sem nome de concorrente em conteúdo público; snapshots somem em 30 dias e só `place_id` fica; catálogo publicado com 100% dos preços confirmados por Sim; "O que te procuram" no dia 1 com dez itens; custo dos dois módulos abaixo de R$ 3 por tenant no piloto.

*Fase 2 · A Fundação Meta para clientes*

## Radar Stars

*Avaliações reais, pedidas na hora certa, pelo WhatsApp da empresa. Sem incentivo, sem seleção.*

O núcleo responde a toda avaliação em até duas horas e deixa o link curto e o QR no balcão. O que ele não faz é pedir. O convite ativo depois do atendimento saiu de propósito, porque exige o WhatsApp da empresa do cliente na plataforma da Meta, e isso é uma fundação inteira: o Radar Urbano como Tech Provider, o Embedded Signup, a conta do WhatsApp Business de cada cliente, os modelos aprovados por conta, o consentimento coletado no atendimento. O Radar Stars é essa fundação mais o convite. A fundação é compartilhada: o Radar Chat usa a mesma. Por isso o Stars vem antes: é o jeito mais barato de montar a fundação com um módulo pequeno em cima.

> *Na vida real · Marcão, Oficina Marcão Auto Center*
> Terça, 17h10. O sistema da oficina fecha a ordem de serviço e avisa a máquina. Às 19h10, o dono do carro recebe pelo WhatsApp da oficina: "Obrigado por escolher a Oficina Marcão Auto Center. Se puder, conte como foi: [link]. Responda SAIR para não receber mais." Às 19h40 a avaliação entra; às 20h05 está respondida. No dia 1, o Boletim de Reputação diz: 62 convites, 14 avaliações novas, nenhum SAIR. Marcão não fez nada.

**O que entra**

- **O que o cliente passa a receber:** Motor de Reputação ganha o convite pós-atendimento: depois de cada atendimento concluído, no intervalo configurado (duas horas, por exemplo), a pessoa recebe pelo WhatsApp da empresa um convite educado com o link curto oficial de avaliação, sem condicionar nada, com saída em uma palavra; no máximo um convite por pessoa a cada 90 dias · O evento `atendimento.concluido` nasce de um webhook simples do sistema do cliente (caixa, agenda, ordem de serviço), de um toque do balcão em um link da máquina ou, a partir da Fase 3, da própria Recepcionista · Boletim de Reputação ganha três contagens: convites enviados, avaliações novas no mês, pedidos de SAIR (contagens, nunca taxas) · Horas Devolvidas ganha "convite enviado 2 min" · O material de balcão continua; o QR passa a poder levar também ao WhatsApp da empresa.
- **Agentes:** Anfitrião ganha o gatilho `atendimento.concluido` e a ferramenta `wa.send_template(tenant, wa_id, 'convite_avaliacao', params)` na conta do cliente; guardrails: só após evento real, só para quem consentiu no atendimento, nunca seletivo por satisfação, limite de 90 dias por pessoa, pausa automática dos convites se a qualidade do número cair; a classificação de avaliação suspeita continua com o Gemini · Redator-chefe manda o lembrete de pendência quando a verificação da empresa na Meta passa de 72 h.
- **Conectores e APIs:** WA Connector ganha a segunda metade: cadastro do Radar Urbano como Tech Provider na Meta; Embedded Signup (Login do Facebook para empresas com uma configuração e `config_id`) numa página `/conectar`; callback com `waba_id` e `phone_number_id` por tenant; webhooks por conta de cliente; modelos por conta (`convite_avaliacao`, categoria utilidade ou marketing conforme a Meta classificar); token de sistema por conta de cliente no Secret Manager. O número da casa continua separado e só fala com o dono.
- **Acessos e cláusulas novas:** Sistema E · WhatsApp da empresa (plataforma Meta): portfólio de negócios do cliente com a empresa verificada (CNPJ e documentos), um número dedicado à plataforma (recomendado um número novo, porque o número sai do aplicativo comum), aceite do Embedded Signup e confirmação por código digitado pelo próprio cliente; nome de exibição aprovado pela Meta; nunca senha. Base legal: o item 3 volta inteiro (consentimento dos clientes finais coletado no atendimento: cadastro, comanda, QR, aviso no balcão; saída em uma palavra em toda mensagem); o item 2 ganha o cliente como controlador dos dados dos clientes finais dele e o Radar Urbano como operador, `wa_id` como hash com sal, retenção dos convites por 12 meses e a Meta como suboperador também para o WhatsApp do cliente; o item 8 ganha a devolução da conta do WhatsApp Business ao cliente no encerramento. Roteiro do Dia 0: entra o passo "Minuto 10 a 14 · WhatsApp da empresa", dentro da folga; a verificação da Meta segue em paralelo e nada espera por ela.
- **Tabelas e tópicos:** `invites(tenant_id, wa_id_hash, enviado_em, origem, status, opt_out_em)` · `tenants` ganha `waba_id` e `phone_number_id` no Firestore e o segredo `tenant-{id}-waba-token` · tópico `atendimento.concluido` · estados novos no onboarding: `wa_linked` ou `wa_pending_verification` · variável `META_EMBEDDED_SIGNUP_CONFIG_ID` · modelo `convite_avaliacao` em cada conta de cliente · runbook novo: número do cliente com qualidade baixa ou bloqueado (pausar convites, revisar SAIR acima de 2%, contestar na Meta, número reserva só com aprovação do cliente).
- **Verbetes novos na Bíblia:** Capítulo XIII · Radar Stars: XIII.1 Virar Tech Provider e montar o Embedded Signup (o cliente entra com dois cliques) · XIII.2 Criar e aprovar o modelo `convite_avaliacao` na conta de cada cliente · XIII.3 O evento `atendimento.concluido`: webhook simples, link do balcão e QR · XIII.4 Runbook: o número do cliente foi bloqueado ou a qualidade caiu · XIII.5 O convite pós-atendimento: a versão de bicicleta. Glossário ganha Embedded Signup, WABA de cliente, Token (Meta) de cliente, Janela de 24 h, Opt-in e opt-out.

**Como se monta**

- **Pré-requisitos e caminho crítico:** A Fase 1 não é pré-requisito. O caminho crítico é a Meta: o cadastro como Tech Provider e a configuração do Embedded Signup levam de dias a semanas e são pedidos no dia 1 da fase; a verificação da empresa de cada cliente leva de horas a dias e corre em paralelo ao piloto; a aprovação de cada modelo leva de minutos a horas. Antes do primeiro convite, o jurídico revisa o item 3 e o texto do modelo. Na Bíblia, o III.7 (portfólio, app e número da casa) já está feito; o XIII.1 parte dele.
- **Prazo de montagem estimado:** Três semanas de código (página `/conectar`, callback e estados, modelos por conta, gatilho e limites do Anfitrião, `invites` e o Boletim de Reputação novo), com o pedido à Meta no primeiro dia. Se a Meta demorar mais que as três semanas, o piloto começa com a conta de teste e entra nas contas dos clientes quando liberar. Piloto de 30 dias com os três clientes.
- **Preço e custo por tenant:** Radar Stars R$ 299/mês. Custo de tecnologia: R$ 2–3 por cliente (60 a 90 convites por mês em modelo de utilidade ou marketing; o Gemini já existia). Alerta: mais R$ 2; um tenant com a Fase 1 e o Stars fica em R$ 30. Custo por contato: a mensalidade somada continua dividindo os mesmos contatos; o convite não é contato e não entra na soma.
- **O que muda nos quatro documentos:** Mapa de Entregas: a entrega 07 ganha o convite e as três contagens no Boletim de Reputação; a Regra do Zero não muda (o dono continua sem fazer nada; o balcão ganha, no máximo, um toque). Mapa de Acessos: Sistema E, o item 3 inteiro, os ajustes nos itens 2 e 8, o passo novo do roteiro, a entrega 07 no mapa por entrega com "consentimento coletado no atendimento". Mapa Mundi: WA Connector com as duas metades no capítulo III, os estados `wa_linked` no VII, o runbook no VIII, o hash de `wa_id` no IX e a receita 07 com o convite. Bíblia: capítulo XIII e cinco palavras no glossário.

> **Critério de pronto** — Um cliente de teste conclui o Embedded Signup em menos de 3 minutos e a máquina manda mensagem pelo número dele; o convite dispara após evento simulado, respeita o consentimento e o limite de 90 dias e nunca sai duas vezes para a mesma pessoa; a auditoria por amostragem não encontra convite seletivo; no piloto, pedidos de SAIR abaixo de 2% e qualidade do número verde por 30 dias; Boletim de Reputação com as três contagens no dia 1.

*Fase 3 · Atendimento e telefone, em tempo real*

## Radar Chat

*Ninguém fica sem resposta. A ligação perdida vira conversa. E o Extrato passa a contar o que a Recepcionista fez.*

O Radar Chat é o maior módulo e o único que traz dado em tempo real. Ele devolve a Recepcionista, a Agenda das 7h, o número de rastreamento e o Resgate de Ligações Perdidas, e com eles voltam ao Extrato de Demanda as linhas que o núcleo não pode contar: quem pediu preço, orçamento ou horário, e quantos horários foram marcados. Precisa de duas fundações: a Meta para clientes, da Fase 2, e a Telefonia, nova. Por isso é a terceira fase e a mais longa. O núcleo mostra ligações pelo perfil com dois ou três dias de atraso; o Chat mostra a ligação que tocou agora.

> *Na vida real · Dra. Lívia, Clínica Lívia Odonto*
> Domingo, 23h14. No WhatsApp da clínica: "Vocês fazem clareamento? Quanto fica?" A Recepcionista responde em oito segundos, avisa que é atendimento automático com gente disponível, explica a avaliação inicial, oferece terça às 9h ou quinta às 18h. A pessoa escolhe terça. Segunda, 7h, a Agenda no celular da Dra. Lívia: "1 avaliação de clareamento marcada, terça 9h, veio do botão do perfil. Ninguém precisa de retorno."

**O que entra**

- **O que o cliente passa a receber:** Recepcionista 24/7: toda mensagem no WhatsApp da empresa respondida em segundos, no tom da casa, com aviso de atendimento automático e humano disponível; tira dúvida de preço, horário e serviço, qualifica, marca horário nos slots reais e registra encomenda; transborda ao dono com o link da conversa quando o assunto pede · Agenda das 7h: card diário com quem falou durante a noite, o que queria, o que ficou marcado e quem precisa de retorno humano · Resgate de Ligações Perdidas: número de rastreamento publicado como telefone principal do perfil, com o original como adicional (prática aceita pelo Google); ligação perdida ou fora do horário vira mensagem de utilidade em até 30 segundos, uma vez por chamada, com saída; card mensal "Recuperados" (perdidas, resgatadas, pediram orçamento, horários marcados) · Dashboard Radar ganha tempo real: chamadas e conversas do dia, ao lado das métricas do Google com data de referência · Extrato de Demanda passa a contar contato assim: ligações atendidas e resgatadas (telefonia), pedidos de rota, cliques no site e mensagens pelo perfil (Google), conversas no WhatsApp; e ganha as linhas "pediram preço, orçamento ou horário", "horários marcados pela Recepcionista" e "custo por horário marcado"; os toques em Ligar do Google ficam como métrica de contexto, para não contar a mesma ligação duas vezes · Boletim de Segunda ganha conversas e horários marcados · Horas Devolvidas ganha "mensagem atendida 3 min" e "ligação resgatada 2 min" · Voz do Cliente passa a ler também as conversas, com frases anonimizadas · Fechamento ganha as duas linhas novas · O evento `atendimento.concluido` do Stars passa a nascer da própria Recepcionista.
- **Agentes:** Recepcionista (agente novo, o sétimo): gatilho pelo webhook `messages` da conta do cliente (tempo real), pelo evento `rescue.request` e pela cadência diária das 07h; cérebro Gemini Flash em streaming, sessão por conversa no ADK, fallback Claude Haiku pela LLMGateway; extração de intenção e de campos em JSON pelo Gemini; ferramentas `wa.send_text`, `wa.send_interactive`, `agenda.slots(servico)`, `agenda.book(slot)`, `crm.tag(conv, intencao)`, `handoff.to_human(conv, motivo)`, `wa.send_template(resgate_ligacao)`; guardrails: latência abaixo de 2 s por turno, no máximo 12 turnos sem humano, não coleta dados de saúde além do necessário para marcar, só slots reais, nunca promete resultado nem negocia fora das faixas · Anfitrião recebe `atendimento.concluido` da Recepcionista · Tesoureiro consolida `calls`, `conversations` e `appointments` · Redator-chefe ganha a Agenda das 7h e as linhas novas do Boletim e do Fechamento.
- **Conectores e APIs:** Voice Connector (conector novo, a Fundação Telefonia): provedor de números virtuais brasileiros com API e webhooks de chamada (Twilio, Zenvia ou Nvoip, a homologar); número fixo local por DDD; encaminhamento condicional para a linha do cliente; webhook com `caller_id`, `status` e `duration`; gravação desligada por padrão. Fluxo: chamada → número de rastreamento → linha do cliente → evento `completed` ou `no-answer` → Pub/Sub `calls.events` → BigQuery `calls` → `rescue.request` se perdida ou fora do horário. Ferramentas `voice.provision_number(tenant, ddd)`, `voice.set_forward(numero, destino)`, `voice.events(numero)`. Testar a exibição do número de quem ligou em três operadoras antes de publicar · WA Connector ganha sessões em tempo real por conta de cliente (Firestore, TTL de 24 h), a janela de 24 h e os modelos `resgate_ligacao` (utilidade, na conta do cliente) e `agenda_7h` (no número da casa, para o dono) · O Dashboard passa a ler `realtime/{tenant}` no Firestore.
- **Acessos e cláusulas novas:** Sistema F · Telefonia (linha da empresa): o cliente autoriza no contrato a publicação do número de rastreamento como principal e o encaminhamento para a linha dele; confirma no Dia 0 qual linha recebe; nenhuma configuração na operadora; nunca a conta da operadora; dados gerados: número de quem ligou, horário, duração, atendida ou não; gravação só com autorização expressa e aviso ao interlocutor, por padrão desligada. O Sistema E (Fase 2) é obrigatório. Base legal: o item 1 ganha o mandato de atendimento em nome da empresa dentro do roteiro aprovado; o item 2 ganha telefone e nome de quem ligou ou escreveu como dados pessoais (hash nas tabelas, claro só na sessão com TTL), retenção de `calls` e `conversations` por 12 meses e o provedor de telefonia como suboperador; o item 3 ganha a mensagem de resgate como utilidade com base no contato iniciado pela própria pessoa (identifica, explica o motivo, oferece saída); o item 8 ganha a transferência ou desativação do número de rastreamento com 30 dias de aviso. Roteiro do Dia 0: "Minuto 12 a 14 · Telefonia" (confirma a linha, aprova o texto de resgate e o roteiro de atendimento com um Sim); com Stars e Chat, o Dia 0 usa os quinze minutos inteiros. Dados que o cliente informa: serviços, preços ou faixas, horários, o que pode ser marcado e o que precisa de humano, grade de horários (por link simples ou integração com a agenda dele).
- **Tabelas e tópicos:** `calls(tenant_id, call_id, inicio, duracao, status, caller_hash, fora_horario, resgate_enviado_em)` · `conversations(tenant_id, wa_id_hash, inicio, origem, intencao, pediu_preco, marcou_horario, transbordo, encerrada_em)` · `appointments(tenant_id, conv_id, data_hora, servico, status)` · `locations` ganha `telefone_rastreio` e `telefone_original` · tópicos `calls.events` e `rescue.request` · estado `voice_linked` · variáveis `VOICE_PROVIDER`, `VOICE_API_KEY`, `VOICE_WEBHOOK_SECRET` · cadências: contínuo (webhooks, sessões, resgates) e diário 07h (Agenda) · SLO novo: primeira resposta p95 abaixo de 10 s, turno p95 abaixo de 3 s · runbook novo: reclamação de cliente final por mensagem indevida (saída imediata, registro, revisão do consentimento no tenant, resposta humana em 4 h úteis) · dimensionamento dos Guardiões cai de 30 → 80 → 150 para 20 → 60 → 120 clientes por operador, porque agora há transbordo em tempo real.
- **Verbetes novos na Bíblia:** Capítulo XIV · Radar Chat: XIV.1 Telefonia: contratar o número de rastreamento e ligar o encaminhamento · XIV.2 Os modelos `resgate_ligacao` e `agenda_7h` · XIV.3 A grade de horários do cliente: o link simples e a integração com a agenda · XIV.4 O roteiro de atendimento: o que a Recepcionista pode, o que não pode e quando chama gente · XIV.5 Cinquenta conversas roteirizadas: o teste de aceitação · XIV.6 Recepcionista e Agenda das 7h: a versão de bicicleta · XIV.7 Resgate de Ligações Perdidas: a versão de bicicleta · XIV.8 Runbook: reclamação de cliente final. Glossário ganha Encaminhamento, Evento de chamada, Número de rastreamento, Transbordo, Sessão.

**Como se monta**

- **Pré-requisitos e caminho crítico:** Fase 2 (Fundação Meta para clientes) pronta, ou montada junto se o Chat vier antes do Stars. Caminho crítico: o cadastro regulatório no provedor de telefonia (CNPJ, endereço, documento do responsável) e a compra de números por DDD, pedidos no dia 1 da fase; o teste de exibição do número em três operadoras; a revisão jurídica dos itens 1, 2, 3 e 8. A tabela de cérebros do Mapa Mundi volta a ter a linha "conversa em tempo real" (Gemini Flash, fallback Claude Haiku), que o núcleo tirou.
- **Prazo de montagem estimado:** Quatro semanas: uma para o Voice Connector (número, encaminhamento, webhook, `calls`); uma e meia para a Recepcionista em streaming com sessão, agenda e transbordo; meia para o Resgate e o card Recuperados; uma para a Agenda das 7h, o Extrato com as linhas novas, o Dashboard em tempo real e as cinquenta conversas roteirizadas. Piloto de 30 dias com os três clientes, Guardião em P0 para os transbordos.
- **Preço e custo por tenant:** Radar Chat R$ 499/mês. Custo de tecnologia: R$ 7–11 por cliente (um número mais cerca de 200 minutos encaminhados: R$ 5–8; mensagens fora da janela e resgates: R$ 1–2; Gemini Flash em streaming: cerca de R$ 1). Alerta: mais R$ 5; um tenant com as Fases 1, 2 e 3 fica em R$ 35, o valor original do Mapa Mundi de seis conectores. Custo por contato com o módulo: a mensalidade somada dividida pelos contatos redefinidos. Exemplo, a padaria só com núcleo e Chat: 131 ligações atendidas, 22 resgatadas, 97 rotas, 31 cliques no site, 14 mensagens pelo perfil e 44 conversas no WhatsApp são 339 contatos; R$ 998 ÷ 339 = R$ 2,94 por contato; os 118 toques em Ligar do Google ficam no rodapé, como contexto. Custo por horário marcado: a mesma mensalidade dividida pelos horários que a Recepcionista marcou; o dono põe o valor dele por cima.
- **O que muda nos quatro documentos:** Mapa de Entregas: três seções de módulo (Recepcionista e Agenda das 7h, Resgate, Recuperados); a entrega 03 ganha tempo real, a 08 ganha as linhas e a nova definição de contato, a 09 ganha duas equivalências, a 10 passa a ler conversas, a 04 e a 11 ganham linhas; a semana do Seu Jorge ganha a quinta 22h40 e a sexta 8h01. Mapa de Acessos: Sistema F, os quatro itens da base legal, o passo "Minuto 12 a 14", três entregas no mapa por entrega. Mapa Mundi: Recepcionista no V, Voice Connector no III, três tabelas e dois tópicos no IV, três receitas no VI, o estado `voice_linked` no VII, cadências, SLO, runbook e dimensionamento no VIII, gravação de chamadas no IX. Bíblia: capítulo XIV e cinco palavras no glossário.

> **Critério de pronto** — Cinquenta conversas roteirizadas (preço, horário, fora de escopo, urgência, saída) passam com 100% das regras; primeira resposta em menos de 10 s; chamada perdida simulada gera a mensagem em menos de 30 s, uma vez só; Agenda chega às 7h com cinco minutos de folga; card Recuperados reconcilia com `calls`; Extrato de Demanda com as linhas novas 100% de SQL e a definição de contato no rodapé; número de quem ligou exibido corretamente em três operadoras; custo do módulo abaixo de R$ 11 por tenant no piloto.

*Fase 4 · Mídia com extrato, depois do telefone*

## Radar Ads

*Cada real investido, e quantos contatos ele trouxe. Linha por linha, com corte automático.*

O Radar Ads é o único módulo com verba além da mensalidade, e a verba é do cliente: fica no cartão dele, cobrada pelo Google. A máquina liga, ajusta e desliga micro-campanhas de busca com raio, só para termos de intenção, e presta contas no Extrato de Mídia como um extrato bancário. Vem depois do Chat por uma razão técnica: sem um número de rastreamento dedicado por campanha, não há como saber qual ligação veio de qual anúncio, e sem isso o custo por contato por campanha é chute. Chute a máquina não publica.

> *Na vida real · Marcão, Oficina Marcão Auto Center*
> Dia 1. Extrato de Mídia: R$ 600 investidos em "freio" e "revisão" num raio de 3 km. 58 contatos, R$ 10,34 por contato. A campanha de "pneu" foi pausada no dia 18 por custo alto. Decisão: manter as duas, testar "ar-condicionado automotivo" com R$ 150 em outubro. Sim ou Não. Marcão responde Sim no semáforo.

**O que entra**

- **O que o cliente passa a receber:** Extrato de Mídia no dia 1: quanto foi investido, quantas ligações, rotas e conversas cada campanha gerou, o custo por contato de cada uma, o que foi pausado e por quê, e a decisão da máquina para o próximo mês; a verba aparece separada da mensalidade · Micro-campanhas de busca: o raio que importa, termos de intenção, horários de atendimento, orçamento diário igual ao teto do contrato dividido por 30,4, nunca acima; campanha nova sempre com um Sim · Corte automático: custo por contato acima do limiar do segmento por 7 dias pausa a campanha e pergunta ao dono · Fechamento Executivo ganha a linha de mídia; o Dashboard ganha a seção de campanhas · Calendário: "Mês 2 · Radar Ads ativado para quem quiser, com o primeiro Extrato de Mídia no fim do mês".
- **Agentes:** Estrategista (agente novo, o oitavo): diário 08h lê o desempenho e decide ajustes dentro do teto; dia 1 escreve o Extrato de Mídia; o evento de ativação faz o bootstrap; cérebro Gemini Pro (decisão de Google Ads é decisão de API do Google), com teto e corte em código, não no modelo; ferramentas `ads.create_campaign`, `ads.set_budget`, `ads.pause`, `ads.report`, `voice.provision_number(campanha)`, `render.pdf(extrato_midia)`; guardrails: teto mensal em código, nenhuma campanha sem `autorizada`, nenhuma alteração sem linha no Diário · Cartógrafo fornece termos e raio (os vermelhos do Mapa são candidatos) · Tesoureiro reconcilia `ads_daily` com `calls` pelo número de cada campanha.
- **Conectores e APIs:** Ads Connector (conector novo): Google Ads API com a conta gerenciadora (MCC) do Radar Urbano, developer token com acesso básico aprovado, OAuth do usuário operacional, `login-customer-id` da MCC e `customer_id` do cliente por tenant; serviços `CampaignBudgetService`, `CampaignService` (busca, raio por `ProximityInfo`), `AdGroupService`, `AdGroupCriterionService` (palavras de intenção), `AssetService` (extensão de chamada com o número de rastreamento da campanha), `GoogleAdsService.search` (relatórios com `metrics.cost_micros` e `metrics.phone_calls`) · Voice Connector: um número de rastreamento por campanha · Armadilhas: a verificação de anunciante pode ser exigida pelo Google e é feita pelo cliente; o Radar Urbano nunca é pagador.
- **Acessos e cláusulas novas:** Sistema G · Google Ads: conta em nome do cliente com o cartão dele; o cliente informa o número de cliente e aceita o pedido de vinculação da MCC (acesso padrão: criar e gerenciar campanhas; sem administração, sem pagamento); nunca senha. Base legal: o item 1 ganha o teto mensal de verba e a faixa de raio, e "campanha acima do teto exige Sim"; a mensalidade de R$ 699 é a gestão, separada da verba; o item 7 repete que não se promete resultado nem posição paga. Roteiro: o passo "Só com Radar Ads" acontece depois, por WhatsApp, em dez minutos, uma vez: número da conta, vinculação por e-mail, cartão no Google, verificação de anunciante se pedida. O Dia 0 não muda.
- **Tabelas e tópicos:** `campaigns(tenant_id, campaign_id, nome, termos[], raio_m, horarios, teto_mensal, numero_rastreio, status, autorizada_em)` · `ads_daily(tenant_id, campaign_id, data, custo, cliques, ligacoes, conversas)` · `calls` ganha `campaign_id`; `conversations` ganha `origem = 'ads'` · estado `ads_linked` · segredo `tenant-{id}-ads-customer` · variáveis `ADS_DEVELOPER_TOKEN`, `ADS_MCC_ID`, `ADS_OAUTH_CLIENT_ID`, `ADS_OAUTH_CLIENT_SECRET` · cadência diário 08h · tabela de configuração nova: `segment_thresholds(segmento, custo_por_contato_max)`, os limiares por segmento (pendência do backlog: definir antes do piloto) · a Google Ads API entra na lista de APIs habilitadas do projeto.
- **Verbetes novos na Bíblia:** Capítulo XV · Radar Ads: XV.1 Google Ads: conta gerenciadora (MCC), developer token e vincular o cliente · XV.2 O teto: como a máquina calcula o orçamento diário e por que nunca passa · XV.3 Limiares de custo por contato por segmento · XV.4 Um número de rastreamento por campanha · XV.5 Extrato de Mídia: a versão de bicicleta. Glossário ganha MCC, Developer token, Extensão de chamada, Verificação de anunciante, Verba.

**Como se monta**

- **Pré-requisitos e caminho crítico:** Fundação Telefonia (Fase 3) pronta: sem ela, não há atribuição. A Recepcionista é recomendada, não obrigatória: quem quer Ads sem Chat recebe a fundação de telefonia sozinha (número, encaminhamento, `calls`), sem Resgate. Caminho crítico: developer token com acesso básico (dias a semanas; nasce em modo teste e só funciona com contas de teste até aprovar), pedido no dia 1 da fase; MCC criada; limiares por segmento definidos; verificação de anunciante dos clientes do piloto; jurídico nos itens 1 e 7.
- **Prazo de montagem estimado:** Três semanas: uma para o Ads Connector e o bootstrap em conta de teste; uma para o Estrategista com teto, corte e Diário; uma para o Extrato de Mídia, a reconciliação com `calls` e a seção do Dashboard. Depois, simulação de 31 dias em conta de teste e piloto de 30 dias com os clientes que quiserem verba.
- **Preço e custo por tenant:** Radar Ads R$ 699/mês de gestão; a verba é do cliente, com teto no contrato, e não entra em nenhuma conta do Radar Urbano. Custo de tecnologia: R$ 1–2 por cliente (a API é gratuita; Gemini Pro uma vez ao dia; um número de rastreamento a mais por campanha). Alerta: mais R$ 5; um tenant com os cinco módulos fica em R$ 40. Custo por contato no Extrato de Mídia é por campanha (verba da campanha dividida pelos contatos que ela trouxe); o custo por contato do Extrato de Demanda continua sendo a mensalidade somada dividida pelos contatos, e a verba aparece em linha própria, para ninguém somar laranja com maçã.
- **O que muda nos quatro documentos:** Mapa de Entregas: uma seção de módulo (Extrato de Mídia), a 11 ganha a linha de mídia, o calendário ganha o Mês 2. Mapa de Acessos: Sistema G, os itens 1 e 7, o passo "Só com Radar Ads" no roteiro, a entrega no mapa por entrega. Mapa Mundi: Estrategista no V, Ads Connector no III, duas tabelas no IV, uma receita no VI, `ads_linked` no VII, a cadência no VIII, a Google Ads API na lista de APIs e as quatro variáveis no apêndice. Bíblia: capítulo XV e cinco palavras no glossário.

> **Critério de pronto** — Em conta de teste, a campanha respeita o teto em simulação de 31 dias e pausa quando o custo por contato simulado passa do limiar por 7 dias; nenhuma campanha nasce sem número de rastreamento próprio nem sem Sim; Extrato de Mídia reconcilia com `ads_daily` e `calls` em 100% das linhas; verificação de anunciante concluída pelos clientes do piloto; nenhum campo de conversão ou receita no template.

*Fase 5 · Os seis pilares, um contrato*

## A suíte

*Um preço, oito agentes, o mesmo Diário. E uma proposta que faz conta, não promessa.*

A suíte não é um módulo: é os cinco ligados no mesmo tenant, com um preço só e uma máquina que compartilha o que dá para compartilhar. Somados à la carte, os seis pilares custam R$ 2.794 por mês (499 + 299 + 499 + 399 + 699 + 399). A suíte fecha entre R$ 1.500 e R$ 2.200, a faixa do dossiê; onde cada cliente cai dentro dela é política comercial (segmento, tempo de casa, praça), não algoritmo. O que a Fase 5 monta é o que só existe quando tudo está junto: o bundle na fatura, a proposta automática de expansão no mês 3, o cross-sell por dado e o custo por módulo.

> *Na vida real · Seu Jorge, Padaria Pão da Praça*
> Dia 1 do quarto mês. No fim do Fechamento Trimestral, uma página a mais: "Nas suas palavras de descoberta apareceram 'bolo de cenoura', 'pão de fermentação' e 'café da manhã'. O Radar Menu coloca o cardápio com preço dentro da busca: R$ 399 por mês. Para o seu custo por contato ficar nos R$ 1,92 de hoje, ele precisaria trazer 208 contatos a mais por mês; se não trouxer nenhum, o custo por contato vai a R$ 3,45. Quer ver como fica? Sim ou Não." Seu Jorge lê duas vezes. Ninguém prometeu nada; a conta está ali.

**O que entra**

- **O que o cliente passa a receber:** Tudo das Fases 1 a 4, no mesmo calendário: todo dia às 7h a Agenda; o tempo todo Recepcionista, Resgate, Sentinela e Diário; segunda às 7h o Boletim; sábado às 9h Quem ganhou a semana; dia 1 Mapa de Domínio, Boletim de Reputação, Extrato de Demanda, Horas Devolvidas, Voz do Cliente, O que te procuram, Extrato de Mídia e Fechamento Executivo; a cada três meses o Fechamento Trimestral · A proposta automática de expansão, no terceiro Fechamento de quem não tem a suíte: uma página a mais com o dado que a máquina viu, o módulo que responde a ele, o preço e a conta de equilíbrio (quantos contatos a mais o módulo precisaria trazer para o custo por contato ficar onde está, e onde ele vai se não trouxer nenhum), com um Sim ou Não; nunca uma previsão · Um Dia 0 de quinze minutos com os oito passos: antes da conversa; cinco perguntas mais as duas dos módulos; Gerente no perfil; WhatsApp da empresa; telefonia; dashboard e Diagnóstico; Ads depois; encerramento quando houver.
- **Agentes:** Os oito e o Guardião: Cartógrafo, Editor, Anfitrião, Recepcionista, Sentinela, Estrategista, Tesoureiro, Redator-chefe. A ordem do dia 1 (02h → 08h) passa a ser Cartógrafo, Editor, Tesoureiro, Anfitrião, Estrategista, Redator-chefe; Sentinela e Recepcionista não têm job mensal · Redator-chefe ganha a proposta de expansão: só números de SQL, verificação cruzada pelo Gemini, sem adjetivo, sem promessa · Tesoureiro ganha o custo por módulo e a fatura com linhas.
- **Conectores e APIs:** Os seis: GBP, Places, WA (número da casa e contas de clientes), Voice, Ads, TTS com Render & Delivery. Nenhum novo.
- **Acessos e cláusulas novas:** Sistemas A a G. Um contrato só, com um anexo por módulo: as cláusulas de cada fase viram anexos que se ativam com o módulo; o bundle na fatura; a cláusula de exclusividade por zona vale para a suíte inteira e não tem exceção comprada. Encerramento por módulo: desligar um módulo remove os acessos daquele módulo (WhatsApp da empresa, telefonia, Google Ads) e mantém o núcleo; encerrar o núcleo encerra tudo e libera a vaga da zona.
- **Tabelas e tópicos:** `tenants.modules_json` com `suite: true` e o preço do bundle · `llm_calls.modulo` e `actions_log.modulo` em toda linha · `cost.per_tenant(tenant, periodo, modulo)` · `expansion_proposals(tenant_id, mes, sinal, modulo_sugerido, contatos_equilibrio, resposta, respondido_em)` · nenhum tópico novo · alerta de custo: R$ 25 + 2 + 1 + 2 + 5 + 5 = R$ 40 por tenant, com custo típico de R$ 25–40, o intervalo do manual original de seis conectores.
- **Verbetes novos na Bíblia:** VII.4 Trocar um tenant para a suíte (e o que acontece na fatura) · VIII.7 Runbook: desligar um módulo sem desligar o núcleo · VIII.8 A proposta de expansão: o que o Redator-chefe pode e não pode escrever. Glossário ganha Suíte, Bundle, Conta de equilíbrio, Cross-sell por dado.

**Cross-sell por dado**

| Sinal contável (três meses de dado) | Módulo | O que a proposta mostra |
|---|---|---|
| Mensagens pelo perfil acima de 20 no mês, ou ligações pelo perfil acima de 100 | Radar Chat | As duas contagens, o preço, os contatos de equilíbrio |
| Palavras-chave de descoberta com nome de produto ou serviço ("bolo de cenoura", "clareamento", "freio") | Radar Menu | As palavras e as impressões de cada uma, o preço, os contatos de equilíbrio |
| Avaliações novas no mês abaixo de cinco, com contatos acima de 150 | Radar Stars | As duas contagens, o preço, e a regra: só avaliações reais, sem incentivo |
| Termo-chave vermelho há três meses com a auditoria do perfil em 100% | Radar Concorrência | O termo, os pontos vermelhos, o preço; quem ocupa o top 3 ali só aparece depois de ligado |
| Termos-chave verdes na maior parte da grade e um termo de intenção ainda vermelho | Radar Ads | O termo, o raio, o teto sugerido e o custo por contato máximo do segmento; nunca uma projeção de contatos |

Regras da proposta: só sai com três meses de dado; sugere um módulo por vez; a resposta Não silencia aquele módulo por seis meses; a conta de equilíbrio é aritmética (mensalidade somada dividida pelo custo por contato atual), não previsão; a padaria do exemplo, a R$ 1,92 por contato, precisaria de 468 contatos com o Menu (R$ 898 ÷ 1,92), 208 a mais que os 260 de hoje.

**Como se monta**

- **Pré-requisitos e caminho crítico:** Os cinco módulos com piloto fechado. Caminho crítico: o provedor de pagamento com plano de bundle e módulos avulsos; o contrato em anexos com o jurídico; um trimestre inteiro de um tenant com tudo ligado, para o primeiro Fechamento Trimestral com proposta.
- **Prazo de montagem estimado:** Duas semanas de código (bundle e fatura, `modulo` em toda linha de custo e de Diário, proposta de expansão, seções do Dashboard, desligamento por módulo) e um trimestre de piloto com os três clientes na suíte.
- **Preço e custo por tenant:** Suíte entre R$ 1.500 e R$ 2.200 por mês por CNPJ; verba de mídia fora. Custo de tecnologia R$ 25–40, alerta em R$ 40. Custo por contato: o preço da suíte dividido pelos contatos redefinidos pelo Chat; o Extrato mostra o preço da suíte, não a soma dos módulos.
- **O que muda nos quatro documentos:** Mapa de Entregas: o ritmo permanente volta a ser o original inteiro, o Mês 3 ganha a proposta com a conta de equilíbrio, a máquina do capítulo V passa a oito agentes. Mapa de Acessos: contrato com anexos por módulo, encerramento por módulo, o roteiro de oito passos. Mapa Mundi: tabela de custo por módulo, a ordem do dia 1 com os oito agentes, dimensionamento com tempo real, apêndice completo. Bíblia: VII.4, VIII.7, VIII.8 e quatro palavras no glossário.

> **Critério de pronto** — Um tenant com os cinco módulos recebe todas as entregas do calendário por 30 dias sem colisão de horário e com o Diário 100% com print; custo por tenant abaixo de R$ 40 no trimestre; a proposta de expansão do mês 3 sai só com números de SQL e passa na verificação cruzada; desligar um módulo em teste não quebra nenhuma entrega do núcleo; o Dia 0 completo leva até 15 minutos cronometrados com três pessoas que nunca viram o produto; nenhuma zona com mais de dois tenants do mesmo segmento, com ou sem suíte.

*Capítulo III · Dependências e ordem alternativa*

## QUEM DEPENDE DE QUEM {.dark}

A ordem das fases é a padrão, não a única. A tabela diz o que cada módulo exige e o que ele deixa pronto para os outros; abaixo, quando faz sentido inverter e três caminhos possíveis. O que nunca inverte: núcleo primeiro, fundação antes do módulo, piloto antes da venda.

| Módulo | Depende de | O que deixa pronto para os outros | Pode inverter com |
|---|---|---|---|
| Radar Concorrência | Núcleo (Cartógrafo, Places, Editor, Delivery) | `top_place_ids` no Mapa; sinais para o Editor; a comparação no Boletim de Reputação | Qualquer um; é o primeiro por não pedir acesso novo |
| Radar Menu | Núcleo (Editor, GBP Connector, Guardião) | Os itens do catálogo, que o cross-sell e a escolha de termos do Ads usam | Qualquer um |
| Radar Stars | Núcleo (Anfitrião) mais a Fundação Meta para clientes | A Fundação Meta, que o Chat usa inteira | O Chat: se vier depois dele, herda a fundação e cai para uma semana |
| Radar Chat | Núcleo (Tesoureiro, Delivery, Dashboard), Fundação Meta para clientes e Fundação Telefonia | `calls`, `conversations`, `appointments`; o número de rastreamento que o Ads usa; o evento `atendimento.concluido` para o Stars | O Stars (vem antes dele); nunca depois do Ads |
| Radar Ads | Núcleo (Cartógrafo para termos e raio) mais a Fundação Telefonia | O Extrato de Mídia para o Fechamento | Nada: só depois da Fundação Telefonia; a Recepcionista é recomendada, não obrigatória |
| A suíte | Os cinco | O bundle, a proposta de expansão, o custo por módulo | Nada: nunca antes de os cinco fecharem piloto |

**Quando faz sentido inverter**

1. **Chat antes de Stars** — Quando a praça pede atendimento: donos que perdem ligação na hora do almoço e mensagem à noite, como oficinas e clínicas. A Fundação Meta para clientes é montada dentro da Fase 3 (o que a leva de quatro para cinco semanas) e o Stars, depois, é uma semana: só o gatilho, o modelo e o Boletim de Reputação novo.
2. **Stars antes da Fase 1** — Quando a praça tem nota baixa e o comercial vende reputação antes de vender território. O Stars não depende de nada além da Fundação Meta; a Fase 1 espera e nada quebra.
3. **Menu sozinho, antes da Concorrência** — Quando o piloto é de alimentação e o cardápio dentro da busca é o que o dono quer ver primeiro. A Fase 1 se parte em duas semanas de Menu e duas de Concorrência; a Sentinela pode esperar.
4. **Ads sem Chat** — Quando um cliente quer verba e não quer atendimento automático. Monta-se só a Fundação Telefonia (número, encaminhamento, `calls`), sem Recepcionista nem Resgate; o Ads roda em cima dela. O custo do tenant sobe R$ 5 pela telefonia e R$ 5 pelo Ads, sem o resto do Chat.
5. **O que nunca inverte** — Ads antes da telefonia (sem atribuição, o Extrato de Mídia vira chute); qualquer módulo antes do núcleo estar vivo com piloto fechado; a suíte antes de os cinco fecharem piloto; venda de módulo antes do piloto dele.

**Três caminhos**

- **Caminho A · O padrão** — 1, 2, 3, 4, 5. Menor acesso primeiro, as duas fundações no meio, a mídia depois do telefone, a suíte por último. É o caminho deste documento e o de menor risco com um engenheiro.
- **Caminho B · Atendimento primeiro** — 3 (com a Fundação Meta dentro), 2, 1, 4, 5. Para praças de oficina e clínica, onde a ligação perdida e a mensagem de domingo doem mais que a posição. O Chat leva cinco semanas; o Stars, uma.
- **Caminho C · Reputação primeiro** — 2, 1, 3, 4, 5. Para praças com nota baixa ou poucas avaliações, onde o convite pós-atendimento é o argumento de venda. A Fundação Meta sobe uma fase e o Chat continua herdando.

*Capítulo IV · O que não muda*

## O QUE NÃO MUDA EM NENHUMA FASE

Dez regras que nenhum módulo negocia. Se um módulo precisar de uma exceção para funcionar, o módulo está errado, não a regra.

1. **Nenhuma métrica de conversão ou receita atribuída (D5)** — O Extrato de Mídia mostra custo por contato por campanha, nunca vendas; a Recepcionista conta horários marcados, não fechamentos; a proposta de expansão faz conta de equilíbrio, não previsão; o Boletim de Reputação conta convites, não "taxa de sucesso". Em nenhuma fase existe "novos clientes", "receita gerada" ou ROI.
2. **Gemini é o cérebro de dados e de Google** — Sentinela em Gemini Pro, Recepcionista em Gemini Flash, Estrategista em Gemini Pro; extração, medição, classificação e qualquer decisão de API do Google passam pelo Gemini. Outros cérebros só para linguagem, atrás da LLMGateway, escolhidos pela avaliação cega mensal.
3. **Nunca a senha do cliente** — Gerente no perfil, Embedded Signup com código digitado pelo cliente, vinculação por convite na MCC, cartão digitado no provedor ou no Google. Nenhum módulo pede senha; se um dia pedir, é golpe.
4. **Zero tempo do dono** — Os únicos minutos são no Dia 0, que com a suíte usa os quinze inteiros. Ligar um módulo é uma pergunta de Sim ou Não mais o toque do acesso novo. Nenhuma fase cria reunião, relatório longo ou tarefa para o dono.
5. **Diário de Bordo append-only com print** — Toda ação de todo módulo: convite, mensagem de resgate, ajuste de campanha, oferta relâmpago, item de catálogo. Coluna `modulo`, mesma tabela, mesma prova.
6. **Custo por cliente é métrica de primeira classe** — Alerta em R$ 25 no núcleo, mais o acréscimo declarado de cada módulo ativo, até R$ 40 na suíte. Acima do alerta, o runbook de custo; nunca "depois a gente vê".
7. **A trava de zona** — No máximo duas empresas por segmento por zona, verificada antes da venda e em código. Vale para a suíte inteira; com o Ads, a máquina não coloca dois tenants da mesma zona e segmento nos mesmos termos e raio: o segundo recebe termos e raio distintos ou espera.
8. **Sem raspagem do Google** — Concorrência usa só a Places API dentro dos termos: sem extração em massa, snapshots de 30 dias, só `place_id` fica. Se um dia a Places não bastar, o módulo espera uma fonte oficial; não raspa.
9. **Só avaliações reais** — Stars convida depois de atendimento real, com consentimento, sem incentivo, sem seleção, sem pedir nota. A resposta continua verdadeira, sem dados do avaliador. Suspeita de avaliação falsa vai para o Guardião denunciar, em qualquer fase.
10. **Frescor honesto** — Métricas do Google sempre com data de referência; dado próprio em até uma hora; tempo real só onde existe de verdade (chamadas e conversas, a partir do Chat). Nenhuma tela mistura os três sem dizer qual é qual.

*Encerramento*

## O NÚCLEO PRIMEIRO, O RESTO POR MÓDULO {.fecho}

*O Radar Urbano vende primeiro o que cabe em quinze minutos e um papel Gerente. Os outros cinco pilares entram na ordem em que pedem menos do cliente e devolvem mais para os que vêm depois: o bairro e a vitrine, o convite, o atendimento e o telefone, a mídia, a suíte. Cada um liga por tenant, com as próprias peças, sem tocar no núcleo, e só se vende depois do piloto. As regras não mudam em nenhuma fase. O que muda é quanto da máquina cada cliente quer ligar.*

Radar Urbano
