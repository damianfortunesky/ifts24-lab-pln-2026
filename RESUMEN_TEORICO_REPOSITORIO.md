# Resumen teórico del repositorio

## 1) Propósito general del curso
El repositorio organiza una **introducción aplicada al PLN** combinando tres ejes: fundamentos de programación en Python, extracción de datos textuales desde la web y análisis lingüístico automatizado con herramientas de NLP. La orientación es práctica, pero con un marco conceptual constante: transformar texto crudo en información estructurada para interpretar fenómenos comunicacionales y sociales.

## 2) Fundamentos de Python para PLN
Los cuadernos iniciales presentan Python como lenguaje de trabajo para manipular texto:
- **Variables, tipos y operadores** como base para modelar información lingüística.
- **Condicionales** para decisiones lógicas sobre cadenas de texto.
- **Estructuras de datos** (listas, tuplas, diccionarios, conjuntos) para representar corpus y frecuencias.
- **Funciones** como encapsulación de procedimientos reutilizables.
- **Programación orientada a objetos (POO)** para diseñar procesadores de texto extensibles.

Conceptualmente, esta sección instala la idea de que el análisis de lenguaje requiere primero una buena ingeniería de datos y abstracciones claras.

## 3) Diseño de aplicaciones de análisis
Con Gradio se introduce el puente entre lógica analítica y experiencia de uso:
- Separación entre **núcleo de procesamiento** (funciones/clases) e **interfaz** (inputs/outputs).
- Ciclo de desarrollo incremental: diseñar función, probar, recién luego integrar UI.
- Comunicación de resultados mediante salidas interpretables (métricas y resumen narrativo).

Desde lo teórico, esto refuerza una competencia clave: convertir modelos analíticos en herramientas utilizables por terceros.

## 4) Web scraping como adquisición de corpus
La secuencia de laboratorios de scraping avanza por niveles:
1. **Requests + BeautifulSoup** para parseo de HTML y navegación de etiquetas.
2. **DOM y selectores CSS** para extracción de mayor precisión.
3. **Trafilatura** para extracción heurística de contenido principal (menos “ruido”).
4. **Playwright** para sitios dinámicos con JavaScript y flujos de interacción reales.
5. **Scrapling / estrategias anti-bot** para contextos con protección activa.

Fundamento central: obtener datos web no es sólo “leer etiquetas”, sino resolver un problema sociotécnico que combina red, estructura documental, renderizado dinámico y restricciones de acceso.

## 5) Limpieza, normalización y preparación textual
Antes del análisis, el curso enfatiza la preparación del texto:
- Eliminación de ruido (puntuación irrelevante, artefactos HTML, stopwords).
- Normalización y tokenización para homogeneizar unidades de comparación.
- Iteración sobre reglas de depuración para mejorar la calidad del corpus.

Teóricamente, esta etapa muestra que la validez de los resultados depende más de la calidad del preprocesamiento que de la complejidad visual o algorítmica posterior.

## 6) PLN con spaCy: de texto plano a estructura lingüística
Los cuadernos de spaCy introducen el salto conceptual del conteo superficial al análisis lingüístico:
- **Tokenización**: unidad mínima con valor analítico.
- **Lematización**: reducción a forma base para agrupar variantes.
- **Etiquetado gramatical (POS)**: función sintáctica de cada palabra.
- **Entidades nombradas (NER)**: reconocimiento de personas, lugares, organizaciones, etc.
- **Dependencias y grupos nominales**: relaciones internas de la oración.

Base teórica: el NLP permite representar el lenguaje como capas de anotación, habilitando análisis semánticos y discursivos más robustos.

## 7) Visualización y comunicación analítica
La parte de visualización plantea que analizar también es **comunicar**:
- Selección de gráfico según tipo de variable y pregunta de investigación.
- Principios de diseño (claridad, contraste, reducción de ruido visual).
- Comparación entre representaciones “atractivas” y representaciones “precisas”.

Fundamento: la visualización no es decoración, es una forma de argumentación basada en datos.

## 8) Agenda setting y producción de sentido
La práctica final conecta técnica y teoría de medios:
- Extracción de titulares como huella de priorización editorial.
- Agrupación temática para identificar foco de agenda.
- Redes léxicas para estudiar encuadres y dominancias discursivas.

En términos conceptuales, el repositorio no se limita al “cómo extraer datos”, sino al **para qué interpretarlos** dentro de un marco crítico de comunicación y construcción de sentido.

## 9) Gestión del trabajo reproducible con Git/GitHub
La guía de Git/GitHub incorpora fundamentos metodológicos:
- Trazabilidad de cambios.
- Versionado incremental.
- Organización formal del repositorio y convenciones de trabajo.

Idea teórica transversal: en ciencia de datos y PLN, la reproducibilidad es parte del conocimiento, no sólo una cuestión operativa.

## Conclusión
El recorrido teórico del repositorio propone una cadena completa:
**programar → recolectar → limpiar → analizar lingüísticamente → visualizar → interpretar críticamente → versionar**.

El código aparece como medio. El objetivo de fondo es desarrollar criterio técnico y conceptual para convertir lenguaje en evidencia analizable y socialmente significativa.
