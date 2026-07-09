from datetime import datetime, timedelta

from state import SunState

from utils.rules import calculate_hour_score


def recommendation_node(state: SunState) -> SunState:

    print("\nRecommendation Node Running...")

    forecast = state["hourly_forecast"]

    best_hour = None

    best_score = -1

    # ------------------------------
    # Find Best Hour
    # ------------------------------

    for hour in forecast:

        score = calculate_hour_score(

            hour["uv_index"],

            hour["temperature"],

            hour["cloud_cover"]

        )

        if score > best_score:

            best_score = score

            best_hour = hour

    # ------------------------------
    # Format Output
    # ------------------------------

    if best_hour:

        dt = datetime.fromisoformat(
            best_hour["time"]
        )

        start = dt.strftime(
            "%I:%M %p"
        ).lstrip("0")

        end = (

            dt +

            timedelta(
                minutes=state["recommended_duration"]
            )

        ).strftime("%I:%M %p").lstrip("0")

        state["best_time"] = f"{start} - {end}"

        state["best_score"] = best_score

    else:

        state["best_time"] = "No suitable time"

        state["best_score"] = 0

    return state