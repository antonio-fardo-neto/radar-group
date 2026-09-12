#!/usr/bin/env python3
"""Radar Urbano · monta os documentos finais a partir das partes (_work/parts) e o TUDO-EM-UM.md.

Uso:
  python3 src/assemble.py parts      # _work/parts/*.md → 02, 03, 04, 05, 11 (e 00, 08, 09, 10 se existirem)
  python3 src/assemble.py tudo       # concatena os arquivos numerados + README em TUDO-EM-UM.md
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = ROOT / "_work" / "parts"

def join(files):
    out = []
    for f in files:
        t = (PARTS / f).read_text(encoding="utf-8").strip("\n")
        out.append(t)
    return "\n\n".join(out) + "\n"

def parts():
    plan = {
        "02-MAPA-DE-ENTREGAS.md": ["entregas.md"],
        "03-MAPA-DE-ACESSOS.md": ["acessos.md"],
        "04-MAPA-MUNDI.md": ["mundi-A.md", "mundi-B.md", "mundi-C.md"],
        "05-BIBLIA.md": ["biblia-A.md", "biblia-B.md", "biblia-C.md", "biblia-D.md", "biblia-E.md"],
        "11-ROADMAP-FASEADO.md": ["roadmap.md"],
        "00-CONTEXTO.md": ["00-CONTEXTO.md"],
        "08-DECISOES.md": ["08-DECISOES.md"],
        "09-PROMPTS-E-GOSTO.md": ["09-PROMPTS-E-GOSTO.md"],
        "10-BACKLOG.md": ["10-BACKLOG.md"],
    }
    for target, srcs in plan.items():
        if not all((PARTS / s).exists() for s in srcs):
            print("pulando", target, "(partes faltando)"); continue
        (ROOT / target).write_text(join(srcs), encoding="utf-8")
        print("ok", target, (ROOT / target).stat().st_size // 1024, "KB")

def tudo():
    order = ["README.md"] + sorted(p.name for p in ROOT.glob("[0-9][0-9]-*.md"))
    out = ["<!-- Radar Urbano · TUDO-EM-UM: todos os arquivos do pacote concatenados, na ordem, para colar de uma vez numa IA ou ler de ponta a ponta. Gerado por src/assemble.py; não editar à mão. -->\n"]
    for name in order:
        p = ROOT / name
        if not p.exists(): continue
        out.append(f"\n\n<!-- ======================================================================\n     ARQUIVO: {name}\n     ====================================================================== -->\n\n")
        out.append(p.read_text(encoding="utf-8").strip("\n") + "\n")
    (ROOT / "TUDO-EM-UM.md").write_text("".join(out), encoding="utf-8")
    print("ok TUDO-EM-UM.md", (ROOT / "TUDO-EM-UM.md").stat().st_size // 1024, "KB", len(order), "arquivos")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "parts"
    {"parts": parts, "tudo": tudo}[cmd]()
