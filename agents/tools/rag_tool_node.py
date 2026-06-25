from rag.rag_service import (
    ask_rag
)


def rag_tool_node(
    question
):

    print("RAG TOOL CALLED")
    
    return ask_rag(
        question
    )