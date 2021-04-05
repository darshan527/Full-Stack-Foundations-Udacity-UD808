from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker
from database_setup import Base, Restaurant, MenuItem
import cgi

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Restaurant's Methods
def addRestaurant(resturantName):
    """
    Adds a new Restaurant to the database.
    """
    temp = Restaurant(name=resturantName)
    session.add(temp)
    session.commit()


def printRestaurant():
    """
    Prints all the Restaurant Names
    from the Restaurant table.
    """

    items = session.query(Restaurant).all()
    if items:
        for item in items:
            print(item.name)
    else:
        print("Restaurants Not Found")


def getRestaurant():
    """
    Returns a List of all Restaurant Names
    """

    items = session.query(Restaurant).all()
    if items:
        l = []
        for item in items:
            l.append(item.name)
        return l
    else:
        return []


def deleteRestaurant(RestaurantName):
    temp = session.query(Restaurant).filter_by(name=RestaurantName).one()
    print(temp.name, "is being DELETED...")
    session.delete(temp)
    session.commit()
    print("Deleted Sucessfully")


def findRestaurant(RestaurantName):
    """
    Checks whether the Restaurant
    is present in the Database or not.
    If not present then message is printed
    else the list of Restaurants will be printed.
    """

    temp = session.query(Restaurant).filter_by(name=RestaurantName).all()
    if not temp:
        print("Restaurant Not Found")
    else:
        for item in temp:
            print(item.name)


# Menu Item Methods
def addMenuItem(
    name=None, id=None, course=None, description=None, price=None, restaurant_id=None
):
    """
    Adds a new Menu Item to the Database,
    each item is associated with a restaurant.
    """

    temp = MenuItem(
        name=name,
        description=description,
        course=course,
        price=price,
        restaurant_id=restaurant_id,
    )
    session.add(temp)
    session.commit()


def printDishes():
    """
    Prints all the available dishes
    from the MenuItem Table
    """

    items = session.query(MenuItem).all()
    for item in items:
        print(item.name)