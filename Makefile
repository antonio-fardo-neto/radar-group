# Radar Urbano · geração dos documentos
# make html   → dist/*.html (apresentações da edição branca, arquivo único, abre em qualquer navegador)
# make pdf    → dist/*.pdf  (precisa de Chrome/Chromium; CHROME=/caminho se não estiver no PATH)
# make tudo   → TUDO-EM-UM.md
# make all    → tudo acima

PY ?= python3

.PHONY: all html pdf tudo clean

all: html pdf tudo

html:
	$(PY) src/build.py --all --fragment

pdf: html
	$(PY) src/make_pdf.py --all

tudo:
	$(PY) src/assemble.py tudo

clean:
	rm -rf dist/*.html dist/*.pdf dist/fragmentos
