from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
from flask_heroku import Heroku

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://wuynfrhtljkkam:8d5fc36b22f364af2961c3530eb30492b17b595b37bea1525755a28f0cd32525@ec2-174-129-255-59.compute-1.amazonaws.com:5432/d6toe3u0ta2f4e"

heroku = Heroku(app)
db = SQLAlchemy(app)

