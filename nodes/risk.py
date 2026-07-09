"""
risk.py

LangGraph node responsible for assessing
sun exposure risk using deterministic rules.
"""

from state import SunState

from utils.rules import (
    evaluate_heatstroke,
    evaluate_sunburn,
    evaluate_vitamin_d,
    evaluate_duration,
)


def risk_node(state: SunState) -> SunState:

    print("\nRisk Node Running...")

    # ----------------------------
    # Heatstroke Risk
    # ----------------------------

    state["heatstroke_risk"] = evaluate_heatstroke(
        state["temperature"]
    )

    # ----------------------------
    # Sunburn Risk
    # ----------------------------

    state["sunburn_risk"] = evaluate_sunburn(
        state["uv_index"]
    )

    # ----------------------------
    # Vitamin D Opportunity
    # ----------------------------

    state["vitamin_d_score"] = evaluate_vitamin_d(
        state["uv_index"]
    )

    # ----------------------------
    # Recommended Duration
    # ----------------------------

    state["recommended_duration"] = evaluate_duration(
    state["skin_type"],
    state["body_area"],
    state["uv_index"]
)
    

    return state