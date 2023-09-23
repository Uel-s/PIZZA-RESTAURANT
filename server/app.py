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