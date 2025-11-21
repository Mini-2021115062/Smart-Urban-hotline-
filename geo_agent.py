from geopy.geocoders import Nominatim

def get_coordinates(location: str):
    """Resolve a short location string to lat/lon. Appends city name to improve accuracy."""
    geolocator = Nominatim(user_agent="urban_hotline_agent")
    loc = geolocator.geocode(f"{location}, Chennai")
    if not loc:
        raise ValueError("Location not found")
    return {"lat": loc.latitude, "lon": loc.longitude}
