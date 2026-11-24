"""Deterministic sample data for offline demonstrations."""
from datetime import datetime, timedelta

def get_sample_weather(city="Jaipur"):
    city = city.strip() or "Jaipur"
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    return {
        "city": city.title(),
        "country": "IN",
        "timezone": "Local sample time",
        "source": "simulation",
        "retrieved_at": now.isoformat(timespec="minutes"),
        "current": {
            "temperature_c": 40.2,
            "feels_like_c": 43.0,
            "humidity": 88,
            "wind_speed_kmh": 18.0,
            "description": "hot and humid (simulated)",
            "rain_probability": 10
        },
        "forecast": [
            {"datetime": (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
             "temperature_c": 39.0, "humidity": 82, "wind_speed_kmh": 22.0,
             "rain_probability": 20, "description": "hot"},
            {"datetime": (now + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"),
             "temperature_c": 31.0, "humidity": 91, "wind_speed_kmh": 56.0,
             "rain_probability": 85, "description": "thunderstorm"},
            {"datetime": (now + timedelta(days=3)).strftime("%Y-%m-%d %H:%M"),
             "temperature_c": 27.0, "humidity": 68, "wind_speed_kmh": 16.0,
             "rain_probability": 15, "description": "cloudy"}
        ]
    }
