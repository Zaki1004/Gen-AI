from langgraph.graph import (
    StateGraph,
    END
)

from agents.agent_state import (
    CoffeeAgentState
)

from agents.router import (
    router_node
)

from agents.tools.sql_tool_node import (
    sql_tool_node
)

from agents.tools.rag_tool_node import (
    rag_tool_node
)

from agents.tools.order_tool_node import (
    order_tool_node
)

from agents.tools.recommendation_tool_node import (
    recommendation_tool_node
)

# Router Wrapper

def route_decision(
    state: CoffeeAgentState
):

    return state["tool"]

# SQL NODE

def sql_node(
    state: CoffeeAgentState
):

    state["tool_result"] = (
        sql_tool_node(
            state["question"]
        )
    )

    return state

# RAG NODE

def rag_node(
    state: CoffeeAgentState
):

    state["tool_result"] = (
        rag_tool_node(
            state["question"]
        )
    )

    return state

# ORDER NODE

def order_node(
    state: CoffeeAgentState
):

    state["tool_result"] = (
        order_tool_node(
            state["question"]
        )
    )

    return state

# RECOMMENDATION NODE

def recommendation_node(
    state: CoffeeAgentState
):

    state["tool_result"] = (
        recommendation_tool_node(
            state["question"]
        )
    )

    return state


# BUILD GRAPH

builder = StateGraph(
    CoffeeAgentState
)

builder.add_node(
    "router",
    router_node
)

builder.add_node(
    "sql",
    sql_node
)

builder.add_node(
    "rag",
    rag_node
)

builder.add_node(
    "order",
    order_node
)

builder.add_node(
    "recommendation",
    recommendation_node
)

# ENTRY POINT

builder.set_entry_point(
    "router"
)

# CONDITIONAL EDGE

builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "sql": "sql",
        "rag": "rag",
        "order": "order",
        "recommendation": "recommendation"
    }
)

# EXIT EDGE

builder.add_edge(
    "sql",
    END
)

builder.add_edge(
    "rag",
    END
)

builder.add_edge(
    "order",
    END
)

builder.add_edge(
    "recommendation",
    END
)

# COMPILE

coffee_graph = (
    builder.compile()
)