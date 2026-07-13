from rag.evaluation.evaluation_dataset import (
    evaluate_retriever
)

report = evaluate_retriever()

print("=" * 80)

print("RETRIEVAL EVALUATION")

print("=" * 80)

for item in report["results"]:

    print()

    print(f"Question : {item['question']}")

    print(f"Expected : {item['expected']}")

    print(f"Retrieved: {item['retrieved']}")

    print(f"Top-1    : {'✅' if item['top1'] else '❌'}")

    print(f"Top-5    : {'✅' if item['top5'] else '❌'}")

    print(f"Distance : {item['distance']:.4f}")

    print("-" * 60)

print()

print("=" * 80)

print(
    f"Top-1 Accuracy : {report['top1_accuracy']:.2%}"
)

print(
    f"Top-5 Accuracy : {report['top5_accuracy']:.2%}"
)

print(
    f"Average Distance : {report['average_distance']:.4f}"
)

print("=" * 80)