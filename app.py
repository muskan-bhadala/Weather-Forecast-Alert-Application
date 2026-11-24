"""Optional Streamlit dashboard. Run: streamlit run app.py"""
import streamlit as st
import pandas as pd
from src.sample_data import get_sample_weather
from src.weather_service import fetch_weather
from src.alerts import generate_alerts
from src.reports import save_report
from src.visualization import create_forecast_chart

st.set_page_config(page_title="Weather Alert Dashboard", page_icon="🌦️", layout="wide")
st.title("🌦️ Weather Forecast & Alert Application")
st.caption("Educational project using public weather data or offline simulation.")
city = st.text_input("Enter city", "Jaipur")
mode = st.selectbox("Data source", ["simulation", "api"])
if st.button("Get weather", type="primary"):
    try:
        data = get_sample_weather(city) if mode == "simulation" else fetch_weather(city)
        alerts = generate_alerts(data)
        save_report(data, alerts)
        c1, c2, c3 = st.columns(3)
        c1.metric("Temperature", f"{data['current']['temperature_c']} °C")
        c2.metric("Humidity", f"{data['current']['humidity']}%")
        c3.metric("Wind", f"{data['current']['wind_speed_kmh']} km/h")
        st.subheader(f"Current conditions — {data['city']}")
        st.write(data["current"]["description"])
        st.subheader("Weather alerts")
        if alerts:
            for a in alerts:
                st.warning(f"{a['level']} — {a['type']}: {a['message']}")
        else:
            st.success("No threshold alerts.")
        df = pd.DataFrame(data["forecast"])
        st.subheader("Forecast")
        st.dataframe(df, use_container_width=True)
        chart = create_forecast_chart(data)
        if chart.startswith("images/"):
            st.image(chart, caption="Forecast temperature chart")
        st.success("Report saved in reports/ and outputs/.")
    except Exception as exc:
        st.error(str(exc))
