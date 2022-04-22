from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, distance_from_sun_million_mi, length_of_year_earth_days):
        self.id = id
        self.name = name
        self.distance_from_sun_million_mi = distance_from_sun_million_mi
        self.length_of_year_earth_days = length_of_year_earth_days

planets = [
    Planet(1, "Mercury", 35.98, 88),
    Planet(2, "Venus", 67.24, 225),
    Planet(3, "Earth", 92.96, 365.24),
    Planet(4, "Mars", 141.6, 693.5)
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "distance_from_sun_million_mi": planet.distance_from_sun_million_mi,
            "length_of_year_earth_days": planet.length_of_year_earth_days
        })
    return jsonify(planet_response)