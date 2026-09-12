# Fontes locais (para gerar PDF sem depender da internet)

Bodoni Moda e Manrope, baixadas do Google Fonts, ambas sob a SIL Open Font License 1.1.
`fonts-local.css` declara as `@font-face` apontando para os `.woff2` desta pasta; `src/make_pdf.py` injeta esse CSS na variante de impressão. Os HTML em `dist/` continuam usando o Google Fonts.
