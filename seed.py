import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        db.session.query(RestaurantPizza).delete()
        db.session.query(Restaurant).delete()
        db.session.query(Pizza).delete()

        pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
        pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
        db.session.add_all([pizza1, pizza2])
        db.session.commit()

        restaurant1 = Restaurant(name="Luigi's", address="123 Italy St")
        restaurant2 = Restaurant(name="Mario's", address="456 Rome Ave")
        db.session.add_all([restaurant1, restaurant2])
        db.session.commit()

        rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
        rp2 = RestaurantPizza(price=15, pizza_id=pizza2.id, restaurant_id=restaurant2.id)
        db.session.add_all([rp1, rp2])
        db.session.commit()

        print("✅ Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
