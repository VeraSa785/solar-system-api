from flask import Blueprint, jsonify, make_response, abort, request
from requests import session
from app.models.planets import Planet
from app import db

# class Planet:
#     def __init__(self, id, name, distance_from_sun_million_mi, length_of_year_earth_days):
#         self.id = id
#         self.name = name
#         self.distance_from_sun_million_mi = distance_from_sun_million_mi
#         self.length_of_year_earth_days = length_of_year_earth_days

# planets = [
#     Planet(1, "Mercury", 35.98, 88),
#     Planet(2, "Venus", 67.24, 225),
#     Planet(3, "Earth", 92.96, 365.24),
#     Planet(4, "Mars", 141.6, 693.96),
#     Planet(5, "Jupiter", 462.31, 4346.36),
#     Planet(6, "Saturn", 918.35, 10774.58),
#     Planet(7, "Uranus", 1.8313, 30680.16),
#     Planet(8, "Neptune", 2.7803, 60191.55)
# ]

def get_planet_or_abort(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"msg": f"Invalid planet ID: {planet_id}"}, 400))
    planet = Planet.query.get(planet_id)
    if planet is None:
        abort(make_response({"msg": f"Could not find planet with ID: {planet_id}"}, 404))
    return planet
    

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_one_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                distance_from_sun_million_mi=request_body["distance_from_sun_million_mi"],
                length_of_year_earth_days=request_body["length_of_year_earth_days"])
    db.session.add(new_planet)
    db.session.commit()
    return{
        "id": new_planet.id,
        "msg": f"Succesfully creates Planet with id {new_planet}"
        },201

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "distance_from_sun_million_mi": planet.distance_from_sun_million_mi,
            "length_of_year_earth_days": planet.length_of_year_earth_days
        })
    return jsonify(planets_response), 300


# get_planet_or_abort(planet_id)


# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "distance_from_sun_million_mi": planet.distance_from_sun_million_mi,
#             "length_of_year_earth_days": planet.length_of_year_earth_days
#         })
#     return jsonify(planet_response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = get_planet_or_abort(planet_id)
        
    rsp = {
        "id": planet.id,
        "name": planet.name,
        "distance_from_sun_million_mi": planet.distance_from_sun_million_mi,
        "length_of_year_earth_days": planet.length_of_year_earth_days
    }
    return jsonify(rsp), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def put_one_planet(planet_id):
    planet = get_planet_or_abort(planet_id)
    request_body = request.get_json()
    try:
        planet.name = request_body["name"]
        planet.distance_from_sun_million_mi = request_body["distance_from_sun_million_mi"]
        planet.length_of_year_earth_days = request_body["length_of_year_earth_days"]
    except KeyError:
        return {
            "msg" : "name, distance from the sun, and length of year are required"
        }, 400
        
    db.session.commit()
    return {
            "msg" : f"planet #{planet_id} successfully replaced"
        }, 200
    
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = get_planet_or_abort(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return {
            "msg" : f"planet #{planet_id} successfully deleted"
        }, 200
    
    
    