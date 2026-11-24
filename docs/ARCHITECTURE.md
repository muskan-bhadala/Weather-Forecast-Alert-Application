# Architecture

```text
User / CLI / Streamlit / API client
              |
              v
       Input: city + mode
              |
       +------+------+
       |             |
  Simulation     OpenWeatherMap
       |          Geocoding + Current
       |          + 5-day Forecast
       +------+------+
              |
        Normalized JSON
              |
       Forecast + threshold rules
              |
       Alerts + JSON/CSV report
              |
       CLI / FastAPI / Streamlit + chart
```

The application defaults to deterministic simulation so it works without an API key. API mode uses OpenWeatherMap's geocoding, current-weather and 5-day/3-hour forecast endpoints. Rain probability is taken from the forecast `pop` field. AQI is not included in this starter version; it can be added with the provider's air-pollution endpoint and an explicit AQI scale.
