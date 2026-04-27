"""Generación de reporte interpretativo mínimo."""

from datetime import datetime, timezone

import pandas as pd


def build_report(features_df: pd.DataFrame) -> dict:
    avg_tokens = float(features_df["tokens_count"].mean()) if not features_df.empty else 0.0
    per_source = (
        features_df.groupby("source", as_index=False)
        .agg(docs=("doc_id", "count"), avg_tokens=("tokens_count", "mean"))
        .to_dict(orient="records")
        if not features_df.empty
        else []
    )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": f"Se analizaron {len(features_df)} documentos.",
        "source_comparison": per_source,
        "global_avg_tokens": avg_tokens,
        "warnings": [],
    }
