from rag.pdf_loader import (
    load_all_pdfs
)

from rag.document_cleaner import (
    remove_empty_pages
)

from rag.chunker import (
    create_chunks
)

docs = load_all_pdfs()

clean_docs = remove_empty_pages(
    docs
)

chunks = create_chunks(
    clean_docs
)

print(
    f"Pages: {len(clean_docs)}"
)

print(
    f"Chunks: {len(chunks)}"
)

print("\n===== CHUNK SAMPLE =====\n")

print(
    chunks[0].page_content[:1000]
)

print("\n===== METADATA =====\n")

print(
    chunks[0].metadata
)