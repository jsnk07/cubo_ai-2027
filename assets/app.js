(function(){
"use strict";
var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- iconos de línea (24x24) ---------- */
var IC = {
  search:'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>',
  gear:'<circle cx="12" cy="12" r="3.2"/><path d="M12 2.8v2.6M12 18.6v2.6M4.2 7.5l2.3 1.3M17.5 15.2l2.3 1.3M4.2 16.5l2.3-1.3M17.5 8.8l2.3-1.3"/><circle cx="12" cy="12" r="7"/>',
  code:'<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 4l-3 16"/>',
  check:'<path d="M4 12.5l5 5L20 6.5"/>',
  shield:'<path d="M12 3l7.5 3v6c0 4.6-3.2 7.8-7.5 9-4.3-1.2-7.5-4.4-7.5-9V6z"/><path d="M8.8 12l2.3 2.3 4.3-4.6"/>',
  bolt:'<path d="M13 2.5L5 13.5h6l-1 8 8-11h-6z"/>',
  cube:'<path d="M12 2.8l8.2 4.6v9.2L12 21.2 3.8 16.6V7.4z"/><path d="M3.8 7.4L12 12l8.2-4.6M12 12v9.2"/>',
  doc:'<path d="M6 2.8h8l4.5 4.5v13.9H6z"/><path d="M14 2.8v4.5h4.5M9 12h6.5M9 15.5h6.5"/>',
  lock:'<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 018 0v3"/>',
  unlock:'<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 017.6-1.8"/>',
  clock:'<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
  users:'<circle cx="9" cy="8.5" r="3.2"/><path d="M3 20c.6-3.4 3-5.5 6-5.5s5.4 2.1 6 5.5"/><circle cx="17" cy="9.5" r="2.5"/><path d="M16.5 14.6c2.4.2 4 1.9 4.5 4.6"/>',
  user:'<circle cx="12" cy="8" r="3.6"/><path d="M5 20.5c.8-3.9 3.6-6.2 7-6.2s6.2 2.3 7 6.2"/>',
  git:'<circle cx="6.5" cy="5.5" r="2.2"/><circle cx="6.5" cy="18.5" r="2.2"/><circle cx="17.5" cy="8.5" r="2.2"/><path d="M6.5 7.7v8.6M17.5 10.7c0 4-11 2.5-11 5.6"/>',
  key:'<circle cx="8" cy="12" r="4.2"/><path d="M12.2 12H21M17.5 12v3.2M20.5 12v2.4"/>',
  hash:'<path d="M9.5 3.5L7.5 20.5M16.5 3.5l-2 17M4 9h16.5M3.5 15H20"/>',
  block:'<rect x="3.5" y="5" width="17" height="14" rx="2.5"/><path d="M3.5 9.5h17M8 14h3M8 16.5h6"/>',
  globe:'<circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4c2.6 2.4 3.9 5.2 3.9 8.6s-1.3 6.2-3.9 8.6c-2.6-2.4-3.9-5.2-3.9-8.6S9.4 5.8 12 3.4z"/>',
  mic:'<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"/>',
  game:'<rect x="2.8" y="7.5" width="18.4" height="10" rx="5"/><path d="M7.5 11v3.2M5.9 12.6h3.2"/><circle cx="15.5" cy="11.5" r=".9"/><circle cx="17.5" cy="13.8" r=".9"/>',
  send:'<path d="M21 3L10 14M21 3l-6.5 18-4.5-7-7-4.5z"/>',
  chart:'<path d="M4 20V4M4 20h16.5"/><path d="M8 16v-5M12 16V8M16 16v-3.5"/>',
  flag:'<path d="M5.5 21V3.8M5.5 4.5h11.5l-2.5 4 2.5 4H5.5"/>',
  book:'<path d="M4 4.5h6.5a2 2 0 012 2v14a2 2 0 00-2-2H4zM20 4.5h-6.5a2 2 0 00-2 2v14a2 2 0 012-2H20z"/>',
  bulb:'<path d="M9 18h6M10 21h4M12 3a6 6 0 00-3.6 10.8c.8.6 1.1 1.4 1.1 2.2h5c0-.8.3-1.6 1.1-2.2A6 6 0 0012 3z"/>',
  layers:'<path d="M12 3.5l9 4.8-9 4.8-9-4.8z"/><path d="M3 12.5l9 4.8 9-4.8M3 16.5l9 4.8 9-4.8"/>',
  target:'<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
  link:'<path d="M10 14a4.5 4.5 0 006.4 0l3-3a4.5 4.5 0 00-6.4-6.4l-1.3 1.3"/><path d="M14 10a4.5 4.5 0 00-6.4 0l-3 3a4.5 4.5 0 006.4 6.4l1.3-1.3"/>',
  ai:'<rect x="5" y="5" width="14" height="14" rx="3"/><path d="M9.5 15l1.7-6h1.6l1.7 6M10 13h4M2.5 9.5H5M2.5 14.5H5M19 9.5h2.5M19 14.5h2.5M9.5 2.5V5M14.5 2.5V5M9.5 19v2.5M14.5 19v2.5"/>',
  scale:'<path d="M12 3.5v17M6 20.5h12M4 7.5h16"/><path d="M6.5 7.5L3.5 14a3 3 0 006 0zM17.5 7.5l-3 6.5a3 3 0 006 0z"/>',
  eye:'<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
  coin:'<circle cx="12" cy="12" r="8.6"/><path d="M10 7.5h3.4a2 2 0 010 4H10zm0 4h4a2.2 2.2 0 010 4.4h-4zM10 7.5v8.4M11.5 6v1.5M11.5 15.9v1.6"/>',
  map:'<path d="M3.5 6.5l5.5-2.5 6 2.5 5.5-2.5v13.5L15 20l-6-2.5-5.5 2.5z"/><path d="M9 4v13.5M15 6.5V20"/>',
  flagc:'<path d="M5.5 21V3.8"/><path d="M5.5 4.5h4v3h-4zM9.5 7.5h4v3h-4zM13.5 4.5h4v3h-4zM5.5 10.5h4M13.5 10.5h4"/>',
  sim:'<circle cx="5.5" cy="12" r="2.2"/><circle cx="18.5" cy="6" r="2.2"/><circle cx="18.5" cy="18" r="2.2"/><circle cx="12" cy="12" r="1.6"/><path d="M7.7 12h2.7M13.4 11l3.2-3.6M13.4 13l3.2 3.6"/>',
  door:'<path d="M5 21V4.5h11V21M3.5 21h17M13 12.5v.5"/>',
  lab:'<path d="M9.5 3.5h5M10 3.5v6L4.8 18.6A1.6 1.6 0 006.2 21h11.6a1.6 1.6 0 001.4-2.4L14 9.5v-6"/><path d="M7.5 15h9"/>',
  stage:'<path d="M3.5 20.5h17M5.5 20.5V10l6.5-5.5 6.5 5.5v10.5"/><path d="M10 20.5v-5h4v5"/>',
  wallet:'<path d="M4 7.5h14.5a2 2 0 012 2v8.5a2 2 0 01-2 2H5.5A1.5 1.5 0 014 18.5z"/><path d="M4 7.5l11-3.5v3.5M16 14h2"/>',
  nodes:'<circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><circle cx="12" cy="10" r="2"/><path d="M6.7 7l3.6 2M17.3 7l-3.6 2M12 12v4"/>'
};
function icon(name){return '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">'+(IC[name]||IC.cube)+'</svg>';}
document.querySelectorAll("[data-ic]").forEach(function(el){el.insertAdjacentHTML("afterbegin",icon(el.getAttribute("data-ic")));});

/* colores del tema leídos de los tokens CSS */
var CS=getComputedStyle(document.documentElement);
function hx(name){var v=CS.getPropertyValue(name).trim()||"#000000";if(v.indexOf("rgb")===0){var m=v.match(/[\d.]+/g);return [+m[0],+m[1],+m[2]];}if(v.length===4)v="#"+v[1]+v[1]+v[2]+v[2]+v[3]+v[3];return [parseInt(v.substr(1,2),16),parseInt(v.substr(3,2),16),parseInt(v.substr(5,2),16)];}
function C(name,a){var c=hx(name);return "rgba("+c[0]+","+c[1]+","+c[2]+","+(a==null?1:a)+")";}
function M(n1,n2,t,a){var x=hx(n1),y=hx(n2);return "rgba("+Math.round(x[0]+(y[0]-x[0])*t)+","+Math.round(x[1]+(y[1]-x[1])*t)+","+Math.round(x[2]+(y[2]-x[2])*t)+","+(a==null?1:a)+")";}
/* ---------- arte generativo en canvas ---------- */
function rng(seed){var s=seed>>>0;return function(){s=(s*1664525+1013904223)>>>0;return s/4294967296;};}
function setup(cv){
  var dpr=Math.min(window.devicePixelRatio||1,2),r=cv.getBoundingClientRect();
  cv.width=Math.max(1,r.width*dpr);cv.height=Math.max(1,r.height*dpr);
  var c=cv.getContext("2d");c.setTransform(dpr,0,0,dpr,0,0);return {c:c,w:r.width,h:r.height};
}
/* cubo isométrico */
function isoCube(c,x,y,s,top,left,right,stroke){
  var h=s*0.5;
  c.beginPath();c.moveTo(x,y-s);c.lineTo(x+s*0.866,y-h);c.lineTo(x,y);c.lineTo(x-s*0.866,y-h);c.closePath();c.fillStyle=top;c.fill();
  c.beginPath();c.moveTo(x-s*0.866,y-h);c.lineTo(x,y);c.lineTo(x,y+s);c.lineTo(x-s*0.866,y+h);c.closePath();c.fillStyle=left;c.fill();
  c.beginPath();c.moveTo(x+s*0.866,y-h);c.lineTo(x,y);c.lineTo(x,y+s);c.lineTo(x+s*0.866,y+h);c.closePath();c.fillStyle=right;c.fill();
  if(stroke){c.strokeStyle=stroke;c.lineWidth=1;c.beginPath();c.moveTo(x,y-s);c.lineTo(x+s*0.866,y-h);c.lineTo(x+s*0.866,y+h);c.lineTo(x,y+s);c.lineTo(x-s*0.866,y+h);c.lineTo(x-s*0.866,y-h);c.closePath();c.moveTo(x,y);c.lineTo(x,y+s);c.moveTo(x,y);c.lineTo(x-s*0.866,y-h);c.moveTo(x,y);c.lineTo(x+s*0.866,y-h);c.stroke();}
}

var scenes = {};
/* escena clara estilo CUBO+ IG: red naranja, brillo de neón y panel de vidrio */
function heroScene(cv,v,isCover){
  var g=setup(cv),R=rng(v*7919+13),w=g.w,h=g.h,pts=[],edges=[],i,j;
  var n=Math.round((w*h)/(isCover?9000:11000));
  for(i=0;i<n;i++){var px=Math.pow(R(),0.6)*w,py=R()*h;pts.push({x:px,y:py,ph:R()*6.28});}
  for(i=0;i<pts.length;i++){var d=[];for(j=0;j<pts.length;j++)if(j!==i)d.push([Math.hypot(pts[i].x-pts[j].x,pts[i].y-pts[j].y),j]);d.sort(function(a,b){return a[0]-b[0];});
    for(var k=0;k<2;k++){var q=d[k][1];if(q>i||d[k][0]>0)edges.push([i,q,R()]);}}
  var pulses=[];for(i=0;i<Math.min(14,edges.length);i++)pulses.push({e:edges[Math.floor(R()*edges.length)],s:0.00012+R()*0.0002,o:R()});
  var narrow=w<700;var cx=narrow?w*0.8:w*(isCover?0.8:0.82),cy=narrow?(isCover?h*0.09:h*0.2):h*0.48,S=narrow?Math.min(w*0.11,h*0.1):Math.min(h*(isCover?0.26:0.3),w*0.16);
  function glowStroke(c,fn,lw){c.save();c.strokeStyle=C("--acc");c.lineWidth=lw;c.lineJoin="round";c.lineCap="round";c.shadowColor=C("--acc",.9);c.shadowBlur=22;fn();c.stroke();c.shadowBlur=8;c.strokeStyle=C("--acc-hi");c.lineWidth=lw*0.45;fn();c.stroke();c.restore();}
  function neon(c,t){
    var p=(Math.sin(t*0.0015)+1)/2;
    // panel de vidrio
    c.save();c.translate(cx,cy);c.transform(1,-0.06,0,1,0,0);
    var pw=S*2.1,ph=S*2.3;c.fillStyle="rgba(255,255,255,.28)";c.strokeStyle="rgba(255,255,255,.9)";c.lineWidth=1.5;
    c.beginPath();if(c.roundRect)c.roundRect(-pw/2,-ph/2,pw,ph,18);else c.rect(-pw/2,-ph/2,pw,ph);c.fill();c.stroke();c.restore();
    c.save();c.translate(cx,cy);c.globalAlpha=0.75+0.25*p;
    var s=S*0.62;
    if(v===7){ glowStroke(c,function(){c.beginPath();c.moveTo(s*0.15,-s*1.05);c.lineTo(-s*0.55,s*0.1);c.lineTo(-s*0.02,s*0.1);c.lineTo(-s*0.2,s*1.05);c.lineTo(s*0.6,-s*0.15);c.lineTo(s*0.05,-s*0.15);c.closePath();},5); }
    else if(v===8){ for(var b=0;b<3;b++){(function(b){var bx=-s*1.05+b*s*0.78,bs=s*0.56;glowStroke(c,function(){c.beginPath();c.rect(bx,-bs/2,bs,bs);if(b<2){c.moveTo(bx+bs,0);c.lineTo(bx+s*0.78,0);}},4);})(b);} }
    else if(v===6){ glowStroke(c,function(){c.beginPath();c.moveTo(0,-s);c.lineTo(s*0.85,-s*0.62);c.lineTo(s*0.85,s*0.05);c.quadraticCurveTo(s*0.8,s*0.75,0,s*1.05);c.quadraticCurveTo(-s*0.8,s*0.75,-s*0.85,s*0.05);c.lineTo(-s*0.85,-s*0.62);c.closePath();c.moveTo(-s*0.35,0);c.lineTo(-s*0.05,s*0.3);c.lineTo(s*0.4,-s*0.25);},5); }
    else if(v===4){ glowStroke(c,function(){c.beginPath();c.rect(-s*0.9,-s*0.8,s*1.8,s*1.65);c.moveTo(-s*0.9,-s*0.35);c.lineTo(s*0.9,-s*0.35);c.moveTo(-s*0.45,-s*1);c.lineTo(-s*0.45,-s*0.6);c.moveTo(s*0.45,-s*1);c.lineTo(s*0.45,-s*0.6);},4);
      c.fillStyle=C("--acc");for(var r=0;r<2;r++)for(var q2=0;q2<3;q2++){c.beginPath();c.arc(-s*0.5+q2*s*0.5,s*0.05+r*s*0.4,s*0.08,0,6.283);c.fill();} }
    else if(v===2){ glowStroke(c,function(){c.beginPath();c.moveTo(-s,-s*0.7);c.bezierCurveTo(-s*0.2,-s*0.7,-s*0.2,0,s*0.5,0);c.moveTo(-s,s*0.7);c.bezierCurveTo(-s*0.2,s*0.7,-s*0.2,0,s*0.5,0);c.moveTo(s*0.3,-s*0.2);c.lineTo(s*0.55,0);c.lineTo(s*0.3,s*0.2);},5); }
    else if(v===3||v===5){ glowStroke(c,function(){c.beginPath();c.moveTo(-s,s*0.9);c.lineTo(-s*0.5,s*0.9);c.lineTo(-s*0.5,s*0.35);c.lineTo(0,s*0.35);c.lineTo(0,-s*0.2);c.lineTo(s*0.5,-s*0.2);c.lineTo(s*0.5,-s*0.75);c.lineTo(s,-s*0.75);},5);
      c.fillStyle=C("--acc-hi");c.beginPath();c.arc(s*0.75,-s*1.0,s*0.12,0,6.283);c.fill(); }
    else { glowStroke(c,function(){var a=s*0.866,hh=s*0.5;c.beginPath();c.moveTo(0,-s);c.lineTo(a,-hh);c.lineTo(a,hh);c.lineTo(0,s);c.lineTo(-a,hh);c.lineTo(-a,-hh);c.closePath();c.moveTo(-a,-hh);c.lineTo(0,0);c.lineTo(a,-hh);c.moveTo(0,0);c.lineTo(0,s);},5);
      }
    c.restore();
  }
  return function(t){
    var c=g.c;c.clearRect(0,0,w,h);c.fillStyle=C("--hero-bg");c.fillRect(0,0,w,h);
    var rg=c.createRadialGradient(cx,cy,10,cx,cy,Math.max(w*0.45,S*3));rg.addColorStop(0,C("--acc",.55));rg.addColorStop(.35,C("--acc",.18));rg.addColorStop(1,C("--acc",0));c.fillStyle=rg;c.fillRect(0,0,w,h);
    c.lineWidth=1.1;
    for(i=0;i<edges.length;i++){var A=pts[edges[i][0]],B=pts[edges[i][1]],al=0.18+0.35*(A.x/w);c.strokeStyle=C("--acc",al);c.beginPath();c.moveTo(A.x,A.y);c.lineTo(B.x,B.y);c.stroke();}
    for(i=0;i<pts.length;i++){var P=pts[i];c.fillStyle=C("--acc",0.25+0.4*(P.x/w));c.beginPath();c.arc(P.x,P.y,1.6,0,6.283);c.fill();}
    for(i=0;i<pulses.length;i++){var pl=pulses[i],e=pl.e,A2=pts[e[0]],B2=pts[e[1]],u=(t*pl.s+pl.o)%1;var X=A2.x+(B2.x-A2.x)*u,Y=A2.y+(B2.y-A2.y)*u;
      c.save();c.shadowColor=C("--acc");c.shadowBlur=10;c.fillStyle=C("--acc-hi");c.beginPath();c.arc(X,Y,2.4,0,6.283);c.fill();c.restore();}
    if(!(narrow&&isCover))neon(c,t);
    var sl=c.createLinearGradient(0,0,w*(isCover?0.72:0.62),0);sl.addColorStop(0,C("--hero-bg",0.98));sl.addColorStop(.6,C("--hero-bg",0.9));sl.addColorStop(1,C("--hero-bg",narrow?0.55:0));c.fillStyle=sl;c.fillRect(0,0,w,h);
  };
}
scenes.cover=function(cv){return heroScene(cv,1,true);};
scenes.part=function(cv){return heroScene(cv,+cv.getAttribute("data-v")||1,false);};

var live=[];
document.querySelectorAll("canvas[data-scene]").forEach(function(cv){
  var draw=scenes[cv.getAttribute("data-scene")](cv);live.push({cv:cv,draw:draw,vis:true});
  draw(1200);
});
if("IntersectionObserver" in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){live.forEach(function(L){if(L.cv===e.target)L.vis=e.isIntersecting;});});});
  live.forEach(function(L){io.observe(L.cv);});
}
if(!reduce){(function loop(t){live.forEach(function(L){if(L.vis)L.draw(t);});requestAnimationFrame(loop);})(0);}
var rt;window.addEventListener("resize",function(){clearTimeout(rt);rt=setTimeout(function(){live.forEach(function(L){L.draw=scenes[L.cv.getAttribute("data-scene")](L.cv);L.draw(1200);});},200);});

/* ---------- calculadora 60/40 ---------- */
var calc=document.getElementById("calc");
if(calc){
  var te=calc.querySelector("#team"),ind=calc.querySelector("#indiv");
  var ot=calc.querySelector("#teamOut"),oi=calc.querySelector("#indivOut"),fin=calc.querySelector("#final"),ver=calc.querySelector("#verdict"),why=calc.querySelector("#why");
  function upd(){
    var T=+te.value,I=+ind.value,F=Math.round((T*0.6+I*0.4)*10)/10;
    ot.textContent=T;oi.textContent=I;fin.textContent=F;
    var L=window.I18N||{},ok=F>=70&&I>=60;ver.textContent=ok?L.ok:L.no;ver.className="verdict "+(ok?"ok":"no");
    why.textContent=ok?L.whyOk:(F<70&&I<60?L.whyBoth:F<70?L.whyF:L.whyI);
  }
  te.addEventListener("input",upd);ind.addEventListener("input",upd);upd();
}

/* ---------- índice: sección activa y menú móvil ---------- */
var toc=document.querySelector(".toc"),mb=document.querySelector(".menu-btn");
if(mb)mb.addEventListener("click",function(){toc.classList.toggle("open");mb.setAttribute("aria-expanded",toc.classList.contains("open"));});
document.querySelectorAll(".toc a").forEach(function(a){a.addEventListener("click",function(){toc.classList.remove("open");});});
var links={};document.querySelectorAll(".toc a[href^='#']").forEach(function(a){links[a.getAttribute("href").slice(1)]=a;});
if("IntersectionObserver" in window){
  var cur=null;
  var so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&links[e.target.id]){if(cur)cur.classList.remove("on");cur=links[e.target.id];cur.classList.add("on");}});},{rootMargin:"-10% 0px -80% 0px"});
  Object.keys(links).forEach(function(id){var el=document.getElementById(id);if(el)so.observe(el);});
}
/* tema */
var tb=document.getElementById("themeBtn");
if(tb)tb.addEventListener("click",function(){var r=document.documentElement,d=r.getAttribute("data-theme");var dark=d?d==="dark":window.matchMedia("(prefers-color-scheme: dark)").matches;r.setAttribute("data-theme",dark?"light":"dark");CS=getComputedStyle(document.documentElement);});
})();
