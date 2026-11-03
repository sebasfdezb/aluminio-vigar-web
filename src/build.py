#!/usr/bin/env python3
"""Genera las páginas HTML estáticas de la web de Vigar.
Uso: python3 src/build.py   (escribe los .html en la raíz del proyecto)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.carpinteriaaluminiovigar.com"

ARR = '<span class="arr"><svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
GO = '<span class="go"><svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
MARK = ('<svg viewBox="0 0 120 32" aria-hidden="true"><rect x="1" y="1" width="30" height="30" rx="8" fill="#0f1733"/>'
        '<rect x="7" y="7" width="8" height="18" rx="2" fill="#eef1f6"/><rect x="17" y="7" width="8" height="18" rx="2" fill="#e8262c"/>'
        '<text x="40" y="24" font-family="Geist, system-ui, sans-serif" font-size="24" font-weight="600" letter-spacing="-1.2" fill="#0f1733">vigar</text></svg>')
WA_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.4-.3Z"/></svg>'
WA_URL = "https://wa.me/34607437106?text=Hola%2C%20quiero%20pedir%20presupuesto"

NAV = [("index.html", "Inicio"), ("productos.html", "Productos"), ("trabajos.html", "Trabajos"),
       ("empresa.html", "Empresa"), ("contacto.html", "Contacto")]


def layout(file, title, desc, body, og_img="img/gen/interior.jpg", extra_head=""):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{cur if h == file else ""}>{t}</a>' for h, t in NAV)
    canon = SITE + "/" + ("" if file == "index.html" else file.replace(".html", ""))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#eef1f6">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{og_img}">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@200..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Saltar al contenido</a>
<header class="header" id="header">
  <div class="header__bar">
    <a href="index.html" class="logo" aria-label="Vigar, carpintería de aluminio · Inicio">{MARK}</a>
    <nav class="nav" id="nav" aria-label="Principal">
      {nav}
      <a href="contacto.html" class="btn btn--sm">Pedir presupuesto {ARR}</a>
    </nav>
    <button class="burger" id="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>
<main id="main">
{body}
</main>
{FOOTER}
<script src="script.js" defer></script>
</body>
</html>
"""


FOOTER = f"""<footer class="footer">
  <div class="wrap">
    <div class="footer__cols">
      <div>
        <h4>Carpintería de Aluminio Vigar S.L.</h4>
        <p>Fabricación e instalación de carpintería de aluminio, PVC y metálica en la Comunidad de Madrid. Instaladores oficiales Cortizo.</p>
      </div>
      <div>
        <h4>Tienda</h4>
        <p>Calle Zigia, 20 – Local<br>28027 Madrid<br><a href="tel:+34913772909">91 377 29 09</a></p>
      </div>
      <div>
        <h4>Fábrica</h4>
        <p>C/ Escayolistas, 10 – Nave 10<br>28891 Velilla de San Antonio<br><a href="tel:+34916551830">91 655 18 30</a></p>
      </div>
      <div>
        <h4>Páginas</h4>
        <ul><li><a href="productos.html">Productos</a></li><li><a href="trabajos.html">Trabajos</a></li><li><a href="empresa.html">Empresa</a></li><li><a href="contacto.html">Contacto</a></li><li><a href="https://www.facebook.com/VIGARSL" target="_blank" rel="noopener">Facebook</a></li></ul>
      </div>
    </div>
    <svg class="biglogo" viewBox="0 0 1000 250" role="img" aria-label="Vigar">
      <rect x="0" y="10" width="230" height="230" rx="56" fill="#0f1733"/>
      <rect x="46" y="56" width="62" height="138" rx="14" fill="#eef1f6"/>
      <rect x="122" y="56" width="62" height="138" rx="14" fill="#e8262c"/>
      <text x="262" y="208" font-family="Geist, system-ui, sans-serif" font-size="250" font-weight="500" letter-spacing="-16" fill="#0f1733" textLength="738" lengthAdjust="spacingAndGlyphs">vigar</text>
    </svg>
    <div class="footer__legal">
      <span>© <span data-year>2026</span> Carpintería de Aluminio Vigar S.L.</span>
      <span><a href="aviso-legal.html">Aviso legal</a> · <a href="privacidad.html">Privacidad</a> · <a href="mailto:info@vigarsl.com">info@vigarsl.com</a></span>
    </div>
  </div>
</footer>"""

JSONLD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Carpintería de Aluminio Vigar S.L.",
"url":"https://www.carpinteriaaluminiovigar.com/","telephone":"+34913772909","email":"info@vigarsl.com",
"image":"https://www.carpinteriaaluminiovigar.com/img/gen/interior.jpg",
"address":{"@type":"PostalAddress","streetAddress":"Calle Zigia, 20 - Local","postalCode":"28027","addressLocality":"Madrid","addressCountry":"ES"},
"areaServed":"Comunidad de Madrid","sameAs":["https://www.facebook.com/VIGARSL"]}
</script>"""

# ---------------------------------------------------------------- INICIO
PRODUCTS = [
    ("r-corredera", "Ventanas correderas", "No ocupan espacio al abrir", "productos.html#ventanas"),
    ("r-oscilo", "Oscilobatientes", "Con rotura de puente térmico", "productos.html#ventanas"),
    ("r-puerta", "Puertas", "De entrada, seguridad y plegables", "productos.html#puertas"),
    ("r-mallorquina", "Mallorquinas", "Celosías sin mantenimiento", "productos.html#mallorquinas"),
    ("r-mampara", "Mamparas", "Baño y ducha a medida", "productos.html#cristal"),
    ("r-pergola", "Pérgolas y techos", "Cerramientos para terrazas", "productos.html#cerramientos"),
]


def prod_cards():
    return "".join(f"""
      <a class="prod rv" href="{href}">
        <img src="img/gen/{img}.jpg" alt="Render 3D de {name.lower()}" loading="lazy" width="800" height="800">
        <div class="prod__body"><div><h3>{name}</h3><p>{sub}</p></div>{GO}</div>
      </a>""" for img, name, sub, href in PRODUCTS)


INDEX = f"""
<section class="hero hero--bg">
  <div class="hero__bg" aria-hidden="true"><img src="img/gen/portada.jpg" alt="" fetchpriority="high" width="2800" height="1200"></div>
  <div class="wrap hero__inner">
    <div class="hero__copy">
      <h1>Ventanas que se abren <span class="tone">a lo que importa.</span></h1>
      <p class="lead">Fabricamos e instalamos carpintería de aluminio a medida en Madrid. Más luz, menos ruido y menos gasto en calefacción.</p>
      <div class="hero__ctas">
        <a href="contacto.html" class="btn">Pedir presupuesto {ARR}</a>
        <a href="productos.html" class="btn btn--light btn--plain">Ver productos</a>
      </div>
      <ul class="hero__trust"><li>Presupuesto gratis</li><li>Medimos a domicilio</li><li>Trabajos garantizados</li></ul>
    </div>
    <div class="hero__floats" aria-hidden="true">
      <div class="float float--years"><b>+30</b><span>años fabricando<br>en Madrid</span></div>
      <div class="float float--cortizo"><img src="img/marcas/cortizo.png" alt="" width="175" height="160"><span><b>Distribuidores oficiales</b>Sistemas Cortizo</span></div>
    </div>
  </div>
</section>

<section class="brands" aria-label="Marcas con las que trabajamos">
  <div class="wrap">
    <p class="brands__title">Trabajamos con fabricantes de primera línea</p>
    <ul class="brands__grid">
      <li class="sq"><img src="img/marcas/cortizo.png" alt="Cortizo" loading="lazy"></li><li><img src="img/marcas/schuco.png" alt="Schüco" loading="lazy"></li><li><img src="img/marcas/deceuninck.png" alt="Deceuninck" loading="lazy"></li><li><img src="img/marcas/velux.png" alt="Velux" loading="lazy"></li><li class="sq"><img src="img/marcas/climalit.png" alt="Climalit" loading="lazy"></li><li><img src="img/marcas/guardian.png" alt="Guardian Sun" loading="lazy"></li><li><img src="img/marcas/somfy.png" alt="Somfy" loading="lazy"></li><li><img src="img/marcas/simon.png" alt="Simon" loading="lazy"></li><li><img src="img/marcas/besam.png" alt="Besam" loading="lazy"></li><li><img src="img/marcas/persycom.png" alt="Persycom" loading="lazy"></li><li class="sq"><img src="img/marcas/sumum.png" alt="Sumum" loading="lazy"></li><li class="sq"><img src="img/marcas/ayuso.png" alt="Grupo Ayuso" loading="lazy"></li>
    </ul>
  </div>
</section>

<section class="section glass-sec" id="servicios">
  <div class="photo-bg fade-y photo-low" aria-hidden="true"><img src="img/gen/fachada.jpg" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="head rv">
      <h2>Del primer mensaje <span class="tone">a la ventana puesta.</span></h2>
      <p>Lo hacemos todo nosotros: medimos, presupuestamos, fabricamos en nuestro taller e instalamos.</p>
    </div>
    <div class="glass-grid">
      <article class="glass glass--light rv">
        <h3>Nos cuentas qué necesitas</h3>
        <p>Por teléfono, por email o en nuestra tienda de la calle Zigia. Te respondemos lo antes posible.</p>
        <div class="ill mform" aria-hidden="true">
          <div class="mform__f"><small>Qué necesitas</small><span>Cambiar 3 ventanas de aluminio</span></div>
          <div class="mform__f"><small>Localidad</small><span>Madrid</span></div>
          <div class="mform__b">Pedir presupuesto</div>
        </div>
      </article>
      <article class="glass glass--dark rv">
        <h3>Medimos en tu casa</h3>
        <p>Vamos a tomar medidas, te enseñamos muestras y te aconsejamos sin compromiso.</p>
        <div class="ill" aria-hidden="true">
          <div class="cal">
            <span class="h">L</span><span class="h">M</span><span class="h">X</span><span class="h">J</span><span class="h">V</span><span class="h">S</span><span class="h">D</span>
            <span>3</span><span class="busy">4</span><span>5</span><span class="on">6</span><span>7</span><span>8</span><span>9</span>
            <span class="busy">10</span><span>11</span><span>12</span><span>13</span><span class="busy">14</span><span>15</span><span>16</span>
          </div>
          <div class="cal-foot"><span>Visita de medición</span><b>Jue 6 · 10:00</b></div>
        </div>
      </article>
      <article class="glass glass--light rv">
        <h3>Presupuesto claro</h3>
        <p>Gratis y detallado, partida por partida. Sabes lo que pagas antes de empezar.</p>
        <div class="ill quote" aria-hidden="true">
          <div class="quote__row"><span>Ventana corredera RPT</span><span>×3</span></div>
          <div class="quote__row"><span>Vidrio bajo emisivo</span><span>✓</span></div>
          <div class="quote__row"><span>Instalación</span><span>✓</span></div>
          <div class="quote__total"><span>Presupuesto</span><span>Gratis</span></div>
        </div>
      </article>
      <article class="glass glass--dark glass--wide rv">
        <h3>Ahorras en calefacción y aire acondicionado</h3>
        <p>Un buen cerramiento garantiza un ahorro en calefacción en invierno y de aire acondicionado en verano.</p>
        <div class="ill seasons" aria-hidden="true">
          <div class="season"><b>Invierno</b><span>Menos gasto en calefacción</span></div>
          <div class="season"><b>Verano</b><span>Menos gasto en aire acondicionado</span></div>
          <div class="season"><b>Todo el año</b><span>Aislamiento térmico y acústico</span></div>
        </div>
      </article>
      <article class="glass glass--light rv">
        <h3>Fabricación propia</h3>
        <p>Lo fabricamos en nuestro taller, adaptado a las medidas de cada cliente.</p>
        <div class="ill track" aria-hidden="true">
          <div class="track__step done"><span>Medición</span><small></small></div>
          <div class="track__step done"><span>Presupuesto</span><small></small></div>
          <div class="track__step now"><span>Fabricación en taller</span><small></small></div>
          <div class="track__step"><span>Instalación</span><small></small></div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section" id="catalogo">
  <div class="wrap">
    <div class="head rv">
      <h2>Lo que fabricamos <span class="tone">a tu medida.</span></h2>
      <p>Aluminio con y sin rotura de puente térmico, PVC, cristal y metal. Cualquier color lacado o efecto madera.</p>
    </div>
    <div class="catalog">{prod_cards()}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="figures rv">
      <div class="fig"><strong>+30<em> años</em></strong><span>trabajando el aluminio en Madrid</span></div>
      <div class="fig"><strong>2<em> sedes</em></strong><span>tienda en Madrid y fábrica propia en Velilla de San Antonio</span></div>
      <div class="fig"><strong>100<em>%</em></strong><span>de los trabajos hechos a medida y garantizados</span></div>
    </div>
  </div>
</section>

<section class="dark-sec on-dark has-right" id="proceso">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/taller.jpg" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="head rv">
      <h2>Así trabajamos, <span class="tone">paso a paso.</span></h2>
      <p>Cuatro pasos, sin sorpresas. Pulsa cualquiera para verlo.</p>
    </div>
    <div class="process" id="process">
      <ol class="steps">
        <li class="step is-on" data-i="0"><h3><b>01</b>Nos escribes o llamas</h3><p>Por teléfono, por email o en la tienda de la calle Zigia. Nos cuentas qué necesitas.</p><i class="prog"></i></li>
        <li class="step" data-i="1"><h3><b>02</b>Medimos en tu casa</h3><p>Tomamos medidas exactas y te aconsejamos el material y la apertura que mejor encajan.</p><i class="prog"></i></li>
        <li class="step" data-i="2"><h3><b>03</b>Fabricamos en nuestro taller</h3><p>Cortamos, ensamblamos y acristalamos en Velilla de San Antonio. Control total de calidad.</p><i class="prog"></i></li>
        <li class="step" data-i="3"><h3><b>04</b>Instalamos y revisamos</h3><p>Instalamos con nuestro equipo y te damos servicio postventa. Todos los trabajos están garantizados.</p><i class="prog"></i></li>
      </ol>
      <div class="screen" aria-live="polite">
        <div class="screen__bar"><i></i><i></i><i></i><span>Vigar</span></div>
        <div class="scene is-on">
          <h4>Nueva solicitud</h4>
          <div class="card-s jobs jobs--plain">
            <div class="job"><span>Ventanas de aluminio</span><small>Qué necesita</small></div>
            <div class="job"><span>Madrid</span><small>Localidad</small></div>
            <div class="job"><span>Por teléfono</span><small>Cómo prefiere que le contactemos</small></div>
          </div>
          <div class="row"><span class="pill">Presupuesto gratis</span><span class="pill pill--lime">Sin compromiso</span></div>
        </div>
        <div class="scene">
          <h4>Toma de medidas</h4>
          <div class="measure"><div class="measure__win"><span class="measure__w">1.480 mm</span><span class="measure__h">1.220 mm</span></div></div>
          <div class="card-s row"><span>Corredera 2 hojas · RPT · Antracita</span><span class="pill pill--lime">Medido</span></div>
        </div>
        <div class="scene">
          <h4>En fábrica</h4>
          <div class="card-s jobs">
            <div class="job"><span>Corte de perfiles a medida</span><small>Perfil RPT · antracita</small></div>
            <div class="job"><span>Ensamblado y herrajes</span><small>Escuadras, juntas y cierres</small></div>
            <div class="job"><span>Acristalado</span><small>Vidrio bajo emisivo 4/16/4</small></div>
            <div class="job"><span>Control de calidad</span><small>Medidas, cierre y estanqueidad</small></div>
          </div>
          <div class="row"><span class="pill">Taller propio</span><span class="pill pill--lime">Listo para instalar</span></div>
        </div>
        <div class="scene">
          <h4>Instalación terminada</h4>
          <div class="card-s track">
            <div class="track__step done"><span>Montaje con nuestro equipo</span><small>✓</small></div>
            <div class="track__step done"><span>Comprobación de cierre y estanqueidad</span><small>✓</small></div>
            <div class="track__step done"><span>Servicio postventa</span><small>✓</small></div>
          </div>
          <div class="row"><span class="pill">Trabajo garantizado</span><span class="pill pill--lime">¡Listo!</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="gamas">
  <div class="wrap">
    <div class="head rv">
      <h2>¿Qué ventana <span class="tone">te conviene?</span></h2>
      <p>Tres opciones para tus ventanas. En la visita te enseñamos el material y te orientamos sobre la que mejor encaja.</p>
    </div>
    <div class="compare">
      <div class="plan rv">
        <h3>Aluminio sin RPT</h3>
        <div class="big">Esencial</div>
        <p class="sub">Aluminio para puertas y ventanas, fabricado en nuestro taller.</p>
        <ul><li>Versátil, ligera y resistente</li><li>Correderas, practicables y oscilobatientes</li><li>Lacada en cualquier color</li><li>Bicolor o efecto madera</li><li>Fabricada a medida</li></ul>
        <a href="contacto.html" class="btn btn--light btn--plain">Consultar</a>
      </div>
      <div class="plan plan--hi rv">
        <span class="tab">Distribuidor oficial</span>
        <h3>Aluminio con RPT · Cortizo</h3>
        <div class="big">Confort</div>
        <p class="sub">Sistemas Cortizo, de los que somos distribuidores e instaladores oficiales.</p>
        <ul><li>Rotura de puente térmico</li><li>Aislamiento térmico y acústico</li><li>Ahorro en calefacción y aire</li><li>Lacado, anodizado o efecto madera</li><li>Vidrio bajo emisivo disponible</li></ul>
        <a href="contacto.html" class="btn btn--lime">Pedir presupuesto {ARR}</a>
      </div>
      <div class="plan rv">
        <h3>PVC</h3>
        <div class="big">Aislante</div>
        <p class="sub">Puertas y ventanas de PVC de todo tipo y colores.</p>
        <ul><li>Altos valores de aislamiento térmico y acústico</li><li>Alternativa ecológicamente responsable</li><li>Hoja con visel, sin vierteaguas adicional</li><li>Efecto madera</li><li>Fabricada a medida</li></ul>
        <a href="contacto.html" class="btn btn--light btn--plain">Consultar</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="trabajos" style="padding-top:0">
  <div class="wrap">
    <div class="head rv">
      <h2>Trabajos reales, <span class="tone">en Madrid.</span></h2>
      <p>Fotos de obras terminadas por nuestro equipo. <a href="trabajos.html">Ver todos los trabajos →</a></p>
    </div>
    <div class="bento rv">
      <a class="w2 h2" href="trabajos.html"><img src="img/trabajos/n19.jpg" alt="Cerramiento con ventanas de medio punto" loading="lazy"><figcaption>Cerramiento con medio punto</figcaption></a>
      <a href="trabajos.html"><img src="img/trabajos/jun21-g-techo-cristal-6.jpg" alt="Techo de cristal" loading="lazy"><figcaption>Techo de cristal</figcaption></a>
      <a class="h2" href="trabajos.html"><img src="img/trabajos/n7.jpg" alt="Mampara de ducha" loading="lazy"><figcaption>Mampara a medida</figcaption></a>
      <a href="trabajos.html"><img src="img/trabajos/n2.jpg" alt="Ventana triangular" loading="lazy"><figcaption>Ventana triangular</figcaption></a>
    </div>
  </div>
</section>

<section class="final has-right" id="cta">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/terraza.jpg" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="final__box rv">
      <h2>¿Hablamos de <span class="mark">tus ventanas?</span></h2>
      <p class="lead">Presupuesto gratis y sin compromiso. Vamos a medir a domicilio en toda la Comunidad de Madrid.</p>
      <div class="btns">
        <a href="contacto.html" class="btn">Pedir presupuesto {ARR}</a>
        <a href="tel:+34913772909" class="btn btn--light btn--plain">91 377 29 09</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- PRODUCTOS
def pdetail(id_, img, title, tone, text, chips):
    ch = "".join(f"<li>{c}</li>" for c in chips)
    return f"""
  <article class="pdetail rv" id="{id_}">
    <div class="pdetail__img"><img src="img/gen/{img}.jpg" alt="Render de {title.lower()}" loading="lazy" width="800" height="800"></div>
    <div>
      <h2>{title} <span class="tone">{tone}</span></h2>
      <p class="lead">{text}</p>
      <p class="opts__t">Opciones disponibles</p>
      <ul class="opts">{ch}</ul>
    </div>
  </article>"""


PRODUCTOS = f"""
<section class="page-hero has-right">
  <div class="photo-bg photo-right photo-window" aria-hidden="true"><img src="img/gen/terraza.jpg" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> / Productos</p>
    <h1>Productos de aluminio, PVC y cristal <span class="tone">hechos a medida.</span></h1>
    <p class="lead">Fabricamos en nuestro taller y somos distribuidores oficiales de Cortizo Sistemas.</p>
  </div>
</section>
<section class="section" style="padding-top:20px">
  <div class="wrap">
  {pdetail("ventanas", "r-corredera", "Ventanas de aluminio", "y PVC.", "Correderas, practicables, oscilobatientes, plegables y elevables. Con o sin rotura de puente térmico, bicolor o mixtas madera/aluminio. También ventanas con forma: medio punto, triangulares y ojos de buey.", ["Rotura de puente térmico", "Canal europeo y canal 16", "Lacado en cualquier color", "Efecto madera", "Velux"])}
  {pdetail("puertas", "r-puerta", "Puertas, rejas", "y cierres.", "Puertas de aluminio de fabricación propia, puertas de seguridad para edificios y puertas plegables de hasta siete hojas para grandes huecos. Rejas fijas y correderas y cierres metálicos enrollables, ciegos, de chapa perforada o de tijera.", ["Puertas de seguridad", "Plegables", "Rejas correderas", "Cierres enrollables", "Motorización"])}
  {pdetail("mallorquinas", "r-mallorquina", "Mallorquinas", "y persianas.", "Persiana mallorquina de aluminio de gran duración y sin mantenimiento, en cualquier color o efecto madera. Persianas de seguridad autoblocantes, motorización de persianas y venta de mecanismos para estores y paneles japoneses.", ["Lamas orientables", "Celosías", "Autoblocantes", "Motorizadas"])}
  {pdetail("cristal", "r-mampara", "Cristalería", "y mamparas.", "Mamparas de baño y ducha a medida de 8 y 10 mm, adaptadas también a movilidad reducida. Doble acristalamiento Climalit, vidrios bajo emisivos y de seguridad, espejos y divisiones de oficina en vidrio templado.", ["Climalit", "Bajo emisivo", "Templado y laminado", "Mamparas a medida", "Divisiones de oficina"])}
  {pdetail("cerramientos", "r-pergola", "Techos, pérgolas", "y cerramientos.", "Techos móviles y fijos para patios, terrazas y áticos, cristal pisable, fachadas de muro cortina, escaparates, toldos y pérgolas manuales o motorizados con sensor de viento, lluvia y sol.", ["Techos móviles", "Cristal pisable", "Muro cortina", "Toldos y pérgolas", "Escaparates"])}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Y para completar la obra, <span class="tone">también.</span></h2><p>Ofrecemos un servicio integral, desde el asesoramiento inicial hasta la instalación final.</p></div>
    <div class="more rv">
      <article class="more__c"><img src="img/trabajos/armarios-1.jpg" alt="Armario empotrado a medida" loading="lazy"><div class="more__g more__g--light"><h3>Armarios a medida</h3><p>Frentes e interiores, con o sin obra. Madera, lacados, lama mallorquina y espejo.</p></div></article>
      <article class="more__c"><img src="img/gen/mosquitera.jpg" alt="Mosquitera enrollable en ventana de aluminio" loading="lazy"><div class="more__g more__g--dark"><h3>Mosquiteras</h3><p>Enrollables, correderas, plisadas y fijas, a la medida de tu ventana.</p></div></article>
      <article class="more__c"><img src="img/trabajos/jun21-g-reja-corredera-5.jpg" alt="Reja corredera metálica" loading="lazy"><div class="more__g more__g--light"><h3>Cerrajería metálica</h3><p>Rejas, barandillas y puertas en hierro y aluminio, hechas a medida.</p></div></article>
      <article class="more__c"><img src="img/trabajos/reformas-1.jpg" alt="Cocina reformada" loading="lazy"><div class="more__g more__g--dark"><h3>Reformas integrales</h3><p>Albañilería, fontanería, electricidad, calefacción, tarima y cocinas.</p></div></article>
    </div>
  </div>
</section>
<section class="final has-right">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/terraza.jpg" alt="" loading="lazy"></div>
  <div class="wrap"><div class="final__box rv">
    <h2>¿No sabes qué elegir? <span class="mark">Te asesoramos.</span></h2>
    <p class="lead">En la visita te enseñamos muestras y te recomendamos lo que mejor encaja con tu casa y tu presupuesto.</p>
    <div class="btns"><a href="contacto.html" class="btn">Pedir visita {ARR}</a></div>
  </div></div>
</section>
"""

# ---------------------------------------------------------------- TRABAJOS
WORKS = [
    ("n19", "ventanas", "Cerramiento con medio punto"), ("n2", "ventanas", "Ventana triangular"),
    ("jun21-g-techo-cristal-6", "cerramientos", "Techo de cristal"), ("n7", "interior", "Mampara de ducha"),
    ("n14", "ventanas", "Ventanas con arco"), ("jun21-g-reja-corredera-5", "puertas", "Reja corredera"),
    ("n20", "ventanas", "Ventanas en fachada"), ("n10", "ventanas", "Ventana de medio punto"),
    ("jun21-g-puerta-ojo-buey-4", "puertas", "Puerta con ojo de buey"), ("n13", "cerramientos", "Cerramiento de piscina"),
    ("n21", "ventanas", "Cerramiento de balcones"), ("n6", "interior", "Mampara de 8 mm"),
    ("jun21-g-escaparate-2", "cerramientos", "Escaparate"), ("n1", "ventanas", "Ojo de buey"),
    ("n22", "ventanas", "Puerta-ventana con arco"), ("n8", "cerramientos", "Fachada con ventanales"),
    ("armarios-1", "interior", "Armario empotrado"), ("n17", "interior", "Mampara de ducha"),
    ("n25", "cerramientos", "Cerramiento de terraza"), ("n12", "cerramientos", "Fachada comercial"),
    ("jun21-g-ojo-buey-3", "ventanas", "Ojos de buey"), ("n18", "ventanas", "Balconera efecto madera"),
    ("n9", "cerramientos", "Suelo de cristal pisable"), ("n16", "cerramientos", "Divisiones de oficina"),
    ("n24", "cerramientos", "Cerramiento de terraza"), ("n15", "ventanas", "Ventanas con arco"),
    ("jun21-g-armario-zapatero-1", "interior", "Armario zapatero"), ("n3", "ventanas", "Vivienda unifamiliar"),
    ("n28", "cerramientos", "Cerramiento de piscina"), ("n11", "puertas", "Puerta de trastero"),
    ("n26", "puertas", "Puerta de aluminio"), ("reformas-1", "interior", "Reforma de cocina"),
    ("n4", "ventanas", "Balconera"), ("n5", "ventanas", "Ventana con reja"),
    ("n23", "interior", "Mampara"), ("reformas-2", "interior", "Reforma integral"),
    ("toldos-y-pergolas-1", "cerramientos", "Toldo en terraza"), ("tiendayfabrica-1", "puertas", "Puerta en exposición"),
]


def gallery():
    return "".join(f'<a href="img/trabajos/{f}.jpg" data-cat="{c}" data-cap="{t}"><img src="img/trabajos/{f}.jpg" alt="{t} instalado por Vigar en Madrid" loading="lazy"></a>' for f, c, t in WORKS)


TRABAJOS = f"""
<section class="page-hero has-right">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/fachada.jpg" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> / Trabajos</p>
    <h1>Trabajos terminados <span class="tone">en Madrid.</span></h1>
    <p class="lead">Fotos reales de nuestras obras: ventanas, puertas, cerramientos, mamparas y reformas.</p>
  </div>
</section>
<section class="section" style="padding-top:20px">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filtrar trabajos">
      <button class="is-on" data-f="all">Todos</button><button data-f="ventanas">Ventanas</button><button data-f="puertas">Puertas y rejas</button><button data-f="cerramientos">Cerramientos y techos</button><button data-f="interior">Baños, armarios y reformas</button>
    </div>
    <div class="gallery" id="gallery">{gallery()}</div>
  </div>
</section>
<div class="lightbox" id="lightbox" hidden>
  <button class="lb-btn lb-close" aria-label="Cerrar">×</button>
  <button class="lb-btn lb-prev" aria-label="Anterior">‹</button>
  <img alt=""><p></p>
  <button class="lb-btn lb-next" aria-label="Siguiente">›</button>
</div>
<section class="final has-right">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/terraza.jpg" alt="" loading="lazy"></div>
  <div class="wrap"><div class="final__box rv">
    <h2>¿El siguiente <span class="mark">es el tuyo?</span></h2>
    <div class="btns"><a href="contacto.html" class="btn">Pedir presupuesto {ARR}</a></div>
  </div></div>
</section>
"""

# ---------------------------------------------------------------- EMPRESA
EMPRESA = f"""
<section class="page-hero has-right">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/fachada.jpg" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> / Empresa</p>
    <h1>Más de 30 años <span class="tone">trabajando el aluminio.</span></h1>
    <p class="lead">Somos una empresa de Madrid con tienda, exposición y fábrica propia. Trabajamos para particulares, negocios, locales comerciales y empresas de reformas.</p>
  </div>
</section>
<section class="section" style="padding-top:30px">
  <div class="wrap">
    <div class="head rv"><h2>Nuestra <span class="tone">historia.</span></h2><p>De un taller de carpintería metálica a fabricar e instalar para toda la Comunidad de Madrid.</p></div>
    <ol class="timeline rv">
      <li><span class="y">Los inicios</span><div><h3>Más de 30 años en el oficio</h3><p>Experiencia acumulada en el sector del aluminio y la carpintería metálica en Madrid.</p></div></li>
      <li><span class="y">La empresa</span><div><h3>Nace Vigar S.L.</h3><p>Nos constituimos como empresa para dar un servicio completo: asesoramiento, fabricación e instalación.</p></div></li>
      <li><span class="y">La tienda</span><div><h3>Tienda y exposición en Calle Zigia</h3><p>En nuestra tienda de Madrid te mostramos materiales y acabados y resolvemos tus dudas.</p></div></li>
      <li><span class="y">Cortizo</span><div><h3>Distribuidores oficiales de Cortizo</h3><p>Cortizo Sistemas confía en nosotros como distribuidores e instaladores de su gama de aluminio y PVC.</p></div></li>
      <li><span class="y">Hoy</span><div><h3>Fábrica propia y reformas integrales</h3><p>Fabricamos a medida en Velilla de San Antonio y coordinamos reformas completas: albañilería, fontanería, electricidad y cocinas.</p></div></li>
    </ol>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap split">
    <div class="rv"><img src="img/trabajos/tiendayfabrica-3.jpg" alt="Tienda y exposición de Vigar en Madrid" loading="lazy"></div>
    <div class="rv">
      <h2>Fabricación propia, <span class="tone">control total.</span></h2>
      <p class="lead" style="margin-top:18px">Tener taller propio nos permite adaptar cada ventana a la medida exacta del hueco y ofrecer una postventa de verdad, porque conocemos cada pieza que instalamos.</p>
      <ul class="ticks"><li>Ventanas correderas, contraventanas y correderas plegables</li><li>Rejas y cerrajería a medida</li><li>Todos los trabajos garantizados</li></ul>
      <a href="contacto.html" class="btn">Visítanos {ARR}</a>
    </div>
  </div>
</section>
<section class="final has-right">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/terraza.jpg" alt="" loading="lazy"></div>
  <div class="wrap"><div class="final__box rv">
    <h2>Ven a vernos a <span class="mark">la tienda.</span></h2>
    <p class="lead">Calle Zigia, 20 · 28027 Madrid</p>
    <div class="btns"><a href="contacto.html" class="btn">Cómo llegar {ARR}</a></div>
  </div></div>
</section>
"""

# ---------------------------------------------------------------- CONTACTO
CONTACTO = f"""
<section class="page-hero has-right" style="min-height:auto;padding-bottom:40px">
  <div class="photo-bg photo-right" aria-hidden="true"><img src="img/gen/vista.jpg" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> / Contacto</p>
    <h1>Cuéntanos qué necesitas <span class="tone">y te ayudamos.</span></h1>
  </div>
</section>
<section class="section" style="padding-top:30px">
  <div class="wrap contact">
    <div class="cdata">
      <div class="cbox cbox--dark"><h3>Llámanos o escríbenos</h3><p><a href="tel:+34913772909">91 377 29 09</a> · <a href="tel:+34607437106">607 43 71 06</a><br><a href="mailto:info@vigarsl.com">info@vigarsl.com</a></p></div>
      <div class="cbox"><h3>Tienda y exposición</h3><p>Calle Zigia, 20 – Local · 28027 Madrid<br><a href="https://www.google.com/maps/search/?api=1&query=Calle+Zigia+20+28027+Madrid" target="_blank" rel="noopener">Cómo llegar →</a></p></div>
      <div class="cbox"><h3>Fábrica</h3><p>C/ Escayolistas, 10 – Nave 10, Pol. El Magdaleno<br>28891 Velilla de San Antonio · <a href="tel:+34916551830">91 655 18 30</a><br><a href="https://www.google.com/maps/search/?api=1&query=Calle+Escayolistas+10+Velilla+de+San+Antonio" target="_blank" rel="noopener">Cómo llegar →</a></p></div>
    </div>
    <form class="form" id="form" novalidate>
      <h2>Pide tu <span class="tone">presupuesto.</span></h2>
      <label>Nombre<input name="nombre" required autocomplete="name"></label>
      <label>Teléfono<input name="telefono" type="tel" required autocomplete="tel"></label>
      <label>Localidad<input name="localidad" placeholder="Madrid, Coslada, Rivas…" autocomplete="address-level2"></label>
      <label>¿Qué te interesa?
        <select name="tipo"><option>Ventanas de aluminio</option><option>Ventanas de PVC</option><option>Puertas, rejas o cierres</option><option>Mallorquinas o persianas</option><option>Cerramiento, techo o pérgola</option><option>Mampara o cristalería</option><option>Armarios</option><option>Reforma integral</option><option>Otro</option></select>
      </label>
      <label class="full">Mensaje<textarea name="mensaje" rows="4" placeholder="Número de ventanas, medidas aproximadas, plazos…"></textarea></label>
      <label class="check full"><input type="checkbox" name="ok" required> He leído y acepto la <a href="privacidad.html">política de privacidad</a>.</label>
      <div class="form__btns">
        <button class="btn" type="submit" data-via="mail">Enviar por email {ARR}</button>
      </div>
      <p class="form__err" id="formErr" role="alert"></p>
    </form>
  </div>
</section>
<section class="section glass-sec">
  <div class="photo-bg fade-y" aria-hidden="true"><img src="img/gen/taller.jpg" alt="" loading="lazy"></div>
  <div class="wrap">
    <div class="head on-dark rv"><h2>Qué pasa después <span class="tone">de escribirnos.</span></h2><p>Presupuesto gratis y sin compromiso.</p></div>
    <ol class="after rv">
      <li><strong>1</strong><h3>Te respondemos</h3><p>Lo antes posible, por teléfono o por email.</p></li>
      <li><strong>2</strong><h3>Vamos a medir</h3><p>Quedamos contigo para tomar medidas y enseñarte muestras.</p></li>
      <li><strong>3</strong><h3>Recibes el presupuesto</h3><p>Detallado y gratis. Tú decides con calma.</p></li>
    </ol>
  </div>
</section>
"""

# ---------------------------------------------------------------- LEGAL
def legal(title, html):
    return f"""
<section class="page-hero" style="min-height:auto;padding-bottom:30px"><div class="wrap"><p class="crumbs"><a href="index.html">Inicio</a> / {title}</p><h1>{title}</h1></div></section>
<section class="section" style="padding-top:20px"><div class="wrap legal">{html}</div></section>"""


PRIV = legal("Política de privacidad", """
<p><strong>Responsable:</strong> Carpintería de Aluminio Vigar S.L. · Calle Zigia, 20 – Local, 28027 Madrid · info@vigarsl.com · 91 377 29 09.</p>
<h2>Qué datos tratamos y para qué</h2>
<p>Los datos que nos facilitas (nombre, teléfono, localidad y mensaje) se usan solo para responder a tu consulta y preparar tu presupuesto. Esta web no guarda los datos del formulario: el formulario abre tu programa de correo para que nos envíes el mensaje directamente.</p>
<h2>Legitimación</h2><p>Tu consentimiento al enviarnos la consulta.</p>
<h2>Conservación</h2><p>Mientras sea necesario para atender tu solicitud y durante los plazos legales aplicables.</p>
<h2>Tus derechos</h2><p>Puedes acceder, rectificar o suprimir tus datos, así como oponerte o limitar su tratamiento, escribiendo a info@vigarsl.com. También puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
<h2>Cookies</h2><p>Esta web no utiliza cookies de seguimiento ni publicidad. Solo se cargan las fuentes tipográficas necesarias para mostrar la página.</p>""")

AVISO = legal("Aviso legal", """
<p><strong>Titular:</strong> Carpintería de Aluminio Vigar S.L.<br><strong>Domicilio:</strong> Calle Zigia, 20 – Local, 28027 Madrid<br><strong>Email:</strong> info@vigarsl.com · <strong>Teléfono:</strong> 91 377 29 09</p>
<h2>Condiciones de uso</h2><p>El acceso a esta web es gratuito e implica la aceptación de estas condiciones. Los contenidos tienen carácter informativo; los precios y características definitivos se indican siempre en el presupuesto personalizado.</p>
<h2>Propiedad intelectual</h2><p>Los textos, fotografías y diseño de esta web pertenecen a Carpintería de Aluminio Vigar S.L. o se usan con autorización. Las marcas citadas pertenecen a sus respectivos titulares.</p>
<h2>Responsabilidad</h2><p>Vigar no se hace responsable del mal uso de los contenidos ni de los daños derivados de interrupciones del servicio ajenas a su control.</p>""")

PAGES = {
    "index.html": ("Carpintería de Aluminio en Madrid · Fábrica propia | Vigar",
                   "Ventanas de aluminio y PVC, puertas, mallorquinas, mamparas y cerramientos a medida en Madrid. Fábrica propia e instaladores oficiales Cortizo. Presupuesto gratis.",
                   INDEX, JSONLD),
    "productos.html": ("Ventanas de aluminio, PVC, puertas y mamparas en Madrid | Vigar",
                       "Ventanas correderas y oscilobatientes con rotura de puente térmico, puertas de seguridad, mallorquinas, mamparas, techos móviles y pérgolas. Fabricación propia en Madrid.",
                       PRODUCTOS, ""),
    "trabajos.html": ("Trabajos de carpintería de aluminio en Madrid | Vigar",
                      "Galería de trabajos reales de Vigar: ventanas de aluminio, cerramientos, techos de cristal, mamparas, puertas y reformas en Madrid.",
                      TRABAJOS, ""),
    "empresa.html": ("Sobre Vigar · Más de 30 años en carpintería de aluminio | Madrid",
                     "Empresa de carpintería de aluminio y metálica en Madrid con tienda en Calle Zigia y fábrica propia en Velilla de San Antonio. Distribuidores oficiales Cortizo.",
                     EMPRESA, ""),
    "contacto.html": ("Contacto y presupuesto · Carpintería de Aluminio Vigar Madrid",
                      "Pide presupuesto gratis para ventanas, puertas, cerramientos o mamparas. Tienda en Calle Zigia 20, Madrid. Tel. 91 377 29 09 · 607 43 71 06.",
                      CONTACTO, ""),
    "privacidad.html": ("Política de privacidad | Vigar", "Política de privacidad de Carpintería de Aluminio Vigar S.L.", PRIV, '<meta name="robots" content="noindex">'),
    "aviso-legal.html": ("Aviso legal | Vigar", "Aviso legal de Carpintería de Aluminio Vigar S.L.", AVISO, '<meta name="robots" content="noindex">'),
}

# Si las imágenes generadas aún no están en img/gen/ (ver src/fetch_images.py),
# se enlazan directamente desde el CDN de Higgsfield para que la web funcione igual.
import re, sys
sys.path.insert(0, str(Path(__file__).parent))
CDN = "https://d8j0ntlcm91z4.cloudfront.net/user_3EVFQGGB0uS6Dss87xRgYs1Fdup/"
GEN = {
 "vista": "hf_20261103_121524_77162703-47b0-4b0b-b8c0-84fc6985fbba.png",
 "fachada": "hf_20261103_121408_2cc4656c-1e90-41c2-96d3-00934950ef6d.png",
 "taller": "hf_20261103_121409_dd332d4c-0fca-4b0f-965a-5e5c49e580a2.png",
 "terraza": "hf_20261103_121407_cb5dd4db-9f4b-453b-b7b4-8e95501d1e7d.png",
 "interior": "hf_20261103_121407_6e40b7ae-5334-4fdf-8781-1cd370b86566.png",
 "portada": "hf_20261103_133027_a204e87b-3413-4ceb-9def-51a6a4312a78.png",
 "mosquitera": "hf_20261103_122642_eaf82400-c699-4b29-af49-542fca5cef3f.png",
 "r-corredera": "hf_20261103_103851_3a438df4-cfcb-4e37-98e2-957f4b90d130.png",
 "r-oscilo": "hf_20261103_103553_11621e1f-5da1-43ef-ae99-75ddffa207ca.png",
 "r-puerta": "hf_20261103_103851_f96a363d-aea3-41fb-b0c2-4cb248231960.png",
 "r-mallorquina": "hf_20261103_103922_d8eef4d0-0f31-4cc0-b013-0b888c70ffc2.png",
 "r-mampara": "hf_20261103_103921_fc507a7e-12d5-46f0-84dc-9d5ebd31f3d0.png",
 "r-pergola": "hf_20261103_103554_3c1e4604-3753-4a78-9978-940aa1b1ff76.png",
}


def resolve(html):
    def sub(m):
        name = m.group(1)
        if (ROOT / "img" / "gen" / f"{name}.jpg").exists():
            return m.group(0)
        return CDN + GEN[name]
    return re.sub(r"img/gen/([a-z-]+)\.jpg", sub, html)


for fname, (title, desc, body, extra) in PAGES.items():
    (ROOT / fname).write_text(resolve(layout(fname, title, desc, body, extra_head=extra)), encoding="utf-8")

urls = "".join(f"<url><loc>{SITE}/{'' if f == 'index.html' else f.replace('.html', '')}</loc></url>" for f in PAGES if f not in ("privacidad.html", "aviso-legal.html"))
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("ok:", ", ".join(PAGES))
