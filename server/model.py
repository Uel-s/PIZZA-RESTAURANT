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

    respizza = db.relationship("Restaurant_Pizzas", backref= "pizzas", lazy=True)



    def  __repr__ (self):
        return f"Pizzas(id={self.id}, name={self.name}, ingredients{self.ingredients})"

class Restaurants(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique = True, nullable = False)
    address = db.Column(db.String)

    respizza = db.relationship("Restaurant_Pizza", backref="restaurants", lazy=True)

    @validates("name")
    def validate_name(self, key, name):
    
        if len(name) > 50:
            raise ValueError("Must have a name less than 50 words")    
        return name

    def __repr__(self):
        return f"Restaurant(id={self.id}, name={self.name}, address={self.address})"


class Restaurant_Pizzas(db.Model):
    __tablename__ = "respizza"

    id = db.Column(db.Integer, primary_key=True)
    price =db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"))

    @validates("price")
    def validate_price(self, key, price):
        if not (1 <= price <= 30 ):
            raise ValueError("Price Must Be Between 1 and 30")

        return price    




    def __repr__(self):
        return f"Restaurant_Pizzas(id={self.id}, price={self.price})"








