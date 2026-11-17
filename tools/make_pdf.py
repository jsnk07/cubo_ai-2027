"""Export a built HTML page to PDF (Letter, print styles, all <details> opened).
Usage: python3 tools/make_pdf.py dist/libro-es.html dist/Libro_Ejecucion_CUBO_ai_2027.pdf
Needs: pip install playwright && playwright install chromium"""
import asyncio, sys, pathlib
from playwright.async_api import async_playwright
SRC, OUT = (pathlib.Path(a).resolve() for a in sys.argv[1:3])
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1100, "height": 1400})
        await pg.goto(SRC.as_uri()); await pg.wait_for_timeout(1500)
        await pg.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
        await pg.emulate_media(media="print")
        await pg.pdf(path=str(OUT), format="Letter", print_background=True, scale=0.78,
                     margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"})
        await b.close()
asyncio.run(main())
