from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Pizzas(db.Model):
    __tablename__ = "pizza"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    respizza = db.relationship("Restaurant_Pizzas", backref= "pizzas")

class Restaurants(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    respizza = db.relationship("Restaurant_Pizza", backref="restaurants")


class Restaurant_Pizzas(db.Column):
    __tablename__ = "respizza"

    id = db.Column(db.Integer, primary_key=True)
    price =db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"))








