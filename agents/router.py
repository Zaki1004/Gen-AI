from agents.agent_state import (
    CoffeeAgentState
)

from utils.order_detector import (
    is_order_request
)

from utils.order_extractor import (
    extract_order
)


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

    print(
        "\nQUESTION:",
        question
    )

    print(
        "ORDERS:",
        orders
    )

    print(
        "IS ORDER:",
        is_order_request(
            question
        )
    )

    if (
        is_order_request(question)
        and
        len(orders) > 0
    ):

        print(
            "ROUTER -> ORDER"
        )

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

        print(
            "ROUTER -> RECOMMENDATION"
        )

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

        print(
            "ROUTER -> SQL"
        )

        state["tool"] = (
            "sql"
        )

        return state

    print(
        "ROUTER -> RAG"
    )

    state["tool"] = (
        "rag"
    )

    return state