# CUBO_ai 2027

**ES** · Programa de formación en Inteligencia Artificial aplicada de la Agencia Nacional de Inteligencia Artificial (ANIA) de El Salvador. Este repositorio contiene la **Guía del estudiante** y el **Libro de ejecución** del programa, en español e inglés, como sitio web navegable y en PDF.

**EN** · Applied Artificial Intelligence training program of El Salvador's National Artificial Intelligence Agency (ANIA). This repository contains the program's **Student Guide** and **Execution Framework**, in Spanish and English, as a browsable website and as PDFs.

> Constructores por encima de creadores de prompts · Builders over prompt crafters

## Sitio web · Website

https://jsnk07.github.io/cubo_ai-2027/

| Página · Page | Español | English |
|---|---|---|
| Guía del estudiante · Student guide | [`index.html`](index.html) | [`student-guide-en.html`](student-guide-en.html) |
| Libro de ejecución · Execution framework | [`libro-es.html`](libro-es.html) | [`book-en.html`](book-en.html) |

## PDF

- [Guía del Estudiante CUBO_ai 2027](dist/Guia_Estudiante_CUBO_ai_2027.pdf)
- [CUBO_ai Student Guide 2027](dist/CUBO_ai_Student_Guide_2027.pdf)
- [Libro de ejecución CUBO_ai 2027](dist/Libro_Ejecucion_CUBO_ai_2027.pdf)
- [CUBO_ai Execution Framework 2027](dist/CUBO_ai_Execution_Framework_2027.pdf)

## Estructura · Structure

| Ruta · Path | Contenido · Contents |
|---|---|
| `guide_es/`, `guide_en/` | Guía del estudiante: F1–F5 con DIY de dos rutas, preparación para The AI Challenge y el Bootcamp, anexos · Student guide: F1–F5 with two-route DIYs, Challenge and Bootcamp prep, annexes |
| `parts/`, `parts_en/` | Libro de ejecución, partes I–VIII · Execution framework, parts I–VIII |
| `cubi.py` | Cubi, la mascota que presenta cada página y comenta las secciones · Cubi, the mascot that introduces each page and comments on sections |
| `shots.py` | Ilustraciones de los pasos técnicos (Docker + Ollama, Jupyter, MCP Inspector) · Illustrated technical steps |
| `assets/`, `fonts/`, `img/` | Estilos, scripts, tipografías y logos · Styles, scripts, fonts and logos |
| `build.py`, `build_guide.py` | Generan cada página autocontenida · Build each self-contained page |
| `tools/build_site.py` | Reconstruye las cuatro páginas del sitio · Rebuilds the four site pages |
| `tools/make_pdf.py` | Exporta una página a PDF · Exports a page to PDF |
| `dist/` | PDFs |

## Reconstruir · Rebuild

```bash
python3 tools/build_site.py
python3 tools/make_pdf.py index.html dist/Guia_Estudiante_CUBO_ai_2027.pdf   # requires playwright
```

Los ejercicios técnicos usan modelos abiertos locales con Docker y Ollama: no hace falta pagar una API ni enviar datos a terceros. · The technical exercises use local open models with Docker and Ollama: no paid API and no data sent to third parties.
