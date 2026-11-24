"""FastAPI service. Start with: uvicorn src.api:app --reload"""
from fastapi import FastAPI, HTTPException, Query
from src.weather_service import fetch_weather
from src.sample_data import get_sample_weather
from src.alerts import generate_alerts
from src.reports import save_report

app = FastAPI(title="Weather Forecast & Alert API", version="1.0.0",
              description="Weather data, forecast and rule-based alerts.")

@app.get("/")
def home():
    return {"message": "Weather Forecast & Alert API", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/weather")
def weather(city: str = Query("Jaipur", min_length=2),
            mode: str = Query("simulation", pattern="^(simulation|api)$")):
    try:
        data = get_sample_weather(city) if mode == "simulation" else fetch_weather(city)
        alerts = generate_alerts(data)
        report = save_report(data, alerts)
        return {"weather": data, "alerts": alerts, "report": report}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))
