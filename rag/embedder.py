from sentence_transformers import (
    SentenceTransformer
)

from config.ai_resources import embedding_model

embedding_model = (
    SentenceTransformer(
        MODEL_NAME
    )
)


def create_embeddings(
    chunks
):

    texts = [
        chunk.page_content
        for chunk in chunks
    ]

    embeddings = (
        embedding_model.encode(
            texts,
            show_progress_bar=True
        )
    )

    return embeddings