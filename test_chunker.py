from rag.pdf_loader import (
    load_all_pdfs
)

from rag.document_cleaner import (
    remove_empty_pages
)

from rag.chunker import (
    create_chunks,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

docs = load_all_pdfs()

docs = remove_empty_pages(
    docs
)

chunks = create_chunks(
    docs
)

print(f"Pages          : {len(docs)}")

print(f"Chunks         : {len(chunks)}")

print(f"Chunk Size     : {CHUNK_SIZE}")

print(f"Chunk Overlap  : {CHUNK_OVERLAP}")

print()

print("===== SAMPLE CHUNK =====\n")

print(
    chunks[0].page_content[:1000]
)

print()

print("===== METADATA =====")

print(
    chunks[0].metadata
)