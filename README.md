# Laboratorio de Introducción al PLN, LLMs y Agentic AI

**IFTS Nº 24 — Ciencia de Datos e Inteligencia Artificial**
**2do año — 1er cuatrimestre 2026**
**Prof. Matías Barreto** — Especialista en Nuevos Medios e Interactividad
matiasbarreto@ifts24.edu.ar

_Lenguaje, Algoritmos y Construcción del Presente_

---

## Qué es este repositorio

Este repositorio contiene los notebooks de laboratorio de la materia. El material se organiza en carpetas numeradas (`001/`, `002/`, `003/`, ...) que se van publicando semana a semana a medida que avanza la cursada.

Cada carpeta corresponde a un bloque temático y contiene los notebooks (`.ipynb`) necesarios para trabajar en clase y fuera de ella.

---

## Requisitos previos

Antes de arrancar, asegurate de tener instalado en tu máquina:

1. **Python 3.11 o superior** — [Descarga oficial](https://www.python.org/downloads/)
   - Durante la instalación en Windows, marcá la opción **"Add Python to PATH"**.
2. **Git** — [Descarga oficial](https://git-scm.com/downloads)
3. **Visual Studio Code** (recomendado) — [Descarga oficial](https://code.visualstudio.com/)
   - Instalá la extensión **Jupyter** desde el marketplace de VS Code.

---

## Setup inicial (una sola vez)

Abrí una terminal (en Windows: PowerShell o Git Bash) y ejecutá los siguientes comandos:

### 1. Clonar el repositorio

```bash
git clone https://github.com/mattbarreto/ifts24-lab-pln-2026.git
cd ifts24-lab-pln-2026
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Git Bash / CMD):**

```bash
.venv\Scripts\activate
```

> Si PowerShell muestra un error de permisos, ejecutá primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Instalar Playwright (navegadores para web scraping)

```bash
playwright install
```

### 6. Instalar componentes de Scrapling

```bash
pip scrapling install
```

### 7. Descargar recursos de NLTK

Abrí Python e ingresá:

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
```

---

## Cómo actualizar cada semana

Cada vez que se publique material nuevo, desde la carpeta del repositorio ejecutá:

```bash
git pull
```

Si se agregan nuevas dependencias, se anunciará en clase. En ese caso, con el entorno activado:

```bash
pip install -r requirements.txt
```

---

## Estructura del repositorio

```
ifts24-lab-pln-2026/
├── README.md               ← Este archivo
├── requirements.txt        ← Dependencias del entorno
├── 001_WebScraping/        ← Semana 1: Web scraping y extracción de texto
│   ├── 001_WEB_Scraping_Parte1.ipynb
│   ├── 002_WebScraping.ipynb
│   └── ...
├── 002_xxx/                ← Semana 2 (próximamente)
└── ...
```

---

## Manual de ejecución y operación de la app

Este repositorio incluye una app demostrativa en `media_analysis_app/` para ejecutar el flujo completo: **ingesta → limpieza → NLP → visualización → interpretación**.

### 1) Preparación específica de la app

Desde la raíz del repo:

```bash
cd media_analysis_app
pip install -r requirements.txt
python -m spacy download es_core_news_md
```

> Si no vas a usar el modelo mediano, también podés configurar uno más liviano (`es_core_news_sm`) desde variables de entorno.

### 2) Variables de entorno recomendadas

Creá un archivo `.env` en `media_analysis_app/` (si no existe) con una base como esta:

```env
SPACY_MODEL=es_core_news_md
LOG_LEVEL=INFO
REQUEST_TIMEOUT=20
MAX_URLS=10
```

### 3) Ejecución de la interfaz (modo operativo principal)

```bash
python app.py
```

Luego abrí en navegador la URL local que imprime Gradio (por ejemplo `http://127.0.0.1:7860`).

### 4) Operación sugerida paso a paso

1. Cargá una o más URLs en el formulario.
2. Definí rango de fechas y límite de notas.
3. Ejecutá por etapas (preparar → scraping/limpieza → NLP/dashboard) o ejecución completa.
4. Revisá tablas/gráficos de términos, entidades y evolución temporal.
5. Exportá resultados en CSV/JSON para entregar evidencia del análisis.

### 5) Verificación rápida de funcionamiento

Antes de una demo o entrega final, validá:

- Que el modelo spaCy esté instalado y cargue sin error.
- Que al menos una URL procese texto con longitud razonable.
- Que se generen métricas/tablas y al menos un gráfico.
- Que la exportación CSV/JSON finalice correctamente.

### 6) Cierre operativo

- Guardá artifacts relevantes (gráficos/reportes) para trazabilidad.
- Si hubo errores, registrá URL, etapa y mensaje para depuración reproducible.
- Ejecutá `git pull` antes de una nueva sesión para trabajar sobre la última versión del material.

---

## Resolución de problemas frecuentes

**"python no se reconoce como comando"**
Python no se agregó al PATH durante la instalación. Reinstalá marcando "Add Python to PATH", o usá `python3` en lugar de `python`.

**"No module named 'xxx'"**
Verificá que el entorno virtual esté activado (debés ver `(.venv)` al inicio de la línea en la terminal). Si lo está, ejecutá `pip install -r requirements.txt` de nuevo.

**Error de permisos en PowerShell al activar el entorno**
Ejecutá: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Playwright no funciona / no encuentra navegador**
Ejecutá `playwright install` con el entorno activado.

---

## Licencia

Este material se distribuye bajo licencia [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es):
podés usarlo y adaptarlo con atribución, sin fines comerciales, y compartiendo bajo la misma licencia.
