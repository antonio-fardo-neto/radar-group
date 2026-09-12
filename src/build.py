#!/usr/bin/env python3
"""Radar Urbano · gerador único: Markdown (fonte de verdade) → apresentação web da edição branca.

Uso:
  python3 src/build.py radar-urbano/05-MAPA-DE-ENTREGAS.md --aba "Entregas" --out dist/radar-urbano-entregas.html
  python3 src/build.py --all            # gera todos os documentos listados em DOCS
  python3 src/build.py --all --fragment # também gera o fragmento (sem <html>/<head>) para publicar como artifact
  python3 src/build.py doc.md --aba "Aba" --titulo "Nome do artifact" --out dist/doc.html --fragment

Convenções do Markdown (as mesmas que o exportador do pacote original produzia):
  # TÍTULO DO DOCUMENTO                → capa (h1 em linhas) · linha seguinte *subtítulo* → capa
  *Capítulo I · Nome*  (linha em itálico antes de um ##) → etiqueta (eyebrow) da seção
  ## TÍTULO DA SEÇÃO {#id .alt .dark .fecho}           → seção; atributos opcionais
  *frase*  logo após o ##            → tagline (nas seções .fecho vira o lead)
  ---  +  # Capítulo R — Nome (Sub)  → divisória de capítulo (numeral romano)
  ### Nome                            → subtítulo de bloco (agente, conector, receita)
  #### Título — Sub                   → cartão de calendário (blocos #### consecutivos viram uma grade)
  **Rótulo** (linha sozinha)          → etiqueta de bloco (k-lab); agrupa o que vem depois
  1. **Lead** — texto                 → linhas numeradas (rows); se sem lead em negrito → passos (steps)
  - **Rótulo:** valor                 → pares rótulo/valor (spec)
  - **Termo**: definição              → lista de definições (dl / glossário)
  - **Lead** — texto  (+ "  - Linha: valor" aninhado)  → cartões (grid), com linhas de conta opcionais
  - texto                             → lista simples
  > **Rótulo** — texto                → faixa preta (band)
  > *Rótulo*  +  > texto              → vinheta (vin)
  > texto                             → citação
  | tabela |                          → tabela
  ```código```                        → bloco de código
  *Figura: ...*                       → legenda (ignorada na apresentação)
Eyebrows do tipo "Entrega 03 · ...", "Verbete III.2 · ...", "Sistema A · ..." geram o número grande da seção.
"""
import html, re, sys, argparse
from pathlib import Path

H = html.escape
ROOT = Path(__file__).resolve().parent.parent
TPL = Path(__file__).with_name("template_branco.html")

# Documentos do pacote: (arquivo md, nome na aba, arquivo de saída, linhas da capa opcionais)
DOCS = [
    ("radar-urbano/01-DOSSIE.md", "Dossiê", "radar-urbano-dossie.html"),
    ("radar-urbano/02-POV-CLIENTE.md", "POV Cliente", "radar-urbano-pov-cliente.html"),
    ("radar-urbano/03-POV-PLAYER.md", "POV Player", "radar-urbano-pov-player.html"),
    ("radar-urbano/04-EXPANSAO.md", "Expansão", "radar-urbano-expansao.html"),
    ("radar-urbano/05-MAPA-DE-ENTREGAS.md", "Mapa de Entregas", "radar-urbano-entregas.html"),
    ("radar-urbano/06-MAPA-DE-ACESSOS.md", "Mapa de Acessos", "radar-urbano-acessos.html"),
    ("radar-urbano/07-MAPA-MUNDI.md", "Mapa Mundi", "radar-urbano-mapa-mundi.html"),
    ("radar-urbano/08-BIBLIA.md", "Bíblia", "radar-urbano-biblia.html"),
]

# ----------------------------------------------------------------- inline
def inl(t):
    t = H(t, quote=False)
    t = re.sub(r"`(.+?)`", lambda m: "<code>" + m.group(1) + "</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\*)([^*\n]+?)\*(?!\w)", r"<em>\1</em>", t)
    return t

def strip_md(t):
    return re.sub(r"[*`]", "", t)

# ----------------------------------------------------------------- parse
ATTR_RE = re.compile(r"\s*\{([^}]*)\}\s*$")

def parse_attrs(title):
    m = ATTR_RE.search(title)
    if not m: return title.strip(), None, []
    title = title[:m.start()].strip()
    id_, cls = None, []
    for tok in m.group(1).split():
        if tok.startswith("#"): id_ = tok[1:]
        elif tok.startswith("."): cls.append(tok[1:])
    return title, id_, cls

def slug(s):
    s = strip_md(s).lower()
    s = re.sub(r"[àáâãä]", "a", s); s = re.sub(r"[èéêë]", "e", s); s = re.sub(r"[ìíîï]", "i", s)
    s = re.sub(r"[òóôõö]", "o", s); s = re.sub(r"[ùúûü]", "u", s); s = s.replace("ç", "c")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:48] or "sec"

def blocks_of(lines):
    """Divide linhas em blocos brutos: (tipo, payload)."""
    out, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith("```"):
            j = i + 1; buf = []
            while j < n and not lines[j].startswith("```"): buf.append(lines[j]); j += 1
            out.append(("code", "\n".join(buf))); i = j + 1; continue
        if l.startswith("<!--"):
            j = i
            while j < n and "-->" not in lines[j]: j += 1
            i = j + 1; continue
        if l.strip() == "---": out.append(("hr", None)); i += 1; continue
        if l.startswith("#"):
            m = re.match(r"^(#{1,4})\s+(.*)$", l)
            out.append(("h" + str(len(m.group(1))), m.group(2).strip())); i += 1; continue
        if l.startswith("|"):
            j = i; buf = []
            while j < n and lines[j].startswith("|"): buf.append(lines[j]); j += 1
            out.append(("table", buf)); i = j; continue
        if l.startswith(">"):
            j = i; buf = []
            while j < n and lines[j].startswith(">"): buf.append(lines[j][1:].strip()); j += 1
            out.append(("quote", buf)); i = j; continue
        if re.match(r"^(\d+)\.\s", l) or re.match(r"^[-*]\s", l):
            ordered = bool(re.match(r"^\d+\.\s", l))
            j = i; items = []
            while j < n and lines[j].strip():
                lj = lines[j]
                if re.match(r"^\s{2,}[-*]\s", lj) and items:
                    items[-1]["sub"].append(re.sub(r"^\s+[-*]\s", "", lj)); j += 1; continue
                m = re.match(r"^(?:\d+\.|[-*])\s+(.*)$", lj)
                if not m: break
                items.append({"text": m.group(1).strip(), "sub": []}); j += 1
            out.append(("ol" if ordered else "ul", items)); i = j; continue
        # parágrafo: junta linhas até linha vazia ou início de outro bloco
        j = i; buf = []
        while j < n and lines[j].strip() and not re.match(r"^(#|```|\||>|---$|\d+\.\s|[-*]\s|<!--)", lines[j]):
            buf.append(lines[j].strip()); j += 1
        if not buf: buf = [l.strip()]; j = i + 1
        out.append(("p", " ".join(buf))); i = j
    return out

# ----------------------------------------------------------------- render de blocos
def is_label_line(t):
    return bool(re.match(r"^\*\*[^*]+\*\*:?$", t.strip()))

def is_italic_line(t):
    t = t.strip()
    return len(t) > 2 and t.startswith("*") and t.endswith("*") and not t.startswith("**") and "*" not in t[1:-1]

def split_lead(text):
    """'**Lead** — resto' → (lead, resto) ; senão None."""
    m = re.match(r"^\*\*(.+?)\*\*\s*[—–-]\s*(.*)$", text)
    return (m.group(1), m.group(2)) if m else None

def split_spec(text):
    m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", text)
    return (m.group(1), m.group(2)) if m else None

def split_def(text):
    m = re.match(r"^\*\*(.+?)\*\*:\s*(.*)$", text)
    return (m.group(1), m.group(2)) if m else None

def render_table(buf):
    rows = []
    for l in buf:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if all(re.match(r"^:?-{2,}:?$", c) for c in cells if c): continue
        rows.append(cells)
    if not rows: return ""
    head, body = rows[0], rows[1:]
    o = ['<div class="tbl rv"><table><thead><tr>'] + [f"<th>{inl(h)}</th>" for h in head] + ["</tr></thead><tbody>"]
    for r in body: o.append("<tr>" + "".join(f"<td>{inl(c)}</td>" for c in r) + "</tr>")
    o.append("</tbody></table></div>")
    return "".join(o)

def render_list(kind, items, ctx):
    texts = [it["text"] for it in items]
    if kind == "ol":
        leads = [split_lead(t) for t in texts]
        if all(leads):
            o = ['<ol class="rows stag">']
            for i, (lead, rest) in enumerate(leads, 1):
                o.append(f'<li><span class="num">{i:02d}</span><div><h3>{inl(lead)}</h3><p>{inl(rest)}</p></div></li>')
            return "".join(o) + "</ol>"
        o = ['<ol class="steps stag">'] + [f"<li>{inl(t)}</li>" for t in texts]
        return "".join(o) + "</ol>"
    specs = [split_spec(t) for t in texts]
    if all(specs):
        o = ['<div class="spec stag">']
        for k, v in specs: o.append(f'<div class="sp-row"><div class="sp-k">{inl(k)}</div><div class="sp-v">{inl(v)}</div></div>')
        return "".join(o) + "</div>"
    defs = [split_def(t) for t in texts]
    if all(defs):
        o = ['<dl class="dl stag">']
        for k, v in defs: o.append(f"<div><dt>{inl(k)}</dt><dd>{inl(v)}</dd></div>")
        return "".join(o) + "</dl>"
    leads = [split_lead(t) for t in texts]
    if all(leads):
        o = ['<div class="cards stag">']
        for it, (lead, rest) in zip(items, leads):
            m = re.match(r"^(\d{1,2}|[IVX]+|[A-H])\s*[·:]\s*(.+)$", lead)
            num, lead2 = (m.group(1), m.group(2)) if m else (None, lead)
            o.append('<div class="card">')
            if num: o.append(f'<span class="p-n">{H(num)}</span>')
            o.append(f"<h3>{inl(lead2)}</h3>")
            if rest: o.append(f"<p>{inl(rest)}</p>")
            for s in it["sub"]:
                ms = re.match(r"^(.*?):\s*(.+)$", s)
                if ms:
                    hi = " hi" if re.search(r"custo por contato|contatos no m", ms.group(1), re.I) else ""
                    lg = "" if (len(ms.group(2)) <= 14 and re.search(r"\d", ms.group(2))) else " long"
                    o.append(f'<div class="c-row{hi}{lg}"><span>{inl(ms.group(1))}</span><b>{inl(ms.group(2))}</b></div>')
                else:
                    o.append(f'<div class="c-row"><span>{inl(s)}</span></div>')
            o.append("</div>")
        return "".join(o) + "</div>"
    o = ['<ul class="list stag">']
    for it in items:
        o.append(f"<li>{inl(it['text'])}")
        if it["sub"]: o.append("<ul>" + "".join(f"<li>{inl(s)}</li>" for s in it["sub"]) + "</ul>")
        o.append("</li>")
    return "".join(o) + "</ul>"

def render_quote(buf):
    text = " ".join(buf).strip()
    if len(buf) >= 2 and is_italic_line(buf[0]):
        return f'<div class="vin rv"><div class="k-lab">{inl(buf[0].strip("*"))}</div><p>{inl(" ".join(buf[1:]))}</p></div>'
    m = re.match(r"^\*\*(.+?)\*\*\s*[—–-]\s*(.*)$", text, re.S)
    if m:
        return f'<div class="band rv"><div class="b-lab">{inl(m.group(1))}</div><p>{inl(m.group(2))}</p></div>'
    return f'<blockquote class="quote rv">{inl(text)}</blockquote>'

def render_body(blocks, sec_cls, ctx):
    """Renderiza o corpo de uma seção (lista de blocos), agrupando cartões de calendário e grupos de etiqueta."""
    out, i, n = [], 0, len(blocks)
    open_vb = False
    def close_vb():
        nonlocal open_vb
        if open_vb: out.append("</div>"); open_vb = False
    while i < n:
        t, p = blocks[i]
        if t == "h4":
            close_vb()
            cards = []
            while i < n and blocks[i][0] == "h4":
                title = blocks[i][1]; i += 1
                mm = re.match(r"^(.*?)\s+[—–]\s+(.*)$", title)
                ct, cs = (mm.group(1), mm.group(2)) if mm else (title, "")
                inner = []
                while i < n and blocks[i][0] in ("p", "ul", "ol") and not (blocks[i][0] == "p" and is_label_line(blocks[i][1])):
                    bt, bp = blocks[i]
                    if bt == "p": inner.append(f"<p>{inl(bp)}</p>")
                    elif bt in ("ul", "ol"): inner.append("<ul>" + "".join(f"<li>{inl(it['text'])}</li>" for it in bp) + "</ul>")
                    else: inner.append(render_block(bt, bp, ctx))
                    i += 1
                cards.append(f'<div class="cal-i"><div class="cal-t">{inl(ct)}</div><div class="cal-s">{inl(cs)}</div>{"".join(inner)}</div>')
            out.append('<div class="cal stag">' + "".join(cards) + "</div>")
            continue
        if t == "h3":
            close_vb()
            m = re.match(r"^(\d{1,2})\s*[·]?\s*(.+)$", p)
            if m: out.append(f'<div class="h3c rv"><span class="h3n">{m.group(1)}</span>{inl(m.group(2))}</div>')
            else:
                # "### Cartógrafo Medir a posição..." → nome (uma palavra, com parêntese opcional) + missão (começa em maiúscula, termina em pontuação)
                m2 = re.match(r"^([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÁÉÍÓÚÂÊÔÃÕÇáéíóúâêôãõç-]*(?:\s\([^)]*\))?)\s+([A-ZÁÉÍÓÚÂÊÔÃÕÇ].+[.!?])$", p)
                if m2 and len(m2.group(1)) < 32: out.append(f'<div class="h3c rv">{inl(m2.group(1))}<span class="h3m">{inl(m2.group(2))}</span></div>')
                else: out.append(f'<div class="h3c rv">{inl(p)}</div>')
            i += 1; continue
        if t == "p" and is_label_line(p):
            close_vb()
            out.append(f'<div class="vb rv"><div class="vb-k">{inl(p.strip("*:"))}</div>'); open_vb = True
            i += 1; continue
        if t == "quote":
            text = " ".join(p).strip()
            if re.match(r"^\*\*(.+?)\*\*\s*[—–-]", text) and not (len(p) >= 2 and is_italic_line(p[0])):
                close_vb()
        out.append(render_block(t, p, ctx)); i += 1
    close_vb()
    return "".join(out)

def render_block(t, p, ctx):
    if t == "p":
        if p.startswith("*Figura:"): return ""
        if is_italic_line(p): return f'<p class="intro rv"><em>{inl(p.strip("*"))}</em></p>'
        return f'<p class="intro rv">{inl(p)}</p>'
    if t in ("ul", "ol"): return render_list(t, p, ctx)
    if t == "quote": return render_quote(p)
    if t == "table": return render_table(p)
    if t == "code": return f'<pre class="rv">{H(p)}</pre>'
    if t == "hr": return ""
    if t in ("h3", "h4"): return f'<div class="h3c rv">{inl(p)}</div>'
    return ""

# ----------------------------------------------------------------- documento
BIGN_RES = [re.compile(r"^Entrega\s+(\d+)"), re.compile(r"^Verbete\s+([IVX]+\.\d+)"), re.compile(r"^Sistema\s+([A-H])\b"),
            re.compile(r"^Seção\s+(\d+)"), re.compile(r"^Fase\s+(\d+)"), re.compile(r"^Módulo\s+(\d+)")]

def build(md_path, aba, out_path, fragment=False, titulo=None, marca=None):
    src = Path(md_path).read_text(encoding="utf-8")
    lines = src.splitlines()
    blocks = blocks_of(lines)
    # capa
    title = next((p for t, p in blocks if t == "h1"), "RADAR URBANO")
    first_h1 = next(i for i, b in enumerate(blocks) if b[0] == "h1")
    sub = ""
    if first_h1 + 1 < len(blocks) and blocks[first_h1 + 1][0] == "p" and is_italic_line(blocks[first_h1 + 1][1]):
        sub = blocks[first_h1 + 1][1].strip("*")
        del blocks[first_h1 + 1]
    del blocks[first_h1]
    # seções
    sections, chapters = [], []   # chapters: (roman, name, sub, id, position=index in sections)
    cur = None; pending_eyebrow = None; auto_alt = False
    i = 0
    while i < len(blocks):
        t, p = blocks[i]
        if t == "h1":
            m = re.match(r"^Cap[íi]tulo\s+([IVXLC0-9]+)\s*[—–-]\s*(.*?)(?:\s*\((.*)\))?$", p)
            if m:
                cid = "c" + m.group(1)
                chapters.append({"r": m.group(1), "name": m.group(2), "sub": m.group(3) or "", "id": cid, "pos": len(sections)})
                auto_alt = False
            i += 1; continue
        if t == "p" and is_italic_line(p) and i + 1 < len(blocks) and blocks[i + 1][0] == "h2":
            pending_eyebrow = p.strip("*"); i += 1; continue
        if t == "h2":
            title2, id_, cls = parse_attrs(p)
            eyebrow = pending_eyebrow or ""; pending_eyebrow = None
            bign = None
            for rx in BIGN_RES:
                mm = rx.match(eyebrow)
                if mm: bign = mm.group(1); break
            if not id_:
                if bign: id_ = ("v" + bign.replace(".", "-")) if "." in bign else (("e" if eyebrow.startswith("Entrega") else "s") + bign)
                else: id_ = slug(title2)
            base_ids = {s["id"] for s in sections}
            k = 2; oid = id_
            while id_ in base_ids: id_ = f"{oid}-{k}"; k += 1
            if not any(c in ("alt", "dark", "fecho") for c in cls):
                if auto_alt: cls.append("alt")
                auto_alt = not auto_alt
            else:
                auto_alt = False
            tag = None
            if i + 1 < len(blocks) and blocks[i + 1][0] == "p" and is_italic_line(blocks[i + 1][1]) and not (i + 2 < len(blocks) and blocks[i + 2][0] == "h2"):
                tag = blocks[i + 1][1].strip("*"); i += 1
            cur = {"id": id_, "title": title2, "eyebrow": eyebrow, "cls": cls, "bign": bign, "tag": tag, "blocks": []}
            sections.append(cur); i += 1; continue
        if cur is not None: cur["blocks"].append((t, p))
        i += 1

    # html das seções
    body = []
    chap_at = {c["pos"]: c for c in chapters}
    for idx, s in enumerate(sections):
        if idx in chap_at:
            c = chap_at[idx]
            body.append(f'<div class="cap" id="{c["id"]}"><div class="wrap"><div class="cap-r rv">{H(c["r"])}</div><div class="cap-n rv">{inl(c["name"])}</div><div class="cap-s rv">{inl(c["sub"])}</div></div></div>')
        cls = " ".join(s["cls"])
        if "fecho" in s["cls"]:
            lead = f'<p class="lead rv">{inl(s["tag"])}</p>' if s["tag"] else ""
            inner = render_body(s["blocks"], cls, {}).replace('class="intro rv"', 'class="lead rv"')
            body.append(f'<section id="{s["id"]}" class="sec fecho"><div class="wrap"><div class="eyebrow rv">{inl(s["eyebrow"])}</div><h2 class="rv">{inl(s["title"])}</h2>{lead}{inner}</div></section>')
            continue
        eb = s["eyebrow"]
        if " · " in eb:
            a, b = eb.split(" · ", 1); eb_html = f"{inl(a)} <span>·</span> {inl(b)}"
        else: eb_html = inl(eb)
        bn = f'<div class="big-n rv">{H(s["bign"])}</div>' if s["bign"] else ""
        tag = f'<p class="tag rv">{inl(s["tag"])}</p>' if s["tag"] else ""
        wide = " wide" if any(b[0] in ("table", "code") for b in s["blocks"]) or len(s["blocks"]) > 14 else ""
        body.append(f'<section id="{s["id"]}" class="sec {cls}{wide}"><div class="wrap"><div class="hd"><div class="eyebrow rv">{eb_html}</div>{bn}<h2 class="rv">{inl(s["title"])}</h2>{tag}</div><div class="bd">{render_body(s["blocks"], cls, {})}</div></div></section>')

    # índice
    idx_html = []
    if chapters:
        idx_html.append('<div class="ix-g"><div class="ix-c"><span class="ix-r">§</span>Capítulos</div>')
        for c in chapters: idx_html.append(f'<a href="#{c["id"]}" data-s="{c["id"]}"><i>{H(c["r"])}</i><span>{inl(c["name"])}</span></a>')
        idx_html.append("</div>")
        groups = []
        pre = [s for s in sections[:chapters[0]["pos"]]]
        if pre: groups.append(("Antes de tudo", pre))
        for ci, c in enumerate(chapters):
            end = chapters[ci + 1]["pos"] if ci + 1 < len(chapters) else len(sections)
            groups.append((c["name"], sections[c["pos"]:end]))
    else:
        groups = []
        for s in sections:
            eb = s["eyebrow"]
            key = eb.split(" · ")[0] if eb else "Seções"
            if groups and groups[-1][0] == key: groups[-1][1].append(s)
            else: groups.append((key, [s]))
        # capítulos = grupos cujo nome começa com "Capítulo"
        caps = [(g[0], g[1][0]) for g in groups if g[0].lower().startswith(("capítulo", "capitulo"))]
        if caps:
            idx_html.append('<div class="ix-g"><div class="ix-c"><span class="ix-r">§</span>Capítulos</div>')
            for name, s0 in caps:
                mm = re.match(r"^Cap[íi]tulo\s+(\S+)", name)
                r = mm.group(1) if mm else "·"
                nm = s0["eyebrow"].split(" · ", 1)[1] if " · " in s0["eyebrow"] else s0["title"]
                idx_html.append(f'<a href="#{s0["id"]}" data-s="{s0["id"]}"><i>{H(r)}</i><span>{inl(nm)}</span></a>')
            idx_html.append("</div>")
    for name, secs in groups:
        if len(secs) < 2 and chapters == [] and name.lower().startswith(("capítulo", "capitulo")): continue
        label = name
        if " · " in secs[0]["eyebrow"] and name.lower().startswith(("capítulo", "capitulo")):
            label = secs[0]["eyebrow"].split(" · ", 1)[1]
        idx_html.append(f'<div class="ix-g"><div class="ix-c">{inl(label)}</div>')
        for k, s in enumerate(secs, 1):
            num = s["bign"] or f"{k:02d}"
            idx_html.append(f'<a href="#{s["id"]}" data-s="{s["id"]}"><i>{H(num)}</i><span>{inl(s["title"])}</span></a>')
        idx_html.append("</div>")

    # capa: linhas do h1
    t = strip_md(title)
    if ":" in t:
        a, b = t.split(":", 1); lines_h1 = [a.strip() + ":"]
        b = b.strip()
        if len(b) > 24:
            words = b.split(); mid = len(b) // 2; acc = ""; cut = 0
            for w in words:
                if len(acc) + len(w) > mid and acc: break
                acc += (" " if acc else "") + w; cut += 1
            lines_h1 += [" ".join(words[:cut]), " ".join(words[cut:])]
        else: lines_h1.append(b)
    else: lines_h1 = [t]
    h1 = "<h1>" + "".join(f'<span class="l"><span>{H(x)}</span></span>' for x in lines_h1 if x) + "</h1>"

    tpl = TPL.read_text(encoding="utf-8")
    page = (tpl.replace("{{SUB}}", inl(sub)).replace("{{INDICE}}", "\n".join(idx_html)).replace("{{CORPO}}", "\n".join(body))
               .replace("</style>", EXTRA_CSS + "</style>")
               .replace("<title>Radar Urbano</title>", f"<title>{H(titulo)}</title>" if titulo else f"<title>Radar Urbano · {H(aba)}</title>"))
    page = re.sub(r"<h1>.*?</h1>", lambda m: h1, page, count=1, flags=re.S)
    if marca:
        page = page.replace("<span>Radar Urbano</span>", f"<span>{H(marca)}</span>")
        page = page.replace('<div class="k">Radar Urbano</div>', f'<div class="k">{H(marca)}</div>')
    if not fragment:
        i = page.index("</style>") + 8
        page = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
                + page[:i] + "\n</head>\n<body>\n" + page[i:] + "\n</body>\n</html>\n")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(page, encoding="utf-8")
    print(f"ok {out_path} {len(page)//1024} KB · {len(sections)} seções · {len(chapters)} capítulos")

EXTRA_CSS = '''
/* blocos comuns aos documentos gerados a partir do Markdown */
.big-n{font-family:var(--serif);font-size:clamp(56px,6.5vw,104px);line-height:.9;color:var(--ink-3);margin:-6px 0 14px;letter-spacing:.01em}
.sec.alt .big-n{color:#C9C9CE}
.tag{font-family:var(--serif);font-style:italic;font-size:clamp(19px,1.6vw,24px);line-height:1.4;color:var(--ink-2);margin-top:18px;max-width:28ch}
.spec{border-top:1px solid var(--line);margin:6px 0 26px}
.sp-row{display:grid;grid-template-columns:180px 1fr;gap:24px;padding:16px 0;border-bottom:1px solid var(--line)}
.sp-k{font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--ink-3);padding-top:4px}
.sp-v{font-size:15.5px;line-height:1.6;color:var(--ink)}
.h3c{font-family:var(--sans);font-size:19px;font-weight:600;margin:44px 0 14px;letter-spacing:.005em;display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
.h3c .h3m{font-family:var(--serif);font-style:italic;font-weight:400;font-size:18px;color:var(--ink-2)}
.h3c .h3n{font-family:var(--serif);font-weight:400;font-size:26px;color:var(--ink-3)}
.vb{margin:0 0 26px}.vb-k{font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--em);margin:26px 0 10px}
.vb .intro{font-size:16.5px}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em;background:var(--bg-2);padding:1px 6px;border-radius:5px;color:var(--ink)}
.sec.alt code{background:#E8E8ED}
pre{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;line-height:1.55;background:var(--ink);color:#E8ECEA;border-radius:16px;padding:22px 24px;overflow-x:auto;margin:10px 0 18px;white-space:pre-wrap}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:16px;background:var(--bg);margin:10px 0 18px}
table{border-collapse:collapse;width:100%;font-size:14px;min-width:560px}
th,td{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left;line-height:1.5}
th{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-3);font-weight:500;background:var(--bg-2)}
tbody tr:last-child td{border-bottom:0}
.steps{margin:6px 0 18px;padding-left:24px}.steps li{font-size:16px;line-height:1.65;color:var(--ink);margin:10px 0}.steps li::marker{color:var(--em);font-family:var(--serif);font-size:18px}
.list{margin:6px 0 18px;padding-left:20px}.list li{font-size:16px;line-height:1.65;color:var(--ink);margin:6px 0}.list ul{padding-left:18px;margin:4px 0}
.dl{margin:6px 0 18px;display:grid;grid-template-columns:1fr;gap:0}
.dl div{border-top:1px solid var(--line);padding:12px 0}.dl dt{font-weight:600;font-size:15px}.dl dd{margin:3px 0 0;color:var(--ink-2);font-size:15px;line-height:1.55}
.sec.dark .dl{grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0 28px}
.sec.dark .dl div{border-color:rgba(255,255,255,.12)}.sec.dark .dl dt{color:#F5F5F7}.sec.dark .dl dd{color:rgba(255,255,255,.65)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin:6px 0 18px}
.card{background:var(--bg);border-radius:22px;padding:26px 26px 22px;border:1px solid var(--line);display:flex;flex-direction:column;gap:8px;transition:transform .6s var(--ease),box-shadow .6s var(--ease)}
.sec.alt .card{border-color:transparent}
.card:hover{transform:translateY(-4px);box-shadow:0 30px 60px -36px rgba(0,0,0,.25)}
.card .p-n{font-family:var(--serif);font-size:20px;color:var(--ink-3)}
.card h3{font-size:16.5px;font-weight:600;line-height:1.35}
.card p{font-size:14.5px;color:var(--ink-2);line-height:1.55}
.c-row{display:flex;justify-content:space-between;gap:16px;padding:9px 0;border-top:1px solid var(--line);font-size:13.5px;color:var(--ink-2)}
.c-row b{font-family:var(--serif);font-weight:400;font-size:18px;color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap}
.c-row.hi{color:var(--ink)}.c-row.hi b{color:var(--em);font-size:22px}
.c-row.long{flex-direction:column;align-items:flex-start;gap:3px}
.c-row.long>span{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-3)}
.c-row.long b{font-family:var(--sans);font-weight:400;font-size:14px;line-height:1.5;white-space:normal;color:var(--ink-2)}
.sec.dark .c-row.long b{color:rgba(255,255,255,.72)}
.sec.dark .card{background:var(--dark-2);border-color:rgba(255,255,255,.08)}.sec.dark .card h3{color:#F5F5F7}.sec.dark .card p{color:rgba(255,255,255,.7)}
.vin{margin-top:36px;padding:30px 0 0;border-top:1px solid var(--line)}
.vin p{font-family:var(--serif);font-size:clamp(19px,1.5vw,23px);line-height:1.5;color:var(--ink);max-width:62ch;text-wrap:pretty}
.band{margin:14px 0 22px}
.band p{font-family:var(--sans);font-size:16.5px;line-height:1.55}
.quote{margin:10px 0 18px;padding:4px 0 4px 22px;border-left:2px solid var(--em);font-family:var(--serif);font-size:19px;line-height:1.5;color:var(--ink)}
.cal{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin:6px 0 18px}
.cal-i{background:var(--bg);border-radius:22px;padding:26px 26px 22px;border:1px solid var(--line)}
.sec.alt .cal-i{border-color:transparent}
.cal-t{font-family:var(--serif);font-size:30px;line-height:1;color:var(--ink);margin-bottom:8px}
.cal-s{font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--ink-3);margin-bottom:14px}
.cal p{font-size:14.5px;color:var(--ink-2);line-height:1.55}
.cal ul{margin:0;padding:0;list-style:none}.cal li{font-size:14.5px;color:var(--ink-2);line-height:1.55;padding:9px 0;border-top:1px solid var(--line)}
.sec.dark .rows li{border-color:rgba(255,255,255,.12)}.sec.dark .rows h3{color:#F5F5F7}.sec.dark .rows p{color:rgba(255,255,255,.7)}.sec.dark .num{color:rgba(255,255,255,.35)}
.sec.dark .k-lab,.sec.dark .vb-k{color:rgba(255,255,255,.5)}.sec.dark .tbl{background:var(--dark-2);border-color:rgba(255,255,255,.1)}.sec.dark th{background:rgba(255,255,255,.05);color:rgba(255,255,255,.5)}.sec.dark td{color:rgba(255,255,255,.8);border-color:rgba(255,255,255,.08)}.sec.dark .intro{color:rgba(255,255,255,.78)}
.sec.dark .sp-row{border-color:rgba(255,255,255,.12)}.sec.dark .sp-v{color:rgba(255,255,255,.85)}.sec.dark .list li,.sec.dark .steps li{color:rgba(255,255,255,.85)}
.sec.dark .cal-i{background:var(--dark-2);border-color:rgba(255,255,255,.08)}.sec.dark .cal-t{color:#F5F5F7}.sec.dark .cal p,.sec.dark .cal li{color:rgba(255,255,255,.7);border-color:rgba(255,255,255,.1)}
.sec.dark .band{background:var(--dark-2);border:1px solid rgba(255,255,255,.1)}.sec.dark .quote{color:#F5F5F7}
.sec.wide .wrap{grid-template-columns:1fr}.sec.wide .hd{position:static;margin-bottom:10px}
.ix-g a i{font-size:12px}
@media (max-width:700px){.sp-row{grid-template-columns:1fr;gap:6px}}
'''

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md", nargs="?")
    ap.add_argument("--aba", default="Documento")
    ap.add_argument("--out")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--fragment", action="store_true", help="gera também a versão fragmento (para artifacts)")
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--titulo", help="título da aba/artifact; sem ele, 'Radar Urbano · <aba>'")
    ap.add_argument("--marca", help="assinatura no topo e na capa; sem ela, 'Radar Urbano'")
    a = ap.parse_args()
    if a.all:
        for md, aba, out in DOCS:
            p = ROOT / md
            if not p.exists(): print("faltando", md); continue
            build(p, aba, Path(a.dist) / out)
            if a.fragment: build(p, aba, Path(a.dist) / "fragmentos" / out, fragment=True)
        return
    if not a.md: ap.error("informe o .md ou --all")
    out = a.out or (Path(a.dist) / (Path(a.md).stem.lower() + ".html"))
    build(a.md, a.aba, out, fragment=a.fragment, titulo=a.titulo, marca=a.marca)

if __name__ == "__main__":
    main()
