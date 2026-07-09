from state import SunState

from tools.weather_api import (
    get_coordinates,
    get_weather,get_hourly_forecast
)


def weather_node(state: SunState) -> SunState:
    """
    Fetch location and current weather,
    then update the shared state.
    """

    print("\nWeather Node Running...")

    city = state["city"]

    location = get_coordinates(city)

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )
    
    forecast = get_hourly_forecast(
    location["latitude"],
    location["longitude"]
)

    state["hourly_forecast"] = forecast
    
    state["latitude"] = location["latitude"]
    state["longitude"] = location["longitude"]
    state["country"] = location["country"]

    state["temperature"] = weather["temperature"]
    state["uv_index"] = weather["uv_index"]
    state["cloud_cover"] = weather["cloud_cover"]
    state["relative_humidity"] = weather["relative_humidity"]
    state["wind_speed"] = weather["wind_speed"]
    state["weather_code"] = weather["weather_code"]

    return state