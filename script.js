(function () {
  // Año
  document.querySelectorAll('[data-year]').forEach(function (e) { e.textContent = new Date().getFullYear(); });

  // Menú de cristal: estado al hacer scroll y desplegable móvil
  var header = document.getElementById('header');
  var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 20); };
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  var burger = document.getElementById('burger'), nav = document.getElementById('nav');
  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', open);
    burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) { nav.classList.remove('is-open'); burger.setAttribute('aria-expanded', false); } });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { nav.classList.remove('is-open'); burger.setAttribute('aria-expanded', false); } });

  // Revelado al entrar en pantalla
  var els = document.querySelectorAll('.rv, .bars');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
    }, { threshold: .12 });
    els.forEach(function (e) { io.observe(e); });
  } else { els.forEach(function (e) { e.classList.add('in'); }); }

  // Proceso animado: los pasos avanzan solos y la pantalla cambia
  var proc = document.getElementById('process');
  if (proc) {
    var steps = proc.querySelectorAll('.step'), scenes = proc.querySelectorAll('.scene'), cur = 0, timer = null, DUR = 4500;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var show = function (i) {
      cur = i;
      steps.forEach(function (s, k) { s.classList.toggle('is-on', k === i); });
      scenes.forEach(function (s, k) {
        s.classList.toggle('is-on', k === i);
        if (k === i) s.querySelectorAll('.fab__bar i').forEach(function (b) { b.style.animation = 'none'; b.offsetWidth; b.style.animation = ''; });
      });
    };
    var start = function () { stop(); if (!reduce) timer = setInterval(function () { show((cur + 1) % steps.length); }, DUR); };
    var stop = function () { if (timer) clearInterval(timer); timer = null; };
    steps.forEach(function (s, k) { s.addEventListener('click', function () { show(k); start(); }); });
    proc.addEventListener('mouseenter', function () { proc.classList.add('paused'); stop(); });
    proc.addEventListener('mouseleave', function () { proc.classList.remove('paused'); start(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { en[0].isIntersecting ? (show(cur), start()) : stop(); }, { threshold: .3 }).observe(proc);
    }
  }

  // Galería: filtros + visor
  var gal = document.getElementById('gallery');
  if (gal) {
    var links = Array.prototype.slice.call(gal.querySelectorAll('a'));
    document.querySelectorAll('.filters button').forEach(function (b) {
      b.addEventListener('click', function () {
        document.querySelectorAll('.filters button').forEach(function (x) { x.classList.toggle('is-on', x === b); });
        var f = b.dataset.f;
        links.forEach(function (a) { a.hidden = !(f === 'all' || a.dataset.cat === f); });
      });
    });
    var lb = document.getElementById('lightbox'), img = lb.querySelector('img'), cap = lb.querySelector('p'), idx = 0;
    var visible = function () { return links.filter(function (a) { return !a.hidden; }); };
    var open = function (a) { var v = visible(); idx = v.indexOf(a); img.src = a.href; img.alt = a.dataset.cap; cap.textContent = a.dataset.cap; lb.hidden = false; document.body.style.overflow = 'hidden'; lb.querySelector('.lb-close').focus(); };
    var close = function () { lb.hidden = true; document.body.style.overflow = ''; };
    var move = function (d) { var v = visible(); idx = (idx + d + v.length) % v.length; var a = v[idx]; img.src = a.href; img.alt = a.dataset.cap; cap.textContent = a.dataset.cap; };
    links.forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); open(a); }); });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { move(-1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { move(1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') move(-1); if (e.key === 'ArrowRight') move(1);
    });
  }

  // Formulario: abre WhatsApp o email con el mensaje (no guarda datos)
  var form = document.getElementById('form');
  if (form) {
    var via = 'mail';
    form.querySelectorAll('[data-via]').forEach(function (b) { b.addEventListener('click', function () { via = b.dataset.via; }); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form), err = document.getElementById('formErr');
      if (!d.get('nombre') || !d.get('telefono')) { err.textContent = 'Indica tu nombre y un teléfono para poder llamarte.'; return; }
      if (!d.get('ok')) { err.textContent = 'Acepta la política de privacidad para continuar.'; return; }
      err.textContent = '';
      var txt = 'Hola, soy ' + d.get('nombre') + '. Me interesa: ' + d.get('tipo') + '.' +
        (d.get('localidad') ? ' Localidad: ' + d.get('localidad') + '.' : '') +
        ' Teléfono: ' + d.get('telefono') + '.' + (d.get('mensaje') ? ' ' + d.get('mensaje') : '');
      if (via === 'mail') location.href = 'mailto:info@vigarsl.com?subject=' + encodeURIComponent('Presupuesto web: ' + d.get('tipo')) + '&body=' + encodeURIComponent(txt);
      else window.open('https://wa.me/34607437106?text=' + encodeURIComponent(txt), '_blank', 'noopener');
    });
  }
})();
