import pandas as pd

def get_pollution(coords: dict):
    """Return nearest sample AQI reading from CSV. This is a prototype stub."""
    df = pd.read_csv("sample_dataset/chennai_air_quality_sample.csv")
    # simple stub: return first row
    row = df.iloc[0]
    return {"station": row["station"], "AQI": int(row["AQI"])}
