"""Build the GitHub Pages site at the repo root.
index.html = Student Guide (ES, home page); student-guide-en.html, libro-es.html, book-en.html.
PDFs live in dist/. Usage (from the repo root): python3 tools/build_site.py"""
import subprocess, sys, pathlib, shutil
ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

PAGES = {  # file: (script, lang, kind)
    "index.html": ("build_guide.py", "es", "guide"),
    "student-guide-en.html": ("build_guide.py", "en", "guide"),
    "libro-es.html": ("build.py", "es", "book"),
    "book-en.html": ("build.py", "en", "book"),
}
FILE = {("book", "es"): "libro-es.html", ("book", "en"): "book-en.html",
        ("guide", "es"): "index.html", ("guide", "en"): "student-guide-en.html"}
L = {"es": dict(home="Inicio", book="Libro de ejecución", guide="Guía del estudiante", pdf="PDF"),
     "en": dict(home="Home", book="Execution framework", guide="Student guide", pdf="PDF")}
PDF = {("book", "es"): "Libro_Ejecucion_CUBO_ai_2027.pdf", ("book", "en"): "CUBO_ai_Execution_Framework_2027.pdf",
       ("guide", "es"): "Guia_Estudiante_CUBO_ai_2027.pdf", ("guide", "en"): "CUBO_ai_Student_Guide_2027.pdf"}

def nav(kind, lang):
    t = L[lang]; other = "en" if lang == "es" else "es"
    tab = lambda k: f'<a href="{FILE[(k, lang)]}"{" class=on aria-current=page" if k == kind else ""}>{t[k]}</a>'
    return (f'<div class="sitenav">'
            f'<div class="row"><span class="home">CUBO_<span class="ai">ai</span> 2027</span>'
            f'<span class="lang"><a class="on" aria-current="true">{lang.upper()}</a>'
            f'<a class="swap" href="{FILE[(kind, other)]}" hreflang="{other}">{other.upper()}</a></span></div>'
            f'<div class="tabs">{tab("guide")}{tab("book")}</div>'
            f'<a class="pdf" href="dist/{PDF[(kind, lang)]}" download>↓ {t["pdf"]}</a>'
            f'</div>'
            '<script>document.addEventListener("click",e=>{const a=e.target.closest(".sitenav .swap");'
            'if(a&&location.hash){e.preventDefault();location.href=a.getAttribute("href")+location.hash}});</script>')

for name, (script, lang, kind) in PAGES.items():
    tmp = f"_site_{name}"
    subprocess.run([sys.executable, "-I", script, "ig", tmp, lang], cwd=ROOT, check=True)
    html = (ROOT / tmp).read_text()
    marker = '<div class="brand">'
    i = html.index(marker); j = html.index("</div>", i) + len("</div>")
    html = html[:j] + nav(kind, lang) + html[j:]
    (ROOT / name).write_text(html)
    (ROOT / tmp).unlink()
    print("built", name)
shutil.rmtree(ROOT / "__pycache__", ignore_errors=True)
