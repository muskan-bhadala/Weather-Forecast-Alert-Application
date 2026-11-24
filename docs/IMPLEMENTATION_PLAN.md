# Fast implementation plan

| Phase | Work | Expected proof |
|---|---|---|
| 1 Setup | Create venv and install requirements | successful installation |
| 2 Structure | Open this folder in VS Code | folder screenshot |
| 3 API key | Copy `.env.example` to `.env` only if using live mode | key configured locally |
| 4 Fetch | Run simulation first, then API mode if key available | terminal output |
| 5 Parse | Inspect normalized current/forecast dictionaries | JSON report |
| 6 Analyze | Review forecast records and temperature chart | CSV and chart |
| 7 Alerts | Adjust thresholds in `.env` and rerun | alert messages |
| 8 Visualize | Run Streamlit | dashboard screenshot |
| 9 API/report | Run FastAPI and inspect `/docs` | API docs + report |
| 10 GitHub | Commit code, docs and safe screenshots | repository page |

Suggested six-day proof schedule:
- Day 1: setup and project structure — `Initial project structure and dependencies`
- Day 2: API integration — `Add OpenWeatherMap integration`
- Day 3: parsing and reports — `Normalize weather data and export reports`
- Day 4: alerts and tests — `Add weather risk rules and tests`
- Day 5: dashboard and charts — `Add dashboard and forecast visualization`
- Day 6: README and GitHub — `Complete documentation and project evidence`

For a fast submission, all starter files are already included: run simulation, tests, API and dashboard, capture screenshots, then publish.
