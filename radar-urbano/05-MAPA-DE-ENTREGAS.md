# Radar Urbano · Mapa de Entregas

Onze entregas: dois objetos de entrada (uma vez) e nove recorrentes. Preço R$ 499/mês (R$ 16,63/dia), mensal, cancelável, sem verba de mídia. Promessa: captura de intenção otimizada, lucrativa e eficiente. Nunca conversão, receita atribuída ou "novos clientes".

## 1. Regra do zero

Vale para as onze entregas. Se uma entrega viola uma regra, a entrega está errada.

1. **Zero reuniões**: o único tempo do dono são até 15 minutos do Dia 0 (roteiro real fecha em cerca de dez; cinco de folga).
2. **Zero login obrigatório**: tudo chega pelo WhatsApp do dono, vindo do número da casa (o número do Radar Urbano); dashboard é opcional; SAIR interrompe os envios, o trabalho no perfil continua.
3. **Zero aprovação**: posts, fotos, horários, descrição, serviços, atributos, respostas a avaliações e perguntas são pré-autorizados no Dia 0; categoria principal, nome, endereço e ofertas chegam como pergunta Sim/Não.
4. **Zero relatório longo**: nenhuma entrega passa de 60 s de áudio ou uma página; dados do Google com data de referência, dados próprios de hora em hora.
5. **Zero surpresa**: toda ação entra no Diário de Bordo (append-only, com print) antes de qualquer resumo; o Guardião audita por amostragem.
6. **Zero cobrança de esforço**: a máquina nunca pede foto, texto, tabela ou senha; entra como Gerente do Perfil da Empresa e sai quando o dono quiser.

## 2. Tabela-mestre

| Nº | Entrega | Grupo | Quando | Por onde chega | Quem faz |
|---|---|---|---|---|---|
| 01 | Diagnóstico de Posição | Entrada | Dia 0, minutos depois do acesso | Card no WhatsApp; PDF de uma página no dashboard | Cartógrafo + Editor + Redator-chefe |
| 02 | Antes e Depois do Perfil | Entrada | Dia 7 (a partir de `created`), automático | Card lado a lado no WhatsApp; arquivo no dashboard | Editor + Cartógrafo |
| 03 | Dashboard Radar | Vendas & Performance | A cada hora; Google com data de referência | Link fixo no WhatsApp, ícone no celular; senha opcional | Tesoureiro |
| 04 | Boletim de Segunda | Vendas & Performance | Segunda, 7h | Áudio ≤ 60 s + card no WhatsApp | Redator-chefe (dados do Tesoureiro e Cartógrafo) |
| 05 | Mapa de Domínio | Vendas & Performance | Mensal, dia 1 (reduzido no Dia 0 e dia 7) | Imagem no WhatsApp; interativo no dashboard | Cartógrafo |
| 06 | Diário de Bordo do Perfil | Vendas & Performance | Contínuo | Seção do dashboard; linha no WhatsApp quando relevante | Editor (Cartógrafo diz o que otimizar) |
| 07 | Motor de Reputação | Vendas & Performance | Respostas ≤ 2 h; Boletim de Reputação dia 1 | Respostas no Google; card no WhatsApp; QR em PDF | Anfitrião |
| 08 | Extrato de Demanda | Controladoria & Eficiência | Mensal, dia 1 | PDF de uma página no WhatsApp; série no dashboard | Tesoureiro |
| 09 | Horas Devolvidas | Controladoria & Eficiência | Mensal, dia 1 | Card no WhatsApp | Tesoureiro (a partir do Diário) |
| 10 | Voz do Cliente | Controladoria & Eficiência | Mensal, dia 1; alerta quando um tema dispara | Card no WhatsApp | Anfitrião classifica; Redator-chefe sintetiza |
| 11 | Fechamento Executivo | Controladoria & Eficiência | Mensal, dia 1; trimestral | PDF no WhatsApp; arquivo permanente no dashboard | Redator-chefe (com Tesoureiro e Cartógrafo) |

Envios ao dono: Boletim segunda 7h; entregas do dia 1 e do dia 7 até as 8h; linhas de uma frase e perguntas Sim/Não só em horário comercial (8h–19h). Reenvio automático se o WhatsApp não confirmar entrega em 2 h, sem duplicar.

## 3. As entregas

### 01 Diagnóstico de Posição

Assim que o dono adiciona o Radar Urbano como Gerente, a máquina mede 2–3 termos-chave (da primeira pergunta do Dia 0) em nove pontos e audita a completude do perfil. O card chega na mesma conversa. É a referência de todo Antes e Depois.

Contém:
- Mapa reduzido dos termos-chave em 9 pontos (verde, cinza, vermelho).
- Auditoria campo a campo: categorias, descrição, horários (inclusive feriados), serviços, atributos, fotos (quantas, de quando), posts, perguntas e avaliações sem resposta, telefone, site, status de verificação.
- Três frases: onde está, o que falta, o que a máquina faz primeiro.
- Data e hora da medição.

Regras:
- Medição reduzida pela Places API; gera a lista de tarefas da primeira semana.
- Único toque do dono: adicionar o e-mail operacional como Gerente. Nunca senha.
- Perfil não verificado: chega o passo a passo; o resto não espera.

### 02 Antes e Depois do Perfil

No dia 7, o perfil do Dia 0 à esquerda e o do dia 7 à direita, campo a campo, com a segunda medição reduzida nos mesmos termos e pontos.

Contém:
- Diff do perfil a partir de `profile_audits` (campo, antes, depois, origem).
- Segunda medição reduzida, com as duas datas.
- Pendência do Dia 0 (ex.: verificação), se houver, como uma única pergunta Sim/Não no fim.

Regras:
- Dia 7 conta a partir de `created`, seja que dia da semana for.
- O card diz que uma semana raramente mexe posição; o que mudou foi o perfil.
- Categorias secundárias entram só com dois olhos humanos; principal só com Sim do dono.

### 03 Dashboard Radar

Painel aberto pelo link fixo (com token; vira ícone no celular). Sem menu, filtro ou configuração.

Contém:
- Contatos: ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil, total, seta contra a semana anterior.
- Contexto: impressões na Busca e no Maps; palavras-chave de descoberta.
- Posição nos termos-chave (medição de sábado) com link para o mapa interativo.
- Reputação: nota, avaliações, novas, respondidas, tempo mediano de resposta, perguntas respondidas.
- Diário de Bordo com prints; custo por contato do mês até a data de referência.

Regras:
- Dois relógios ditos na tela: Google com data de referência ("dados do Google até quinta, 10"), coletado todo dia 3h (D-3..D-1); dados próprios de hora em hora. Sem número em tempo real.
- Rodapé: "ligações pelo perfil" são toques no botão Ligar contados pelo Google, não ligações atendidas.
- Senha opcional, criada pelo dono no primeiro acesso; link mágico entra sem senha; ninguém do Radar Urbano vê a senha.
- Todo número vem de SQL; o cérebro só escreve as três frases de contexto, após conferir.

### 04 Boletim de Segunda

Áudio de até 60 s com a voz da casa e card de uma tela, toda segunda às 7h, inclusive feriado.

Contém:
- Frase que declara a semana coberta (dados do Google até a data de referência, tipicamente quinta ou sexta anterior).
- Ligações pelo perfil, rotas, cliques no site, mensagens; avaliações novas e respondidas.
- Posição nos termos-chave (medição de sábado 3h).
- Ações do Diário; o que vem nos próximos sete dias.
- Card com os mesmos números, seta contra a semana anterior, data de referência no rodapé.

Regras:
- Segunda 4h post do Editor; 6h Redator-chefe confere cada número contra o banco e escreve no tom do Dia 0; TTS grava (Chirp 3 HD pt-BR, `voice_id` fixo, OGG/Opus); 7h envio.
- Janela de 24 h fechada: modelo `boletim_segunda` (card + voz em MP4); aberta: card PNG e áudio OGG livres.
- Primeira segunda antes de fechar a semana: o Boletim vem e diz quantos dias cobre.

### 05 Mapa de Domínio

Posição da empresa por termo, ponto a ponto, em grade 3×3 (raio de bairro) a 5×5 (região maior). Um mapa por termo e um resumo: pontos verdes de pontos medidos, contra o mês anterior.

Contém:
- Mapa por termo-chave (imagem); todos os termos, ponto clicável e série mensal no dashboard.
- Termos que subiram, desceram ou entraram no top 3; o que a máquina fará sobre o vermelho no mês.
- Rodapé de método e data/hora de cada medição.

Regras:
- Cores: verde = top 3; cinza = 4º a 10º; vermelho = fora do top 10 ou não encontrado no top 20.
- Sem comparação nominal com concorrentes; o mapa mostra só a posição do cliente.
- Método declarado: `places:searchText` com `locationBias` por ponto, como proxy da lista local; validação mensal com 20 buscas manuais.
- Places API dentro dos termos: nada guardado além de 30 dias exceto `place_id`; medição própria (data, termo, ponto, posição) fica na série. Sem raspagem.
- Cadência: Dia 0 e dia 7 reduzido (termos-chave, 9 pontos); sábado 3h reduzido (alimenta Boletim e dashboard, não vira mapa); dia 1 2h completo.
- Cartógrafo gera `editor.tasks` para os vermelhos.

### 06 Diário de Bordo do Perfil

Registro append-only de toda ação no perfil: data, hora, agente, campo, antes, depois, print. Nada entra no perfil sem linha; nada some.

Contém:
- Post semanal (segunda 4h) com foto real do perfil ou enviada pelo dono.
- Fotos existentes avaliadas (nitidez, luz, atualidade) para capa e destaques; novas publicadas no mesmo dia.
- Descrição, serviços e atributos escritos para os termos que trazem cliente; revistos por tarefa do Cartógrafo e na auditoria do dia 1.
- Horários e feriados; categorias; respostas a perguntas do perfil (Anfitrião registra aqui).

Regras:
- Nunca gerar foto do estabelecimento; nunca pedir foto.
- Descrição: limite de 750 caracteres.
- Feriados: checagem diária 5h; tabela própria de feriados nacionais e municipais por cidade; 72 h antes, horário especial no perfil e post de aviso; regra do dono do Dia 0 (fecha, meio período, normal); na dúvida, pergunta Sim/Não também 72 h antes.
- Categorias sempre com dois olhos; principal só com Sim do dono. Nunca termos de busca no nome.
- Linha no WhatsApp só para ação relevante (feriado, descrição reescrita, capa trocada), em horário comercial; post de rotina não gera mensagem.
- Serviços em lista, sem catálogo com preço.

### 07 Motor de Reputação

Polling de avaliações e perguntas a cada 30 min. Resposta humanizada e específica a toda avaliação em até 2 h; perguntas públicas em menos de 4 h. Boletim de Reputação no dia 1. Material de QR para o balcão.

Contém:
- Respostas no próprio Google, no tom da casa, citando o que a pessoa disse.
- Link curto oficial "Receber mais avaliações" e QR em PDF para balcão, comanda ou porta (gerado na segunda semana; reenviado a pedido).
- Boletim de Reputação: nota, novas avaliações, respondidas e em quanto tempo, temas elogiados, temas de atenção, perguntas respondidas.
- Sinal de avaliação suspeita (perfil recém-criado, texto repetido, série de notas baixas no mesmo dia) para o Guardião denunciar pelo canal oficial.

Regras:
- Notas 1 e 2 passam pelo Guardião em qualquer patamar, ainda dentro das 2 h.
- Sem dado do avaliador na resposta; texto não é armazenado (só hash, temas, sentimento).
- Só avaliações reais: sem incentivo, sem seleção, sem convite ativo por mensagem.
- Verificação de política de conteúdo do Google antes de publicar; a máquina não discute em público.
- SLO: mediana < 2 h, 100% em 24 h; perguntas < 4 h.

### 08 Extrato de Demanda

Uma página por mês só com o que se conta. Custo por contato = R$ 499 ÷ contatos do mês. O dono coloca o valor dele por cima.

Contém:
- Quatro linhas e a soma: ligações pelo perfil, pedidos de rota, cliques no site, mensagens pelo perfil.
- Custo por contato.
- Contexto fora da soma: impressões (Busca e Maps) e as dez palavras-chave de descoberta.
- Série dos últimos seis meses.

Regras:
- Definição de contato: o que o Google conta a partir do perfil. Explicar uma vez que ligações pelo perfil são toques no botão Ligar, não ligações atendidas; mensagens pelo perfil só existem se o dono mantém o chat do perfil ligado.
- Data de referência na página; correção posterior do Google corrige a série e diz quando.
- Coleta diária 3h (`getDailyMetricsTimeSeries`); extrato fechado dia 1 5h; números só de SQL.
- Sem conversão presumida, sem receita atribuída.

### 09 Horas Devolvidas

Contador do trabalho executado, tirado linha a linha do Diário de Bordo e convertido em tempo humano por tabela fixa. Comparado com o tempo do dono: os minutos das respostas Sim/Não registradas.

Tabela de equivalência (rodapé do card; não muda no meio do mês):

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

Regras:
- Nenhuma hora sem linha de Diário com print.
- Exemplo (clínica, um mês): 8 posts (2h40) · 6 fotos (1h) · 27 avaliações (2h42) · 5 perguntas (20 min) · 4 ajustes (40 min) · 240 medições (2h) · auditoria (1h) · boletins, extratos, mapa e fechamento (3h45) = 14h07; tempo da dona: 2 min. Frase de balcão: "catorze horas por R$ 499".

### 10 Voz do Cliente

Leitura de todas as avaliações e perguntas públicas do mês, classificadas por tema e sentimento. Só avaliações e perguntas; a máquina não lê conversa de ninguém.

Contém:
- Três elogios mais recorrentes (proteger) e três atritos mais recorrentes (corrigir), cada um com frequência e uma frase real sem nome do autor.
- Atrito resolvível no perfil (horário, informação faltando, serviço não listado): corrigido e avisado no card. Atrito de operação: só mostrado.
- Histórico mês a mês no dashboard.

Regras:
- Alerta de uma linha quando o mesmo atrito aparece 3 vezes em 7 dias, antes do dia 1.
- Armazenado: tema, sentimento e hash do texto; nunca o texto nem o nome.
- Classificação em lote noturno (Gemini Flash); síntese pelo Redator-chefe.

### 11 Fechamento Executivo

Uma página em PDF no dia 1, último da manhã de entregas. Trimestral no dia 1 de cada terceiro mês, junto com o mensal.

Contém:
- Quatro contatos e total, contra o mês anterior; impressões como contexto; custo por contato.
- Nota e avaliações (novas, respondidas, tempo mediano).
- Mapa de Domínio em miniatura: pontos verdes por termo contra o mês anterior.
- Horas devolvidas; o que a máquina fez (Diário) e o que vai fazer (tarefas do Cartógrafo ao Editor).
- Data de referência do Google no rodapé.
- Trimestral: três meses lado a lado e a curva desde o Dia 0 (contatos, custo por contato, pontos verdes, nota).

Regras:
- Redator-chefe confere cada número contra o banco antes de escrever.
- Sem cópia automática a terceiros: o dono encaminha o PDF a quem quiser.
- Arquivo permanente no dashboard, um por mês.

## 4. Calendário

| Período | O que acontece |
|---|---|
| Dia 0 | Antes (fora dos 15 min): `zone.check`, contrato por link, cartão no provedor. Min 0–5: cinco perguntas por áudio. Min 5–8: Gerente no perfil. Min 8–10: link do dashboard, senha opcional, Diagnóstico de Posição. Opt-in registrado com hora no Sim final. |
| Semana 1 | Perfil auditado e corrigido (serviços, atributos, descrição, feriados do ano, fotos, capa). Dashboard no ar; primeiros números do Google na madrugada seguinte. Reputação ligada no dia 1: avaliações e perguntas paradas respondidas. Primeiro sábado 3h: medição reduzida. Dia 7: Antes e Depois. |
| Semana 2 | Primeiro Boletim com semana inteira fechada. Post semanal em ritmo. Material do QR em PDF. Segunda medição de sábado. |
| Semana 3 | Série de posição com 4–5 pontos; vermelhos viram tarefas do Editor. Primeiro feriado tratado 72 h antes, se houver. Lote noturno classificando temas. Primeiro alerta de tema, se houver. |
| Semana 4 | Dia 1 do mês seguinte, 2h–8h: medição completa, auditoria, extratos, cards, PDFs, envios. Chegam Mapa de Domínio, Boletim de Reputação, Extrato de Demanda, Horas Devolvidas, Voz do Cliente, Fechamento Executivo. |
| Mês 2 | Termos novos testados; esforço movido para o vermelho (descrição, serviços, atributos, posts). Segunda auditoria mensal. Voz do Cliente orienta correções; Extrato ganha o segundo ponto da série. |
| Mês 3 | Primeiro Fechamento Trimestral com a curva desde o Dia 0. Comparativo de território desde o Diagnóstico. Proposta de novos termos e raio (raio maior passa por `zone.check`). |
| Ritmo permanente | 30 min: avaliações e perguntas. Hora: dashboard. Diário 3h: coleta do Google; 5h: horários e feriados. Segunda 4h post, 7h Boletim. Sábado 3h medição reduzida. Dia 1: seis entregas mensais. Trimestral: Fechamento Trimestral. Domingo: nada chega. |

## 5. A máquina

Cinco agentes e um humano com painel. Gemini obrigatório para tudo que mede, lê ou escreve no Google; linguagem pode vir de outro modelo, atrás do `LLMGateway`.

| Nome | Missão | Gatilhos |
|---|---|---|
| Cartógrafo | Mede posição por termo e ponto (Places API), desenha o Mapa de Domínio, faz o Diagnóstico, diz ao Editor o que otimizar | Dia 0 e dia 7 (reduzida), sábado 3h (reduzida), dia 1 2h (completa) |
| Editor | Mantém o perfil vivo: post, fotos, descrição, horários e feriados, serviços, atributos, auditoria de completude; categoria só com Guardião | Segunda 4h, diário 5h, `editor.tasks`, dia 1 |
| Anfitrião | Responde avaliações (≤ 2 h) e perguntas (< 4 h), classifica tema e sentimento, sinaliza avaliação suspeita, gera QR, escreve o Boletim de Reputação | Polling 30 min, lote noturno, dia 1 |
| Tesoureiro | Consolida em número: coleta do Performance API, visões do dashboard, Extrato, Horas Devolvidas, custo por contato e custo por tenant; números só de SQL | Hora, diário 3h, dia 1 5h |
| Redator-chefe | Dado em 60 s de áudio e uma página: três frases do Diagnóstico, Boletim, Voz do Cliente, Fechamento mensal e trimestral; confere números antes; lembra pendências com pergunta | Segunda 6h, dia 1 6h, trimestral |
| Guardião (humano) | Aprova em lote, audita por amostragem (10% no P2), trata exceções; dois olhos para categoria, nome, endereço e notas ≤ 2; denuncia avaliação falsa; atende texto livre do dono | Contínuo |

Patamares: P0 tudo aprovado antes; P1 lote com meta > 85% sem edição; P2 publicação direta com QA de 10%.

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
| Mensalidade | R$ 499 | R$ 499 | R$ 499 |
| **Custo por contato** | **R$ 1,92** | **R$ 2,97** | **R$ 3,12** |

Semana típica da padaria (Boletim): 31 ligações pelo perfil, 22 rotas, 8 cliques no site, 3 avaliações novas respondidas, 1º em "padaria perto de mim" em 7 de 9 pontos, 1 post, feriado ajustado.

## 7. Trava territorial

- No máximo 2 empresas do mesmo segmento por zona. Segmento = categoria principal do perfil no Google. Zona = bairro do Google Maps ou raio equivalente, escrita no contrato com cidade e segmento.
- Motivo: a busca local tem três posições na primeira tela; perfis concorrentes na mesma malha disputam as mesmas posições e degradam o resultado de ambos.
- Verificação (`zone.check`) antes da proposta e de novo na assinatura. Resposta: livre (0 ou 1 de 2) ou lotada (2 de 2, fila).
- Reserva: conversa não reserva; proposta escrita reserva por 5 dias úteis; a vaga só se ocupa na assinatura (transação em `zones`).
- Fila por ordem de chegada; ninguém fura, nem cliente antigo. Quem sai libera a vaga no encerramento.
- Mudança de endereço, categoria principal ou raio roda a verificação de novo. Com vaga: aditivo e vaga antiga liberada no dia. Sem vaga: opera até o fim do ciclo pago e entra na fila da zona nova; o endereço no perfil muda mesmo assim. Zona redesenhada pelo Radar Urbano: quem está, fica.
- Cláusula de exclusividade limitada no contrato; o cliente pode perguntar quantos há na zona dele e ouve o número. Nada disso muda a mensalidade.

## 8. Por que fecha

1. O valor chega antes da fatura: Diagnóstico no Dia 0, Antes e Depois no dia 7, conta completa no dia 1.
2. Toda entrega é tangível (áudio, card, mapa, extrato, PDF), com a data do dado impressa.
3. Tempo do dono é zero por arquitetura: a máquina nunca pede insumo, reunião, relatório ou senha; só perguntas Sim/Não.
4. A promessa é só o que se conta e se confere no Google: contatos e custo por contato, nunca conversão ou venda.
5. Cancelar custa mais do que ficar: perfil parado, avaliações sem resposta, mapa e extrato somem, e a vaga na zona abre para o vizinho.
