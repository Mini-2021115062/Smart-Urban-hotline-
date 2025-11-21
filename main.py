from fastapi import FastAPI, HTTPException
from agents.geo_agent import get_coordinates
from agents.flood_agent import check_flood_risk
from agents.pollution_agent import get_pollution
from agents.traffic_agent import get_traffic_status
from agents.safety_agent import generate_safety_advice
import uvicorn

app = FastAPI(title="Smart Urban Hotline")

@app.get("/urban_hotline")
async def hotline(location: str):
    try:
        coords = get_coordinates(location)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Geocoding failed: {e}")

    flood = check_flood_risk(coords)
    air = get_pollution(coords)
    traffic = get_traffic_status(coords)
    safety = generate_safety_advice(flood, air, traffic)

    return {
        "location": location,
        "coordinates": coords,
        "flood_risk": flood,
        "air_quality": air,
        "traffic": traffic,
        "safety_advice": safety
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
