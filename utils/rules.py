"""
rules.py

Business rules for safe sunlight exposure.

This module contains ONLY deterministic logic.

No API calls.
No LangGraph code.
No LLM code.
"""

from typing import Tuple


# ----------------------------------
# Heatstroke Risk
# ----------------------------------

def evaluate_heatstroke(
    temperature: float
) -> str:

    if temperature < 30:
        return "LOW"

    elif temperature <= 35:
        return "MODERATE"

    return "HIGH"


# ----------------------------------
# Sunburn Risk
# ----------------------------------

def evaluate_sunburn(
    uv_index: float
) -> str:

    if uv_index <= 2:
        return "LOW"

    elif uv_index <= 5:
        return "MODERATE"

    elif uv_index <= 7:
        return "HIGH"

    elif uv_index <= 10:
        return "VERY HIGH"

    return "EXTREME"


# ----------------------------------
# Vitamin D Opportunity
# ----------------------------------

def evaluate_vitamin_d(
    uv_index: float
) -> str:

    if uv_index < 2:
        return "POOR"

    elif uv_index <= 5:
        return "GOOD"

    elif uv_index <= 8:
        return "GOOD (Short Exposure)"

    return "LIMITED"


# ----------------------------------
# Base Duration
# ----------------------------------

def get_base_duration(
    skin_type: int
) -> int:

    duration = {

        1: 10,

        2: 15,

        3: 20,

        4: 25,

        5: 35,

        6: 45

    }

    return duration.get(skin_type, 20)  # 20 is default value 
  


# ----------------------------------
# Final Duration
# ----------------------------------


def evaluate_duration(
    skin_type: int,
    body_area: int,
    uv_index: float
) -> int:
    """
    Calculate safe exposure duration.

    Factors:
    1. Skin type
    2. Body area exposed
    3. UV Index
    """

    duration = get_base_duration(skin_type)

    # -------------------------
    # Body Area Adjustment
    # -------------------------

    if body_area <= 10:
        duration += 10

    elif body_area <= 25:
        duration += 5

    elif body_area <= 50:
        duration += 0

    else:
        duration -= 5

    # -------------------------
    # UV Adjustment
    # -------------------------

    if uv_index > 8:
        duration -= 5

    elif uv_index < 2:
        duration += 10

    return max(duration, 5)
  
  
def calculate_hour_score(
    uv: float,
    temperature: float,
    cloud_cover: int
) -> int:

    score = 0

    # --------------------------
    # UV Score
    # --------------------------

    if uv < 2:
        score += 0

    elif uv < 3:
        score += 30

    elif uv <= 6:
        score += 60

    elif uv <= 8:
        score += 40

    else:
        score += 10

    # --------------------------
    # Temperature Score
    # --------------------------

    if temperature < 25:
        score += 10

    elif temperature <= 32:
        score += 30

    elif temperature <= 35:
        score += 20

    else:
        score += 0

    # --------------------------
    # Cloud Score
    # --------------------------

    if cloud_cover < 30:
        score += 10

    elif cloud_cover <= 70:
        score += 5

    else:
        score += 0

    return score