from app import db
from app.models.planets import Planet
from app.models.moon import Moon
from flask import Blueprint, jsonify, make_response, request, abort

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        known_moons=request_body["known_moons"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    
    planets = Planet.query.all()
    print(planets)
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name":planet.name, 
            "description": planet.description,
            "known_moons":planet.known_moons
        })
    #if not planets_response:
        #return make_response("Invalid request",400)
    return jsonify(planets_response)
    # print(planets_response)
    # return {"hello": "hi"}
    # return make_response(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet{planet_id} not found"}, 404))

    return planet


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description":planet.description,
        "known_moons":planet.known_moons
    }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.known_moons = request_body["known_moons"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"planet #{planet.id} successfully deleted")




@moons_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()
    new_moon = (Moon(size=request_body["size"],
                 description=request_body["description"]))
                    

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} successfully created"), 201)

@moons_bp.route("", methods=["GET"])
def read_all_moons():
    
    moons = Moon.query.all()

    moons_response = []
    for moon in moons:
        moons_response.append(
       {
                "size": moon.size,
                "description": moon.description
            })
    
    return jsonify(moons_response)
