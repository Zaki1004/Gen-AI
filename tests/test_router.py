from agents.router import (
    router_node
)

state = {
    "question":
        "Saya suka kopi manis dingin",

    "tool":
        "",

    "tool_result":
        "",

    "answer":
        ""
}

result = (
    router_node(
        state
    )
)

print(
    result["tool"]
)