#!/usr/bin/env python3
"""Radar Urbano · HTML gerado → PDF (Chrome/Chromium headless) → remoção de páginas em branco (pypdfium2).

Uso:
  python3 src/make_pdf.py dist/radar-urbano-entregas.html            # gera dist/radar-urbano-entregas.pdf
  python3 src/make_pdf.py --all                                        # todos os HTML de dist/
  CHROME=/caminho/para/chrome python3 src/make_pdf.py --all            # se o navegador não estiver no PATH

Fluxo: cria uma variante de impressão (sem <script>, com o CSS de impressão abaixo), imprime em 1440×900 px
(16:10, uma seção por página), remove páginas totalmente em branco e grava o PDF final ao lado do HTML.
"""
import os, re, shutil, subprocess, sys, tempfile, argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PRINT_CSS = '''
@page{size:1440px 900px;margin:0}
html,body{background:#fff!important}
*{print-color-adjust:exact;-webkit-print-color-adjust:exact}
.bar,#prog,.ix,.cover .hint,.fim{display:none!important}
.cover{padding:150px 96px 90px;min-height:0;break-after:page}
.cover .rule{width:360px!important}
.cap{break-before:page;padding:120px 96px 40px;min-height:820px;display:flex;align-items:center}
.sec{break-before:page;min-height:840px;padding:100px 96px 60px}
/* o Chrome headless avalia as media queries pela janela, não pela página: força o grid de duas colunas */
.sec .wrap{grid-template-columns:minmax(0,5fr) minmax(0,7fr)!important;gap:64px!important}
.sec.wide .wrap,.fecho .wrap{grid-template-columns:1fr!important}
.rows li{grid-template-columns:56px 1fr!important;gap:20px!important;padding:24px 0!important}
.f-row{flex-direction:row!important}
.hd{position:static!important}
.rv,.stag>*{opacity:1!important;transform:none!important}
.card,.kpi,.cal-i,.rows li,.sp-row,.vb,.band,.vin,.tbl,pre,.dl div,.steps li{break-inside:avoid}
.sec.fecho{padding:200px 96px}
h2{font-size:28px}
'''

def find_chrome():
    for env in ("CHROME", "CHROME_BIN", "BROWSER"):
        if os.environ.get(env) and Path(os.environ[env]).exists(): return os.environ[env]
    cands = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"]
    for c in cands:
        p = shutil.which(c)
        if p: return p
    for pat in ["/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "C:/Program Files/Google/Chrome/Application/chrome.exe"]:
        import glob
        g = sorted(glob.glob(pat))
        if g and Path(g[-1]).exists(): return g[-1]
    sys.exit("Chrome/Chromium não encontrado. Defina CHROME=/caminho/para/o/binário.")

FONTS = Path(__file__).with_name("fonts")

def local_fonts_css():
    """@font-face com as fontes locais (src/fonts), para o PDF sair com Bodoni Moda e Manrope mesmo sem internet."""
    css_path = FONTS / "fonts-local.css"
    if not css_path.exists(): return ""
    css = css_path.read_text(encoding="utf-8")
    return re.sub(r"url\(([^)]+\.woff2)\)", lambda m: "url(" + (FONTS / m.group(1)).resolve().as_uri() + ")", css)

def print_variant(html_path):
    s = Path(html_path).read_text(encoding="utf-8")
    s = re.sub(r"<script>.*?</script>", "", s, flags=re.S)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>', "", s)
    s = s.replace("<style>", "<style>\n" + local_fonts_css() + "\n", 1)
    s = s.replace("</style>", PRINT_CSS + "</style>", 1)
    return s

def strip_blank_pages(pdf_in, pdf_out):
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(str(pdf_in))
    blank = []
    for i in range(len(pdf)):
        page = pdf[i]
        tp = page.get_textpage(); txt = tp.get_text_range().strip(); tp.close()
        if not txt:
            img = page.render(scale=0.15).to_pil().convert("L")
            # página em branco: quase todos os pixels claros
            hist = img.histogram(); dark = sum(hist[:235]); total = sum(hist)
            if dark / max(total, 1) < 0.002: blank.append(i)
        page.close()
    for i in reversed(blank): pdf.del_page(i)
    pdf.save(str(pdf_out))
    n = len(pdf); pdf.close()
    return n, blank

def make(html_path, out_pdf=None):
    html_path = Path(html_path)
    out_pdf = Path(out_pdf) if out_pdf else html_path.with_suffix(".pdf")
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as td:
        p_html = Path(td) / ("print-" + html_path.name)
        p_html.write_text(print_variant(html_path), encoding="utf-8")
        raw = Path(td) / "raw.pdf"
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", "--window-size=1440,900",
               "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
               f"--print-to-pdf={raw}", p_html.resolve().as_uri()]
        subprocess.run(cmd, check=True, capture_output=True, timeout=300)
        n, blank = strip_blank_pages(raw, out_pdf)
    print(f"ok {out_pdf} · {n} páginas (removidas {len(blank)} em branco)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html", nargs="?")
    ap.add_argument("--out")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    a = ap.parse_args()
    if a.all:
        for h in sorted(Path(a.dist).glob("radar-urbano-*.html")): make(h)
        return
    if not a.html: ap.error("informe o .html ou --all")
    make(a.html, a.out)

if __name__ == "__main__":
    main()
