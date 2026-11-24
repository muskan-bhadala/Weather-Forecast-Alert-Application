from src.alerts import generate_alerts
from src.sample_data import get_sample_weather

def test_sample_weather_triggers_heat_and_humidity():
    alerts = generate_alerts(get_sample_weather("Jaipur"))
    kinds = {a["type"] for a in alerts}
    assert "HEAT" in kinds
    assert "HUMIDITY" in kinds
    assert "RAIN" in kinds

def test_alerts_returns_list():
    assert isinstance(generate_alerts(get_sample_weather()), list)
