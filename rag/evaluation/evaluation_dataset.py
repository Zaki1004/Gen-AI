import os

from rag.retriever import (
    retrieve_context
)


EVALUATION_DATASET = [

    {
        "question": "Apa itu roasting kopi?",
        "expected_source": "apa_itu_roasting_kopi.pdf"
    },

    {
        "question": "Apa itu reaksi maillard?",
        "expected_source": "apa_itu_roasting_kopi.pdf"
    },

    {
        "question": "Apa fungsi cooling tray?",
        "expected_source": "apa_itu_roasting_kopi.pdf"
    },

    {
        "question": "Apa perbedaan arabika dan robusta?",
        "expected_source": "apa_itu_roasting_kopi.pdf"
    },

    {
        "question": "Apa itu espresso?",
        "expected_source": "istilah_dalam_coffee_shop.pdf"
    }

]


def evaluate_retriever():

    total = len(EVALUATION_DATASET)

    top1_correct = 0

    top5_correct = 0

    distances = []

    results = []

    for item in EVALUATION_DATASET:

        retrieved = retrieve_context(
            item["question"],
            k=5
        )

        expected = item["expected_source"]

        retrieved_sources = [

            os.path.basename(
                doc.metadata["source"]
            )

            for doc in retrieved
        ]

        retrieved_distance = [
            doc.metadata["distance"]
            for doc in retrieved
        ]

        distances.extend(
            retrieved_distance
        )

        top1_hit = (
            retrieved_sources[0] == expected
        )

        top5_hit = (
            expected in retrieved_sources
        )

        if top1_hit:

            top1_correct += 1

        if top5_hit:

            top5_correct += 1

        results.append({

            "question":
                item["question"],

            "expected":
                expected,

            "retrieved":
                retrieved_sources[0],

            "top1":
                top1_hit,

            "top5":
                top5_hit,

            "distance":
                retrieved_distance[0]

        })

    return {

        "results": results,

        "top1_accuracy":
            top1_correct / total,

        "top5_accuracy":
            top5_correct / total,

        "average_distance":
            sum(distances) / len(distances)

    }