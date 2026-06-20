import re


def extract_remove_item(question):

    question = question.lower()

    pattern = (
        r'(hapus|remove|batalkan)'
        r'\s+'
        r'(?:\d+\s+)?'
        r'([a-zA-Z ]+)'
    )

    match = re.search(
        pattern,
        question
    )

    if not match:
        return None

    return (
        match.group(2)
        .strip()
    )