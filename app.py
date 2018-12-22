from flask import Flask
from flask import render_template, request
from flask_pymongo import PyMongo 
import os 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://52.57.83.2:27017/hoodcops"
mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/subscribe", methods=["POST"])
def process_subscription():
    pass
    