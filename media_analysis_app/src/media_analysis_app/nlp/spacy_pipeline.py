"""Procesamiento NLP con spaCy."""

from dataclasses import dataclass

import pandas as pd
import spacy

from media_analysis_app.processing.cleaner import CleanDocument


@dataclass
class NLPDocument:
    doc_id: str
    lemmas: list[str]
    entities: list[dict[str, str]]
    pos_counts: dict[str, int]


def run_spacy(documents: list[CleanDocument], model_name: str) -> tuple[list[NLPDocument], pd.DataFrame]:
    nlp = spacy.load(model_name)
    outputs: list[NLPDocument] = []
    rows: list[dict] = []

    for item in documents:
        doc = nlp(item.clean_text)
        lemmas = [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_space]
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

        pos_counts: dict[str, int] = {}
        for token in doc:
            pos_counts[token.pos_] = pos_counts.get(token.pos_, 0) + 1

        outputs.append(NLPDocument(item.doc_id, lemmas, entities, pos_counts))
        rows.append(
            {
                "doc_id": item.doc_id,
                "source": item.source,
                "tokens_count": item.tokens_count,
                "unique_lemmas": len(set(lemmas)),
                "top_entity_type": entities[0]["label"] if entities else None,
            }
        )

    return outputs, pd.DataFrame(rows)
