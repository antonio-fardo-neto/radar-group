# Radar Urbano · Mapa de Entregas

Onze entregas: dois objetos de entrada (uma vez) e nove recorrentes. Preço R$ 499/mês (R$ 16,63/dia), mensal, cancelável, sem verba de mídia. Promessa: captura de intenção otimizada, lucrativa e eficiente. Nunca conversão, receita atribuída ou "novos clientes".

## 1. Regra do zero

1. **Zero reuniões**: o único tempo do dono são até 15 minutos do Dia 0 (roteiro real fecha em cerca de dez).
2. **Zero login obrigatório**: tudo chega pelo WhatsApp do dono, vindo do número da casa; dashboard opcional; SAIR interrompe os envios, o trabalho no perfil continua.
3. **Zero aprovação**: posts, fotos, horários, descrição, serviços, atributos e respostas são pré-autorizados no Dia 0; categoria principal, nome, endereço e ofertas chegam como pergunta Sim/Não.
4. **Zero relatório longo**: nada passa de 60 s de áudio ou uma página; dados do Google com data de referência, dados próprios de hora em hora.
5. **Zero surpresa**: toda ação entra no Diário de Bordo (append-only, com print) antes de qualquer resumo; o Guardião audita por amostragem.
6. **Zero cobrança de esforço**: a máquina nunca pede foto, texto, tabela ou senha; entra como Gerente do Perfil da Empresa e sai quando o dono quiser.

## 2. Tabela-mestre

| Nº | Entrega | Grupo | Quando | Por onde chega | Quem faz |
|---|---|---|---|---|---|
| 01 | Diagnóstico de Posição | Entrada | Dia 0, minutos depois do acesso | Card no WhatsApp; PDF de uma página no dashboard | Cartógrafo + Editor + Redator-chefe |
| 02 | Antes e Depois do Perfil | Entrada | Dia 7 (a partir de `created`) | Card lado a lado no WhatsApp; arquivo no dashboard | Editor + Cartógrafo |
| 03 | Dashboard Radar | Vendas & Performance | A cada hora; Google com data de referência | Link fixo no WhatsApp, ícone no celular; senha opcional | Tesoureiro |
| 04 | Boletim de Segunda | Vendas & Performance | Segunda, 7h | Áudio ≤ 60 s + card no WhatsApp | Redator-chefe |
| 05 | Mapa de Domínio | Vendas & Performance | Mensal, dia 1 (reduzido no Dia 0 e dia 7) | Imagem no WhatsApp; interativo no dashboard | Cartógrafo |
| 06 | Diário de Bordo do Perfil | Vendas & Performance | Contínuo | Seção do dashboard; linha no WhatsApp quando relevante | Editor |
| 07 | Motor de Reputação | Vendas & Performance | Respostas ≤ 2 h; Boletim de Reputação dia 1 | Respostas no Google; card no WhatsApp; QR em PDF | Anfitrião |
| 08 | Extrato de Demanda | Controladoria & Eficiência | Mensal, dia 1 | PDF de uma página no WhatsApp; série no dashboard | Tesoureiro |
| 09 | Horas Devolvidas | Controladoria & Eficiência | Mensal, dia 1 | Card no WhatsApp | Tesoureiro |
| 10 | Voz do Cliente | Controladoria & Eficiência | Mensal, dia 1; alerta quando um tema dispara | Card no WhatsApp | Anfitrião + Redator-chefe |
| 11 | Fechamento Executivo | Controladoria & Eficiência | Mensal, dia 1; trimestral | PDF no WhatsApp; arquivo permanente no dashboard | Redator-chefe |

Horários de envio: Boletim segunda 7h; dia 1 e dia 7 até as 8h; linhas de uma frase e perguntas Sim/Não só das 8h às 19h. Reenvio se o WhatsApp não confirmar em 2 h, sem duplicar.

## 3. As entregas

### 01 Diagnóstico de Posição

Assim que o dono adiciona o Radar Urbano como Gerente, a máquina mede 2–3 termos-chave em nove pontos, audita a completude do perfil e manda o card na mesma conversa. É a referência de todo Antes e Depois.

- Contém: mapa reduzido (verde, cinza, vermelho); auditoria campo a campo (categorias, descrição, horários e feriados, serviços, atributos, fotos, posts, perguntas e avaliações sem resposta, telefone, site, verificação); três frases (onde está, o que falta, o que a máquina faz primeiro); data e hora.
- Gera a lista de tarefas da primeira semana.
- Único toque do dono: adicionar o e-mail operacional como Gerente. Nunca senha. Perfil não verificado: passo a passo, o resto não espera.

### 02 Antes e Depois do Perfil

Perfil do Dia 0 à esquerda, do dia 7 à direita, campo a campo, com a segunda medição reduzida nos mesmos termos e pontos.

- Contém: diff de `profile_audits` (campo, antes, depois, origem); segunda medição com as duas datas; pendência do Dia 0, se houver, como uma única pergunta Sim/Não.
- O card diz que uma semana raramente mexe posição; o que mudou foi o perfil.
- Categorias secundárias só com dois olhos humanos; principal só com Sim do dono.

### 03 Dashboard Radar

Painel aberto pelo link fixo (com token; vira ícone no celular). Sem menu, filtro ou configuração.

- Contém: contatos (ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil, total, seta semanal); impressões e palavras-chave de descoberta; posição nos termos-chave (sábado) com link para o mapa; reputação (nota, avaliações, novas, respondidas, tempo mediano, perguntas); Diário com prints; custo por contato até a data de referência.
- Dois relógios ditos na tela: Google com data de referência ("dados do Google até quinta, 10"), coleta diária 3h (D-3..D-1); dados próprios de hora em hora. Sem tempo real.
- Rodapé: "ligações pelo perfil" são toques no botão Ligar contados pelo Google, não ligações atendidas.
- Senha opcional criada pelo dono; link mágico entra sem senha; ninguém do Radar Urbano vê a senha.
- Números só de SQL; o cérebro escreve três frases de contexto, após conferir.

### 04 Boletim de Segunda

Áudio de até 60 s com a voz da casa e card de uma tela, toda segunda às 7h, inclusive feriado.

- Contém: frase da semana coberta (Google até a data de referência, tipicamente quinta ou sexta anterior); os quatro contatos; avaliações novas e respondidas; posição nos termos-chave (sábado 3h); ações do Diário; o que vem. Card com seta semanal e data de referência.
- Segunda 4h post; 6h Redator-chefe confere cada número contra o banco e escreve no tom do Dia 0; TTS grava (Chirp 3 HD pt-BR, `voice_id` fixo, OGG/Opus); 7h envio.
- Janela de 24 h fechada: modelo `boletim_segunda` (card + voz em MP4); aberta: card PNG e áudio OGG livres.
- Primeira semana incompleta: o Boletim vem e diz quantos dias cobre.

### 05 Mapa de Domínio

Posição da empresa por termo, ponto a ponto, em grade 3×3 (raio de bairro) a 5×5 (região maior). Um mapa por termo e um resumo: pontos verdes de pontos medidos, contra o mês anterior.

- Cores: verde = top 3; cinza = 4º a 10º; vermelho = fora do top 10 ou não encontrado no top 20.
- Sem comparação nominal com concorrentes; só a posição do cliente.
- Rodapé de método: `places:searchText` com `locationBias` por ponto, proxy da lista local; validação mensal com 20 buscas manuais. Data e hora de cada medição.
- Places API dentro dos termos: nada guardado além de 30 dias exceto `place_id`; a medição própria (data, termo, ponto, posição) fica na série. Sem raspagem.
- Cadência: Dia 0 e dia 7 reduzido (termos-chave, 9 pontos); sábado 3h reduzido (alimenta Boletim e dashboard, não vira mapa); dia 1 2h completo.
- Termos vermelhos viram `editor.tasks`.

### 06 Diário de Bordo do Perfil

Registro append-only de toda ação no perfil: data, hora, agente, campo, antes, depois, print. Nada entra no perfil sem linha; nada some.

- Post semanal segunda 4h, com foto real do perfil ou enviada pelo dono. Nunca gerar foto do estabelecimento; nunca pedir.
- Fotos existentes avaliadas (nitidez, luz, atualidade) para capa e destaques; novas publicadas no mesmo dia.
- Descrição (limite 750 caracteres), serviços (lista, sem preço) e atributos escritos para os termos que trazem cliente; revistos por tarefa do Cartógrafo e na auditoria do dia 1.
- Feriados: checagem diária 5h; tabela própria de feriados nacionais e municipais por cidade; 72 h antes, horário especial no perfil e post de aviso, pela regra do dono (fecha, meio período, normal); na dúvida, pergunta Sim/Não também 72 h antes.
- Categorias sempre com dois olhos; principal só com Sim do dono. Nunca termos de busca no nome.
- Linha no WhatsApp só para ação relevante (feriado, descrição reescrita, capa trocada), em horário comercial. Post de rotina não gera mensagem.
- Respostas a perguntas do perfil também registradas aqui.

### 07 Motor de Reputação

Polling de avaliações e perguntas a cada 30 min. Resposta humanizada e específica a toda avaliação em até 2 h; perguntas públicas em menos de 4 h. Boletim de Reputação no dia 1. QR para o balcão.

- Contém: respostas no próprio Google, no tom da casa; link curto oficial "Receber mais avaliações" e QR em PDF para balcão, comanda ou porta (gerado na segunda semana; reenviado a pedido); Boletim de Reputação (nota, novas, respondidas e em quanto tempo, temas elogiados e de atenção, perguntas respondidas).
- Notas 1 e 2 passam pelo Guardião em qualquer patamar, ainda dentro das 2 h.
- Sem dado do avaliador na resposta; texto não armazenado (hash, temas, sentimento).
- Só avaliações reais: sem incentivo, sem seleção, sem convite ativo por mensagem.
- Avaliação suspeita (perfil recém-criado, texto repetido, série de notas baixas no mesmo dia) vira sinal para o Guardião denunciar pelo canal oficial; a máquina não discute em público.
- Verificação da política de conteúdo do Google antes de publicar. SLO: mediana < 2 h, 100% em 24 h; perguntas < 4 h.

### 08 Extrato de Demanda

Uma página por mês só com o que se conta. Custo por contato = R$ 499 ÷ contatos do mês. O dono coloca o valor dele por cima.

- Contém: quatro linhas e a soma (ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil); custo por contato; contexto fora da soma (impressões na Busca e no Maps, dez palavras-chave); série de seis meses.
- Explicar uma vez: ligações pelo perfil são toques no botão Ligar, não ligações atendidas; mensagens pelo perfil só existem se o dono mantém o chat do perfil ligado.
- Data de referência na página; correção posterior do Google corrige a série e diz quando.
- Coleta diária 3h (`getDailyMetricsTimeSeries`); extrato fechado dia 1 5h; números só de SQL. Sem conversão presumida.

### 09 Horas Devolvidas

Trabalho executado, tirado linha a linha do Diário e convertido em tempo humano por tabela fixa (rodapé do card; não muda no meio do mês). Comparado com o tempo do dono: os minutos das respostas Sim/Não registradas.

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

- Nenhuma hora sem linha de Diário com print.
- Exemplo (clínica): 8 posts (2h40) · 6 fotos (1h) · 27 avaliações (2h42) · 5 perguntas (20 min) · 4 ajustes (40 min) · 240 medições (2h) · auditoria (1h) · boletins, extratos, mapa e fechamento (3h45) = 14h07; tempo da dona: 2 min. Frase de balcão: "catorze horas por R$ 499".

### 10 Voz do Cliente

Todas as avaliações e perguntas públicas do mês classificadas por tema e sentimento. Só avaliações e perguntas; a máquina não lê conversa de ninguém.

- Contém: três elogios e três atritos mais recorrentes, cada um com frequência e uma frase real sem nome; histórico mês a mês no dashboard.
- Atrito resolvível no perfil (horário, informação faltando, serviço não listado): corrigido e avisado no card. Atrito de operação: só mostrado.
- Alerta de uma linha quando o mesmo atrito aparece 3 vezes em 7 dias.
- Armazenado: tema, sentimento e hash; nunca texto nem nome. Classificação em lote noturno (Gemini Flash).

### 11 Fechamento Executivo

Uma página em PDF, o último envio da manhã do dia 1. Trimestral no dia 1 de cada terceiro mês, junto com o mensal.

- Contém: quatro contatos e total contra o mês anterior; impressões; custo por contato; nota e avaliações; Mapa de Domínio em miniatura (pontos verdes por termo contra o mês anterior); horas devolvidas; o que a máquina fez (Diário) e vai fazer (tarefas ao Editor); data de referência no rodapé.
- Trimestral: três meses lado a lado e a curva desde o Dia 0 (contatos, custo por contato, pontos verdes, nota).
- Cada número conferido contra o banco antes de escrever.
- Sem cópia automática a terceiros: o dono encaminha o PDF a quem quiser.

## 4. Calendário

| Período | O que acontece |
|---|---|
| Dia 0 | Antes, fora dos 15 min: `zone.check`, contrato por link, cartão no provedor. Min 0–5: cinco perguntas por áudio. Min 5–8: Gerente no perfil. Min 8–10: link do dashboard, senha opcional, Diagnóstico. Opt-in registrado com hora no Sim final. |
| Semana 1 | Perfil auditado e corrigido; feriados do ano na agenda. Dashboard no ar; Google entra na madrugada seguinte. Reputação ligada: pendências antigas respondidas. Primeiro sábado 3h: medição reduzida. Dia 7: Antes e Depois. |
| Semana 2 | Primeiro Boletim com semana fechada. Post semanal em ritmo. QR em PDF. Segunda medição de sábado. |
| Semana 3 | Série de posição com 4–5 pontos; vermelhos viram tarefas do Editor. Primeiro feriado tratado 72 h antes, se houver. Lote noturno classificando temas; primeiro alerta, se houver. |
| Semana 4 | Dia 1, 2h–8h: medição completa, auditoria, extratos, cards, PDFs, envios. Chegam as seis entregas mensais. |
| Mês 2 | Termos novos testados; esforço movido para o vermelho. Segunda auditoria. Voz do Cliente orienta correções; Extrato ganha o segundo ponto. |
| Mês 3 | Primeiro Fechamento Trimestral. Comparativo de território desde o Diagnóstico. Proposta de novos termos e raio (raio maior passa por `zone.check`). |
| Permanente | 30 min: avaliações e perguntas. Hora: dashboard. Diário 3h coleta; 5h feriados. Segunda 4h post, 7h Boletim. Sábado 3h medição. Dia 1: seis entregas. Trimestral: Fechamento Trimestral. Domingo: nada chega. |

## 5. A máquina

Cinco agentes e um humano com painel. Gemini obrigatório para tudo que mede, lê ou escreve no Google; linguagem pode vir de outro modelo, atrás do `LLMGateway`.

| Nome | Missão | Gatilhos |
|---|---|---|
| Cartógrafo | Mede posição por termo e ponto (Places API), desenha o Mapa de Domínio, faz o Diagnóstico, diz ao Editor o que otimizar | Dia 0, dia 7, sábado 3h (reduzida); dia 1 2h (completa) |
| Editor | Mantém o perfil vivo: post, fotos, descrição, horários e feriados, serviços, atributos, auditoria; categoria só com Guardião | Segunda 4h, diário 5h, `editor.tasks`, dia 1 |
| Anfitrião | Responde avaliações (≤ 2 h) e perguntas (< 4 h), classifica tema e sentimento, sinaliza avaliação suspeita, gera QR, escreve o Boletim de Reputação | 30 min, lote noturno, dia 1 |
| Tesoureiro | Consolida em número: coleta do Performance API, dashboard, Extrato, Horas Devolvidas, custo por contato e por tenant; só SQL | Hora, diário 3h, dia 1 5h |
| Redator-chefe | Dado em 60 s de áudio e uma página: Diagnóstico, Boletim, Voz do Cliente, Fechamento mensal e trimestral; confere números antes; lembra pendências com pergunta | Segunda 6h, dia 1 6h, trimestral |
| Guardião (humano) | Aprova em lote, audita 10% no P2, trata exceções; dois olhos para categoria, nome, endereço e notas ≤ 2; denuncia avaliação falsa; atende texto livre do dono | Contínuo |

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

- No máximo 2 empresas do mesmo segmento por zona. Segmento = categoria principal do perfil. Zona = bairro do Google Maps ou raio equivalente, escrita no contrato com cidade e segmento.
- Motivo: três posições na primeira tela da busca local; perfis concorrentes na mesma malha disputam as mesmas posições e degradam o resultado de ambos.
- `zone.check` antes da proposta e de novo na assinatura. Resposta: livre (0 ou 1 de 2) ou lotada (2 de 2, fila).
- Conversa não reserva; proposta escrita reserva por 5 dias úteis; a vaga só se ocupa na assinatura (transação em `zones`).
- Fila por ordem de chegada; ninguém fura, nem cliente antigo. Quem sai libera a vaga no encerramento.
- Mudança de endereço, categoria principal ou raio roda a verificação de novo. Com vaga: aditivo e vaga antiga liberada no dia. Sem vaga: opera até o fim do ciclo pago e entra na fila da zona nova; o endereço no perfil muda mesmo assim. Zona redesenhada: quem está, fica.
- Cláusula de exclusividade limitada no contrato; o cliente pode perguntar quantos há na zona dele. Nada disso muda a mensalidade.

## 8. Por que fecha

1. O valor chega antes da fatura: Diagnóstico no Dia 0, Antes e Depois no dia 7, conta completa no dia 1.
2. Toda entrega é tangível (áudio, card, mapa, extrato, PDF), com a data do dado impressa.
3. Tempo do dono é zero por arquitetura: nunca insumo, reunião, relatório ou senha; só perguntas Sim/Não.
4. A promessa é só o que se conta e se confere no Google: contatos e custo por contato, nunca conversão ou venda.
5. Cancelar custa mais do que ficar: perfil parado, avaliações sem resposta, mapa e extrato somem, e a vaga na zona abre para o vizinho.
