# Radar Urbano — pacote de continuidade (produto inicial)

> Leia este arquivo primeiro. É o ponto de entrada para qualquer pessoa ou IA que vá tocar o projeto sem o contexto das conversas originais. Tudo aqui é Markdown; as apresentações (HTML e PDF) são geradas a partir dele por `src/build.py`.

## O que é o projeto

**Radar Urbano** é um serviço B2B de captura de intenção para pequenos negócios locais: posicionamento e operação do perfil da empresa no Google Maps e na Busca local, por assinatura de **R$ 499/mês**, entregue por agentes de IA, com **zero tempo do dono**. Este pacote descreve o **produto inicial**: o que o dossiê da holding chamava "Radar Maps (Core)", agora chamado simplesmente Radar Urbano. Os outros cinco módulos (Stars, Chat, Concorrência, Ads, Menu) não fazem parte deste escopo e estão organizados em fases no `11-ROADMAP-FASEADO.md`.

Em uma linha: **onze entregas, cinco agentes e um humano com painel, quatro conectores, um cérebro obrigatório (Gemini) para tudo que é dado e Google, no máximo duas empresas por segmento por zona.**

## Mapa deste pacote

| Arquivo | O que é | Quando abrir |
|---|---|---|
| `README.md` | Este mapa | Sempre primeiro |
| `00-CONTEXTO.md` | História, o que existe, onde está, o que saiu do escopo e por quê | Antes de qualquer decisão |
| `01-DOSSIE.md` | A tese da holding em 52 seções, **texto verbatim** (peça de visão; não é o escopo do produto inicial) | Quando precisar do conteúdo de negócio |
| `02-MAPA-DE-ENTREGAS.md` | As onze entregas tangíveis, calendário, a máquina, a conta na mesa, a trava territorial | Produto e operação |
| `03-MAPA-DE-ACESSOS.md` | Contas, papéis, permissões legais, mapa por entrega, roteiro do Dia 0, a zona | Onboarding de cliente e jurídico |
| `04-MAPA-MUNDI.md` | Manual de montagem da máquina: camadas, cérebros, conectores, fundação, agentes, receitas, operação, LGPD, seis semanas | Engenharia |
| `05-BIBLIA.md` | Livro de consulta: verbetes passo a passo na numeração do Mapa Mundi, versões de bicicleta, glossário | Quando travar em qualquer passo |
| `06-DESIGN.md` | O sistema visual (tokens, fontes, layout, movimento, impressão) | Ao gerar qualquer documento novo |
| `07-COMO-GERAR.md` | Toolchain: Markdown → HTML → PDF, publicação, convenções | Ao regenerar ou criar documento |
| `08-DECISOES.md` | Registro de decisões com o porquê (ADR), D1 a D33 | Antes de mudar algo estrutural |
| `09-PROMPTS-E-GOSTO.md` | As instruções originais do Victor e o gosto | Ao escrever ou desenhar qualquer coisa nova |
| `10-BACKLOG.md` | O que está aberto, em ordem | Para saber o que fazer a seguir |
| `11-ROADMAP-FASEADO.md` | Os outros produtos, em fases modulares, com dependências | Quando for hora de crescer |
| `TUDO-EM-UM.md` | Todos os arquivos acima concatenados | Ingestão rápida por uma IA |
| `src/` | `build.py` (Markdown → HTML), `make_pdf.py` (HTML → PDF), `assemble.py`, `build_dossie.py`, `template_branco.html`, `conteudo-52.md` | Para regenerar |
| `dist/` | HTML e PDF gerados (não editar à mão) | Para enviar ou publicar |

## Regras inegociáveis (resumo; detalhes em `08-DECISOES.md`)

1. **Nenhuma métrica de conversão ou receita atribuída.** Só o que a máquina conta: ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil, impressões, posição, avaliações, custo por contato. A promessa é "captura de intenção otimizada, lucrativa e eficiente".
2. **Gemini é o cérebro obrigatório** para dados, medição, aferição e tudo que toca API ou superfície do Google. Outros modelos só para linguagem, atrás do `LLMGateway`.
3. **Nunca a senha do cliente.** Um único acesso: papel Gerente no Perfil da Empresa. Senha nova só no dashboard, criada pelo cliente.
4. **Zero tempo do dono.** Os únicos minutos são no Dia 0 (até quinze; na prática, dez).
5. **Trava territorial.** No máximo duas empresas por segmento por zona, verificado antes da venda e em código.
6. **O texto do dossiê (`01-DOSSIE.md`) é verbatim.** Não se parafraseia. Ele descreve a holding de seis produtos; o produto inicial é o recorte descrito nos arquivos 02 a 05.
7. **Estética:** fundo branco, ar da Apple, tipografia de maison (Bodoni Moda nos números e itálicos, sans leve e espaçada nos títulos), esmeralda profundo como único acento, nada "tech".
8. **Idioma:** português do Brasil, direto, sem hype, sem jargão sem tradução.
9. **Conteúdo em Markdown; HTML e PDF gerados.** Nunca editar `dist/` à mão.

## Como começar em um dispositivo novo

```bash
git clone https://github.com/antonio-fardo-neto/radar-group && cd radar-group
python3 src/build.py --all          # dist/*.html (sem dependências além do Python 3.11+)
python3 src/build_dossie.py         # dist/radar-urbano-dossie.html
pip install pypdfium2 pillow && python3 src/make_pdf.py --all   # dist/*.pdf (precisa de Chrome/Chromium)
python3 src/assemble.py tudo        # TUDO-EM-UM.md
```

Se estiver usando uma IA de código: aponte para esta pasta e diga "leia README.md, 00-CONTEXTO.md e 08-DECISOES.md antes de qualquer coisa", ou cole `TUDO-EM-UM.md`.
