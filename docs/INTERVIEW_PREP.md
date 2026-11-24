# Interview preparation

## Explain your project
I built a Weather Forecast & Alert Application in Python. It can run in offline simulation mode or retrieve live weather from OpenWeatherMap. The application normalizes current and forecast JSON, checks configurable thresholds for heat, cold, humidity, rain probability and wind, then exposes the result through a CLI, FastAPI and an optional Streamlit dashboard. It also saves JSON and CSV reports and a temperature chart.

## 10 interview questions and answers

1. **What problem does the project solve?** It demonstrates how weather information can be converted into understandable, rule-based risk notifications for planning.
2. **How does an API request work?** The client sends an HTTP request with query parameters and an API key; the server returns JSON, which the application validates and parses.
3. **Why use JSON?** It is a lightweight structured format that maps naturally to Python dictionaries and lists.
4. **Why use `requests`?** It simplifies HTTP requests, query parameters, timeouts and response handling.
5. **How are alerts generated?** A rule engine compares normalized values against configurable thresholds and creates alert records when a rule is met.
6. **Why use environment variables?** They keep secrets and environment-specific configuration out of source code.
7. **What is FastAPI used for?** It exposes weather and alert functionality as REST endpoints and automatically provides OpenAPI/Swagger documentation.
8. **Why create CSV and JSON reports?** CSV supports spreadsheet analysis; JSON preserves nested structured data and alerts.
9. **How did you test without a live API?** I created deterministic sample weather data that exercises heat, humidity, rain and wind rules, then wrote pytest tests.
10. **What would you improve next?** Add AQI with a documented scale, scheduled refresh, database history, user-defined alert settings, email/SMS notifications, caching and deployment.

## HR explanation
This project helped me practice building a complete Python application rather than only writing isolated scripts. I worked on API integration, data processing, error handling, visualization, automated tests and GitHub documentation. I also included simulation mode so the application can be demonstrated without relying on an external service.
