from rag.pdf_loader import (
    load_all_pdfs
)

from rag.document_cleaner import (
    remove_empty_pages
)

# ==========================
# Load PDF
# ==========================

docs = load_all_pdfs()

# ==========================
# Clean Documents
# ==========================

clean_docs = remove_empty_pages(
    docs
)

# ==========================
# Summary
# ==========================

print(
    f"Original Pages : {len(docs)}"
)

print(
    f"Clean Pages    : {len(clean_docs)}"
)

# ==========================
# Sample 1
# ==========================

print("\n===== SAMPLE 1 =====\n")

print(
    clean_docs[0].page_content[:700]
)

# ==========================
# Sample 2
# ==========================

print("\n===== SAMPLE 2 =====\n")

print(
    clean_docs[50].page_content[:700]
)

# ==========================
# Sample 3
# ==========================

print("\n===== SAMPLE 3 =====\n")

print(
    clean_docs[200].page_content[:700]
)

# ==========================
# Metadata
# ==========================

print("\n===== METADATA =====\n")

print(
    clean_docs[0].metadata
)