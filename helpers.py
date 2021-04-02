from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def printDishes():
    items = session.query(MenuItem).all()
    for item in items:
        print(item.name)


def printRestaurant():
    items = session.query(Restaurant).all()
    for item in items:
        print(item.name)


def addRestaurant(resturantName):
    temp = Restaurant(name=resturantName)
    session.add(temp)
    session.commit()


def addMenuItem(
    name=None, id=None, course=None, description=None, price=None, restaurant_id=None
):
    temp = MenuItem(
        name=name,
        description=description,
        course=course,
        price=price,
        restaurant_id=restaurant_id,
    )
    session.add(temp)
    session.commit()
