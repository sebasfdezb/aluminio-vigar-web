# Carpintería de Aluminio Vigar · web

Web estática (HTML + CSS + JS, sin dependencias) lista para Vercel.

- `src/build.py` genera las páginas `.html` de la raíz. Para cambiar textos, edita `src/build.py` y ejecuta `python3 src/build.py`.
- `src/fetch_images.py` descarga las imágenes generadas con Higgsfield a `img/gen/`. Si faltan, las páginas las enlazan desde el CDN de Higgsfield.
- `img/trabajos/` contiene fotos reales de trabajos de Vigar.
- `vercel.json` activa URLs limpias (`/productos`) y redirige las URLs de la web antigua.
- `img/gen/portada.jpg` está retocada a mano (pared aclarada para que se lea el texto): no la sobrescribas con `fetch_images.py`.
