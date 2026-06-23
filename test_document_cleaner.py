from rag.pdf_loader import (
    load_all_pdfs
)

from rag.document_cleaner import (
    remove_empty_pages
)

docs = load_all_pdfs()

clean_docs = remove_empty_pages(
    docs
)

print(
    f"Original Pages: {len(docs)}"
)

print(
    f"Clean Pages: {len(clean_docs)}"
)