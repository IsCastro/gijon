# De bares por Gijón, y lo que surja 🍎🌊

Guía web para un viaje de amigos a **Gijón**. Una sola página, sin build ni dependencias de servidor: todo vive en `index.html` (HTML + CSS + JS vanilla).

## Qué incluye

- 🗺️ **Mapa interactivo** con filtro por categoría (Restaurantes · Bares · Pubs · Playas · Alojamiento).
  - Usa **Google Maps** si la API está activada; si no, cae automáticamente a **Leaflet** (OpenStreetMap / CARTO oscuro).
  - Capa de **satélite** con imágenes de Esri.
- 📸 **Galería de puntos de interés** (horizontal en PC, rejilla en móvil), enlazada al mapa.
- 🕐 **"¿Qué hay abierto ahora?"** — filtra por la hora real del dispositivo (horarios aproximados).
- ⚽ **Ticker del Mundial 2026** en vivo (datos de [TheSportsDB](https://www.thesportsdb.com/)).
- 🤖 **Asistente en lenguaje natural** que responde sobre los sitios del viaje.
- 👥 **Carruseles animados** con la gente del viaje (fotos en B/N + frase).

## Cómo ejecutarlo

Es estático; sírvelo con cualquier servidor. Por ejemplo, con Python:

```bash
python -m http.server 8055
```

y abre <http://localhost:8055>.

## Estructura

| Ruta | Qué es |
|------|--------|
| `index.html` | Toda la aplicación (HTML + CSS + JS). |
| `img/people/` | Fotos de la gente del viaje (caras recortadas, B/N). |
| `crop.py` | Script (Pillow) para recortar una cara y pasarla a B/N. |

## Notas técnicas

- **Mapa**: el mapa cae a Leaflet automáticamente si Google Maps no consigue pintar (p. ej. con la *Maps JavaScript API* sin activar). Para usar Google de forma nativa hay que habilitar la API + facturación.
- **API key de Google**: la clave incrustada en `index.html` es una *clave de cliente* y queda **pública** en el repositorio. Si haces el repo público, **restríngela por dominio (referrer HTTP)** en Google Cloud Console o elimínala.
- **Horarios** de "abierto ahora": son aproximados. Para datos reales haría falta la *Google Places API*.

---

Hecho a mano para el viaje. 🍻
