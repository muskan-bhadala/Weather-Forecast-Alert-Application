"""Rule-based weather risk alerts. Thresholds can be configured in .env."""
from src.config import MAX_TEMP_C, MIN_TEMP_C, HIGH_HUMIDITY, RAIN_PROBABILITY, HIGH_WIND_KMH

def generate_alerts(weather):
    alerts = []
    current = weather["current"]
    def add(level, kind, message):
        alerts.append({"level": level, "type": kind, "message": message})

    temp = current["temperature_c"]
    if temp >= MAX_TEMP_C:
        add("HIGH", "HEAT", f"Current temperature is {temp}°C (threshold {MAX_TEMP_C}°C). Stay hydrated and avoid prolonged outdoor activity.")
    if temp <= MIN_TEMP_C:
        add("MEDIUM", "COLD", f"Current temperature is {temp}°C (threshold {MIN_TEMP_C}°C). Dress warmly.")
    if current["humidity"] >= HIGH_HUMIDITY:
        add("MEDIUM", "HUMIDITY", f"Humidity is {current['humidity']}% (threshold {HIGH_HUMIDITY}%).")
    if current.get("wind_speed_kmh", 0) >= HIGH_WIND_KMH:
        add("HIGH", "WIND", f"Wind speed is {current['wind_speed_kmh']} km/h (threshold {HIGH_WIND_KMH} km/h).")

    for item in weather.get("forecast", []):
        if item.get("rain_probability", 0) >= RAIN_PROBABILITY:
            add("MEDIUM", "RAIN", f"Rain probability is {item['rain_probability']}% at {item['datetime']}. Carry rain protection.")
        if item.get("wind_speed_kmh", 0) >= HIGH_WIND_KMH:
            add("HIGH", "WIND", f"Forecast wind speed is {item['wind_speed_kmh']} km/h at {item['datetime']}.")
    return alerts
