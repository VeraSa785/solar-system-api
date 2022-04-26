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
    Planet(4, "Mars", 141.6, 693.96),
    Planet(5, "Jupiter", 462.31, 4346.36),
    Planet(6, "Saturn", 918.35, 10774.58),
    Planet(7, "Uranus", 1.8313, 30680.16),
    Planet(8, "Neptune", 2.7803, 60191.55)
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        # return {"msg": f"Invalid planet ID: {planet_id}"}
        rsp = {"msg": f"Invalid planet ID: {planet_id}"}
        # return jsonify(rsp), 400
    
    chosen_planet = None
    for planet in planets:
        if planet.id == planet_id:
            chosen_planet = planet
            break
    if chosen_planet is None:
        # return {"msg": f"Could not find planet with ID: {planet_id}"}
        
        rsp = {"msg": f"Could not find planet with ID: {planet_id}"}
        # return jsonify(rsp), 404
    
    

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
    return jsonify(planet_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    # planet = validate_planet(planet_id)
    rsp = validate_planet(planet_id)
    for planet in planets:
        if planet.id == planet.id:
            chosen_planet = planet
        
    rsp = {
        "id": chosen_planet.id,
        "name": chosen_planet.name,
        "distance_from_sun_million_mi": chosen_planet.distance_from_sun_million_mi,
        "length_of_year_earth_days": chosen_planet.length_of_year_earth_days
    }
    return jsonify(rsp), 200
    