# ☀️ SunSafe AI

## AI-powered Vitamin D Exposure Recommendation System

### Overview

SunSafe AI is a LangGraph-based AI application that recommends safe
sunlight exposure for Vitamin D using live weather, deterministic health
rules, and Google Gemini for explanations.

## Features

-   LangGraph workflow
-   Streamlit dashboard
-   Open-Meteo weather integration
-   Gemini explanations
-   UV, heatstroke and sunburn assessment
-   Body area and Fitzpatrick skin type support
-   Hourly recommendation scoring

## Architecture

``` text
User
 |
 v
Streamlit UI
 |
 v
LangGraph
 |- Profile Node
 |- Weather Node
 |- Risk Node
 |- Recommendation Node
 |- Explainer Node
 |
 v
Dashboard
```

## Folder Structure

``` text
SunSafe-Agent/
├── app.py
├── graph.py
├── state.py
├── requirements.txt
├── README.md
├── .env
├── nodes/
├── tools/
├── utils/
└── prompts/
```

## Workflow

1.  Collect user profile.
2.  Fetch coordinates.
3.  Fetch live weather.
4.  Assess risks.
5.  Compute duration and best hour.
6.  Generate Gemini explanation.
7.  Display dashboard.

## Tech Stack

-   Python
-   LangGraph
-   LangChain
-   Streamlit
-   Google Gemini
-   Open-Meteo API

## Installation

``` bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

Create a `.env` file:

``` text
GOOGLE_API_KEY=YOUR_API_KEY
```

## Future Improvements

-   Pydantic models
-   Multi-day forecast
-   Medical knowledge base
-   Wearables integration

## License

MIT
