from sentence_transformers import (
    SentenceTransformer
)

from rag.vector_store import (
    load_faiss_index
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

    query_embedding = (
        embedding_model.encode(
            [question]
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

    for i, idx in enumerate(indices[0]):

        retrieved_chunks.append(
            {
                "content":
                    chunks[idx].page_content,

                "source":
                    chunks[idx].metadata.get(
                        "source",
                        "Unknown"
                    ),

                "page":
                    chunks[idx].metadata.get(
                        "page",
                        0
                    ),

                "distance":
                    float(
                        distances[0][i]
                    )
            }
        )

    return retrieved_chunks