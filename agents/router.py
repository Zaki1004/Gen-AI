from agents.agent_state import (
    CoffeeAgentState
)

from utils.order_detector import (
    is_order_request
)

from utils.order_extractor import (
    extract_order
)

from utils.conversation_intent import detect_intent

def router_node(
    state: CoffeeAgentState
):

    question = (
        state["question"]
        .lower()
    )

    orders = extract_order(
        question
    )

    intent = detect_intent(
        question
    )

    if (
        (
            is_order_request(question)
            and
            len(orders) > 0
        )
        or 
        intent in [
            "add_item",
            "view_cart",
            "remove_item",
            "clear_cart",
            "checkout",
            "update_quantity"
        ]
    ):

        state["tool"] = (
            "order"
        )

        return state

    recommendation_keywords = [
        "rekomendasi",
        "sarankan",
        "suka kopi"
    ]

    if any(
        keyword in question
        for keyword in recommendation_keywords
    ):

        state["tool"] = (
            "recommendation"
        )

        return state

    sql_keywords = [
        "termurah",
        "termahal",
        "rating",
        "stok",
        "menu"
    ]

    if any(
        keyword in question
        for keyword in sql_keywords
    ):

        state["tool"] = (
            "sql"
        )

        return state

    state["tool"] = (
        "rag"
    )

    return state