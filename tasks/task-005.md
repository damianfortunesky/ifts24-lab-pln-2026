# Task 005 — Productivización: Docker, base de datos y observabilidad

## Objetivo
Definir prompts para robustecer la solución en entorno reproducible.

## Prompt sugerido
"Actuá como Data/ML Ops Engineer. Diseñá una versión productiva de la app en Python usando Docker (y docker-compose opcional), con base de datos relacional (PostgreSQL opcional), y buenas prácticas de operación.

Entregá:
1) Dockerfile y compose base,
2) esquema de persistencia (tablas de documentos, entidades, ejecuciones),
3) migraciones o estrategia de inicialización,
4) configuración por variables de entorno,
5) healthcheck + logging estructurado,
6) plan de monitoreo básico (métricas de scraping, tiempos de pipeline, tasa de error),
7) CI mínima (lint + tests + build).

Proponé una versión mínima obligatoria y una versión extendida opcional.
"

## Criterio de aceptación
- La app se puede levantar de forma reproducible.
- Queda definido un camino claro de MVP a producción.
