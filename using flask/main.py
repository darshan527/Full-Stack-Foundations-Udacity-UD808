from flask import Flask
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker
from database_setup import Base, Restaurant, MenuItem
import cgi

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
