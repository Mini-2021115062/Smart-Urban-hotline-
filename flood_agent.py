import requests

def check_flood_risk(coords: dict):
    """Uses Open-Meteo hourly rainfall as a simple heuristic for flood risk."""
    lat, lon = coords.get("lat"), coords.get("lon")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=rain&forecast_days=1"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        rain_vals = data.get("hourly", {}).get("rain", [])
        rain = sum(rain_vals) if rain_vals else 0
    except Exception:
        # fallback: mark medium risk if API fails
        rain = None

    if rain is None:
        level = "MEDIUM"
    elif rain > 20:
        level = "HIGH"
    elif rain > 5:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {"rain_mm": rain, "risk_level": level}
