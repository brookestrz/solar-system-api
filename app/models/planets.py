
# class Planet:
#     def __init__(self,id,name,description,known_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.known_moons = known_moons

    

# PLANETS = [
#     Planet(1,"Mercury","Closest planet to the sun",0),
#     Planet(2,"Venus","Hottest planet", 0),
#     Planet(3,"Earth"," The baddies live here!",1),
#     Planet(4,"Mars","Really cold",2)






# @planets_bp.route("", methods=["GET"])
# def get_all_planets():  
#     planets_response = [vars(planet) for planet in PLANETS]

#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):

#     return validate_planet(planet_id)
    
    #planet_id = int(planet_id)
    #for planet in PLANETS: 
        #if planet.id == planet_id:
            #return { "id": planet.id, "description": planet.description, 
                    #"known_moons": planet.known_moons
                


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         return abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in PLANETS:
#         if planet.id == planet_id:
#             return vars(planet)

#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))


from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    known_moons = db.Column(db.Integer)
    moon_id = db.Column(db.Integer, db.ForeignKey('moon.id'))
    moon = db.relationship("Moon", back_populates="planets")


    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["known_moons"] = self.known_moons

        return planet_as_dict

    # # @classmethod
    # def from_dict(cls, book_data):
    #     new_book = Book(title=book_data["title"],
    #                     description=book_data["description"])
    #     return new_book

