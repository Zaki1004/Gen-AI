# rag/document_cleaner.py

def remove_empty_pages(
    documents
):

    cleaned = []

    for doc in documents:

        content = (
            doc.page_content
            .strip()
        )

        if len(content) < 50:
            continue

        cleaned.append(
            doc
        )

    return cleaned