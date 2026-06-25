from typing import TypedDict


class CoffeeAgentState(
    TypedDict
):

    question: str

    tool: str

    tool_result: str

    answer: str