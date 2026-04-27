# Contratos de entrada/salida por módulo

## Esquemas base (JSON serializable)

### RawDocument
```json
{
  "source": "lanacion",
  "url": "https://...",
  "fetched_at": "2026-04-27T10:00:00Z",
  "title": "Titular",
  "raw_html": "<html>...</html>",
  "extracted_text": "texto extraído",
  "language": "es"
}
```

### CleanDocument
```json
{
  "doc_id": "hash(url)",
  "source": "lanacion",
  "url": "https://...",
  "title": "Titular",
  "published_at": null,
  "clean_text": "texto normalizado",
  "tokens_count": 543,
  "language": "es"
}
```

### NLPDocument
```json
{
  "doc_id": "hash(url)",
  "lemmas": ["economía", "inflación"],
  "entities": [
    {"text": "Argentina", "label": "LOC"}
  ],
  "pos_counts": {"NOUN": 120, "VERB": 80},
  "sentiment": null
}
```

---

## Contrato por módulo

## 1) ingestion
- **Input**: `SourceConfig`

```json
{
  "source_name": "lanacion",
  "urls": ["https://..."],
  "use_playwright": false,
  "timeout_seconds": 20
}
```

- **Output**: `list[RawDocument]` (JSONL / DataFrame)

## 2) processing
- **Input**: `list[RawDocument]`
- **Output**: `list[CleanDocument]`
- **Errores esperados**:
  - documento vacío,
  - idioma no soportado,
  - texto debajo de umbral mínimo.

## 3) nlp
- **Input**: `list[CleanDocument]` + `spacy_model`
- **Output**:
  1. `list[NLPDocument]`
  2. `pandas.DataFrame` de features por documento:
     - `doc_id`, `source`, `tokens_count`, `unique_lemmas`, `top_entity_type`

## 4) visualization
- **Input**: `DataFrame` de features + colección de términos/entidades.
- **Output**:
  - archivos `PNG/SVG` (frecuencias, entidades, nube de palabras)
  - `DataFrame` agregado por fuente/tema.

## 5) interpretation
- **Input**:
  - DataFrames agregados,
  - top términos,
  - top entidades.
- **Output**: `InsightReport`

```json
{
  "generated_at": "2026-04-27T10:30:00Z",
  "summary": "Hallazgos clave",
  "top_terms": ["economía", "gobierno"],
  "top_entities": ["Argentina", "Milei"],
  "source_comparison": [
    {"source": "lanacion", "docs": 10, "avg_tokens": 450}
  ],
  "warnings": []
}
```
