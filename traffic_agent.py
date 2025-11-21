import json

def get_traffic_status(coords: dict):
    """Return sample traffic status from JSON file."""
    with open("sample_dataset/traffic_data_sample.json") as f:
        data = json.load(f)
    return {"status": data.get("traffic_status")}
