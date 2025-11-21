# Safety agent uses an LLM (Gemini or Gemma) to convert structured inputs into human-readable safety advice.
# This is a simple local stub; in production you would call Vertex AI's Generative Models APIs.

def generate_safety_advice(flood: dict, air: dict, traffic: dict):
    parts = []
    parts.append(f"Flood risk: {flood.get('risk_level')} (rain:{flood.get('rain_mm')})")
    parts.append(f"AQI at station {air.get('station')}: {air.get('AQI')}")
    parts.append(f"Traffic: {traffic.get('status')}")
    parts.append("")
    parts.append("Recommendations:")
    if flood.get("risk_level") == "HIGH":
        parts.append("- Avoid low-lying roads and move to higher ground.")
        parts.append("- Monitor local alerts and seek emergency help if needed.")
    elif flood.get("risk_level") == "MEDIUM":
        parts.append("- Exercise caution; avoid traveling through waterlogged streets.")
    else:
        parts.append("- Normal conditions, but be cautious during heavy showers.")

    aqi = air.get('AQI') or 0
    if aqi > 150:
        parts.append("- AQI is unhealthy. Reduce outdoor activity; wear mask if sensitive.")
    return "\n".join(parts)
