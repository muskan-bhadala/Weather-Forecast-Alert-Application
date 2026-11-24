"""CLI entry point for the Weather Forecast & Alert Application."""
import argparse
from pathlib import Path
from src.weather_service import fetch_weather
from src.sample_data import get_sample_weather
from src.alerts import generate_alerts
from src.reports import save_report
from src.visualization import create_forecast_chart

def main():
    parser = argparse.ArgumentParser(description="Weather forecast and alert application")
    parser.add_argument("--mode", choices=["simulation", "api"], default="simulation",
                        help="Use built-in sample data or fetch live data")
    parser.add_argument("--city", default="Jaipur", help="City to check")
    args = parser.parse_args()

    print("\\n=== WEATHER FORECAST & ALERT APPLICATION ===")
    print(f"Mode: {args.mode.upper()} | City: {args.city}")

    try:
        weather = get_sample_weather(args.city) if args.mode == "simulation" else fetch_weather(args.city)
        alerts = generate_alerts(weather)
        print(f"\\nLocation: {weather['city']}, {weather['country']}")
        print(f"Current temperature: {weather['current']['temperature_c']} °C")
        print(f"Feels like: {weather['current']['feels_like_c']} °C")
        print(f"Humidity: {weather['current']['humidity']}%")
        print(f"Condition: {weather['current']['description']}")
        print("\\nForecast:")
        for day in weather["forecast"]:
            print(f"  {day['datetime']}: {day['temperature_c']} °C | "
                  f"rain {day['rain_probability']}% | {day['description']}")
        print("\\nAlerts:")
        if alerts:
            for alert in alerts:
                print(f"  [{alert['level']}] {alert['type']}: {alert['message']}")
        else:
            print("  No threshold alerts. Conditions are within configured limits.")

        report_path = save_report(weather, alerts)
        chart_path = create_forecast_chart(weather)
        print(f"\\nSaved report: {report_path}")
        print(f"Saved chart:  {chart_path}")
    except Exception as exc:
        print(f"\\nERROR: {exc}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
