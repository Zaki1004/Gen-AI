import re


def extract_remove_item(question):

    question = question.lower()

    pattern = (
        r"(hapus|remove|batalkan|kurangi)"
        r"\s*"
        r"(\d+)?"
        r"\s*"
        r"([a-zA-Z ]+)"
    )

    match = re.search(
        pattern,
        question
    )

    if not match:

        return None

    quantity = (
        int(match.group(2))
        if match.group(2)
        else None
    )

    return {

        "menu":
        match.group(3).strip(),

        "quantity":
        quantity

    }