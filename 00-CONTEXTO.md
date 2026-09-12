# 00 · Contexto e história do projeto

## Linha do tempo (setembro de 2026)

1. **Origem.** O Victor recebeu do Gemini dois prompts destinados ao Lovable, com um "dossiê" do **Radar Urbano** em 19 seções, e depois a versão completa com **52 seções** (título, subtítulo, seções 1–52). Esse texto é a tese do negócio e é tratado como **verbatim**: nunca é reescrito. Ele descreve uma holding de seis produtos; hoje é a peça de visão, não o escopo do produto inicial (ver o passo 10 e a decisão D33).
2. **Projeto irmão (referência, não fonte).** Antes do Radar Urbano, foi feito um trabalho chamado **Radar Group V2** (pasta `../Radar Group V2` na máquina de origem), que auditou o mesmo rascunho contra briefings anteriores (`../Radar Group v1/1-BRIEFINGS`) e produziu um dossiê com números diferentes (valuation R$ 125–187 mi, múltiplo 8–12x, 7 produtos, status em cada número). O Victor decidiu **partir do zero** com o texto original do Radar Urbano, sem considerar esse material. Ele existe, é consistente internamente, e pode servir de referência crítica (auditoria em `../Radar Group V2/00-AUDITORIA-GEMINI.md`), mas **não** governa o Radar Urbano. Não está neste repositório.
3. **Apresentação escura (v1).** Primeira versão do dossiê: fundo carvão, esmeralda, vidro fosco, menu escondido, "universo em expansão" ao fundo, estética Armani/grife. Arquivo `index.html` na pasta do projeto na máquina de origem; artifact `https://claude.ai/code/artifact/038b6320-3f54-48da-94ce-31c2508cf270`. Não está neste repositório.
4. **Edição branca (a vigente).** Fundo branco, ar da Apple, tipografia de maison de luxo, 52 seções, capítulos com numeral romano, blocos pretos nos quatro estágios e no manifesto. Na origem era gerada por `build_branco.py` a partir de `conteudo-52.md`; aqui é `src/build_dossie.py` lendo `src/conteudo-52.md` e escrevendo `dist/radar-urbano-dossie.html` (e o PDF ao lado). Artifact `https://claude.ai/code/artifact/7d5ad112-cce5-480d-a8ac-8c3ae4d6e207`. PDF de 61 páginas.
5. **Manual das Entregas (versão da holding).** 15 entregas tangíveis (dashboard + 14), calendário, uma semana na vida do cliente, 8 agentes, a conta na mesa. **Correção importante:** a primeira versão trazia conversão estimada e receita atribuída; o Victor apontou que isso não é medível nem garantível. A versão seguinte só trazia métricas contadas (contatos, pedidos de preço/orçamento/horário, horários marcados pela Recepcionista, custo por contato) e a promessa "captura de intenção otimizada, lucrativa e eficiente". Artifact `https://claude.ai/code/artifact/920769a3-1e3f-4c5e-af3b-b8cab390738c`. Substituído pelo **Mapa de Entregas** no passo 10.
6. **Mapa de Acessos e Permissões (versão da holding).** Sete sistemas (perfil, WhatsApp da empresa, WhatsApp do dono, telefonia, Google Ads, dashboard, contrato), por entrega: contas, papéis, autorizações legais, dados informados e regra de senha (nunca a do cliente). Base legal escrita como pauta para advogado. Artifact `https://claude.ai/code/artifact/d0cf5793-18c3-4135-8d65-72edbfbad1d8`. Substituído pelo **Mapa de Acessos** no passo 10.
7. **Manual de Montagem da Máquina (versão da holding).** Organograma em 5 camadas, cérebros (Gemini obrigatório para dados/Google), 6 conectores, fundação no Google Cloud, 8 agentes e o Guardião com prompt-esqueleto e teste de aceitação, 15 receitas com critério de pronto, onboarding técnico, operação (cadências, papéis, runbooks, custo, SLOs), LGPD técnico, plano de 8 semanas, apêndice. Artifact `https://claude.ai/code/artifact/ed6ea2ff-50bc-42bc-8972-aea6789854ba`. Substituído pelo **Mapa Mundi** no passo 10.
8. **Livro de Consulta (versão da holding).** 61 verbetes na numeração do Manual, passo a passo "vai ali, clica aqui", versões de bicicleta das 15 entregas, glossário A–Z. Artifact `https://claude.ai/code/artifact/b04c4df3-9b39-421d-9f34-a607f706afef`. Substituído pela **Bíblia** no passo 10.
9. **Pacote de handoff.** Tudo acima exportado para Markdown (`handoff/`, com `export_md.py` e os geradores `build_*.py`), para continuar em outro dispositivo. É a matéria-prima do passo 10.
10. **Enxugamento para o produto inicial (setembro de 2026).** O Victor pediu: "adapta tudo desse modelo, enxugando tudo para um produto inicial radar urbano e radar maps (chame tudo de radar urbano), considerando todos os detalhes e intricacias. E além disso me produz um arquivo que me coloque em fases as implementações dos outros produtos de forma faseada e modular." O primeiro conjunto pode ser detalhado e profundo; o roadmap, não. Do pedido saíram: um **brief de escopo** que governa tudo; os quatro documentos reescritos (**Mapa de Entregas**, **Mapa de Acessos**, **Mapa Mundi**, **Bíblia**) só com o que é Google e com o que o brief acrescentou (trava territorial por zona, número da casa, Diagnóstico de Posição e Antes e Depois como entregas); o **Roadmap faseado** com os outros cinco módulos; o repositório GitHub `antonio-fardo-neto/radar-group`; e um gerador único (`src/build.py`) que lê o Markdown da raiz e produz as apresentações. Este arquivo, o registro de decisões (D21 a D33), o gosto (instrução 11) e o backlog foram atualizados junto.

## O que é o Radar Urbano agora

**Radar Urbano** é o nome de tudo: da empresa, do produto e da máquina. O produto inicial é o que o dossiê chamava "Radar Maps (Core)": posicionamento e captura de intenção no Google Maps e na Busca local, por assinatura, entregue por agentes de IA, com zero tempo do dono. A partir de agora esse nome antigo só aparece no dossiê verbatim e em notas de contexto como esta; nos quatro documentos, nunca.

- **Preço:** R$ 499/mês, fixo. R$ 16,63 por dia. Mensal, cancelável, sem fidelidade abusiva. Não existe verba de mídia neste produto.
- **Promessa oficial:** "captura de intenção otimizada, lucrativa e eficiente". Nunca conversão, receita atribuída, "novos clientes" ou ROI. Quando precisa de conta, é custo por contato (R$ 499 ÷ contatos do mês) e o dono põe o valor dele por cima.
- **Contato**, neste produto, é o que o Google conta a partir do perfil: ligações pelo perfil (toques no botão Ligar, não ligações atendidas), pedidos de rota, cliques no site e mensagens pelo perfil. Impressões e palavras-chave de descoberta são contexto; não entram na soma. Não há dado em tempo real: o que é contato vem do Google com data de referência (atraso típico de 2–3 dias); o que é próprio (medições, respostas, ações) é atualizado a cada hora.
- **Onze entregas**, numeração fixa, em três grupos. Entrada: 01 Diagnóstico de Posição (Dia 0) · 02 Antes e Depois do Perfil (Dia 7). Vendas & Performance: 03 Dashboard Radar · 04 Boletim de Segunda · 05 Mapa de Domínio · 06 Diário de Bordo do Perfil · 07 Motor de Reputação. Controladoria & Eficiência: 08 Extrato de Demanda · 09 Horas Devolvidas · 10 Voz do Cliente · 11 Fechamento Executivo.
- **Cinco agentes e um humano com painel:** Cartógrafo (mede posição e desenha o Mapa de Domínio), Editor (mantém o perfil vivo, inclusive feriados 72 h antes), Anfitrião (responde avaliações em até 2 h e perguntas do perfil, gera o material do QR), Tesoureiro (tudo em número, custo por tenant), Redator-chefe (60 segundos de áudio e uma página), e o Guardião (humano; regra dos dois olhos para categoria, nome, endereço e notas ≤ 2).
- **Quatro conectores e um serviço de entrega:** GBP Connector (Perfil da Empresa: informações, desempenho, avaliações, posts, mídia, perguntas e respostas), Places Connector (Places API (New), busca por texto em grade), WA Connector (o número da casa: uma única conta do Radar Urbano na plataforma Meta, só para falar com o dono), TTS Connector (Chirp 3 HD pt-BR, a voz da casa), mais Render & Delivery (cards PNG, mapa SVG, PDFs de uma página, dashboard, reenvio após 2 h).
- **Um cérebro obrigatório:** Gemini para dados, medição, aferição e tudo que toca API ou superfície do Google. Outros modelos só para linguagem, atrás do `LLMGateway`.
- **Trava territorial:** no máximo duas empresas por segmento por zona (bairro ou raio equivalente). Dois perfis concorrentes na mesma malha de busca disputam as mesmas posições e degradam o resultado dos dois. Verificação da zona pelo comercial antes de vender, cláusula de exclusividade limitada no contrato, campos `segmento` e `zona` no tenant, job `zone.check` antes de o tenant nascer, `MAX_TENANTS_PER_ZONE_SEGMENT=2`.
- **Um único acesso do cliente:** papel Gerente no Perfil da Empresa no Google. Nunca a senha. Senha nova só no dashboard, criada pelo cliente.
- **Setup:** "até 15 minutos no Dia 0" continua sendo a promessa pública. Sem WhatsApp da empresa e sem telefonia, o roteiro real fecha em cerca de dez; os cinco restantes são folga para quem trava no perfil.
- **Custo de tecnologia por cliente:** referência R$ 12–25/mês; alerta em R$ 25 (antes R$ 35).
- **Plano de montagem:** seis semanas (antes oito), piloto com 3 clientes por 30 dias na sexta.

## O que saiu e foi para o roadmap

Cada módulo volta como um conjunto de agentes, conectores, tabelas, acessos e entregas ligável por tenant (`modules_json`), sem tocar no núcleo. Detalhe em `11-ROADMAP-FASEADO.md`.

| O que saiu do produto inicial | Para onde foi | Por quê |
|---|---|---|
| Comparação nominal com concorrentes, snapshots de concorrentes, card "Quem ganhou a semana", sinais de concorrente e de clima, Sentinela como agente | Fase 1 · Radar Concorrência | Só Google, sem acesso novo do cliente; mas exige guardar dados de terceiros e um agente a mais. No núcleo, o Mapa de Domínio mostra só a posição própria (verde, cinza, vermelho) e o calendário de feriados vive dentro do Editor |
| Catálogo/cardápio com preços, card "O que te procuram", Vitrine Indexada | Fase 1 · Radar Menu | É a única entrega que pede insumo do dono (preços); no núcleo fica a lista de serviços sem preço |
| Convite ativo de avaliação por WhatsApp a clientes finais, evento `atendimento.concluido`, modelo `convite_avaliacao`, WhatsApp da empresa do cliente, Tech Provider, Embedded Signup | Fase 2 · Radar Stars | Exige a Fundação Meta para o cliente e consentimento de cliente final. No núcleo ficam as respostas a todas as avaliações e perguntas, o link curto e o QR de avaliação para o balcão e o Boletim de Reputação |
| Recepcionista 24/7, Agenda das 7h, Resgate de Ligações Perdidas, telefonia, número de rastreamento, "pediu preço", "horários marcados", contatos em tempo real, Voz do Cliente a partir de conversas | Fase 3 · Radar Chat | Exige telefonia e WhatsApp da empresa. No núcleo, contato é o que o Google conta, com atraso; Voz do Cliente vem só de avaliações e perguntas |
| Google Ads, MCC, developer token, Estrategista, Extrato de Mídia, ofertas relâmpago com Sim/Não | Fase 4 · Radar Ads | Exige vinculação de conta de anúncios e depende do número de rastreamento da Fase 3 para atribuir |
| Suíte (bundle R$ 1.500–2.200), proposta automática de expansão para outros produtos, cross-sell por dado | Fase 5 · A suíte | Só faz sentido com mais de um módulo montado. No calendário do núcleo, a proposta do mês 3 é de novos termos e raio |

## Onde as coisas vivem agora

Repositório GitHub **`antonio-fardo-neto/radar-group`**. O conteúdo é Markdown na raiz; tudo que é HTML e PDF é gerado.

```
radar-group/
  README.md                      mapa do pacote; leia primeiro
  00-CONTEXTO.md                 este arquivo
  01-DOSSIE.md                   a tese da holding, 52 seções, verbatim (peça de visão)
  02-MAPA-DE-ENTREGAS.md         as onze entregas, calendário, a máquina, a conta na mesa, a zona
  03-MAPA-DE-ACESSOS.md          quatro sistemas (A–D), base legal em 8 itens, mapa por entrega, Dia 0, a zona
  04-MAPA-MUNDI.md               manual de montagem: camadas, cérebros, conectores, fundação, agentes, receitas, operação, LGPD, seis semanas
  05-BIBLIA.md                   57 verbetes na numeração do Mapa Mundi, bicicletas VI.01–VI.11, glossário
  06-DESIGN.md                   sistema visual da edição branca
  07-COMO-GERAR.md               toolchain e convenções do Markdown que o gerador entende
  08-DECISOES.md                 D1 a D33
  09-PROMPTS-E-GOSTO.md          as instruções do Victor (1 a 11) e o gosto
  10-BACKLOG.md                  o que está aberto, em ordem
  11-ROADMAP-FASEADO.md          fases 1 a 5, modulares, com dependências
  TUDO-EM-UM.md                  todos os arquivos acima concatenados (gerado por src/assemble.py tudo)
  Makefile                       make html · make pdf · make tudo · make all
  src/
    build.py                     gerador único: Markdown → HTML da edição branca (--all, --fragment)
    template_branco.html         a casca visual (CSS, índice, JS)
    make_pdf.py                  HTML → PDF (Chrome headless; remove páginas em branco com pypdfium2)
    build_dossie.py              gerador próprio do dossiê verbatim
    conteudo-52.md               texto-fonte do dossiê
    assemble.py                  monta 02, 03, 04, 05, 11 (e 00, 08, 09, 10) a partir de _work/parts; gera TUDO-EM-UM.md
    fonts/                       Bodoni Moda e Manrope locais, para o PDF sair sem internet
  dist/                          radar-urbano-*.html e *.pdf gerados; dist/fragmentos/ para publicar como artifact
  _work/                         pasta local de trabalho, fora do git: BRIEF.md (o brief de escopo), prompts/, parts/, test/, shots/
```

- **Fluxo:** editar o `.md` na raiz → `python3 src/build.py --all --fragment` → `python3 src/make_pdf.py --all` → `python3 src/assemble.py tudo`. Ou `make all`. Nunca editar `dist/` à mão (decisões D20 e D32).
- **Nomes de saída:** `radar-urbano-entregas.html`, `radar-urbano-acessos.html`, `radar-urbano-mapa-mundi.html`, `radar-urbano-biblia.html`, `radar-urbano-roadmap.html`, `radar-urbano-dossie.html`, cada um com o PDF ao lado.
- **Publicação:** artifacts do Claude a partir de `dist/fragmentos/`; redeploy no mesmo caminho mantém a URL. Fora do Claude, qualquer hospedagem estática serve os HTML de `dist/`. Os artifacts são privados por padrão; o dono libera pelo botão **Share**.
- **O brief de escopo** (`_work/BRIEF.md`) governou a reescrita: personas, números de exemplo, as onze entregas, os cinco agentes, os conectores, as tabelas, os tópicos, as ferramentas, os estados, as cadências, o plano de seis semanas, a lista de 57 verbetes e as convenções de Markdown. Se um dia os documentos e o brief divergirem, os documentos da raiz são a versão vigente e o brief é histórico.

## Os documentos originais como referência

A pasta `handoff/` (o passo 9) não está no repositório. Fica na máquina de origem e no scratchpad da sessão que fez o enxugamento. É referência de três coisas: **formato** (foi exportada do HTML e mostra exatamente as formas que o gerador entende), **voz** (frases curtas, nomes próprios, cenas reais) e **profundidade** (o enxugamento tirou módulos, não detalhe). Nunca é fonte de escopo: o que está lá e não está aqui saiu de propósito.

| Original (handoff) | Vigente (repositório) | O que mudou |
|---|---|---|
| `02-ENTREGAS.md` · Manual das Entregas, 15 entregas, 8 agentes, 8 cenas com Recepcionista e Sentinela | `02-MAPA-DE-ENTREGAS.md` · Mapa de Entregas, 11 entregas, 5 agentes + Guardião, capítulo novo sobre a trava territorial | Entram o Diagnóstico de Posição e o Antes e Depois como entregas 01 e 02; saem seis entregas de módulos; todas as vinhetas reescritas |
| `03-ACESSOS.md` · Mapa de Acessos e Permissões, 7 sistemas | `03-MAPA-DE-ACESSOS.md` · Mapa de Acessos, 4 sistemas (A Perfil, B WhatsApp do dono, C Dashboard, D Contrato), capítulo novo sobre a zona | Base legal continua com 8 itens: sai o consentimento para mensagens a clientes finais, entra a exclusividade limitada por zona |
| `04-MANUAL.md` · Manual de Montagem, 6 conectores, 15 receitas, 8 semanas | `04-MAPA-MUNDI.md` · Mapa Mundi, 4 conectores + Render & Delivery, 11 receitas, 6 semanas | Saem Voice Connector e Ads Connector; o WA Connector vira o número da casa; alerta de custo R$ 25 |
| `05-LIVRO-DE-CONSULTA.md` · 61 verbetes | `05-BIBLIA.md` · 57 verbetes | Saem telefonia, Embedded Signup, Ads e as bicicletas das entregas de módulos; entram III.7 (número da casa), III.11 (link curto e QR), V.5 (a grade e a validação com 20 buscas), VII.2 (a zona) |
| (não existia) | `11-ROADMAP-FASEADO.md` | Os cinco módulos em fases, com dependências e critério de pronto |

## Personas e nomes fixos usados nos exemplos

- **Seu Jorge, Padaria Pão da Praça** (alimentação) · **Marcão, Oficina Marcão Auto Center** (automotivo) · **Dra. Lívia, Clínica Lívia Odonto** (saúde). Sempre marcados como exemplo.
- **Entregas (11, numeração fixa):** 01 Diagnóstico de Posição · 02 Antes e Depois do Perfil · 03 Dashboard Radar · 04 Boletim de Segunda · 05 Mapa de Domínio · 06 Diário de Bordo do Perfil · 07 Motor de Reputação · 08 Extrato de Demanda · 09 Horas Devolvidas · 10 Voz do Cliente · 11 Fechamento Executivo. Na Bíblia, as bicicletas são VI.01 a VI.11 na mesma numeração.
- **Agentes:** Cartógrafo, Editor, Anfitrião, Tesoureiro, Redator-chefe, e o **Guardião** (humano com painel). Frase de contagem: "cinco agentes e um humano com painel". Recepcionista, Sentinela e Estrategista só existem no roadmap.
- **Conectores:** GBP Connector, Places Connector, WA Connector (número da casa), TTS Connector, mais Render & Delivery. Frase de contagem: "quatro conectores e um serviço de entrega".
- **Preço:** só R$ 499/mês. Os preços dos módulos (Stars R$ 299 · Chat R$ 499 · Concorrência R$ 399 · Ads R$ 699 · Menu R$ 399) e a suíte (R$ 1.500–2.200/mês) só aparecem no dossiê e no roadmap.
- **Números de exemplo do mês típico:** padaria 260 contatos (118 ligações pelo perfil, 97 rotas, 31 cliques no site, 14 mensagens) e R$ 1,92 por contato · oficina 168 contatos e R$ 2,97 · clínica 160 contatos e R$ 3,12. Semana típica da padaria no Boletim: 31 ligações pelo perfil, 22 rotas, 8 cliques no site, 3 avaliações novas respondidas, 1º lugar para "padaria perto de mim" em 7 dos 9 pontos. Horas Devolvidas da clínica: 14h07 no mês contra 2 minutos da Dra. Lívia; frase de balcão: "catorze horas por R$ 499".
- **Cores do Mapa de Domínio:** verde = top 3 · cinza = 4º a 10º · vermelho = fora do top 10. Sem concorrentes nomeados.
- **A zona:** no máximo dois do mesmo segmento na mesma zona. A tabela `zones` tem `limite=2`.

## Quem é o Victor (para calibrar tom)

Fundador, decide no estratégico, não quer micro-decisão. Fala direto, gosta de "masterpiece", pede vinte perguntas antes de começar quando quer personalização, e corrige rápido quando algo não é garantível (foi assim com a métrica de conversão). Português do Brasil, informal na conversa; entregáveis institucionais, elegantes, sem hype vazio.
