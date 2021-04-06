from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)


engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/hello")
def HelloWorld():
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ""
    for i in items:
        output += i.name + "</br>" + i.price + "</br>" + i.description
        output += "</br></br>"
    return output


@app.route("/restaurant/<int:restaurant_id>/")
def getRestaurantById(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)

    return render_template("menu.html", restaurant=restaurant, items=items)


@app.route("/restaurant/<int:restaurant_id>/addItem/", methods=["GET", "POST"])
def addMenuItem(restaurant_id):
    if request.method == "POST":
        newItem = MenuItem(name=request.form["name"], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for("getRestaurantById", restaurant_id=restaurant_id))
    else:
        return render_template("addMenuItemForm.html", restaurant_id=restaurant_id)


@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/editItem/")
def editMenuItem(restaurant_id, menu_id):
    return "Pass editMenuItem"


@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/deleteItem/")
def deleteMenuItem(restaurant_id, menu_id):
    pass


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
