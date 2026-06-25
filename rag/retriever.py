from sentence_transformers import (
    SentenceTransformer
)

from rag.vector_store import (
    load_faiss_index
)

from rag.query_expansion import (
    expand_query
)

MODEL_NAME = (
    "all-MiniLM-L6-v2"
)

embedding_model = (
    SentenceTransformer(
        MODEL_NAME
    )
)


def retrieve_context(
    question,
    k=5
):

    index, chunks = (
        load_faiss_index()
    )

    expanded_query = expand_query(
        question
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

        doc.metadata["distance"] = float(
            distance
        )

        retrieved_chunks.append(
            doc
        )

    return retrieved_chunks