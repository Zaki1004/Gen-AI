from rag.pdf_loader import (
    load_all_pdfs
)

docs = load_all_pdfs()

empty_pages = 0

for doc in docs:

    if not doc.page_content.strip():

        empty_pages += 1

print(
    f"Total Pages: {len(docs)}"
)

print(
    f"Empty Pages: {empty_pages}"
)

print(
    f"Valid Pages: {len(docs)-empty_pages}"
)