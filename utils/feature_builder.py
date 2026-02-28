import pandas as pd
from datetime import datetime

def build_features(
    distance,
    cab_type,
    source,
    destination,
    weather
):
    now = datetime.now()

    data = {
        "distance": distance,
        "cab_type": cab_type,
        "source": source,
        "destination": destination,
        "hour": now.hour,
        "day_of_week": now.weekday(),
        "is_weekend": 1 if now.weekday() >= 5 else 0,
        "temp": weather["temp"],
        "rain": weather["rain"],
        "is_rainy": 1 if weather["rain"] > 0 else 0,
        "humidity": weather["humidity"],
        "wind": weather["wind"],
        "pressure": weather["pressure"],
        "clouds": weather["clouds"]
    }

    return pd.DataFrame([data])
