#!/usr/bin/env python3
"""Gera dist/radar-urbano-dossie.html a partir de conteudo-52.md: o dossiê da holding (52 seções, texto verbatim).
Mantido como peça de visão; o produto inicial está nos arquivos 02 a 05. Uso: python3 src/build_dossie.py"""
import html, re
from pathlib import Path

SRC = Path(__file__).with_name("conteudo-52.md")  # cópia de referencia/01-DOSSIE-HOLDING-VERBATIM.md em formato-fonte
OUT = Path(__file__).resolve().parent.parent / "dist" / "radar-urbano-dossie-holding-verbatim.html"

def inl(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t)
    return t

# ---------- parse ----------
txt = SRC.read_text(encoding="utf-8")
lines = txt.splitlines()
title = lines[0][2:].strip()
subtitle = lines[1].strip().strip("*")
secs = []
cur = None
for l in lines[2:]:
    m = re.match(r"^## SEÇÃO (\d+): (.+)$", l)
    if m:
        cur = {"n": int(m.group(1)), "t": m.group(2).strip(), "paras": [], "items": []}
        secs.append(cur); continue
    if cur is None or not l.strip() or l.strip() == "---": continue
    if l.startswith("  * "):
        cur["items"][-1].setdefault("sub", []).append(l[4:].strip()); continue
    m = re.match(r"^(?:\* |\d+\. )(.+)$", l)
    if m:
        body = m.group(1).strip()
        lm = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", body) or re.match(r"^\*\*(.+?)\*\*:\s*(.*)$", body)
        if lm: cur["items"].append({"lead": lm.group(1), "rest": lm.group(2), "raw": body})
        else: cur["items"].append({"lead": None, "rest": body, "raw": body})
        continue
    cur["paras"].append(l.strip())
assert len(secs) == 52, len(secs)

# ---------- capítulos (só navegação) ----------
CAPS = [("I", "A Tese", 1, 3), ("II", "O Ecossistema", 4, 7), ("III", "Os Quatro Estágios", 8, 11),
        ("IV", "Execução", 12, 19), ("V", "Escala", 20, 29), ("VI", "Governança", 30, 39),
        ("VII", "Perenidade", 40, 49), ("VIII", "O Manifesto", 50, 52)]
def cap_of(n):
    for r, nome, a, b in CAPS:
        if a <= n <= b: return (r, nome, a)

# números-herói que já estão no texto (eco visual, não conteúdo novo)
KPI = {3: [("15 milhões", 15, 0, "", " milhões"), ("3,5 milhões", 3.5, 1, "", " milhões"), ("10.000", 10000, 0, "", "")],
       7: [("R$ 36.000,00", 36000, 0, "R$ ", ",00"), ("R$ 1.800,00", 1800, 0, "R$ ", ",00"), ("20 para 1", 20, 0, "", " para 1"), ("1 mês", 1, 0, "", " mês")]}
DARK = {8, 9, 10, 11, 50}
TIMELINE = {13, 25, 33, 51}

def cnt(label, val, dec, pre, suf):
    return f'<span class="cnt" data-t="{val}" data-dec="{dec}" data-pre="{html.escape(pre)}" data-suf="{html.escape(suf)}">{html.escape(label)}</span>'

def money_tag(v):
    v = v.strip()
    neg = v.startswith("-")
    return neg, v

def header(s, dark=False):
    r, nome, _ = cap_of(s["n"])
    return (f'<div class="hd"><div class="eyebrow rv">Seção {s["n"]} <span>·</span> {r} {html.escape(nome)}</div>'
            f'<h2 class="rv">{inl(s["t"])}</h2></div>')

def rows(items, numerals=True):
    out = ['<ol class="rows stag">']
    for i, it in enumerate(items, 1):
        num = f'<span class="num">{i:02d}</span>' if numerals else '<span class="num dot"></span>'
        if it["lead"]:
            out.append(f'<li>{num}<div><h3>{inl(it["lead"])}</h3><p>{inl(it["rest"])}</p></div></li>')
        else:
            out.append(f'<li>{num}<div><p>{inl(it["rest"])}</p></div></li>')
    out.append("</ol>")
    return "".join(out)

def render(s):
    n = s["n"]; cls = ["sec"]
    if n in DARK: cls.append("dark")
    elif n % 2 == 0: cls.append("alt")
    inner = []
    if n == 52:
        inner.append(f'<section id="s52" class="sec fecho"><div class="wrap"><div class="eyebrow rv">Seção 52</div><h2 class="rv">{inl(s["t"])}</h2>'
                     + "".join(f'<p class="lead rv">{inl(p)}</p>' for p in s["paras"]) + '</div></section>')
        return "".join(inner)
    inner.append(f'<section id="s{n}" class="{" ".join(cls)}"><div class="wrap">')
    inner.append(header(s))
    inner.append('<div class="bd">')
    for p in s["paras"]:
        inner.append(f'<p class="intro rv">{inl(p)}</p>')
    if n in KPI:
        inner.append('<div class="kpis stag">')
        for it, (lab, val, dec, pre, suf) in zip(s["items"], KPI[n]):
            inner.append(f'<div class="kpi"><div class="k-lab">{inl(it["lead"])}</div><div class="k-big">{cnt(lab, val, dec, pre, suf)}</div><p>{inl(it["rest"])}</p></div>')
        inner.append('</div>')
    elif n == 4:
        prods = [it for it in s["items"] if not it["lead"].startswith("Ticket")]
        tk = [it for it in s["items"] if it["lead"].startswith("Ticket")]
        inner.append('<div class="prods stag">')
        for i, it in enumerate(prods, 1):
            m = re.match(r"^(.*?)\s*(\(Ticket:.*\))\.?$", it["rest"])
            desc, foot = (m.group(1), m.group(2)) if m else (it["rest"], "")
            inner.append(f'<div class="prod"><span class="p-n">{i:02d}</span><h3>{inl(it["lead"])}</h3><p>{inl(desc)}</p><div class="p-foot">{inl(foot)}</div></div>')
        inner.append('</div>')
        for it in tk:
            inner.append(f'<div class="band rv"><div class="b-lab">{inl(it["lead"])}</div><p>{inl(it["rest"])}</p></div>')
    elif 8 <= n <= 11:
        est = s["items"][0]; mat = s["items"][1]; caixa = s["items"][2]; val = s["items"][3]
        inner.append(f'<div class="est rv"><div class="k-lab">{inl(est["lead"])}</div><p>{inl(est["rest"])}</p></div>')
        inner.append(f'<div class="k-lab rv" style="margin-top:40px">{inl(mat["lead"])}</div><div class="fin stag">')
        for sub in mat["sub"]:
            mm = re.match(r"^\*?\*?(.+?):\*?\*?\s*\*\*(.+?)\*\*$", sub)
            lab, v = (mm.group(1), mm.group(2)) if mm else (sub, "")
            lab = lab.replace("**", "")
            neg = v.strip().startswith("-")
            soma = "Receita Efetiva" in lab
            inner.append(f'<div class="f-row{" neg" if neg else ""}{" soma" if soma else ""}"><span>{inl(lab)}</span><b>{html.escape(v)}</b></div>')
        inner.append('</div>')
        cm = re.match(r"^\*\*(.+?)\*\*\s*\*(.+?)\*$", caixa["rest"])
        cval, cnote = (cm.group(1), cm.group(2)) if cm else (caixa["rest"].replace("**", ""), "")
        num = float(re.sub(r"[^\d,]", "", cval.split("/")[0]).replace(".", "").replace(",", ".")) if cval else 0
        inner.append(f'<div class="res stag"><div class="r-card"><div class="k-lab">{inl(caixa["lead"])}</div><div class="r-big">{cnt(cval, int(num), 0, "R$ ", ",00 / mês")}</div><div class="r-note">{inl(cnote)}</div></div>')
        vv = val["rest"].replace("**", "")
        vm = re.match(r"R\$ ([\d\.,]+) (.+)$", vv)
        vnum = float(vm.group(1).replace(".", "").replace(",", ".")) if vm else 0
        vdec = 1 if "," in (vm.group(1) if vm else "") else 0
        inner.append(f'<div class="r-card val"><div class="k-lab">{inl(val["lead"])}</div><div class="r-big">{cnt(vv, vnum, vdec, "R$ ", " " + (vm.group(2) if vm else ""))}</div></div></div>')
    elif n in TIMELINE:
        inner.append('<div class="tl stag">')
        for it in s["items"]:
            inner.append(f'<div class="tl-i"><span class="tl-dot"></span><div class="tl-lab">{inl(it["lead"])}</div><p>{inl(it["rest"])}</p></div>')
        inner.append('</div>')
    elif n == 50:
        inner.append('<div class="mani stag">')
        for i, it in enumerate(s["items"], 1):
            inner.append(f'<div class="m-i"><span class="num">{i:02d}</span><div><h3>{inl(it["lead"])}</h3><p>{inl(it["rest"])}</p></div></div>')
        inner.append('</div>')
    elif s["items"]:
        inner.append(rows(s["items"]))
    inner.append('</div></div></section>')
    return "".join(inner)

# ---------- índice ----------
idx = []
for r, nome, a, b in CAPS:
    idx.append(f'<div class="ix-g"><div class="ix-c"><span class="ix-r">{r}</span>{html.escape(nome)}</div>')
    for s in secs[a-1:b]:
        idx.append(f'<a href="#s{s["n"]}" data-s="s{s["n"]}"><i>{s["n"]:02d}</i><span>{inl(s["t"])}</span></a>')
    idx.append('</div>')

body = []
for r, nome, a, b in CAPS:
    body.append(f'<div class="cap" id="c{r}"><div class="wrap"><div class="cap-r rv">{r}</div><div class="cap-n rv">{html.escape(nome)}</div><div class="cap-s rv">Seções {a}–{b}</div></div></div>')
    for s in secs[a-1:b]:
        body.append(render(s))

tpl = Path(__file__).with_name("template_branco.html").read_text(encoding="utf-8")
out = (tpl.replace("{{TITULO}}", inl(title)).replace("{{SUB}}", inl(subtitle))
          .replace("{{INDICE}}", "\n".join(idx)).replace("{{CORPO}}", "\n".join(body)))
OUT.parent.mkdir(parents=True, exist_ok=True)
i = out.index("</style>") + 8
out = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n' + out[:i] + "\n</head>\n<body>\n" + out[i:] + "\n</body>\n</html>\n")
OUT.write_text(out, encoding="utf-8")
print("ok", len(out)//1024, "KB", len(secs), "seções")
