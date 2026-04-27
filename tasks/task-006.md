# Task 006 — Verificación final y checklist operativo de la app

## Objetivo
Definir una última task para revisar y verificar que la app funcione de punta a punta antes de cierre o entrega.

## Prompt sugerido
"Actuá como QA Engineer + Tech Lead y realizá una validación final integral de la app de análisis de medios.

Necesito:
1) checklist de pre-ejecución (dependencias, variables de entorno, modelos NLP, rutas),
2) smoke test de ejecución completa (ingesta → limpieza → NLP → visualización → interpretación),
3) pruebas funcionales mínimas por etapa (entradas válidas, vacías e inválidas),
4) validación de outputs esperados (archivos, métricas y reportes),
5) verificación de interfaz (CLI o Gradio) y mensajes de error,
6) registro de incidencias con severidad (bloqueante/alta/media/baja),
7) criterio de Go/No-Go para liberar.

Entregá:
- pasos concretos con comandos,
- resultados esperados por prueba,
- plantilla de reporte final de validación,
- plan de corrección priorizado para fallas detectadas.

Restricciones:
- Priorizar pruebas reproducibles y de bajo costo.
- Evitar cambios de arquitectura en esta fase.
- Documentar cualquier supuesto operativo."

## Entregables esperados
- Checklist de verificación final ejecutable.
- Evidencia de corrida de smoke test y validaciones clave.
- Reporte de incidencias con prioridad y estado.
- Recomendación final de liberación (Go/No-Go) con justificación.

## Criterio de aceptación
- Existe una guía clara para verificar funcionamiento end-to-end.
- Se pueden detectar fallas críticas antes de publicar o presentar.
- La decisión de liberación queda documentada con criterios objetivos.
