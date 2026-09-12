# Radar Urbano

Pacote de documentos do **Radar Urbano**: serviço B2B de captura de intenção no Google Maps e na Busca local para pequenos negócios, por assinatura de **R$ 499/mês**, entregue por agentes de IA, com zero tempo do dono. Só o produto inicial (o que a versão antiga da holding chamava "Radar Maps"); os outros módulos aparecem apenas no arquivo de expansão.

## Os oito arquivos (em `radar-urbano/`)

| Arquivo | O que é |
|---|---|
| `01-DOSSIE.md` | A tese do negócio com as variáveis de um produto só: mercado, produto, modelo comercial, economia unitária, estágios, riscos |
| `02-POV-CLIENTE.md` | O que o cliente vê, contrata, recebe e nunca faz; preço; trava territorial; o que medimos e o que não prometemos |
| `03-POV-PLAYER.md` | O memorando para investidor/player: economia unitária, fases de escala, capacidade, riscos, uso de capital |
| `04-EXPANSAO.md` | Como cresce: por zonas e praças (produto único) e por módulos (fases 1 a 5) |
| `05-MAPA-DE-ENTREGAS.md` | As onze entregas, calendário, a máquina, a conta na mesa, a trava |
| `06-MAPA-DE-ACESSOS.md` | Contas, papéis, base legal, mapa por entrega, roteiro do Dia 0, a zona |
| `07-MAPA-MUNDI.md` | Manual de montagem da máquina: camadas, cérebros, conectores, fundação, agentes, receitas, operação, LGPD, seis semanas |
| `08-BIBLIA.md` | Livro de consulta: 57 verbetes passo a passo na numeração do Mapa Mundi, com glossário |

`TUDO-EM-UM.md` concatena os oito para colar de uma vez numa IA.

## Regras que valem em todos os arquivos

1. Nenhuma métrica de conversão, receita atribuída ou "novos clientes" prometida ao cliente. Só contagens (ligações pelo perfil, rotas, cliques no site, mensagens pelo perfil, impressões, posição, avaliações) e custo por contato.
2. Gemini é o cérebro obrigatório para dados, medição e tudo que toca o Google.
3. Nunca a senha do cliente. Um único acesso: papel Gerente no Perfil da Empresa.
4. Zero tempo do dono: até 15 minutos no Dia 0.
5. No máximo duas empresas por segmento por zona, verificado antes da venda e em código.
6. Dados do Google com data de referência; sem tempo real neste produto.
7. Alerta de custo de tecnologia em R$ 25 por cliente por mês.

## Outras pastas

- `referencia/` — `01-DOSSIE-HOLDING-VERBATIM.md` (o dossiê original da holding, 52 seções, intocado) e `BRIEF-DE-ESCOPO.md` (as decisões de recorte que governaram a reescrita; inclui o adendo de alinhamento).
- `detalhado/` — as versões longas e aprofundadas (entregas, acessos, mapa mundi, roadmap, contexto, decisões, backlog, design, como gerar). São rascunhos em revisão; ver `detalhado/README.md`.
- `src/` — gerador de apresentações web (edição branca) e PDF a partir do Markdown: `python3 src/build.py --all`, `python3 src/make_pdf.py --all`, `python3 src/assemble.py tudo`. Ver `detalhado/07-COMO-GERAR.md`.
- `garowa-ai/` — os dois documentos da **Garowa.AI** (a casa de IA do grupo Garowa): `01-HORIZONTE.md` (trinta e seis posições possíveis em três anéis de distância, as combinações que só o grupo consegue fazer e cinco formas inteiras de empresa) e `02-ESTRUTURA.md` (o que precisa existir para qualquer forma operar: empresa, contratos, gente, caixa, máquina, operação, conformidade, primeiro ano e painel). Ver `garowa-ai/README.md`.
- `dist/` — HTML e PDF gerados.
