"""Illustrated screens (Docker + Ollama, Jupyter, MCP Inspector) for the CUBO_ai Student Guide DIYs.
UI labels stay in English as the apps show them; captions and legends are localized."""
from html import escape

MONO = "font-family:'IBM Plex Mono',ui-monospace,monospace"
SANS = "font-family:'Archivo',system-ui,sans-serif"

def t(x, y, s, size=13, w=400, fill="var(--ink)", anchor="start", font=SANS, extra=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="{font};font-size:{size}px;font-weight:{w};fill:{fill}{extra}" xml:space="preserve">{escape(s)}</text>'

def window(x, y, w, h, title, dark=False):
    body = "var(--night)" if dark else "var(--surface)"
    bar = "var(--night-2)" if dark else "var(--paper)"
    tc = "var(--on-night-muted)" if dark else "var(--muted)"
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{body}" stroke="var(--line)"/>'
            f'<path d="M{x} {y+12}a12 12 0 0 1 12-12h{w-24}a12 12 0 0 1 12 12v18h-{w}z" fill="{bar}"/>'
            + "".join(f'<circle cx="{x+18+i*16}" cy="{y+15}" r="5" fill="{c}"/>' for i, c in enumerate(["#E5534B", "#E9A23B", "#3FB950"]))
            + t(x + w / 2, y + 20, title, 12, 600, tc, "middle"))

def call(n, x, y):
    return (f'<circle cx="{x}" cy="{y}" r="13" fill="var(--acc)" stroke="var(--surface)" stroke-width="3"/>'
            + t(x, y + 5, str(n), 13, 800, "#fff", "middle"))

def btn(x, y, w, label, primary=False, hot=False, h=28):
    fill = "var(--acc)" if primary else "var(--surface)"
    tc = "#fff" if primary else "var(--ink)"
    stroke = "var(--acc)" if (hot or primary) else "var(--line)"
    sw = 2.5 if hot else 1
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
            + t(x + w / 2, y + h / 2 + 5, label, 12.5, 700, tc, "middle"))

def node(x, y, name, kind, sel=False, w=140):
    stroke = "var(--acc)" if sel else "var(--line)"
    sw = 2.5 if sel else 1.2
    if kind == "btc":
        icon = (f'<circle cx="{x+24}" cy="{y+27}" r="14" fill="var(--acc)"/>' + t(x + 24, y + 33, "₿", 16, 800, "#fff", "middle"))
        sub = "Bitcoin Core"
    else:
        icon = (f'<rect x="{x+10}" y="{y+13}" width="28" height="28" rx="7" fill="var(--ink)"/>'
                f'<path d="M{x+26} {y+17} l-8 11 h6 l-3 9 l9-12 h-6 l2-8z" fill="#FFD23F"/>')
        sub = "LND"
    return (f'<rect x="{x}" y="{y}" width="{w}" height="54" rx="9" fill="var(--surface)" stroke="{stroke}" stroke-width="{sw}"/>'
            + icon + t(x + 48, y + 24, name, 14, 700) + t(x + 48, y + 41, sub, 10.5, 500, "var(--muted)", font=MONO))

def grid_bg(x, y, w, h, pid):
    return (f'<defs><pattern id="{pid}" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="var(--line)"/></pattern></defs>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{pid})"/>')

def term_lines(x, y, lines, lh=19, size=12.5):
    """lines: list of (text, kind) kind in prompt|out|dim|hi"""
    out = []
    for i, (s, k) in enumerate(lines):
        yy = y + i * lh
        if k == "prompt":
            p, cmd = s.split("$ ", 1)
            out.append(f'<text x="{x}" y="{yy}" style="{MONO};font-size:{size}px" xml:space="preserve">'
                       f'<tspan style="fill:var(--acc);font-weight:700">{escape(p)}$ </tspan><tspan style="fill:var(--on-night)">{escape(cmd)}</tspan></text>')
        else:
            col = {"out": "var(--on-night-muted)", "dim": "var(--on-night-dim)", "hi": "#7EE2A8"}[k]
            out.append(t(x, yy, s, size, 500, col, font=MONO))
    return "".join(out)

def svg(w, h, body, label):
    return f'<div class="scroll"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" style="min-width:620px;width:100%">{body}</svg></div>'

# ---------------------------------------------------------------- screens
def shot_ollama_f1(en):
    W, H = 900, 400
    b = window(0, 0, W, H, "Terminal", dark=True)
    L = [
        ("~/cuboai-f1$ docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama", "prompt"),
        ("Unable to find image 'ollama/ollama:latest' locally · Pull complete", "dim"),
        ("3f9c2a7d41be8e0c5a1f…", "out"),
        ("~/cuboai-f1$ docker exec -it ollama ollama pull llama3.2:1b", "prompt"),
        ("pulling manifest · pulling 74701a8c35f6… 100% ▕████████████████▏ 1.3 GB", "dim"),
        ("success", "hi"),
        ("~/cuboai-f1$ docker exec -it ollama ollama run llama3.2:1b \"" + ("What is the capital of El Salvador?" if en else "¿Cuál es la capital de El Salvador?") + "\"", "prompt"),
        ("The capital of El Salvador is San Salvador." if en else "La capital de El Salvador es San Salvador.", "out"),
        ("~/cuboai-f1$ python " + ("test_model.py && cut -d, -f3 results.csv | head -3" if en else "prueba.py && cut -d, -f3 resultados.csv | head -3"), "prompt"),
        ("model" if en else "modelo", "dim"),
        (("\"The Procedure Simplification Act was passed in 1987…\"   ← check this") if en else ("\"La Ley de Simplificación de Trámites fue aprobada en 1987…\"   ← verifica esto"), "out"),
        ("\"The procedure requires an ID and proof of address.\"" if en else "\"El trámite requiere DUI y comprobante de domicilio.\"", "out"),
    ]
    b += term_lines(22, 62, L, lh=26, size=12.2)
    b += call(1, 868, 104) + call(2, 868, 182) + call(3, 868, 234) + call(4, 868, 336)
    return svg(W, H, b, "Ollama in Docker" if en else "Ollama en Docker")

def shot_jupyter_f4(en):
    W, H = 900, 470
    b = window(0, 0, W, H, "localhost:8888 · " + ("f4-digits.ipynb" if en else "f4-digitos.ipynb"))
    b += f'<rect x="1" y="30" width="{W-2}" height="40" fill="var(--surface)"/><line x1="0" y1="70" x2="{W}" y2="70" stroke="var(--line)"/>'
    for i, s in enumerate(["File", "Edit", "View", "Run", "Kernel"]):
        b += t(20 + i * 62, 55, s, 12.5, 600, "var(--muted)")
    b += btn(360, 39, 74, "▶ Run", primary=True, h=24)
    b += t(W - 20, 55, "Python 3 (ipykernel)  ○", 11.5, 600, "var(--muted)", "end")
    # code cell
    b += t(22, 104, "[3]:", 12, 700, "var(--acc-deep)", font=MONO)
    b += f'<rect x="70" y="86" width="808" height="74" rx="6" fill="var(--paper)" stroke="var(--line)"/>'
    code = ["m = MLPClassifier(hidden_layer_sizes=(64,), max_iter=500, random_state=0).fit(Xtr, ytr)",
            ("print(\"train:\", m.score(Xtr, ytr), \"test:\", accuracy_score(yte, m.predict(Xte)))" if en else "print(\"entrenamiento:\", m.score(Xtr, ytr), \"prueba:\", accuracy_score(yte, m.predict(Xte)))"),
            "print(confusion_matrix(yte, m.predict(Xte)))"]
    for i, s in enumerate(code):
        b += t(82, 106 + i * 19, s, 11.6, 500, font=MONO)
    # output
    b += t(82, 190, ("train: 1.0 test: 0.9755555555555555" if en else "entrenamiento: 1.0 prueba: 0.9755555555555555"), 12, 600, font=MONO)
    rows = ["[[37  0  0  0  0  0  0  0  0  0]", " [ 0 41  0  0  0  0  1  0  1  0]", " [ 0  0 44  0  0  0  0  0  0  0]",
            " [ 0  0  0 43  0  0  0  0  2  0]", " [ 0  0  0  0 37  0  0  1  0  0]", " [ 0  0  0  1  0 47  0  0  0  0]",
            " [ 0  1  0  0  0  0 51  0  0  0]", " [ 0  0  0  0  0  0  0 48  0  0]", " [ 0  2  0  0  0  0  0  0 46  0]",
            " [ 0  0  0  0  0  1  0  1  0 45]]"]
    for i, s in enumerate(rows):
        b += t(82, 216 + i * 19, s, 12, 500, font=MONO)
    b += f'<rect x="76" y="{216 + 8*19 - 14}" width="290" height="19" rx="4" fill="none" stroke="var(--acc)" stroke-width="2"/>'
    b += f'<rect x="76" y="{216 + 3*19 - 14}" width="290" height="19" rx="4" fill="none" stroke="var(--acc)" stroke-width="1.5" stroke-dasharray="4 3"/>'
    # digits thumbnails
    b += t(560, 216, "Mal clasificados" if not en else "Misclassified", 12, 700, "var(--muted)")
    MIS = [(8, 1, [0, 0, 10, 13, 0, 0, 0, 0, 0, 0, 14, 15, 11, 0, 0, 0, 0, 0, 12, 9, 16, 8, 2, 0, 0, 0, 5, 14, 16, 11, 1, 0, 0, 0, 3, 16, 10, 0, 0, 0, 0, 0, 12, 11, 16, 0, 0, 0, 0, 1, 16, 7, 16, 5, 0, 0, 0, 0, 11, 16, 13, 1, 0, 0]), (8, 1, [0, 0, 2, 13, 4, 0, 0, 0, 0, 0, 8, 14, 11, 0, 0, 0, 0, 0, 10, 6, 14, 5, 2, 0, 0, 0, 2, 14, 12, 14, 0, 0, 0, 0, 1, 15, 13, 2, 0, 0, 0, 0, 11, 13, 14, 1, 0, 0, 0, 0, 13, 8, 10, 4, 0, 0, 0, 0, 2, 11, 16, 7, 0, 0]), (3, 8, [0, 0, 2, 11, 12, 1, 0, 0, 0, 2, 14, 9, 9, 8, 0, 0, 0, 10, 12, 0, 13, 6, 0, 0, 0, 6, 5, 2, 13, 2, 0, 0, 0, 0, 0, 10, 9, 0, 0, 0, 0, 0, 0, 1, 10, 9, 1, 0, 0, 0, 6, 7, 0, 12, 6, 0, 0, 0, 1, 12, 16, 16, 5, 0])]
    for k, (real, pred, px) in enumerate(MIS):
        x0 = 560 + k * 100
        for r in range(8):
            for c in range(8):
                shade = int(255 - px[r*8 + c] * 15)
                b += f'<rect x="{x0 + c*9}" y="{230 + r*9}" width="9" height="9" fill="rgb({shade},{shade},{shade})"/>'
        b += t(x0 + 36, 320, ("real " if not en else "true ") + str(real) + " → " + str(pred), 11.5, 600, "var(--ink)", "middle", font=MONO)
    b += call(1, 446, 51) + call(2, 470, 186) + call(3, 382, 361) + call(4, 860, 260)
    return svg(W, H, b, "Jupyter notebook with model results" if en else "Cuaderno de Jupyter con resultados del modelo")

def shot_inspector_f5(en):
    W, H = 900, 470
    b = window(0, 0, W, H, "MCP Inspector · localhost:6274")
    # sidebar
    b += f'<rect x="1" y="30" width="230" height="{H-31}" fill="var(--paper)"/><line x1="231" y1="30" x2="231" y2="{H}" stroke="var(--line)"/>'
    b += t(18, 60, "Transport Type", 11, 700, "var(--muted)")
    b += f'<rect x="18" y="68" width="196" height="28" rx="6" fill="var(--surface)" stroke="var(--line)"/>' + t(28, 87, "STDIO", 12.5, 600, font=MONO)
    b += t(18, 118, "Command", 11, 700, "var(--muted)")
    b += f'<rect x="18" y="126" width="196" height="28" rx="6" fill="var(--surface)" stroke="var(--line)"/>' + t(28, 145, "python", 12.5, 600, font=MONO)
    b += t(18, 176, "Arguments", 11, 700, "var(--muted)")
    b += f'<rect x="18" y="184" width="196" height="28" rx="6" fill="var(--surface)" stroke="var(--line)"/>' + t(28, 203, "server.py", 12.5, 600, font=MONO)
    b += btn(18, 228, 196, "Connect", h=30)
    b += f'<circle cx="28" cy="282" r="5" fill="#3FB950"/>' + t(40, 286, "Connected", 12, 700, "#14915F")
    # tabs
    tabs = ["Resources", "Prompts", "Tools", "Ping", "Sampling", "Roots"]
    for i, s in enumerate(tabs):
        x = 252 + i * 98
        on = s == "Tools"
        b += f'<rect x="{x}" y="44" width="90" height="28" rx="6" fill="{"var(--surface)" if on else "var(--paper)"}" stroke="{"var(--acc)" if on else "var(--line)"}" stroke-width="{2 if on else 1}"/>'
        b += t(x + 45, 63, s, 12, 700 if on else 500, "var(--ink)" if on else "var(--muted)", "middle")
    # tool list
    b += f'<rect x="252" y="88" width="250" height="{H-108}" rx="8" fill="var(--surface)" stroke="var(--line)"/>'
    b += t(266, 112, "Tools", 13, 800) + btn(392, 96, 98, "List Tools", h=24)
    b += f'<rect x="262" y="132" width="230" height="56" rx="6" fill="var(--acc-soft)" stroke="var(--acc)"/>'
    b += t(274, 154, "search_documents" if en else "buscar_documentos", 12.5, 700, font=MONO)
    b += t(274, 174, "Returns the most relevant…" if en else "Devuelve los documentos más…", 11, 500, "var(--muted)")
    # tool detail
    b += f'<rect x="516" y="88" width="368" height="{H-108}" rx="8" fill="var(--surface)" stroke="var(--line)"/>'
    b += t(530, 112, "search_documents" if en else "buscar_documentos", 13, 800, font=MONO)
    b += t(530, 138, "question" if en else "pregunta", 11, 700, "var(--muted)")
    b += f'<rect x="530" y="145" width="340" height="28" rx="6" fill="var(--paper)" stroke="var(--line)"/>' + t(540, 164, "What does procedure X require?" if en else "¿Qué requisitos pide el trámite X?", 12, 500)
    b += t(530, 192, "k", 11, 700, "var(--muted)")
    b += f'<rect x="530" y="199" width="80" height="28" rx="6" fill="var(--paper)" stroke="var(--line)"/>' + t(540, 218, "2", 12, 500, font=MONO)
    b += btn(530, 238, 120, "▶ Run Tool", primary=True, h=30)
    b += t(530, 294, "Tool Result: Success", 12, 700, "#14915F")
    b += f'<rect x="530" y="302" width="340" height="140" rx="6" fill="var(--night)"/>'
    res = (['{', '  "source": "procedure.md",', '  "text": "# Procedure X\\nRequirements:', '          ID and proof of address."', '}', '{ "source": "hours.md", … }'] if en else
           ['{', '  "fuente": "tramite.md",', '  "texto": "# Trámite X\\nRequisitos:', '           DUI y comprobante de domicilio."', '}', '{ "fuente": "horarios.md", … }'])
    for i, s in enumerate(res):
        b += t(542, 324 + i * 19, s, 11.6, 500, "var(--on-night-muted)" if i < 5 else "var(--on-night-dim)", font=MONO)
    b += call(1, 220, 282) + call(2, 546, 46) + call(3, 486, 160) + call(4, 664, 253) + call(5, 870, 316)
    return svg(W, H, b, "MCP Inspector testing the server" if en else "MCP Inspector probando el servidor")

# ---------------------------------------------------------------- legends & assembly
def legend(items):
    return '<ol class="shot-legend">' + "".join(f'<li><span class="n">{i+1}</span><span>{s}</span></li>' for i, s in enumerate(items)) + "</ol>"

def fig(svg_html, items, cap, en):
    F = "Figure" if en else "Figura"
    return f'<figure class="fig shot">{svg_html}{legend(items)}<figcaption><b>{F} 0</b>{cap}</figcaption></figure>'

def block(en, figs):
    head = "What it looks like · technical route" if en else "Así se ve · ruta técnica"
    note = ("Simplified illustrations: colors, versions and exact output may differ on your screen, but the steps and their order are the same."
            if en else "Ilustraciones simplificadas: los colores, las versiones y la salida exacta pueden variar en tu pantalla, pero los pasos y su orden son los mismos.")
    return f'<div class="diy-shots"><div class="lbl">{head}</div><p class="shot-note">{note}</p>{"".join(figs)}</div>'

def shots(lang):
    en = lang == "en"
    S = {}
    S["F1"] = block(en, [fig(shot_ollama_f1(en),
        (["The first time, Docker downloads the Ollama image and returns the container ID. The model API is now at <code>localhost:11434</code>.",
          "<code>ollama pull</code> downloads the model inside the container. <code>llama3.2:1b</code> weighs about 1.3 GB.",
          "A quick test from the terminal: if it answers, the model works.",
          "Your script saves each answer. Compare it with the correct one: a fluent answer with an invented date or law counts as a hallucination."] if en else
         ["La primera vez, Docker descarga la imagen de Ollama y devuelve el ID del contenedor. La API del modelo queda en <code>localhost:11434</code>.",
          "<code>ollama pull</code> descarga el modelo dentro del contenedor. <code>llama3.2:1b</code> pesa cerca de 1.3 GB.",
          "Una prueba rápida desde la terminal: si responde, el modelo funciona.",
          "Tu script guarda cada respuesta. Compárala con la correcta: una respuesta fluida con una fecha o ley inventada cuenta como alucinación."]),
        ("Starting a local model with Docker and Ollama." if en else "Arrancar un modelo local con Docker y Ollama."), en)])
    S["F4"] = block(en, [fig(shot_jupyter_f4(en),
        (["<b>Run</b> executes the selected cell (or press Shift + Enter).",
          "Training 1.0 and test about 0.98: the model memorized training a little, but still generalizes well.",
          "Each row of the confusion matrix is a true digit; each column, the predicted one. The highlighted row shows two 8s read as 1s.",
          "Showing the misclassified images helps you explain why the model failed."] if en else
         ["<b>Run</b> ejecuta la celda seleccionada (o presiona Shift + Enter).",
          "Entrenamiento 1.0 y prueba cerca de 0.98: el modelo memorizó un poco el entrenamiento, pero todavía generaliza bien.",
          "Cada fila de la matriz de confusión es un dígito real; cada columna, el predicho. La fila resaltada muestra dos 8 leídos como 1.",
          "Mostrar las imágenes mal clasificadas te ayuda a explicar por qué falló el modelo."]),
        ("Training and evaluating the digit classifier in Jupyter." if en else "Entrenar y evaluar el clasificador de dígitos en Jupyter."), en)])
    S["F5"] = block(en, [fig(shot_inspector_f5(en),
        (["<code>npx @modelcontextprotocol/inspector python server.py</code> opens the Inspector in your browser with the command already filled in. Press <b>Connect</b> until it says <b>Connected</b>.",
          "Open the <b>Tools</b> tab and press <b>List Tools</b>.",
          "Your <code>search_documents</code> tool appears with the description you wrote in its docstring.",
          "Fill in the question and <code>k</code>, then press <b>Run Tool</b>.",
          "The result shows the source of each fragment: that is what your agent will cite."] if en else
         ["<code>npx @modelcontextprotocol/inspector python server.py</code> abre el Inspector en tu navegador con el comando ya escrito. Presiona <b>Connect</b> hasta que diga <b>Connected</b>.",
          "Abre la pestaña <b>Tools</b> y presiona <b>List Tools</b>.",
          "Aparece tu herramienta <code>buscar_documentos</code> con la descripción que escribiste en su docstring.",
          "Escribe la pregunta y <code>k</code>, y presiona <b>Run Tool</b>.",
          "El resultado muestra la fuente de cada fragmento: eso es lo que tu agente va a citar."]),
        ("Testing the MCP server with the MCP Inspector." if en else "Probar el servidor MCP con el MCP Inspector."), en)])
    return S
