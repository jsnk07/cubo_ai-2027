import re, base64, math, pathlib, html, sys as _s
_s.path.insert(0, str(pathlib.Path(__file__).parent))

B = pathlib.Path(__file__).parent

import sys, json
ACC = {"--acc":"#2B7FE0","--acc-hi":"#7FB4FF","--acc-lo":"#1A4880","--on-acc":"#FFFFFF"}
PALETTES = {

 "ig": dict(
  light={"--paper":"#EEEEEB","--surface":"#FFFFFF","--ink":"#0E0E0E","--muted":"#5C5C58","--line":"#DADAD5","--sec":"#1C1C1C","--sec-deep":"#000000","--sec-soft":"#E4E4E0","--on-sec":"#FFFFFF","--acc-deep":"#235FA9","--acc-soft":"#DCE9FA",
         "--hero-bg":"#F4F4F2","--hero-ink":"#0E0E0E","--hero-muted":"#4A4A47","--glass":"rgba(255,255,255,.72)","--glass-line":"rgba(255,255,255,.9)"},
  night={"--night":"#141414","--night-2":"#2B2B2A","--night-deep":"#0A0A0A","--night-line":"#3A3A38","--on-night":"#F6F6F4","--on-night-muted":"#BDBDB8","--on-night-dim":"#85857F","--sec-hi":"#BDBDB8","--sec-panel":"#232323","--sec-panel-2":"#3A3A39","--earth":"#1A4880","--earth-2":"#2B7FE0"},
  dark=None),
 "grafito": dict(
  light={"--paper":"#F5F4F1","--surface":"#FFFFFF","--ink":"#171614","--muted":"#67625B","--line":"#E2DED7","--sec":"#4A5560","--sec-deep":"#333C45","--sec-soft":"#E9ECEE","--on-sec":"#FFFFFF","--acc-deep":"#B5600A","--acc-soft":"#FDF0E1"},
  night={"--night":"#161513","--night-2":"#2A2723","--night-deep":"#0E0D0C","--night-line":"#3F3B36","--on-night":"#F4F1EC","--on-night-muted":"#B3ADA4","--on-night-dim":"#7C766E","--sec-hi":"#AEB9C4","--sec-panel":"#333C45","--sec-panel-2":"#56626E","--earth":"#3B2814","--earth-2":"#5E3D17"},
  dark={"--paper":"#0E0D0C","--surface":"#1A1917","--ink":"#F2EFEA","--muted":"#A8A299","--line":"#34312D","--sec":"#9FB0BF","--sec-deep":"#6E7F8E","--sec-soft":"#22272C","--on-sec":"#0E0D0C","--acc-deep":"#FFB054","--acc-soft":"#2A1E0E"}),
 "petroleo": dict(
  light={"--paper":"#F3F6F6","--surface":"#FFFFFF","--ink":"#0E1E22","--muted":"#52686D","--line":"#D5E1E2","--sec":"#0D8A8F","--sec-deep":"#096468","--sec-soft":"#DDF1F1","--on-sec":"#FFFFFF","--acc-deep":"#B5600A","--acc-soft":"#FDF0E1"},
  night={"--night":"#0C2228","--night-2":"#16404A","--night-deep":"#07161A","--night-line":"#24505B","--on-night":"#EEF6F6","--on-night-muted":"#A3C3C7","--on-night-dim":"#6F9298","--sec-hi":"#6FD3D3","--sec-panel":"#096468","--sec-panel-2":"#0D8A8F","--earth":"#3D2713","--earth-2":"#64401A"},
  dark={"--paper":"#07161A","--surface":"#0F262C","--ink":"#E8F2F2","--muted":"#94B3B7","--line":"#1F4049","--sec":"#4CC2C4","--sec-deep":"#2E9497","--sec-soft":"#12353A","--on-sec":"#04191C","--acc-deep":"#FFB054","--acc-soft":"#2A1E0E"}),
 "volcan": dict(
  light={"--paper":"#F4F5F0","--surface":"#FFFFFF","--ink":"#142019","--muted":"#5A6A5F","--line":"#DCE2D8","--sec":"#2E7A57","--sec-deep":"#1F5A3F","--sec-soft":"#E2EFE6","--on-sec":"#FFFFFF","--acc-deep":"#B5600A","--acc-soft":"#FDF0E1"},
  night={"--night":"#12221A","--night-2":"#1F3A2C","--night-deep":"#0A1610","--night-line":"#2C4B3B","--on-night":"#EFF4EE","--on-night-muted":"#A9BFB0","--on-night-dim":"#74907E","--sec-hi":"#7FCFA5","--sec-panel":"#1F5A3F","--sec-panel-2":"#2E7A57","--earth":"#3E2913","--earth-2":"#66421A"},
  dark={"--paper":"#0A1610","--surface":"#13241B","--ink":"#EAF2EB","--muted":"#9CB4A3","--line":"#233D30","--sec":"#5DBB8C","--sec-deep":"#3E8E66","--sec-soft":"#173326","--on-sec":"#06140D","--acc-deep":"#FFB054","--acc-soft":"#2A1E0E"}),
}
PNAME = sys.argv[1] if len(sys.argv) > 1 else "ig"
OUT = sys.argv[2] if len(sys.argv) > 2 else "index.html"
LANG = sys.argv[3] if len(sys.argv) > 3 else "es"
EN = LANG == "en"
PARTS = "guide_en" if EN else "guide_es"
FIG = "Figure" if EN else "Figura"
P = PALETTES[PNAME]
def decl(d): return "".join(f"{k}:{v};" for k,v in d.items())
FIXED = {"--f-display":'"Anton","Impact","Arial Narrow",sans-serif',"--f-body":'"Archivo",system-ui,-apple-system,"Segoe UI",sans-serif',"--f-mono":'"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace',"--read":"68ch","--wide":"1000px","--r":"14px"}
TOKENS = (":root{/* CUBO_ai · paleta " + PNAME + ". Layout: índice fijo a la izquierda, columna de lectura de ~68ch, figuras a lo ancho. */"
  + decl(FIXED) + decl(ACC) + decl(P["light"]) + decl(P["night"]) + "--ok:#14915F;--stop:#C8362F;color-scheme:light}"
  + ("" if not P["dark"] else "@media (prefers-color-scheme:dark){:root:not([data-theme=\"light\"]){" + decl(P["dark"]) + "--ok:#3CCB8C;--stop:#FF7A70;color-scheme:dark}}"
  + ":root[data-theme=\"dark\"]{" + decl(P["dark"]) + "--ok:#3CCB8C;--stop:#FF7A70;color-scheme:dark}"))
css = (B/"assets/style.css").read_text()
js = (B/"assets/app.js").read_text()

def datauri(p):
    return "data:image/png;base64," + base64.b64encode((B/p).read_bytes()).decode()


FONTFACES = ""
for fam, fn, wt, st in [("Anton","anton-latin-400-normal",400,"normal"),("Archivo","archivo-latin-400-normal",400,"normal"),("Archivo","archivo-latin-400-italic",400,"italic"),("Archivo","archivo-latin-600-normal",600,"normal"),("Archivo","archivo-latin-700-normal",700,"normal"),("Archivo","archivo-latin-800-normal",800,"normal"),("IBM Plex Mono","ibm-plex-mono-latin-500-normal",500,"normal"),("IBM Plex Mono","ibm-plex-mono-latin-600-normal",600,"normal"),("IBM Plex Mono","ibm-plex-mono-latin-700-normal",700,"normal")]:
    data = base64.b64encode((B/"fonts"/(fn+".woff2")).read_bytes()).decode()
    FONTFACES += f'@font-face{{font-family:"{fam}";font-style:{st};font-weight:{wt};font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2")}}\n'

LOGO_W = datauri("img/cuboai-blanco-hor.png")
LOGO_O = datauri("img/cuboai-azul-hor.png")
onbtc_path = B/"img/ania.png"
ONBTC = datauri("img/ania.png") if onbtc_path.exists() else None

def onbtc_slot(cls=""):
    if ONBTC:
        return f'<span class="logo-slot onbtc-img {cls}"><img src="{ONBTC}" alt="{"National Artificial Intelligence Agency (ANIA)" if EN else "Agencia Nacional de Inteligencia Artificial (ANIA)"}"></span>'
    return f'<span class="logo-slot onbtc {cls}">Logo ANIA</span>'

# ---------- static SVG generators ----------
def wheel14(n=14):
    R1, R0 = 140, 62; out = []
    for i in range(n):
        a0 = -math.pi/2 + i*2*math.pi/n + 0.012
        a1 = -math.pi/2 + (i+1)*2*math.pi/n - 0.012
        p = lambda r, a: f"{r*math.cos(a):.1f},{r*math.sin(a):.1f}"
        d = f"M{p(R0,a0)}L{p(R1,a0)}A{R1},{R1} 0 0 1 {p(R1,a1)}L{p(R0,a1)}A{R0},{R0} 0 0 0 {p(R0,a0)}Z"
        delay = f"{i*0.5:.1f}s"
        out.append(f'<path class="wseg" d="{d}" style="animation-delay:{delay}"/>')
        am = (a0+a1)/2; r = (R0+R1)/2
        out.append(f'<text x="{r*math.cos(am):.1f}" y="{r*math.sin(am)+4:.1f}" text-anchor="middle" style="font:700 12px IBM Plex Mono,monospace;fill:var(--on-night)">{i+1:02d}</text>')
    out.append('<g transform="translate(0 0)"><path d="M0-34L29-17V17L0 34-29 17V-17z" fill="var(--acc)"/><path d="M0-34L29-17 0 0-29-17z" fill="var(--acc-hi)"/><path d="M0 0L29-17V17L0 34z" fill="var(--acc-lo)"/></g>')
    return "".join(out)

def donut():
    parts = [(a if EN else b, w, c) for (a, b, w, c) in [("Problem & context","Problema y contexto",10,"var(--acc)"),("Opportunity & value","Oportunidad y valor",10,"#4A93E8"),("Solution & architecture","Solución y arquitectura",10,"#3672C4"),
             ("Execution & functionality","Ejecución y funcionalidad",15,"#1F5FB0"),("Validation","Validación",5,"#9CC4F5"),("Documentation & presentation","Documentación y presentación",10,"#BFD8F8"),
             ("Individual","Individual",40,"var(--sec)")]]
    R1, R0 = 140, 92; a = -math.pi/2; out = []
    for name, w, col in parts:
        a2 = a + w/100*2*math.pi
        large = 1 if (a2-a) > math.pi else 0
        p = lambda r, ang: f"{r*math.cos(ang):.1f},{r*math.sin(ang):.1f}"
        d = f"M{p(R0,a+0.01)}L{p(R1,a+0.01)}A{R1},{R1} 0 {large} 1 {p(R1,a2-0.01)}L{p(R0,a2-0.01)}A{R0},{R0} 0 {large} 0 {p(R0,a+0.01)}Z"
        out.append(f'<path d="{d}" fill="{col}"><title>{name}: {w} %</title></path>')
        am = (a+a2)/2; r = (R0+R1)/2
        out.append(f'<text x="{r*math.cos(am):.1f}" y="{r*math.sin(am)+4:.1f}" text-anchor="middle" style="font:700 11px IBM Plex Mono,monospace;fill:{"#fff" if col.startswith("var") or w>=15 else "var(--on-acc)"}">{w}</text>')
        a = a2
    out.append('<text x="0" y="-8" text-anchor="middle" style="font:400 30px Anton,sans-serif;fill:var(--ink)">60·40</text>')
    out.append(f'<text x="0" y="16" text-anchor="middle" style="font:600 11px IBM Plex Mono,monospace;fill:var(--muted)">{"team · individual" if EN else "equipo · individual"}</text>')
    out.append(f'<text x="0" y="34" text-anchor="middle" style="font:600 11px IBM Plex Mono,monospace;fill:var(--muted)">{"individual minimum 60" if EN else "mínimo individual 60"}</text>')
    return "".join(out)

# ---------- assemble parts ----------
body = ""
for i in range(0, 9):
    body += (B/PARTS/f"g{i}.html").read_text() + "\n"
import shots
_S = shots.shots("en" if EN else "es")
for _k, _v in _S.items(): body = body.replace("{{SHOTS_" + _k + "}}", _v)

# section wrappers -> ids on headings (keeps nesting valid)
body = re.sub(r'<section class="sec" id="([\w-]+)">\s*<h3 class="sec-h">', r'<h3 class="sec-h sec" id="\1">', body)
body = re.sub(r'<section class="sec" id="([\w-]+)">', r'<div class="sec" id="\1"></div>', body)
body = re.sub(r'(?m)^\s*</section>\s*$', '', body)
body = body.replace('<div class="col"></section></div>', '')
body = body.replace('</section>\n</div>', '\n</div>')
body = re.sub(r'</li></ul>\s*</section>', '</li></ul>', body)
body = body.replace('</p>\n</section>', '</p>')
# keep only part-opener sections
body = re.sub(r'</section>(?!</)', lambda m: m.group(0), body)

body = re.sub(r'(<svg viewBox="-160 -160 320 320" role="img" aria-label="[^"]*") id="wheel(\d+)"></svg>', lambda m: m.group(1)+'>'+wheel14(int(m.group(2)))+'</svg>', body)
body = body.replace('id="donut"></svg>', f'>{donut()}</svg>')
body = body.replace('<span class="logo-slot cubo-end"></span>', f'<span class="logo-slot"><img src="{LOGO_O}" alt="CUBO_ai"></span>' + onbtc_slot('end'))


# ---------- figure numbering ----------
keys = {"Tres semanas, tres compuertas": "challenge", "Three weeks, three gates": "challenge", "Una semana: cuatro días": "days", "One week: four days": "days", "Siete líneas de proyecto": "tracks", "Seven project lines": "tracks"}
n = 0; fignum = {}
def numfig(m):
    global n
    n += 1
    cap = m.group(2)
    for k, v in keys.items():
        if cap.startswith(k): fignum[v] = n
    return f'<figcaption><b>{FIG} {n}</b><span class="fc">{cap}</span>'
body = re.sub(r'<figcaption><b>(?:Figura|Figure) (\d+)</b>([^<]*)', numfig, body)
for k in ("challenge","days","tracks"):
    if k in fignum:
        body = re.sub(r'<a data-fig="%s" href="(#[\w-]+)">(?:Figura|Figure) \d+</a>' % k, lambda m, k=k: '<a data-fig="%s" href="%s">%s %d</a>' % (k, m.group(1), FIG, fignum[k]), body)

# ---------- TOC ----------
toc = []
for m in re.finditer(r'<section class="part" id="(parte-\d)".*?<div class="num">([^<]+)</div><h2>([^<]+)</h2>|<h3 class="sec-h sec" id="([\w-]+)"><span class="n">([^<]+)</span>([^<]+)</h3>|<div class="diy" id="([\w-]+)">.*?<h4>([^<]+)</h4>', body, re.S):
    if m.group(1):
        toc.append(("part", m.group(1), m.group(2), m.group(3)))
    elif m.group(4):
        toc.append(("sec", m.group(4), m.group(5), m.group(6)))
    else:
        toc.append(("sec", m.group(7), "DIY", m.group(8)))
toc_html = ""
open_ol = False
for kind, id_, num, title in toc:
    if kind == "part":
        if open_ol: toc_html += "</ol>"
        toc_html += f'<h2>{num}</h2><ol><li><a href="#{id_}"><b>{title}</b></a></li>'
        open_ol = True
    else:
        toc_html += f'<li><a href="#{id_}"><small>{num}</small>{title}</a></li>'
toc_html += "</ol>"

T = dict(
 lang="en" if EN else "es",
 title="CUBO_ai Student Guide 2027" if EN else "Guía del Estudiante CUBO_ai 2027",
 kicker="Cohort 2027 · Student Guide" if EN else "Cohorte 2027 · Guía del Estudiante",
 h1="Student <span>guide</span>" if EN else "Guía del <span>estudiante</span>",
 sub="Topics, learning objectives and DIY workshops for the Foundations, The AI Challenge and the Technical Bootcamp of CUBO_ai." if EN else "Temas, objetivos de aprendizaje y talleres DIY para recorrer los Fundamentos, The AI Challenge y el Bootcamp técnico de CUBO_ai.",
 dt1="Target audience" if EN else "Dirigido a", dd1="CUBO_ai Selection Board &amp; Academic Committee" if EN else "Junta de Selección y Comité Académico de CUBO_ai",
 dt2="Governing institution" if EN else "Institución rectora", dd2="National Artificial Intelligence Agency (ANIA)" if EN else "Agencia Nacional de Inteligencia Artificial (ANIA)",
 dt3="Jurisdiction" if EN else "Jurisdicción", dd3="Republic of El Salvador" if EN else "República de El Salvador",
 toc="Contents" if EN else "Índice", tocsub="Student Guide · Cohort 2027" if EN else "Guía del Estudiante · Cohorte 2027",
)
I18N = ('{"ok":"Advances to Bootcamp","no":"Does not advance","whyOk":"Meets the minimum final score of 70 and the minimum individual score of 60.","whyBoth":"Missing both the final score of 70 and the individual score of 60.","whyF":"The final score is below 70.","whyI":"The individual score is below 60, even if the final score reaches 70."}' if EN else
        '{"ok":"Avanza al Bootcamp","no":"No avanza","whyOk":"Cumple la nota final mínima de 70 y la individual mínima de 60.","whyBoth":"Le faltan la nota final de 70 y la individual de 60.","whyF":"La nota final está por debajo de 70.","whyI":"La nota individual está por debajo de 60, aunque la final llegue a 70."}')
cover = f'''<header class="cover" id="inicio">
<canvas data-scene="cover" aria-hidden="true"></canvas>
<div class="inner">
 <div class="logos"><span class="logo-slot cubo"><img src="{LOGO_O}" alt="CUBO_ai"></span>{onbtc_slot()}</div>
 <div class="kicker">{T["kicker"]}</div>
 <h1>{T["h1"]}</h1>
 <p class="sub">{T["sub"]}</p>
 <dl>
  <div><dt>{T["dt2"]}</dt><dd>{T["dd2"]}</dd></div>
  <div><dt>{T["dt3"]}</dt><dd>{T["dd3"]}</dd></div>
 </dl>
</div>
</header>'''

def _lc(h):
    return re.sub(r'>([^<]*)<', lambda m: '>' + m.group(1).replace('CUBO_ai', 'CUBO_<span class="ai">ai</span>') + '<', h)
cover = _lc(cover); body = _lc(body); toc_html = _lc(toc_html)
page = f'''<!DOCTYPE html>
<html lang="{T["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{T["title"]}</title>
<style>{FONTFACES}{TOKENS}
{css}
.toc .brand img{{height:30px;width:auto}}
.ai{{text-transform:none!important;color:inherit}}
.logo-slot.onbtc-img{{height:52px;padding-left:22px;border-left:1px solid var(--line)}}
.endmark .logo-slot{{display:inline-flex;margin:0 10px 14px}}
.endmark .onbtc-img{{height:34px;padding-left:0;border:0}}
</style>
</head>
<body>
<div class="shell">
<nav class="toc" aria-label="{T["toc"]}">
 <div class="brand"><span class="logo-slot"><img src="{LOGO_O}" alt="CUBO_ai"></span></div>
 <a href="#inicio" style="font-size:13px;color:var(--muted);text-decoration:none">{T["tocsub"]}</a>
 {toc_html}
 
</nav>
<main>
{cover}
{body}
</main>
</div>
<button class="btn menu-btn" type="button" aria-expanded="false">☰ {T["toc"]}</button>
<script>window.I18N={I18N};</script>\n<script>{js}</script>
</body>
</html>'''
(B/OUT).write_text(page)
print("figuras:", n, fignum, "toc items:", len(toc), "bytes:", len(page))
