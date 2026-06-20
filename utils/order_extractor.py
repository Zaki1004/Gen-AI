import re

from utils.number_converter import (
    replace_text_numbers
)


def extract_order(question):

    question = replace_text_numbers(
        question.lower()
    )

    orders = []

    pattern = (
        r'(\d+)\s+'
        r'([a-zA-Z ]+?)'
        r'(?=\s+dan\s+\d+|$)'
    )

    matches = re.findall(
        pattern,
        question
    )

    for qty, menu_name in matches:

        orders.append({
            "menu_name": menu_name.strip(),
            "quantity": int(qty)
        })

    return orders