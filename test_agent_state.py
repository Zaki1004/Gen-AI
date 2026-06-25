from agents.agent_state import (
    CoffeeAgentState
)

state = CoffeeAgentState(
    question=
    "Apa itu roasting?",

    tool="rag",

    tool_result="",

    answer=""
)

print(state)