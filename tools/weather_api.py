"""
weather_api.py

Utility functions for interacting with the Open-Meteo APIs.

Responsibilities:
1. Convert a city name into latitude and longitude.
2. Fetch current weather information for those coordinates.

This module should NEVER contain business logic such as
heat-risk calculation or vitamin D recommendations.
"""

from typing import Dict, Any
import requests
from requests.exceptions import RequestException


# -----------------------------
# API Endpoints
# -----------------------------

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

CURRENT_WEATHER_FIELDS = (
    "temperature_2m,"
    "relative_humidity_2m,"
    "cloud_cover,"
    "wind_speed_10m,"
    "weather_code,"
    "uv_index"
)


# -----------------------------
# Geocoding
# -----------------------------

def get_coordinates(city: str) -> Dict[str, Any]:
    """
    Convert a city name into latitude and longitude.

    Parameters
    ----------
    city : str
        Name of the city.

    Returns
    -------
    dict
        {
            "name": str,
            "country": str,
            "latitude": float,
            "longitude": float
        }

    Raises
    ------
    ValueError
        If the city cannot be found.

    ConnectionError
        If the API request fails.
    """

    try:

        response = requests.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "format": "json"
            },
            timeout=10
        )

        response.raise_for_status()

    except RequestException as e:
        raise ConnectionError(f"Geocoding API failed: {e}")

    data = response.json()

    results = data.get("results")

    if not results:
        raise ValueError(f"City '{city}' not found.")

    location = results[0]

    return {

        "name": location["name"],

        "country": location["country"],

        "latitude": location["latitude"],

        "longitude": location["longitude"]

    }


# -----------------------------
# Weather
# -----------------------------

def get_weather(latitude: float, longitude: float) -> Dict[str, Any]:
    """
    Fetch current weather information.

    Parameters
    ----------
    latitude : float

    longitude : float

    Returns
    -------
    dict
    """

    try:

        response = requests.get(

            FORECAST_URL,

            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": CURRENT_WEATHER_FIELDS,
                "timezone": "auto"
            },

            timeout=10

        )

        response.raise_for_status()

    except RequestException as e:

        raise ConnectionError(f"Weather API failed: {e}")

    current = response.json()["current"]

    return {

        "temperature": current["temperature_2m"],

        "relative_humidity": current["relative_humidity_2m"],

        "cloud_cover": current["cloud_cover"],

        "wind_speed": current["wind_speed_10m"],

        "weather_code": current["weather_code"],

        "uv_index": current["uv_index"]

    }


# -----------------------------
# Hourly weather
# -----------------------------
def get_hourly_forecast(latitude: float, longitude: float):
    """
    Fetch hourly UV index and temperature for today.
    """

    response = requests.get(
        FORECAST_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m,uv_index,cloud_cover",
            "forecast_days": 1,
            "timezone": "auto"
        },
        timeout=10
    )

    response.raise_for_status()

    hourly = response.json()["hourly"]

    forecast = []

    for time, temp, uv,cloud in zip(
        hourly["time"],
        hourly["temperature_2m"],
        hourly["uv_index"],
        hourly["cloud_cover"]
    ):

        forecast.append({

            "time": time,

            "temperature": temp,

            "uv_index": uv,
            
            "cloud_cover": cloud

        })

    return forecast
# -----------------------------
# Test Module
# -----------------------------

if __name__ == "__main__":

    city = input("Enter city: ")

    location = get_coordinates(city)

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    print("\nLocation")

    print(location)

    print("\nWeather")

    print(weather)