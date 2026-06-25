from rag.retriever import (
    retrieve_context
)

questions = [

    "Apa itu roasting kopi?",

    "Apa itu reaksi maillard?",

    "Apa fungsi cooling tray?",

    "Apa perbedaan arabika dan robusta?",

    "Apa itu espresso?"

]

for question in questions:

    print("=" * 80)

    print("QUESTION :")

    print(question)

    print()

    results = retrieve_context(
        question,
        k=5
    )

    for i, doc in enumerate(results):

        print(f"TOP {i+1}")

        print(
            f"Distance : {doc.metadata['distance']:.4f}"
        )

        print(
            f"Source   : {doc.metadata['source']}"
        )

        print(
            f"Page     : {doc.metadata['page']}"
        )

        print()

        print(
            doc.page_content[:300]
        )

        print()

    print("=" * 80)

    print()