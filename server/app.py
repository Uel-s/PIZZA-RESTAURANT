from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from model import db, Pizzas, Restaurant_Pizzas, Restaurants

app = Flask(__name__) #initializes app
app. config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)

pass


if __name__ == "__main__":
    app.run(port=5555, debug=True)