from config.embedding import (
    get_embedding_model
)

embedding_model = (
    get_embedding_model()
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