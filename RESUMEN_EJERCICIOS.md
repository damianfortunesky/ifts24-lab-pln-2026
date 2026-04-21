# Resumen del proyecto (guía rápida para hacer los ejercicios)

## 1) Objetivo general de la materia
El repositorio es un **laboratorio práctico de Introducción al PLN, LLMs y Agentic AI**. La lógica del curso es progresiva:
1. base de Python,
2. extracción de texto desde la web,
3. análisis lingüístico con spaCy,
4. y aplicación en mini-proyectos de análisis.

## 2) Qué se vio por bloques

### A. `001_python/` — Base de programación para PLN
- **Clase 1 (`001_Python_para_PLN.ipynb`)**: fundamentos de Python aplicados a texto.
- **Clase 2 (`002_Python_para_PLN.ipynb`)**: funciones, objetos y aplicación práctica en tareas de PLN.
- **Guía integradora (`003_Guia_Ejercicio_Integrador.ipynb`)**: pistas para resolver un ejercicio completo uniendo lo anterior.

**Qué deberías dominar para ejercicios:**
- variables, tipos y estructuras (`list`, `dict`, etc.),
- bucles y condicionales,
- funciones reutilizables,
- manipulación básica de strings,
- enfoque de “pipeline” (entrada de texto -> procesamiento -> salida).

### B. `002_WebScraping/` — Obtención de datos reales
- **`000_Gradio_&_BS.ipynb`**: interfaces simples con Gradio + análisis básico con BeautifulSoup.
- **`001_WEB_Scraping_Parte1.ipynb`**: extracción de textos (ej. Gutenberg) para armar corpus.
- **`002_WebScraping.ipynb`**: navegación del DOM y selectores CSS.
- **`003_trafilatura.ipynb`**: extracción inteligente de contenido + estructuración con pandas.
- **`004_LaNacion_Playwright.ipynb`**: automatización del navegador para sitios dinámicos.
- **`005_GatesNotes_Scrapling.ipynb`**: scraping en escenarios con anti-bot y contenido dinámico.
- **`006_Visualizacion_Datos.ipynb`**: visualización para comunicar hallazgos.
- **`007_Practica_Agenda_Medios.ipynb`**: práctica aplicada (agenda setting / producción de sentido).

**Qué deberías dominar para ejercicios:**
- pedir HTML y parsear,
- elegir selectores robustos,
- limpiar texto y metadatos,
- guardar resultados en DataFrames,
- automatizar cuando el sitio usa JS,
- visualizar resultados para interpretar.

### C. `003_spacy/` — NLP aplicado
- **`001_intro.ipynb`**: por qué una computadora no “entiende” texto crudo y cómo modelarlo.
- **`002_spacy_basico.ipynb`**: tokenización y análisis lingüístico básico.

**Qué deberías dominar para ejercicios:**
- tokenización,
- atributos lingüísticos (lemma, POS, etc.),
- primeras tareas de análisis sobre corpus ya recolectado.

## 3) Herramientas del entorno (lo que probablemente usarás)
Según `requirements.txt`, las librerías centrales son:
- **Datos:** `pandas`, `numpy`
- **Scraping:** `requests`, `beautifulsoup4`, `trafilatura`, `playwright`, `scrapling`
- **PLN:** `nltk`, `spacy`
- **Visualización:** `matplotlib`, `seaborn`, `wordcloud`
- **Apps rápidas:** `gradio`

## 4) Flujo tipo para resolver ejercicios
Usá este esquema como plantilla:
1. **Definir objetivo** (qué pregunta querés responder).
2. **Conseguir datos** (scraping o fuente dada).
3. **Limpiar/normalizar** (texto, fechas, nulos, duplicados).
4. **Estructurar** en `pandas`.
5. **Analizar** (frecuencias, NLP con spaCy, comparaciones).
6. **Visualizar** resultados.
7. **Conclusión**: responder la pregunta inicial con evidencia.

## 5) Checklist rápido antes de entregar
- [ ] ¿El notebook corre de principio a fin sin errores?
- [ ] ¿Las celdas están en orden lógico?
- [ ] ¿Hay limpieza mínima de datos?
- [ ] ¿Mostrás al menos una salida interpretable (tabla o gráfico)?
- [ ] ¿La conclusión responde explícitamente la consigna?
- [ ] ¿Evitaste hardcodear rutas o supuestos frágiles?

## 6) Sugerencia práctica para estudiar
Si querés preparar ejercicios rápido:
1. Repasá primero `001_python/001` y `001_python/002`.
2. Hacé 1 laboratorio corto de scraping (`002_WebScraping/001` o `002`).
3. Sumá `003_spacy/002` para análisis NLP básico.
4. Terminá con `002_WebScraping/007` para integrar técnica + interpretación.

---

Si querés, en un siguiente paso te puedo armar una **guía de resolución por tipo de ejercicio** (ej.: “scraping + limpieza”, “NLP básico”, “visualización y conclusiones”) con plantillas de código reutilizables.
