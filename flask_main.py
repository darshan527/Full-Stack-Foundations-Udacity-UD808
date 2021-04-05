from flask import Flask
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker
from database_setup import Base, Restaurant, MenuItem
import cgi

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def HelloWorld():
    return "Hello Worlllld!"


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port="8080")
