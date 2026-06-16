def normalize_question(question: str):

    question = question.lower()

    replacements = {
        "kopi": "coffee",
        "non kopi": "non coffee",
        "makanan berat": "heavy meal"
    }

    for old, new in replacements.items():
        question = question.replace(old, new)

    return question