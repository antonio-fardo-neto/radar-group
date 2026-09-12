# Radar Urbano · Mapa de Acessos

O que o Radar Urbano precisa do cliente para operar em nome dele. Quatro sistemas, um único papel concedido, nenhuma senha do cliente.

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
| **A · Perfil da Empresa no Google** | Conta Google do cliente, perfil reivindicado e verificado, ele como Proprietário. Perfil de terceiro: Solicitar acesso (3 dias). Não verificado: vídeo, telefone, e-mail ou carta | Gerente para o e-mail operacional (conta única, 2FA, só pelo conector via OAuth `business.manage`). Edita, publica, responde, lê desempenho. Não gerencia usuários, não transfere nem exclui. Categoria principal, nome e endereço: só com Sim do cliente e dois olhos | Maps > Seu perfil comercial > Configurações > Gerentes/Usuários > Adicionar > Gerente > Convidar (ou business.google.com > Usuários). A conta operacional aceita; a máquina localiza o perfil por nome e endereço | Nunca | Cliente remove o usuário na mesma tela. A máquina percebe na chamada seguinte, congela Editor e Anfitrião e avisa o Head de Operação |
| **B · WhatsApp do dono** | Nenhuma conta nova: o número do dono, informado no contrato e confirmado na quinta pergunta do Dia 0. Do lado do Radar Urbano, uma conta na WhatsApp Business Platform com o número da casa | Nenhum. Só recebe. Responde Sim, Não, SAIR ou texto livre (vai a uma pessoa) | Aceite marcado no contrato; abre a conversa pelo link da página (se não abrir em 1 h, o número da casa manda `pergunta_sim_nao` "Podemos começar?"); o Sim ao fim das cinco perguntas é o opt-in, com hora | Nunca | SAIR interrompe na hora, com registro. Não cancela o contrato: entregas ficam no dashboard. Trocar número: quinta pergunta de novo |
| **C · Dashboard Radar** | Criada pelo Radar Urbano no Identity Platform, na ativação | Cliente: leitura de tudo o que é dele. Radar Urbano: nenhum papel na conta dele | Recebe o link fixo com token pelo WhatsApp no minuto 8 do Dia 0 | Nova e opcional, criada pelo cliente por link único (morre após uso), em hash; a operação não lê nem redefine. Sem senha, entra pelo link fixo (mágico) | Cliente pede link novo ou desativa. No encerramento vira arquivo entregue e a conta fecha |
| **D · Contrato, pagamento e nota fiscal** | Cartão na página do provedor; dados fiscais; número e aceite do número da casa marcados no contrato; assinatura digital | Cobrança recorrente de R$ 499/mês, cancelável, sem fidelidade abusiva. O Radar Urbano recebe só o estado da assinatura e os últimos dígitos | Link do contrato (só após o comercial confirmar a vaga na zona) e link do provedor. Cinco minutos, antes da conversa | Nunca | Cancelamento por mensagem ao número da casa ou pelo dashboard, sem multa; encerramento no mesmo dia |

Dados gerados: A, métricas com data de referência (atraso de 2–3 dias), diff com print, avaliações e perguntas só como hash e temas. B, número do dono (hash com sal), nome de tratamento, aceite, status de entrega (reenvio após 2 h). C, aberturas do link, senha em hash. D, estado da assinatura, notas fiscais, contrato, zona e segmento.

Regras de uso: em A, só API oficial; nunca termo de busca no nome, categoria principal sem humano ou foto gerada; perfil `SUSPENDED`/`PENDING_VERIFICATION` congela edição e abre incidente. Em B, só modelos de utilidade aprovados (`boletim_segunda`, `entrega_radar`, `entrega_radar_pdf`, `pergunta_sim_nao`, `aviso_radar`), rodapé "Responda SAIR para parar", cerca de 25 mensagens/mês. Horários: Boletim segunda 7h; dia 1 e dia 7 até 8h; `aviso_radar` e perguntas Sim/Não só das 8h às 19h; lembrete de pendência no máximo semanal.

## 3. Base legal (pauta para o advogado)

Pauta, não parecer. Nenhum cliente entra antes da revisão do jurídico externo.

1. **Mandato de operação.** Publicar, editar e responder em nome da empresa no Perfil da Empresa. Sem perguntar: posts com foto real, fotos existentes, descrição (750 caracteres), horários e feriados (72 h antes), serviços sem preço, atributos, respostas a avaliações e perguntas. Com Sim registrado: categoria principal, nome, endereço, ofertas. Nunca: prometer posição ou resultado, incentivo por avaliação, termo de busca no nome, imagem gerada. Sem mandato de atendimento, anúncio ou mensagem a clientes finais. O Sim pelo WhatsApp vale como autorização por escrito.
2. **LGPD.** Cliente controlador do que a máquina trata em nome dele; Radar Urbano operador, e controlador dos dados cadastrais do dono (nome e número, hash na base analítica). Textos públicos de avaliações e perguntas: só para responder e classificar, guardados como hash e temas; nome do avaliador nunca em resposta ou card. Nenhum dado de cliente final. Suboperadores: Google Cloud e APIs do Google; Meta (só número da casa); provedor do cérebro de linguagem; provedor de pagamento. Hospedagem em São Paulo; Meta e provedor de linguagem podem tratar fora do Brasil: prever transferência internacional. Retenção: `actions_log` 5 anos; `llm_calls` 12 meses; dados do tenant contrato + 90 dias; respostas da Places API 30 dias (só `place_id` fica; posição do próprio cliente é medição própria); áudio do Dia 0 apagado 7 dias após confirmação escrita. Pedidos de titular respondidos em 15 dias. Sigilo.
3. **Política de avaliações e conteúdo do Google.** Só avaliações reais; sem incentivo, sem seleção (link curto e QR à vista de todos no balcão), sem pedir nota. Respostas verdadeiras, sem dados do avaliador; notas 1 e 2 com dois olhos. Suspeita: Guardião denuncia pelo canal oficial; ninguém pede remoção de avaliação legítima.
4. **Marca, fotos e imagem.** Uso autorizado de marca, nome e fotos existentes e das enviadas depois. Rosto só com termo de imagem; sem termo, fotos sem pessoas. Nenhuma imagem gerada por IA. Voz dos áudios é a voz sintética da casa, nunca imitação do dono. O publicado é do cliente; cópia no Diário, devolvida no encerramento.
5. **Preços, horários e informações.** O cliente responde pela veracidade de horários, serviços, atributos, endereço, telefone e do que disse no Dia 0; a máquina registra a origem de cada dado. Feriados: calendário nacional e municipal, regra do Dia 0, na dúvida pergunta 72 h antes. Sem preço publicado; pergunta sobre preço é respondida sem valor.
6. **Exclusividade limitada por zona.** Máximo de duas empresas do mesmo segmento (categoria principal) na mesma zona (bairro ou raio equivalente), escrita no contrato com cidade e segmento. Não é exclusividade de mercado nem promessa de posição; motivo técnico: mais de dois perfis na mesma malha degradam todos. Proposta escrita reserva a vaga por 5 dias úteis; ocupa na assinatura. Mudança para zona lotada: operação até o fim do ciclo pago, lista de espera por ordem de chegada, vaga antiga liberada na mudança confirmada, cancelamento sem multa. Redesenho de zona: quem está fica.
7. **Limitação de responsabilidade.** Sem promessa de posição, conversão, receita ou clientes novos. Promete a operação medida e registrada e a captura de intenção otimizada, lucrativa e eficiente, demonstrada por contagens do Google com data de referência (ligações pelo perfil = toques no botão Ligar). O que o Google muda ou suspende está fora do controle; o Diário prova a diligência. Custo por contato = mensalidade ÷ contatos; o valor do contato é do cliente.
8. **Reversibilidade.** Remoção do Gerente; histórico em arquivo com link por 30 dias; fim dos envios; dashboard encerrado; exclusão no prazo, salvo nota fiscal, contrato e Diário como prova; vaga liberada. Nada sai do perfil. Quem volta concede tudo de novo e passa pela verificação de zona.

## 4. Mapa por entrega

A Perfil da Empresa · B WhatsApp do dono · C Dashboard. D sustenta todas. Senha: sempre nunca (em 03, senha nova criada pelo cliente).

| Nº | Entrega | Sist. | Acesso necessário | Ação do cliente | Dados que informa |
|---|---|---|---|---|---|
| 01 | Diagnóstico de Posição | A B C | Gerente para auditoria de completude; medição por Places API sem conta do cliente; número; dashboard | Cinco perguntas; conceder Gerente. Sem Gerente, sai com medição pública e auditoria do visível | O que vende e como procuram; bairros ou raio; nome e número |
| 02 | Antes e Depois | A B C | Gerente para o diff Dia 0 → 7 com origem; segunda medição; número; dashboard | Nenhuma; dia 7 desde `created`, mesmo com pendência | Nenhum |
| 03 | Dashboard Radar | A B C | Performance API com data de referência; conta do dashboard; número | Abrir o link fixo; senha opcional; ícone | Número |
| 04 | Boletim de Segunda | A B C | Desempenho da semana fechada; avaliações; medição de sábado; número; dashboard | Aceite no Dia 0; depois nada | Número; nome; jeito da casa de falar |
| 05 | Mapa de Domínio | A B C | Nenhum acesso à conta para medir (Places API, grade 3×3 a 5×5); Gerente só para ler o `place_id`; número; dashboard | Confirmar raio e termos sugeridos | Raio; termos |
| 06 | Diário de Bordo do Perfil | A B C | Gerente: campos, descrição, horários, serviços, atributos, posts, fotos; categoria só com humano. Número para linha curta e Sim/Não; dashboard | Conceder Gerente; foto real opcional; responder Sim/Não | Jeito de falar; o que nunca publicar; horários e regra de feriado; serviços sem preço; cidade |
| 07 | Motor de Reputação | A B | Gerente: ler e responder avaliações e perguntas; link curto oficial de avaliação. Número para Boletim de Reputação e PDF do QR | Conceder Gerente; QR no balcão | Frases proibidas; assinatura das respostas; resposta a preço; onde fica o QR |
| 08 | Extrato de Demanda | A B C | Performance API (ligações pelo perfil, rotas, cliques no site, mensagens somam; impressões e palavras-chave são contexto); número; dashboard | Nenhuma | Nenhum |
| 09 | Horas Devolvidas | B C | Nenhum acesso à conta: Diário + tabela de equivalência; número; dashboard | Nenhuma | Nenhum |
| 10 | Voz do Cliente | A B C | Leitura de avaliações e perguntas; número; dashboard | Nenhuma | Nenhum |
| 11 | Fechamento Executivo | A B C | Todas as leituras acima; número; dashboard | Nenhuma; encaminha o PDF a quem quiser | Nenhum |

## 5. Roteiro do Dia 0

Teto de 15 minutos cronometrados; o roteiro real fecha em cerca de dez.

| Momento | O que acontece | Toque do cliente | Estado |
|---|---|---|---|
| Antes | Comercial roda `zone.check`. Só com vaga: contrato por link (lista do que faz e pergunta, número, aceite, assinatura) e cartão no provedor. A página termina no link que abre a conversa com o número da casa | Assina; cartão; primeira mensagem | `created` → `billing_active` |
| 0–5 min | Cinco perguntas por áudio: o que vende e como procuram; bairros ou raio; jeito de falar; o que pode fazer sem perguntar; número e nome. Gemini transcreve; confirmação por escrito | Áudios; Sim (opt-in com hora) | `profiled` |
| 5–8 min | Adiciona o e-mail operacional como Gerente, passo a passo na tela. Não verificado: recebe o roteiro de verificação; o resto não espera | Um toque | `gbp_linked` ou `gbp_pending_verification` |
| 8–10 min | Link fixo do dashboard; senha opcional; Diagnóstico de Posição na mesma conversa. Última mensagem: "A partir de agora você só recebe. Segunda, 7h, o primeiro Boletim. Dia 7, o Antes e Depois." | Abre o link | `live` |
| 10–15 min (folga) | Só para quem trava no perfil: não acha o menu (print, orientação); não verificado (vídeo: fachada, placa, interior); perfil de terceiro (Solicitar acesso, 3 dias); inexistente (criar e verificar). Nada segura Diagnóstico nem dashboard. Passou de 15: comercial encerra; lembrete semanal até resolver | Conforme o caso | mantém |
| Encerramento | Seção 7 | Nenhum | encerrado |

## 6. A zona

- **Definições:** segmento = categoria principal do perfil (padaria e pizzaria são segmentos diferentes); zona = bairro do Google Maps ou raio equivalente, no contrato com cidade e segmento. Limite 2 por segmento por zona (`MAX_TENANTS_PER_ZONE_SEGMENT=2`, tabela `zones`).
- **Verificação antes da venda:** comercial anota cidade, segmento e zona; roda `zone.check` (planilha na versão de bicicleta): 0/2 ou 1/2 livre, 2/2 lotada. Livre: contrato com zona e segmento escritos. Lotada: dito na primeira conversa, antes de qualquer link; lista de espera sem cobrança e sem prazo. Cada unidade é um tenant e uma vaga.
- **Reserva:** conversa não reserva. Proposta escrita reserva por 5 dias úteis. A vaga se ocupa na assinatura (transação em `zones`; `zone.changed` avisa). Contador acima de dois: tenant não nasce, Head de Operação decide.
- **Fila:** ordem de chegada, sempre; ninguém fura, nem cliente antigo. Vaga liberada vai ao primeiro da lista; comercial confirma interesse antes do contrato.
- **Mudança de endereço:** nova verificação antes. Com vaga: aditivo, vaga antiga liberada. Sem vaga: operação até o fim do ciclo pago; lista de espera da zona nova; vaga antiga libera no dia da mudança confirmada; o endereço no perfil muda mesmo assim (Guardião aprova); cancelamento sem multa.
- **Mudança de categoria principal:** Sim do dono e dois olhos; Guardião roda `zone.check` no segmento novo antes de aprovar. Sem vaga, regra do endereço.
- **Redesenho de zona:** quem está fica; novos pela regra nova; aviso escrito aos clientes da zona.
- **Liberação:** no offboarding, no mesmo dia, pela máquina.

## 7. Encerramento (offboarding)

1. Cancelamento registrado; provedor interrompe a cobrança; sem multa.
2. A máquina remove o e-mail operacional do papel Gerente (o cliente pode remover antes).
3. Fim dos envios do número da casa, com aviso final de uma linha.
4. Histórico exportado (Diário com prints, extratos, Fechamentos, cards, Mapas, fotos, posts, respostas); link por 30 dias.
5. Dashboard encerrado após a exportação.
6. Exclusão dos dados do tenant em contrato + 90 dias, salvo nota fiscal, contrato e `actions_log` (5 anos).
7. Vaga da zona liberada; comercial avisa o primeiro da lista.
8. Nada sai do perfil. Retorno: novos acessos e nova verificação de zona.
