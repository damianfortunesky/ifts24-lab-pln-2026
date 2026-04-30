# Resumen de la materia + guía de defensa oral del TPI2

## 1) Mapa general de la materia: qué problema resuelve cada bloque

La materia está organizada como una **cadena de producción de evidencia textual**. El objetivo no es “usar herramientas sueltas”, sino aprender a responder preguntas sociales/comunicacionales con método.

Secuencia lógica del repositorio:

1. **Python para PLN (`001_python/`)**: construir pensamiento computacional para manipular texto de forma reproducible.
2. **Adquisición de corpus (`002_adquisicion_corpus/` y `002_WebScraping/`)**: pasar de intuiciones a datos concretos (notas, titulares, transcripciones).
3. **Análisis lingüístico con spaCy (`003_spacy/`)**: convertir texto plano en estructura analítica (lemas, POS, entidades, dependencias).
4. **Integradores y TPIs (`004_tpi_1/`, `006_lab_integrador_guiado/`, `007_tpi_2/`)**: combinar técnicas en un flujo completo y justificar decisiones.
5. **Vectorización (`005_Vectorizacion/`)**: representar el texto numéricamente para comparar discursos.
6. **Representaciones semánticas (`008_representaciones_semanticas/`)**: ampliar la mirada hacia niveles de significado y relaciones.
7. **App operativa (`media_analysis_app/`)**: traducir el método en una herramienta usable (de ingesta a interpretación).

**Idea eje para defender oralmente:** la materia enseña a pasar de “texto como opinión” a “texto como dato interpretable”, sin perder lectura crítica. 【F:README.md†L8-L17】【F:README.md†L95-L103】

---

## 2) Conceptos clave (con el “por qué”)

## A. Programación aplicada al lenguaje
- **Qué se aprende:** estructuras de datos, funciones y modularidad.
- **Para qué sirve:** sin esto no hay pipeline trazable ni reproducible; habría análisis manual y frágil.
- **Fundamento:** en PLN, cada decisión (limpieza, tokenización, filtros) debe poder repetirse exactamente.

## B. Construcción del corpus (web scraping)
- **Qué se aprende:** `requests`, BeautifulSoup, selectores CSS, Trafilatura, Playwright y estrategias para sitios dinámicos/anti-bot.
- **Para qué sirve:** construir el dato primario desde fuentes reales en vez de datasets idealizados.
- **Fundamento:** la calidad de inferencia depende de la calidad de captura (si scrapeás mal, interpretás mal).

## C. Preprocesamiento
- **Qué se aprende:** normalización, limpieza de ruido, tokenización y control de calidad.
- **Para qué sirve:** homogeneizar textos para que las comparaciones sean válidas.
- **Fundamento:** comparar textos con diferente nivel de ruido produce sesgos más fuertes que cualquier mejora algorítmica.

## D. spaCy y estructura lingüística
- **Qué se aprende:** lematización, POS tagging, NER, dependencias.
- **Para qué sirve:** no quedarse sólo en conteos; analizar actores, acciones y marcos enunciativos.
- **Fundamento:** el lenguaje no es bolsa de palabras; tiene estructura gramatical y semántica.

## E. Vectorización y comparación
- **Bag of Words (BoW):** mide presencia/frecuencia. Útil para “de qué se habla”.
- **TF-IDF:** pondera distintividad. Útil para “qué diferencia a un grupo del otro”.
- **Fundamento:** frecuencia ≠ relevancia discursiva; TF-IDF corrige parte de ese problema.

## F. Visualización y argumentación
- **Qué se aprende:** tablas y gráficos legibles para sostener hipótesis.
- **Para qué sirve:** comunicar hallazgos y justificar decisiones metodológicas.
- **Fundamento:** en análisis de discurso con datos, el gráfico no reemplaza la lectura, la orienta.

---

## 3) Qué defender oralmente sobre la materia (guion breve)

1. **Pregunta de investigación**: qué problema discursivo quiero comparar.
2. **Diseño de corpus**: por qué esas fuentes y no otras.
3. **Procesamiento**: cómo pasé de texto crudo a observables.
4. **Comparación**: qué aporta BoW y qué agrega TF-IDF.
5. **Validación cualitativa**: vuelta al fragmento para evitar sobreinterpretaciones.
6. **Límites**: tamaño de corpus, sesgo de fuente, límites del método.

---

## 4) Explicación detallada del TPI2

El TPI2 exige **autonomía metodológica**: ya no se trata de ejecutar pasos mecánicos, sino de justificar un diseño comparativo y sostenerlo con evidencia. 【F:007_tpi_2/TPI_2_Consigna_y_Rubrica.md†L9-L16】

### 4.1 Problema central del TPI2
Comparar **dos grupos de textos** sobre una misma temática para detectar diferencias de agenda, enfoque o encuadre discursivo.

- Puede ser medio vs medio, columnista vs columnista, etc. 【F:007_tpi_2/TPI_2_Consigna_y_Rubrica.md†L18-L31】
- Debe haber 6 a 10 textos, dos grupos y columnas obligatorias de trazabilidad. 【F:007_tpi_2/TPI_2_Consigna_y_Rubrica.md†L33-L46】

### 4.2 Lógica del notebook (paso a paso y por qué)

## Paso 0 — Entregables y criterio de aprobación
El cuaderno abre con qué hay que entregar y qué invalida una resolución superficial.

**Fin metodológico:** alinear técnica con evaluación (evitar “código sin interpretación”). 【F:007_tpi_2/TPI_2_Text_Mining_y_Analisis_Discursivo_Comparado.ipynb†L1-L34】

## Paso 1 — Condiciones del corpus
Define reglas de comparabilidad (tamaño, grupos, temática consistente).

**Por qué:** sin comparabilidad mínima, cualquier diferencia puede deberse al muestreo y no al discurso.

## Paso 2 — Configuración
Variables editables para ruta del corpus y parámetros de análisis.

**Por qué:** separar configuración de lógica permite reproducibilidad y auditoría.

## Paso 3 — Carga y validación de corpus
Chequeo de columnas obligatorias y estructura.

**Por qué:** controlar integridad antes de modelar evita errores silenciosos y conclusiones inválidas.

## Paso 4 — Justificación del recorte
Narrativa del caso elegido (qué se compara y con qué hipótesis inicial).

**Por qué:** todo análisis discursivo necesita marco interpretativo explícito, no sólo métricas.

## Paso 5 — Exploración inicial
Tablas y gráficos de cantidad de documentos/palabras por grupo.

**Por qué:** diagnosticar desbalances de volumen que podrían sesgar frecuencias y TF-IDF.

## Paso 6 — Procesamiento con spaCy
Carga de modelo, normalización de lemas y extracción de información lingüística.

**Por qué:** estandarizar formas y filtrar ruido para comparar contenidos con mayor robustez.

## Paso 7 — Observables iniciales
Términos frecuentes, entidades nombradas y bigramas por grupo.

**Por qué:** producir primeras pistas de marcos discursivos (actores, temas, asociaciones léxicas).

## Paso 8 — BoW vs TF-IDF
Construcción de matrices y visualización de términos distintivos.

**Por qué:** combinar volumen (BoW) y especificidad (TF-IDF) para distinguir centralidad de diferenciación.

## Paso 9 — Del patrón al fragmento
Selección de términos distintivos y extracción de fragmentos de contexto.

**Por qué:** evitar “fetichismo de métricas”; la evidencia final se sostiene en texto concreto.

## Paso 10 — Escritura interpretativa
Conclusiones comparadas + límites del enfoque.

**Por qué:** convertir resultados en argumento defendible, no sólo en dashboard.

## Paso 11 — Checklist final
Control de completitud antes de entrega.

**Por qué:** asegurar cumplimiento técnico y conceptual de rúbrica.

### 4.3 Qué evalúa realmente la rúbrica
La rúbrica pondera: recorte, corrección técnica, calidad visual, interpretación con evidencia y reflexión metodológica. 【F:007_tpi_2/TPI_2_Consigna_y_Rubrica.md†L78-L86】

**Lectura estratégica para oral:** el mayor peso no está sólo en “que corra el notebook”, sino en **explicar por qué los hallazgos son plausibles y qué no permiten afirmar**.

### 4.4 Errores frecuentes (y cómo defenderse)
1. **Listar palabras sin interpretar.**
   - Defensa correcta: conectar términos con hipótesis de encuadre.
2. **Confiar sólo en gráficos.**
   - Defensa correcta: mostrar fragmentos textuales que confirmen/contradigan el patrón.
3. **Corpus desbalanceado o mal definido.**
   - Defensa correcta: justificar límites y explicitar impacto en resultados.
4. **No incluir límites del método.**
   - Defensa correcta: reconocer que BoW/TF-IDF capturan huellas léxicas, no verdad semántica total.

---

## 5) Plantilla breve para defensa oral del TPI2

1. **Pregunta:** “Comparo A vs B sobre X para identificar diferencias de encuadre”.
2. **Corpus:** “Tomé N textos, dos grupos, mismas condiciones temáticas/temporales”.
3. **Método:** “Validé columnas, procesé con spaCy, construí observables, comparé BoW y TF-IDF”.
4. **Hallazgos:** “Grupo A enfatiza…, grupo B enfatiza… (evidencia: términos + entidades + fragmentos)”.
5. **Límites:** “Tamaño y selección de corpus; el método mide patrones léxicos, no intención autoral completa”.
6. **Cierre:** “La comparación es defendible porque combina lectura distante y vuelta al texto”.

