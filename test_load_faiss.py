from rag.vector_store import (
    load_faiss_index
)

index, chunks = (
    load_faiss_index()
)

print(
    index.ntotal
)

print(
    chunks[0].metadata
)