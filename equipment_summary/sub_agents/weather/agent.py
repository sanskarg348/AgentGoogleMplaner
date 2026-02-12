# equipment_summary/sub_agents/weather/agent.py

import requests
import os
from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-pro"

# Placeholder for city to coordinates mapping. In a real application, a Geocoding API would be used.
CITY_COORDINATES = {
    "london": {"latitude": 51.5074, "longitude": 0.1278},
    "new york": {"latitude": 40.7128, "longitude": -74.0060},
    "paris": {"latitude": 48.8566, "longitude": 2.3522},
    "tokyo": {"latitude": 35.6895, "longitude": 139.6917},
}

def get_current_weather_tool(location: str):
    """
    Fetches current weather information for a given location using the Google Weather API.
    Requires a Google Maps Platform API key with the Weather API enabled, set as an environment variable `GOOGLE_WEATHER_API_KEY`.
    """
    api_key = "AIzaSyCHkPdCCJCCXKmLBbxgpQcvGB_dCAtcgD0"
    if not api_key:
        return {"error": "Google Weather API key not found. Please set the GOOGLE_WEATHER_API_KEY environment variable."}

    coords = CITY_COORDINATES.get(location.lower())
    if not coords:
        return {"error": f"Coordinates for '{location}' not found. Please provide latitude and longitude if not a predefined city, or add '{location}' to CITY_COORDINATES."}

    latitude = coords["latitude"]
    longitude = coords["longitude"]

    base_url = "https://weather.googleapis.com/v1/currentConditions:lookup"
    params = {
        "key": api_key,
        "location.latitude": latitude,
        "location.longitude": longitude
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        weather_data = response.json()

        # Extract relevant information. The exact structure depends on the API response.
        # This is a simplified extraction based on general API response patterns.
        current_conditions = weather_data.get("currentConditions", {})
        temperature = current_conditions.get("temperature", {}).get("value")
        weather_code = current_conditions.get("weatherCode")
        
        # Example of mapping weather code to description (this might need refinement based on actual API codes)
        weather_description = "Unknown"
        if weather_code:
            # This is a placeholder; actual mapping depends on Google's weatherCode definitions
            # For simplicity, let's assume a few common ones for now.
            if weather_code == 1000: weather_description = "Clear"
            elif weather_code == 1001: weather_description = "Cloudy"
            elif weather_code == 1003: weather_description = "Partly Cloudy"
            elif weather_code == 1063: weather_description = "Patchy rain possible"
            elif weather_code == 1069: weather_description = "Sleet"
            elif weather_code == 1183: weather_description = "Light rain"
            # Add more mappings as needed from API documentation

        return weather_data

        return {
            "location": location,
            "latitude": latitude,
            "longitude": longitude,
            "temperature": f"{temperature}°C" if temperature else "N/A",
            "conditions": weather_description # More detailed parsing would be needed here
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}