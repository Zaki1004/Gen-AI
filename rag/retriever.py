from config.embedding import (
    get_embedding_model
)

from config.faiss_loader import (
    get_vector_store
)

from rag.query_expansion import (
    expand_query
)

embedding_model = (
    get_embedding_model()
)


def retrieve_context(
    question,
    k=5
):

    index, chunks = (
        get_vector_store()
    )

    expanded_query = (
        expand_query(question)
    )

    query_embedding = (
        embedding_model.encode(
            [expanded_query]
        )
    )

    distances, indices = (
        index.search(
            query_embedding.astype(
                "float32"
            ),
            k
        )
    )

    retrieved_chunks = []

    for distance, idx in zip(
        distances[0],
        indices[0]
    ):

        doc = chunks[idx]

        doc.metadata["distance"] = (
            float(distance)
        )

        retrieved_chunks.append(
            doc
        )

    return retrieved_chunks