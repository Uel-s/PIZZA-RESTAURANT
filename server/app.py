from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from model import db, Pizzas, Restaurant_Pizzas, Restaurants


app = Flask(__name__) #initializes app
app. config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


@app.route("/")
def index():
    return "<h1>The Pizza Place</h1>"

class Restaurant(Resource):
    
    def get(self):
        restaurants = Restaurants.query.all()
        index = []
        for restaurant in restaurants:
            data = {
                "id":restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
                }
            index.append(data) 

           
        return make_response (jsonify(index),200)

api.add_resource(Restaurant,"/restaurants")


class RestaurantId(Resource):
    def get(self, id):
        restaurant = Restaurants.query.get(id)
        if restaurant:
            data = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": [
                    {
                        "id": pizza.id,
                        "name": pizza.pizzas.name,  # Access the 'name' attribute from the associated Pizza object
                        "ingredients": pizza.pizzas.ingredients  # Access the 'ingredients' attribute from the associated Pizza object
                    }
                    for pizza in restaurant.respizza
                ],
            }
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)


api.add_resource(RestaurantId, "/resid/<int:id>")   


class Restaurant_Delete(Resource):
    
    def delete(self, id):

        res_delete = Restaurants.query.filter_by(id=id).first()

        if res_delete:

            for respizza in res_delete.respizza:
                db.session.delete(respizza)
                db.session.commit()
                return make_response("",204)

        else: 
            return make_response(jsonify({"error":"Restaurant not found"})) 

api.add_resource(Restaurant_Delete,"/deleteres/<int:id>") 


class Pizza_Get(Resource):

    def get (self):

        pizzas = Pizzas.query.all()
        pizza_dict = []
        for n in pizzas:
            data = {
                "id":n.id,
                "name":n.name,
                "ingredients":n.ingredients
            }

            pizza_dict.append(data)

            return make_response(jsonify(pizza_dict),200)


    

api.add_resource(Pizza_Get,"/pizza")        



class Restaurant_pizza(Resource):

     def post(self):

        data = request.get_json ()

        new_data = Restaurant_Pizzas(
            price= data["price"],
            pizza_id = data["pizza_id"],
            restaurant_id = data["restaurant_id"]
        ) 

        db.session.add(new_data)
        db.session.commit()

        return make_response("", 201)

api.add_resource(Restaurant_pizza,"/restaurant_pizzas")



if __name__ == "__main__":
    app.run(port=5555, debug=True)