# Task 002 — Diseñar pipeline robusto de ingesta y calidad de datos

## Objetivo
Definir prompts para construir el pipeline de captura de noticias/texto web con validaciones de calidad.

## Prompt sugerido
"Sos ingeniero/a de datos. Diseñá un pipeline en Python para recolectar datos textuales desde múltiples fuentes web, aplicando técnicas vistas en clase: requests+BeautifulSoup, trafilatura y Playwright para contenido dinámico.

Entregá:
1) estrategia de scraping por tipo de sitio,
2) esquema de datos unificado (titulo, fecha, medio, url, texto, autor, seccion, timestamp_ingesta, hash_contenido),
3) validaciones de calidad (nulos, duplicados, longitud mínima, idioma, fecha),
4) estrategia anti-fragilidad ante cambios de DOM,
5) almacenamiento bruto y curado,
6) logging y manejo de errores,
7) pruebas automáticas del pipeline.

Incluí pseudocódigo y ejemplos de funciones Python.
"

## Criterio de aceptación
- El diseño cubre escenarios estáticos y dinámicos.
- Se incluyen controles de calidad y trazabilidad de datos.
