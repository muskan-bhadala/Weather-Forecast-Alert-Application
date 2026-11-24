"""OpenWeatherMap API integration (Geocoding + Current + 5-day forecast)."""
import requests
from src.config import OPENWEATHER_API_KEY, BASE_URL

TIMEOUT = 15

def _get_json(url, params):
    try:
        response = requests.get(url, params=params, timeout=TIMEOUT)
        if response.status_code == 401:
            raise RuntimeError("API key is missing or invalid. Check your .env file.")
        if response.status_code == 404:
            raise RuntimeError("City not found. Check the spelling and try again.")
        response.raise_for_status()
        return response.json()
    except requests.Timeout as exc:
        raise RuntimeError("Weather API request timed out. Please retry.") from exc
    except requests.RequestException as exc:
        raise RuntimeError(f"Could not contact weather API: {exc}") from exc

def fetch_weather(city):
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("OPENWEATHER_API_KEY is not set. Add it to your .env file.")
    geo = _get_json(f"{BASE_URL}/geo/1.0/direct",
                    {"q": city, "limit": 1, "appid": OPENWEATHER_API_KEY})
    if not geo:
        raise RuntimeError(f"No location found for '{city}'.")
    lat, lon = geo[0]["lat"], geo[0]["lon"]
    common = {"lat": lat, "lon": lon, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    current = _get_json(f"{BASE_URL}/data/2.5/weather", common)
    forecast = _get_json(f"{BASE_URL}/data/2.5/forecast", common)

    current_data = {
        "temperature_c": round(current["main"]["temp"], 1),
        "feels_like_c": round(current["main"]["feels_like"], 1),
        "humidity": int(current["main"]["humidity"]),
        "wind_speed_kmh": round(current.get("wind", {}).get("speed", 0) * 3.6, 1),
        "description": current["weather"][0]["description"].title(),
        "rain_probability": 0
    }
    items = []
    for item in forecast.get("list", [])[:8]:
        items.append({
            "datetime": item["dt_txt"],
            "temperature_c": round(item["main"]["temp"], 1),
            "humidity": int(item["main"]["humidity"]),
            "wind_speed_kmh": round(item.get("wind", {}).get("speed", 0) * 3.6, 1),
            "rain_probability": round(float(item.get("pop", 0)) * 100),
            "description": item["weather"][0]["description"].title()
        })
    return {
        "city": geo[0]["name"], "country": geo[0].get("country", ""),
        "timezone": "API local timestamps", "source": "OpenWeatherMap",
        "retrieved_at": current.get("dt", ""),
        "current": current_data, "forecast": items
    }
