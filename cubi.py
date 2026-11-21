"""Cubi, the CUBO_ai block mascot: a floating guide that introduces the page and
comments on each section as the reader scrolls. build.py and build_guide.py inline
CSS and js(); the page's <body data-doc="book|guide"> and <html lang> pick the script."""
import json

SVG = '''<svg viewBox="28 100 212 236" aria-hidden="true">
<ellipse cx="140" cy="330" rx="56" ry="6" fill="#000" opacity=".1"/>
<path d="M140 190V132M140 152h10" stroke="#263445" stroke-width="4" stroke-linecap="round"/>
<circle class="led" cx="140" cy="124" r="7" fill="#0A1628" stroke-width="3"/>
<circle class="led-dot" cx="140" cy="124" r="2.5"/>
<g class="arm-l"><path d="M72 238L52 216L46 190" fill="none" stroke="#263445" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M46 190l-7-11M46 190l7-11" stroke="#263445" stroke-width="4" stroke-linecap="round"/>
<circle cx="52" cy="216" r="5" fill="#0F1B2B"/><circle cx="46" cy="190" r="4" fill="#0F1B2B"/></g>
<circle cx="72" cy="238" r="6" fill="#0F1B2B"/>
<path d="M208 240l16 18 2 24" fill="none" stroke="#263445" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M226 282l-7 10M226 282l7 10" stroke="#263445" stroke-width="4" stroke-linecap="round"/>
<circle cx="208" cy="240" r="6" fill="#0F1B2B"/><circle cx="224" cy="258" r="5" fill="#0F1B2B"/><circle cx="226" cy="282" r="4" fill="#0F1B2B"/>
<path d="M118 298v24M162 298v24" stroke="#263445" stroke-width="7" stroke-linecap="round"/>
<circle cx="118" cy="311" r="4.5" fill="#0F1B2B"/><circle cx="162" cy="311" r="4.5" fill="#0F1B2B"/>
<rect x="104" y="322" width="28" height="7" rx="3" fill="#0F1B2B"/><rect x="148" y="322" width="28" height="7" rx="3" fill="#0F1B2B"/>
<g class="body">
<polygon points="140,150 209.3,190 140,230 70.7,190" fill="#7FB4FF" stroke="#7FB4FF" stroke-width="6" stroke-linejoin="round"/>
<polygon points="70.7,190 140,230 140,310 70.7,270" fill="#2B7FE0" stroke="#2B7FE0" stroke-width="6" stroke-linejoin="round"/>
<polygon points="140,230 209.3,190 209.3,270 140,310" fill="#1A4880" stroke="#1A4880" stroke-width="6" stroke-linejoin="round"/>
<polygon points="140,166 182,190 140,214 98,190" fill="none" stroke="#C9DEFF" stroke-width="1.5" opacity=".9"/>
<path d="M140 190v-14" stroke="#263445" stroke-width="4" stroke-linecap="round"/>
<circle cx="78" cy="202" r="2.2" fill="#A9CCFF"/><circle cx="78" cy="266" r="2.2" fill="#A9CCFF"/>
<circle cx="202" cy="202" r="2.2" fill="#3E6EA8"/><circle cx="202" cy="266" r="2.2" fill="#3E6EA8"/>
<path d="M88 270l40 23M174 276l14-8" stroke="#1F6BC2" stroke-width="2" stroke-linecap="round"/>
<circle cx="192" cy="266" r="3" fill="none" stroke="#3E6EA8" stroke-width="2"/>
<polygon points="84,219.7 140,252 140,282 84,249.7" fill="#0A1628" stroke="#0A1628" stroke-width="6" stroke-linejoin="round"/>
<polygon points="140,252 196,219.7 196,249.7 140,282" fill="#0A1628" stroke="#0A1628" stroke-width="6" stroke-linejoin="round"/>
<path d="M146 253l42-24" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".15"/>
</g>
<g class="e e-norm"><g class="blink">
<g transform="translate(116 253) skewY(30)"><rect x="-8" y="-5" width="16" height="10" rx="3" fill="#5CE1FF"/></g>
<g transform="translate(164 253) skewY(-30)"><rect x="-8" y="-5" width="16" height="10" rx="3" fill="#5CE1FF"/></g></g>
<path d="M128 268l12 7 12-7" fill="none" stroke="#5CE1FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></g>
<g class="e e-happy">
<path d="M108 256q8-12 16-2M156 254q8-10 16 2" fill="none" stroke="#5CE1FF" stroke-width="3" stroke-linecap="round"/>
<path d="M126 266l14 9 14-9" fill="none" stroke="#5CE1FF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>
<g class="e e-think">
<circle class="d1" cx="113" cy="250" r="4" fill="#5CE1FF"/><circle class="d2" cx="140" cy="266" r="4" fill="#5CE1FF"/><circle class="d3" cx="167" cy="250" r="4" fill="#5CE1FF"/></g>
<g class="e e-alert">
<g transform="translate(116 253) skewY(30)"><rect x="-8" y="-2.5" width="16" height="5" rx="2" fill="#FFB020"/></g>
<g transform="translate(164 253) skewY(-30)"><rect x="-8" y="-2.5" width="16" height="5" rx="2" fill="#FFB020"/></g>
<path d="M130 270l10 5 10-5" fill="none" stroke="#FFB020" stroke-width="2.5" stroke-linecap="round"/></g>
</svg>'''

CSS = r'''
#cubi{position:fixed;right:18px;bottom:16px;z-index:70;display:flex;align-items:flex-end;gap:8px;pointer-events:none;font-family:inherit}
#cubi>*{pointer-events:auto}
.cubi-bot{width:92px;height:102px;padding:0;border:0;background:none;cursor:pointer;flex:0 0 auto;border-radius:16px}
.cubi-bot:focus-visible{outline:2px solid var(--acc);outline-offset:4px}
.cubi-bot svg{width:100%;height:100%;display:block;overflow:visible;animation:cubiBob 4.5s ease-in-out infinite}
#cubi .e{display:none}
#cubi[data-mood=tip] .e-norm,#cubi:not([data-mood]) .e-norm,#cubi[data-mood=happy] .e-happy,#cubi[data-mood=think] .e-think,#cubi[data-mood=alert] .e-alert{display:inline}
#cubi .led{stroke:#5CE1FF;animation:cubiLed 2.6s ease-in-out infinite}
#cubi .led-dot{fill:#5CE1FF}
#cubi[data-mood=alert] .led{stroke:#FFB020}#cubi[data-mood=alert] .led-dot{fill:#FFB020}
#cubi .blink{transform-box:fill-box;transform-origin:center;animation:cubiBlink 5s infinite}
#cubi .arm-l{transform-box:view-box;transform-origin:72px 238px}
#cubi.wave .arm-l{animation:cubiWave 1.1s ease-in-out 3}
#cubi .e-think circle{animation:cubiDots 1.2s ease-in-out infinite}
#cubi .e-think .d2{animation-delay:.2s}#cubi .e-think .d3{animation-delay:.4s}
.cubi-bubble{position:relative;width:min(300px,calc(100vw - 140px));margin-bottom:46px;padding:12px 14px 10px;background:var(--surface);color:var(--ink);border:1px solid var(--line);border-radius:14px;box-shadow:0 12px 32px rgba(10,22,40,.16);font-size:14px;line-height:1.5;transform-origin:bottom right;animation:cubiIn .25s ease-out}
.cubi-bubble::after{content:"";position:absolute;right:-7px;bottom:22px;width:12px;height:12px;background:var(--surface);border-right:1px solid var(--line);border-top:1px solid var(--line);transform:rotate(45deg)}
.cubi-bubble[hidden]{display:none}
.cubi-head{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:6px}
.cubi-tag{font:600 10.5px/1 var(--f-mono);letter-spacing:.09em;text-transform:uppercase;color:var(--acc-deep)}
#cubi[data-mood=alert] .cubi-tag{color:#B26A00}
.cubi-x{border:0;background:none;color:var(--muted);font-size:18px;line-height:1;cursor:pointer;padding:0 2px}
.cubi-x:hover{color:var(--ink)}
.cubi-text{margin:0}
.cubi-text code{font-size:12.5px}
.cubi-foot{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:10px}
.cubi-steps{font:500 11px/1 var(--f-mono);color:var(--muted)}
.cubi-btns{display:flex;gap:6px;margin-left:auto}
.cubi-btns button{font-size:12px;font-weight:600;line-height:1;font-family:inherit;border-radius:8px;padding:7px 10px;cursor:pointer;border:1px solid var(--line);background:var(--paper);color:var(--ink)}
.cubi-btns button.pri{background:var(--acc);border-color:var(--acc);color:#fff}
.cubi-btns button:hover{border-color:var(--acc)}
@keyframes cubiBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@keyframes cubiLed{0%,100%{opacity:1}50%{opacity:.45}}
@keyframes cubiBlink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(.1)}}
@keyframes cubiWave{0%,100%{transform:rotate(0)}30%{transform:rotate(-16deg)}70%{transform:rotate(10deg)}}
@keyframes cubiDots{0%,100%{opacity:.3}50%{opacity:1}}
@keyframes cubiIn{from{opacity:0;transform:translateY(6px) scale(.97)}to{opacity:1;transform:none}}
@media (max-width:980px){#cubi{bottom:72px;right:10px}.cubi-bot{width:70px;height:78px}.cubi-bubble{margin-bottom:30px;font-size:13.5px}}
@media (prefers-reduced-motion:reduce){#cubi *,#cubi{animation:none!important}}
@media print{#cubi{display:none!important}}
'''

UI = {
 "es": {"tags": {"tip": "Dato clave", "think": "Para pensar", "alert": "Atención", "happy": "Cubi"},
        "next": "Siguiente", "start": "Empezar", "skip": "Saltar", "mute": "Silenciar", "unmute": "Activar comentarios",
        "close": "Cerrar", "bot": "Cubi, tu guía. Toca para ver su comentario", "intro": "Ver presentación"},
 "en": {"tags": {"tip": "Key point", "think": "Think about it", "alert": "Heads up", "happy": "Cubi"},
        "next": "Next", "start": "Let's go", "skip": "Skip", "mute": "Mute", "unmute": "Turn comments on",
        "close": "Close", "bot": "Cubi, your guide. Tap to see its comment", "intro": "Show intro"},
}

MSGS = {
"guide": {
 "es": {
  "intro": [
   ["happy", "Hola, soy <b>Cubi</b>. Te voy a acompañar en la Guía del estudiante de CUBO_ai mientras avanzas por los módulos."],
   ["tip", "Cada módulo tiene objetivos, temas, autoevaluación y un DIY con dos rutas: técnica y complementaria. Puedes hacer las dos."],
   ["alert", "Una regla desde ya: todo lo que entregas, lo defiendes. Usa la IA, pero verifica y responde por el resultado."],
   ["happy", "Te dejaré comentarios en esta esquina según la sección. Si prefieres leer sin mí, toca <b>Silenciar</b>. ¡Empecemos!"]],
  "sec": {
   "g-kit": ["tip", "Prepara Docker y Ollama la primera semana. Un modelo pequeño como <code>llama3.2:1b</code> basta para todos los DIY."],
   "g-ruta": ["tip", "Para pasar al Bootcamp necesitas 70 de nota final y 60 de nota individual. El equipo no compensa lo individual."],
   "f1": ["tip", "F1 es la base de todo: primero el problema, después la tecnología."],
   "f1-3": ["alert", "Que una respuesta suene segura no la hace correcta. Verifica siempre lo que importa."],
   "f1-4": ["think", "Antes de seguir: ¿el problema que elegiste es un síntoma o una causa?"],
   "diy-f1": ["tip", "Anota porcentajes, no impresiones: diez preguntas con respuesta conocida dicen más que una demo."],
   "f2": ["tip", "En F2 aprendes a pedir con precisión y a comprobar lo que recibes."],
   "f2-1": ["tip", "Define cómo se ve una buena respuesta antes de escribir el prompt."],
   "f2-2": ["think", "Si cambias solo el nombre en la entrada, ¿cambia la decisión del modelo? Esa es tu primera prueba de sesgo."],
   "diy-f2": ["tip", "Haz commit de cada versión del prompt: el historial es tu evidencia."],
   "f3": ["think", "La ética está en cada decisión de diseño, no en un capítulo aparte."],
   "f3-2": ["alert", "Nunca pegues datos personales reales en un asistente en la nube."],
   "f3-3": ["tip", "La supervisión humana se diseña: quién aprueba, con qué información y qué queda registrado."],
   "diy-f3": ["alert", "Usa solo datos inventados en este DIY y documenta lo que se escapa de tu filtro."],
   "f4": ["tip", "En proyectos reales, la mayor parte del tiempo se va en los datos, no en el modelo."],
   "f4-2": ["alert", "Nunca midas con los mismos datos con que entrenaste."],
   "f4-3": ["think", "Si tus imágenes de entrenamiento se tomaron de día, ¿qué pasa de noche?"],
   "diy-f4": ["tip", "Muestra ejemplos concretos de errores: explican más que la exactitud sola."],
   "f5": ["tip", "F5 conecta todo: modelos, documentos, herramientas e infraestructura."],
   "f5-2": ["think", "Si tu RAG responde mal, ¿falló la búsqueda o la generación? Revisa primero los fragmentos recuperados."],
   "f5-3": ["tip", "Con MCP el modelo no toca tus datos: solo pide ejecutar herramientas que tú defines."],
   "f5-5": ["think", "¿Qué servicios deberían correr en infraestructura propia? Calcula el costo por consulta antes de decidir."],
   "diy-f5": ["tip", "Tu agente debe saber decir “no está en los documentos”. Pruébalo con preguntas sin respuesta."],
   "c-1": ["happy", "Preparación para el Challenge: tres semanas, cuatro personas, un problema real."],
   "c-2": ["tip", "Una rama por tarea y pull requests revisados. Nadie mezcla su propio trabajo sin otra lectura."],
   "c-5": ["alert", "Una demo que salió bien no valida nada. Valida con un conjunto de evaluación."],
   "c-7": ["think", "Practica en voz alta: ¿qué aportaste tú y qué decisión cambiarías?"],
   "b-1": ["happy", "Llegaste al Bootcamp. Aquí ya no se filtra: se profundiza."],
   "b-3": ["alert", "Llega con tu entorno listo. El hackathon no deja tiempo para instalar."],
   "b-5": ["tip", "Incluye en tu demo un caso donde el sistema dice que no sabe. Eso genera confianza."],
   "b-6": ["tip", "Tu credencial la emite ANIA y cualquiera puede verificarla por su cuenta."],
   "a-1": ["tip", "Copia estas plantillas a tu repositorio desde el primer día."]}},
 "en": {
  "intro": [
   ["happy", "Hi, I'm <b>Cubi</b>. I'll be with you through the CUBO_ai Student Guide as you move through the modules."],
   ["tip", "Each module has objectives, topics, a self-assessment and a DIY with two routes: technical and complementary. You can do both."],
   ["alert", "One rule from the start: everything you deliver, you defend. Use AI, but verify and answer for the result."],
   ["happy", "I'll leave comments in this corner depending on the section. If you'd rather read without me, tap <b>Mute</b>. Let's go!"]],
  "sec": {
   "g-kit": ["tip", "Set up Docker and Ollama in the first week. A small model like <code>llama3.2:1b</code> is enough for every DIY."],
   "g-ruta": ["tip", "To reach the Bootcamp you need a final score of 70 and an individual score of 60. The team can't make up for the individual part."],
   "f1": ["tip", "F1 is the base of everything: problem first, technology second."],
   "f1-3": ["alert", "An answer that sounds confident isn't necessarily right. Always verify what matters."],
   "f1-4": ["think", "Before you go on: is the problem you chose a symptom or a cause?"],
   "diy-f1": ["tip", "Record percentages, not impressions: ten questions with known answers say more than a demo."],
   "f2": ["tip", "In F2 you learn to ask precisely and to check what you get back."],
   "f2-1": ["tip", "Define what a good answer looks like before writing the prompt."],
   "f2-2": ["think", "If you change only the name in the input, does the model's decision change? That's your first bias test."],
   "diy-f2": ["tip", "Commit every version of the prompt: the history is your evidence."],
   "f3": ["think", "Ethics lives in every design decision, not in a separate chapter."],
   "f3-2": ["alert", "Never paste real personal data into a cloud assistant."],
   "f3-3": ["tip", "Human oversight is designed: who approves, with what information and what gets logged."],
   "diy-f3": ["alert", "Use only made-up data in this DIY and document what slips past your filter."],
   "f4": ["tip", "In real projects, most of the time goes into the data, not the model."],
   "f4-2": ["alert", "Never measure with the same data you trained on."],
   "f4-3": ["think", "If your training images were taken in daylight, what happens at night?"],
   "diy-f4": ["tip", "Show concrete examples of errors: they explain more than accuracy alone."],
   "f5": ["tip", "F5 connects everything: models, documents, tools and infrastructure."],
   "f5-2": ["think", "If your RAG answers badly, did retrieval or generation fail? Check the retrieved fragments first."],
   "f5-3": ["tip", "With MCP the model never touches your data: it only asks to run tools you define."],
   "f5-5": ["think", "Which services should run on your own infrastructure? Calculate the cost per query before deciding."],
   "diy-f5": ["tip", "Your agent must be able to say “not in the documents”. Test it with unanswerable questions."],
   "c-1": ["happy", "Challenge prep: three weeks, four people, one real problem."],
   "c-2": ["tip", "One branch per task and reviewed pull requests. Nobody merges their own work unread."],
   "c-5": ["alert", "A demo that went well validates nothing. Validate with an evaluation set."],
   "c-7": ["think", "Practice out loud: what did you contribute, and which decision would you change?"],
   "b-1": ["happy", "You made it to the Bootcamp. No more filtering here: you go deeper."],
   "b-3": ["alert", "Arrive with your environment ready. The hackathon leaves no time to install."],
   "b-5": ["tip", "Include a case in your demo where the system says it doesn't know. It builds trust."],
   "b-6": ["tip", "ANIA issues your credential, and anyone can verify it on their own."],
   "a-1": ["tip", "Copy these templates into your repository from day one."]}}},
"book": {
 "es": {
  "intro": [
   ["happy", "Hola, soy <b>Cubi</b>. Este es el Libro de ejecución de CUBO_ai: cómo funciona el programa de principio a fin."],
   ["tip", "Está organizado en 8 partes. Usa el índice o el mapa de referencias del final para ir directo a una pregunta."],
   ["happy", "Te dejaré notas en esta esquina según la sección. Puedes silenciarme cuando quieras."]],
  "sec": {
   "s1": ["tip", "La ruta tiene 10 fases. The AI Challenge es el filtro práctico central."],
   "s2": ["think", "Los 8 principios aparecen en todas las fases. ¿Cuál crees que pesa más en la evaluación?"],
   "s4": ["tip", "Dos perfiles, un mismo problema. Los complementarios no son “desarrolladores a medias”."],
   "s5": ["tip", "13 competencias compartidas, cada una con su evidencia de verificación."],
   "s7": ["tip", "Tres compuertas separan las etapas. Cada una se abre solo con evidencia."],
   "s8": ["tip", "Los cinco módulos se desarrollan en detalle, con DIY, en la Guía del estudiante."],
   "s9": ["alert", "El Challenge no es un curso introductorio: es una evaluación práctica de tres semanas."],
   "s11": ["tip", "Durante el Challenge, calcula entre 18 y 25 horas por semana."],
   "s13": ["alert", "El número de commits no mide productividad. Se evalúan calidad, evolución y autoría."],
   "s14": ["think", "Prueba la calculadora: una nota de equipo alta no compensa una individual menor a 60."],
   "s18": ["tip", "Umbral de 70 en la nota final y 60 en la individual, sujeto a cupo."],
   "s19": ["tip", "Mentores asesoran, el jurado califica, el comité decide y ANIA certifica. Nadie concentra todo."],
   "s20": ["alert", "Cada riesgo tiene sus mitigaciones. El primero: trabajo de IA sin verificar."],
   "s21": ["happy", "El Bootcamp: cuatro días para aprender a fondo y 48 horas para demostrarlo."],
   "s22": ["think", "Completar no es lo mismo que dominar ni que defender. La evaluación separa las tres cosas."],
   "s24": ["tip", "La credencial es institucional (ANIA); la verificación es criptográfica. Son cosas distintas."],
   "s25": ["tip", "Cualquier persona puede verificar el certificado: huella SHA-256, marca de tiempo y prueba."],
   "s29": ["alert", "Las excepciones se documentan y las aprueba una autoridad designada. La rúbrica nunca cambia de manera informal."],
   "s32": ["happy", "Llegaste al final. Usa el mapa de referencias para volver a cualquier regla."]}},
 "en": {
  "intro": [
   ["happy", "Hi, I'm <b>Cubi</b>. This is the CUBO_ai Execution Framework: how the program works from start to finish."],
   ["tip", "It's organized in 8 parts. Use the contents or the cross-reference map at the end to jump straight to a question."],
   ["happy", "I'll leave notes in this corner depending on the section. You can mute me anytime."]],
  "sec": {
   "s1": ["tip", "The route has 10 phases. The AI Challenge is the central practical filter."],
   "s2": ["think", "The 8 principles show up in every phase. Which one do you think weighs most in evaluation?"],
   "s4": ["tip", "Two profiles, one problem. Complementary participants are not “half developers”."],
   "s5": ["tip", "13 shared competencies, each with its own verification evidence."],
   "s7": ["tip", "Three gates separate the stages. Each one opens only with evidence."],
   "s8": ["tip", "The five modules are developed in detail, with DIYs, in the Student Guide."],
   "s9": ["alert", "The Challenge is not an introductory course: it's a three-week practical assessment."],
   "s11": ["tip", "During the Challenge, plan for 18 to 25 hours per week."],
   "s13": ["alert", "Commit counts don't measure productivity. Quality, evolution and authorship are evaluated."],
   "s14": ["think", "Try the calculator: a high team score can't make up for an individual score below 60."],
   "s18": ["tip", "Threshold of 70 on the final score and 60 on the individual score, subject to capacity."],
   "s19": ["tip", "Mentors advise, the panel scores, the committee decides and ANIA certifies. Nobody holds it all."],
   "s20": ["alert", "Every risk has its mitigations. The first: unverified AI work."],
   "s21": ["happy", "The Bootcamp: four days to learn in depth and 48 hours to prove it."],
   "s22": ["think", "Completing isn't the same as mastering or defending. The evaluation separates all three."],
   "s24": ["tip", "The credential is institutional (ANIA); verification is cryptographic. They're different things."],
   "s25": ["tip", "Anyone can verify the certificate: SHA-256 fingerprint, timestamp and proof."],
   "s29": ["alert", "Exceptions are documented and approved by a designated authority. The rubric never changes informally."],
   "s32": ["happy", "You made it to the end. Use the cross-reference map to get back to any rule."]}}}}

JS = r'''
(function(){
var body=document.body,doc=body.getAttribute("data-doc")||"guide",lang=(document.documentElement.lang||"es").slice(0,2)==="en"?"en":"es";
var D=(window.CUBI_MSGS[doc]||{})[lang];if(!D)return;var U=window.CUBI_UI[lang];
function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
function put(k,v){try{localStorage.setItem(k,v)}catch(e){}}
var KM="cubi-muted",KI="cubi-intro-"+doc;
var w=document.createElement("div");w.id="cubi";w.setAttribute("data-mood","happy");
w.innerHTML='<div class="cubi-bubble" role="status" aria-live="polite" hidden><div class="cubi-head"><span class="cubi-tag"></span><button class="cubi-x" type="button" aria-label="'+U.close+'">×</button></div><p class="cubi-text"></p><div class="cubi-foot"><span class="cubi-steps"></span><div class="cubi-btns"></div></div></div><button class="cubi-bot" type="button" aria-label="'+U.bot+'">'+window.CUBI_SVG+'</button>';
body.appendChild(w);
var bub=w.querySelector(".cubi-bubble"),tag=w.querySelector(".cubi-tag"),txt=w.querySelector(".cubi-text"),steps=w.querySelector(".cubi-steps"),btns=w.querySelector(".cubi-btns");
var muted=get(KM)==="1",inIntro=false,step=0,current=null,timer=null,seen={};
function mood(m){w.setAttribute("data-mood",m);if(m==="happy"){w.classList.remove("wave");void w.offsetWidth;w.classList.add("wave")}}
function button(label,pri,fn){var b=document.createElement("button");b.type="button";b.textContent=label;if(pri)b.className="pri";b.onclick=fn;btns.appendChild(b)}
function show(m,html){clearTimeout(timer);mood(m);tag.textContent=U.tags[m]||"Cubi";txt.innerHTML=html;bub.hidden=false;bub.style.animation="none";void bub.offsetWidth;bub.style.animation=""}
function hide(){clearTimeout(timer);bub.hidden=true;if(inIntro){inIntro=false;put(KI,"1")}}
function muteBtn(){button(muted?U.unmute:U.mute,false,function(){muted=!muted;put(KM,muted?"1":"0");if(muted)hide();else{btns.innerHTML="";muteBtn()}})}
function intro(){inIntro=true;step=0;renderIntro()}
function renderIntro(){var it=D.intro[step];show(it[0],it[1]);steps.textContent=(step+1)+" / "+D.intro.length;btns.innerHTML="";
 if(step<D.intro.length-1){button(U.skip,false,hide);button(U.next,true,function(){step++;renderIntro()})}
 else{muteBtn();button(U.start,true,hide)}}
function comment(id,auto){var c=D.sec[id];if(!c)return;current=id;show(c[0],c[1]);steps.textContent="";btns.innerHTML="";muteBtn();if(auto)timer=setTimeout(function(){bub.hidden=true},14000)}
w.querySelector(".cubi-x").onclick=hide;
w.querySelector(".cubi-bot").onclick=function(){if(!bub.hidden){hide();return}if(current)comment(current,false);else intro()};
var ids=Object.keys(D.sec),els=ids.map(function(i){return document.getElementById(i)}).filter(Boolean);
var tick=false,last=null;
function where(){tick=false;var line=window.innerHeight*0.4,cur=null;for(var i=0;i<els.length;i++){if(els[i].getBoundingClientRect().top<=line)cur=els[i].id;else break}
 if(!cur||cur===last)return;last=cur;current=cur;if(inIntro||muted||seen[cur])return;seen[cur]=1;comment(cur,true)}
els.sort(function(a,b){return a.compareDocumentPosition(b)&2?1:-1});
window.addEventListener("scroll",function(){if(!tick){tick=true;requestAnimationFrame(where)}},{passive:true});
if(get(KI)!=="1")setTimeout(intro,900);else mood("tip");
})();
'''


def js():
    return ("window.CUBI_SVG=" + json.dumps(SVG) + ";window.CUBI_UI=" + json.dumps(UI, ensure_ascii=False)
            + ";window.CUBI_MSGS=" + json.dumps(MSGS, ensure_ascii=False) + ";" + JS)
