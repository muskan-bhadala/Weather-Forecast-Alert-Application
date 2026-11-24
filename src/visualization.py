from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def create_forecast_chart(weather):
    Path("images").mkdir(exist_ok=True)
    forecast = weather.get("forecast", [])
    if not forecast:
        return "No forecast chart created (no forecast records)."
    labels = [x["datetime"][5:16] for x in forecast]
    temps = [x["temperature_c"] for x in forecast]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(labels, temps, marker="o", linewidth=2)
    ax.set_title(f"Temperature Forecast — {weather['city']}")
    ax.set_xlabel("Forecast time")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    path = Path("images") / "forecast_temperature.png"
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return str(path)
