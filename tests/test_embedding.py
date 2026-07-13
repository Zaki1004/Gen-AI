from rag.pdf_loader import (
    load_all_pdfs
)

from rag.document_cleaner import (
    remove_empty_pages
)

from rag.chunker import (
    create_chunks
)

from rag.embedder import (
    create_embeddings
)

docs = load_all_pdfs()

docs = remove_empty_pages(
    docs
)

chunks = create_chunks(
    docs
)

embeddings = create_embeddings(
    chunks
)

print(
    f"Chunks: {len(chunks)}"
)

print(
    f"Embeddings: {len(embeddings)}"
)

print(
    f"Vector Dimension: {len(embeddings[0])}"
)