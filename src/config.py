import os
from dotenv import load_dotenv
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "").strip()
BASE_URL = "https://api.openweathermap.org"
MAX_TEMP_C = float(os.getenv("MAX_TEMP_C", "38"))
MIN_TEMP_C = float(os.getenv("MIN_TEMP_C", "5"))
HIGH_HUMIDITY = int(os.getenv("HIGH_HUMIDITY", "85"))
RAIN_PROBABILITY = int(os.getenv("RAIN_PROBABILITY", "70"))
HIGH_WIND_KMH = float(os.getenv("HIGH_WIND_KMH", "50"))
