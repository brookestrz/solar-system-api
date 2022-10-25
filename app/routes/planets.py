from flask import Blueprint, jsonify,abort,make_response

class Planet:
    def __init__(self,id,name,description,known_moons):
        self.id = id
        self.name = name
        self.description = description
        self.known_moons = known_moons

    

PLANETS = [
    Planet(1,"Mercury","Closest planet to the sun",0),
    Planet(2,"Venus","Hottest planet", 0),
    Planet(3,"Earth"," The baddies live here!",1),
    Planet(4,"Mars","Really cold",2)


]

planets_bp = Blueprint("planets_bp",__name__,url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():  
    planets_response = [vars(planet) for planet in PLANETS]

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):

    return validate_planet(planet_id)
    
    #planet_id = int(planet_id)
    #for planet in PLANETS: 
        #if planet.id == planet_id:
            #return { "id": planet.id, "description": planet.description, 
                    #"known_moons": planet.known_moons
                


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in PLANETS:
        if planet.id == planet_id:
            return vars(planet)

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

