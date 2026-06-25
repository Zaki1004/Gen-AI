from agents.graph import (
    coffee_graph
)


def run_agent(
    question: str
):

    state = {

        "question": question,

        "tool": "",

        "tool_result": "",

        "answer": ""

    }

    result = coffee_graph.invoke(
        state
    )

    return result["tool_result"]