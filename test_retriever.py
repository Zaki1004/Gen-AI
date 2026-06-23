from rag.retriever import (
    retrieve_context
)

results = retrieve_context(
    "Apa itu roasting kopi?"
)

print(
    f"Total Retrieved: {len(results)}"
)

for i, doc in enumerate(results):

    print(
        f"\n===== CHUNK {i+1} ====="
    )

    print(
        f"Source: {doc['source']}"
    )

    print(
        f"Page: {doc['page']}"
    )

    print(
        f"Distance: {doc['distance']}"
    )

    print()

    print(
        doc["content"][:500]
    )