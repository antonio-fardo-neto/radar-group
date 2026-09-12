# 07 · Como gerar tudo de novo

## Requisitos

- Python 3.11+ (sem dependências para gerar HTML).
- Para PDF: Google Chrome ou Chromium instalado e `pip install pypdfium2 pillow` (remoção de páginas em branco). Se o navegador não estiver no PATH, `CHROME=/caminho/para/o/binário`.
- Internet na primeira abertura das páginas (Google Fonts: Bodoni Moda, Manrope).

## Fluxo

```
texto (.md na raiz do repositório)
   └─ src/build.py + src/template_branco.html  →  dist/radar-urbano-*.html   (arquivo único, abre em qualquer navegador)
        ├─ --fragment                          →  dist/fragmentos/*.html     (começa em <title>, sem <html>/<head>: para publicar como artifact)
        └─ src/make_pdf.py (CSS de impressão, sem <script>) → Chrome headless → remove páginas em branco → dist/*.pdf
01-DOSSIE (verbatim) segue o gerador próprio: src/build_dossie.py lê src/conteudo-52.md → dist/radar-urbano-dossie.html
src/assemble.py tudo → TUDO-EM-UM.md
```

## Comandos

```bash
python3 src/build.py --all --fragment   # Entregas, Acessos, Mapa Mundi, Bíblia, Roadmap
python3 src/build.py 02-MAPA-DE-ENTREGAS.md --aba "Mapa de Entregas" --out dist/radar-urbano-entregas.html   # um só
python3 src/build_dossie.py             # dossiê
python3 src/make_pdf.py --all           # PDFs de tudo que está em dist/
python3 src/assemble.py tudo            # TUDO-EM-UM.md
make all                                # tudo acima
```

## Convenções do Markdown (o que o gerador entende)

O gerador é um só para todos os documentos. Ele reconhece as formas abaixo; qualquer outra coisa vira parágrafo.

| Forma no `.md` | Vira |
|---|---|
| `# RADAR URBANO: O NOME` + `*subtítulo*` na linha seguinte | Capa (título em linhas, subtítulo em Bodoni itálico) |
| `*Capítulo I · Nome*` em itálico, sozinho, logo antes de um `##` | Etiqueta (eyebrow) da seção; "Entrega 03", "Verbete III.2", "Sistema A", "Fase 2" geram o número grande |
| `## TÍTULO {#id .alt .dark .fecho}` | Seção; atributos opcionais (fundo cinza, fundo preto, encerramento). Sem atributo, alterna branco/cinza sozinho |
| `*frase*` logo depois do `##` | Tagline em itálico (no `.fecho`, o lead) |
| `---` e `# Capítulo III — Nome (Verbetes III.x)` | Divisória de capítulo com numeral romano (Bíblia) |
| `### Nome` | Subtítulo de bloco (agente, conector, receita); `### 05 Nome` ganha numeral |
| `#### Título — Sub` + bullets | Cartão de calendário; blocos `####` seguidos viram uma grade |
| `**Rótulo**` sozinho na linha | Etiqueta de bloco (as sete partes de um verbete, "Regras do onboarding") |
| `1. **Lead** — texto` | Linhas numeradas com título (rows) |
| `1. texto` | Passos simples |
| `- **Rótulo:** valor` | Pares rótulo/valor (spec) |
| `- **Termo**: definição` | Lista de definições (glossário) |
| `- **01 · Nome** — frase` (+ `  - Linha: valor` aninhado) | Cartões em grade, com linhas de conta opcionais |
| `- texto` | Lista simples |
| `> **Rótulo** — texto` | Faixa preta (band) |
| `> *Rótulo*` + `> texto` | Vinheta (cena) |
| Tabela Markdown / cerca de código | Tabela / bloco de código |

IDs de seção: `e{n}` para entregas, `v{cap}-{n}` para verbetes, `s{n}` para sistemas/fases, senão um slug do título. O índice (botão "Índice") é montado sozinho a partir dos capítulos e seções.

## Publicação

- Artifacts do Claude: publicar o fragmento em `dist/fragmentos/`. Redeploy no mesmo caminho mantém a URL.
- Fora do Claude: qualquer hospedagem estática serve os `dist/radar-urbano-*.html`. Os PDFs vão por WhatsApp ou e-mail.

## Se for mudar a estética

Só `src/template_branco.html` (casca) e o bloco `EXTRA_CSS` em `src/build.py` (blocos). Depois, `make all`. Nunca editar `dist/` à mão (decisão D20 e D32).
