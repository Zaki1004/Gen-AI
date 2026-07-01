from rag.retriever import (
    retrieve_context
)

question = "Apa itu roasting kopi?"

results = retrieve_context(
    question
)

print(f"Total Retrieved: {len(results)}")

for i, doc in enumerate(results):

    print(f"\n===== CHUNK {i+1} =====")

    print(
        f"Source: {doc.metadata['source']}"
    )

    print(
        f"Page: {doc.metadata['page']}"
    )

    print(
        f"Distance: {doc.metadata['distance']}"
    )

    print()

    print(
        doc.page_content[:500]
    )