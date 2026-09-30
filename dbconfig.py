from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask("__name__")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_BINDS'] = {'clients': 'sqlite:///clients.db'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

class book(database.Model):
    id = database.Column(database.Integer,  primary_key=True)
    title = database.Column(database.String(300), nullable = False)
    readme = database.Column(database.String(500), nullable = True)
    author = database.Column(database.String(200), nullable = False)
    price = database.Column(database.Float, nullable = False)
    category= database.Column(database.String(200), nullable = True)
    cover = database.Column(database.String(200), nullable=True)

class client(database.Model):
    __bind_key__ = 'clients'
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(300), nullable = False)
    number = database.Column(database.Integer, nullable = False)
    addr =database.Column(database.String(400), nullable = False)
    title = database.Column(database.String(300), nullable = True)
    quantity = database.Column(database.Integer, nullable= True)




with app.app_context():
    database.create_all()
    if(True):
        print("data base created !!!!!")




