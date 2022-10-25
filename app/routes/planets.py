from flask import Blueprint, jsonify

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


