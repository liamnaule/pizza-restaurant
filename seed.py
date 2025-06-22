from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Clear existing data
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()
    db.session.commit()

    # Create Pizzas (based on potential IDs from POST request)
    pizza1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    db.session.add(pizza1)
    db.session.commit()

    # Create Restaurants (based on potential IDs from POST request)
    restaurant1 = Restaurant(name="Kiki's Pizza", address="address3")
    restaurant2 = Restaurant(name="Karen's Pizza Shack", address="address1")
    db.session.add_all([restaurant1, restaurant2])
    db.session.commit()

    # Create RestaurantPizza (based on POST request example)
    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    db.session.add(rp1)
    db.session.commit()

    print("Database seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()