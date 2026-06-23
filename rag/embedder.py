from sentence_transformers import (
    SentenceTransformer
)

MODEL_NAME = (
    "all-MiniLM-L6-v2"
)

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