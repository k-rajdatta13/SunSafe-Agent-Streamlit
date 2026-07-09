from langgraph.graph import StateGraph, START, END

from state import SunState


# -----------------------------
# Node 1-User Profile
# -----------------------------
from nodes.profile import profile_node

# -----------------------------
# Node 2-Weather
# -----------------------------
from nodes.weather import weather_node

# -----------------------------
# Node 3-Risk
# -----------------------------

from nodes.risk import risk_node

# -----------------------------
# Node 4-Recommendation
# -----------------------------

from nodes.recommendation import recommendation_node


# -----------------------------
# Node 4-AI Explanation
# -----------------------------

from nodes.explainer import explainer_node


# -----------------------------
# Build Graph
# -----------------------------


builder = StateGraph(SunState)


#------Nodes--------------

builder.add_node("profile",profile_node)

builder.add_node("weather", weather_node)

builder.add_node("risk", risk_node)

builder.add_node("recommendation",recommendation_node)

builder.add_node("explainer",explainer_node)


#------Edges--------------

builder.add_edge(START,"profile")

builder.add_edge("profile","weather")

builder.add_edge("weather", "risk")

builder.add_edge("risk", "recommendation")

builder.add_edge("recommendation","explainer")

builder.add_edge("explainer",END)


graph = builder.compile()



# -----------------------------------------
# Run Agent
# -----------------------------------------

def run_agent(
    city: str,
    skin_type: int,
    body_area: int,
    age: int
):

    result = graph.invoke({

        "city": city,

        "skin_type": skin_type,

        "body_area": body_area,

        "age": age

    })

    return result