import csv, json
from pathlib import Path
from datetime import datetime

OUTPUT_DIR = Path("outputs")
REPORT_DIR = Path("reports")

def save_report(weather, alerts):
    OUTPUT_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"weather_report_{stamp}.json"
    csv_path = OUTPUT_DIR / f"forecast_{stamp}.csv"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump({"weather": weather, "alerts": alerts}, f, indent=2)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "city", "datetime", "temperature_c", "humidity",
            "wind_speed_kmh", "rain_probability", "description"])
        writer.writeheader()
        for item in weather.get("forecast", []):
            writer.writerow({"city": weather["city"], **item})
    return str(json_path)
