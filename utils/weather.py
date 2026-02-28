import pandas as pd

_weather_df = None

def load_weather_data():
    global _weather_df
    if _weather_df is None:
        df = pd.read_csv("weather.csv")
        df["datetime"] = pd.to_datetime(df["time_stamp"], unit="s")
        df["hour"] = df["datetime"].dt.hour
        _weather_df = df
    return _weather_df

from datetime import datetime

def get_weather_from_dataset(location):
    df = load_weather_data()

    current_hour = datetime.now().hour

    subset = df[
        (df["location"] == location) &
        (df["hour"] == current_hour)
    ]

    if subset.empty:
        subset = df[df["location"] == location]

    row = subset.sample(1).iloc[0]

    return {
        "temp": row["temp"],
        "rain": row["rain"],
        "humidity": row["humidity"],
        "wind": row["wind"],
        "pressure": row["pressure"],
        "clouds": row["clouds"]
    }
