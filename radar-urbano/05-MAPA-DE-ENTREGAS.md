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
