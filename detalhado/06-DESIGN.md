# 06 · Sistema visual (edição branca)

> Reproduza exatamente isto para qualquer documento novo do Radar Urbano. A casca está em `src/template_branco.html`; os blocos (cartões, pares rótulo/valor, verbetes, calendário, tabelas) estão no `EXTRA_CSS` de `src/build.py`.

## Direção

Apple no ar e no ritmo (uma ideia por tela, muito branco, cinza-gelo alternado, cantos generosos). Maison de luxo na tipografia (serifa Didone nos números-herói e itálicos; sans leve, caixa alta e espaçada nos títulos). Tecnologia só no acabamento (nada de neon, grid, glow ou "dashboard look"). Magnetismo vem do ritmo: capa → capítulos com numeral romano → blocos pretos nos momentos de dinheiro e no manifesto.

## Tokens

```
--bg:#FFFFFF  --bg-2:#F5F5F7  --bg-3:#EDEDF0  --dark:#0B0B0C  --dark-2:#151517
--ink:#1D1D1F  --ink-2:#6E6E73  --ink-3:#A1A1A6  --line:rgba(0,0,0,.09)  --line-2:rgba(0,0,0,.16)
--em:#0B7A55 (esmeralda profundo, único acento)  --em-light:#37C48E (esmeralda sobre preto)
--sans: -apple-system, "SF Pro Display", Manrope (Google Fonts, 300–600)
--serif: "Bodoni Moda" (Google Fonts, opsz 6..96, 400/500 + itálico)
--ease: cubic-bezier(.22,1,.36,1)
```

## Tipografia

- Título de capa: sans 500, caixa alta, `letter-spacing:.03em`, `clamp(28px,4.4vw,64px)`, linhas separadas em `<span class="l">`.
- Subtítulo de capa: Bodoni itálico, `clamp(20px,2vw,29px)`, cor `--ink-2`.
- Título de seção (h2): sans 500, caixa alta, `letter-spacing:.03em`, `clamp(21px,2.2vw,32px)`.
- Etiqueta (eyebrow): sans 11px, `letter-spacing:.36em`, caixa alta, `--ink-3`.
- Corpo: sans 18px, `line-height:1.6`, máximo 62–66 caracteres por linha.
- Números-herói: Bodoni 400, `clamp(36px,3.6vw,52px)`, `font-variant-numeric:tabular-nums`; em esmeralda quando é dinheiro ou resultado.
- Numerais de lista: Bodoni 22px em `--ink-3`, esmeralda no hover.

## Layout

- Largura máxima 1400px; seção com grid `5fr / 7fr`: título fixo (sticky) à esquerda, conteúdo à direita. Em mobile, empilha.
- Seções alternam branco e `--bg-2`. Momentos de dinheiro (estágios, manifesto, máquina, operação) em `--dark`.
- Divisória de capítulo: numeral romano em Bodoni `clamp(44px,6vw,84px)` + nome em caixa alta espaçada + "Seções x–y".
- Cartões: `border-radius:22px`, borda `--line` (ou sem borda sobre fundo cinza), hover sobe 4px com sombra suave.
- Tabelas financeiras: linhas finas, rótulo à esquerda, valor em Bodoni à direita; deduções em branco 55% sobre preto; "Receita Efetiva" em esmeralda.
- Índice: overlay branco com blur, grade de colunas, itens agrupados por capítulo, ativo em esmeralda. Botão "Índice" em pílula no topo direito. Barra de progresso de 2px em esmeralda.

## Movimento (contido)

- Capa: linhas do título sobem de trás de uma máscara (1.4s), etiqueta e subtítulo aparecem, uma régua cresce, arcos de radar se desenham.
- Seções: `.rv` (fade + 22px de subida, 1s) e `.stag` (filhos em cascata, 90ms entre eles) via IntersectionObserver.
- Números: contam de zero até o valor (`.cnt` com `data-t`, `data-dec`, `data-pre`, `data-suf`), 1.5s, easing quártico.
- `prefers-reduced-motion`: tudo estático.
- Sem parallax, sem scroll-jacking, sem partículas na edição branca. (A edição escura v1 tinha "universo em expansão" em canvas; não usar na branca.)

## Impressão / PDF

- Página `1440×900px` (16:10), margem 0, cores de fundo preservadas.
- Cada seção começa em página nova; título e conteúdo em duas colunas; blocos com `break-inside:avoid`.
- Capa sem `min-height` para não gerar página em branco; páginas em branco remanescentes são removidas por script (pypdfium2).
- Gerado por `src/make_pdf.py`; detalhes em `07-COMO-GERAR.md`.

## Proibições

Roxo, vermelho, gradientes coloridos, neon, ícones genéricos, emojis como marcador, fotos de banco de imagem, "outlier", parágrafos centralizados longos, qualquer coisa que pareça painel de software.

## Blocos do gerador (além dos da casca)

- **Número grande** (`.big-n`): Bodoni, cinza-claro, acima do título das entregas, verbetes, sistemas e fases.
- **Pares rótulo/valor** (`.spec`): rótulo em caixa alta espaçada à esquerda, valor à direita, linhas finas.
- **Cartões** (`.cards`): grade responsiva, cantos 22px, numeral em Bodoni, linhas de conta com valor em Bodoni (esmeralda quando é contato ou custo por contato).
- **Verbete** (`.vb`): etiqueta em esmeralda, caixa alta espaçada; passos com marcador em Bodoni esmeralda; "Como saber que deu certo" em faixa preta.
- **Calendário** (`.cal`): cartões com título em Bodoni 30px e etiqueta em caixa alta.
- **Vinheta** (`.vin`): cena em Bodoni 19–23px sobre uma régua fina.
- **Seções largas** (`.wide`): quando há tabela ou código, o título deixa de ser fixo e o conteúdo ocupa a largura toda.
