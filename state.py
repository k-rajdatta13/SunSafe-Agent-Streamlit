
    
from typing import TypedDict


class SunState(TypedDict):
    # -------------------------
    # User Profile
    # -------------------------
    city: str
    skin_type: int
    body_area: int
    age: int

    # -------------------------
    # Location
    # -------------------------
    latitude: float
    longitude: float
    country: str

    # -------------------------
    # Weather
    # -------------------------
    temperature: float
    uv_index: float
    cloud_cover: int
    relative_humidity: int
    wind_speed: float
    weather_code: int
    hourly_forecast: list

    # -------------------------
    # Assessment
    # -------------------------
    heatstroke_risk: str
    sunburn_risk: str
    vitamin_d_score: str

    # -------------------------
    # Recommendation
    # -------------------------
    recommended_duration: int
    best_time: str
    recommendation: str
    best_score: int
    
    # -------------------------
    # AI Explanation
    # -------------------------
    explanation: str