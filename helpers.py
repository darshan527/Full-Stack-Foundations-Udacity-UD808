from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


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
