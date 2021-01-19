# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

import traintime


# create a Flask instance
"Setting up the keys are needed for the database"
app = Flask(__name__)
app.config['SECRET_KEY'] = ':)'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
Bootstrap(app)
db = SQLAlchemy(app)
records = []

"Initialize Database with specific Items"


class items(db.Model):
    id = db.Column('item_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.Float(200))


def __init__(self, station, time, line):
    self.name = station
    self.id = time
    self.type = line



"Create Database"
db.create_all()


class ItemForm(FlaskForm):
    name = StringField('station', validators=[InputRequired(), Length(min=1,max=15)])
    type = StringField('type', validators=[InputRequired(), Length(min=1,max=80)])





