# Weather Forecast & Alert Application

A beginner-friendly Python project that retrieves current weather and forecast data, evaluates configurable risk thresholds, displays alerts, and saves JSON/CSV reports and a temperature chart. It supports **offline simulation by default** and optional live data through OpenWeatherMap.

## Problem statement and industry relevance
Weather can disrupt travel, outdoor events, agriculture, delivery routes and logistics. This project demonstrates how a software service can normalize weather API data, apply transparent rules, and communicate potential risks. It is an educational prototype, not an official warning service.

## Features
- City-based weather lookup
- Offline simulation (no key or internet required)
- Optional OpenWeatherMap geocoding, current weather and forecast integration
- Heat, cold, humidity, rain-probability and high-wind alerts
- FastAPI endpoints with interactive Swagger docs
- Optional Streamlit dashboard
- JSON report, forecast CSV and Matplotlib chart
- Basic automated tests

## Tech stack
Python, requests, JSON, datetime, python-dotenv, Pandas, Matplotlib, FastAPI, Uvicorn, Streamlit, pytest.

## Folder structure
```text
Weather-Forecast-Alert-Application/
├── data/                 # Place optional input datasets here
├── src/                  # API integration, alert rules, reports and charts
├── outputs/              # Generated forecast CSV files
├── images/               # Generated charts and evidence screenshots
├── reports/              # Generated JSON reports
├── docs/                 # Architecture and project documentation
├── tests/                # Automated tests
├── main.py               # Command-line entry point
├── app.py                # Optional Streamlit dashboard
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Quick start (Windows PowerShell)
```powershell
cd path\to\Weather-Forecast-Alert-Application
py -3.13 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py --mode simulation --city Jaipur
```

## Live API setup
1. Create an OpenWeatherMap account and obtain an API key.
2. Copy `.env.example` to `.env`.
3. Put your key after `OPENWEATHER_API_KEY=`.
4. Run `python main.py --mode api --city Jaipur`.

Never commit `.env` or publish API keys. `.env.example` contains only a placeholder. New API keys or newly enabled API products may take time to become active.

## Run the FastAPI service
```powershell
uvicorn src.api:app --reload
```
Open `http://127.0.0.1:8000/docs`. Example: `http://127.0.0.1:8000/weather?city=Jaipur&mode=simulation`.

## Run the Streamlit dashboard
```powershell
streamlit run app.py
```
Choose simulation for an offline demo or API for live data.

## Tests
```powershell
pytest -q
```

## Generated files
- `reports/weather_report_*.json` — normalized weather and alerts
- `outputs/forecast_*.csv` — forecast records
- `images/forecast_temperature.png` — temperature chart

## Sample simulation
The included deterministic sample intentionally contains high temperature, high humidity, and forecast rain/wind conditions so alert paths can be demonstrated. These are **simulated values**, not actual Jaipur observations.

## Screenshots to capture
Save screenshots in `images/`:
1. `01_project_structure.png` — project folder in VS Code
2. `02_simulation_terminal.png` — CLI simulation output
3. `03_api_docs.png` — FastAPI Swagger `/docs`
4. `04_streamlit_dashboard.png` — dashboard
5. `05_forecast_chart.png` — generated chart
6. `06_generated_reports.png` — JSON and CSV report files
7. `07_github_repository.png` — GitHub repository page

## Learning outcomes
API integration, HTTP status/error handling, JSON parsing, modular Python, rule-based alerting, CSV/JSON reporting, data visualization, REST API development, dashboard development, testing, Git and GitHub.

## Limitations and responsible use
- This is a learning/demo application, not a substitute for official meteorological warnings.
- Weather data availability, forecast horizon and API quotas depend on the provider and account.
- AQI, email/SMS notifications, database persistence and Next.js frontend are extension ideas.
- Do not use simulated values as real forecasts.
