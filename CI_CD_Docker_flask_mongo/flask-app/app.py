from flask import Flask, jsonify, request
from db_config import mongo_db
from bson.json_util import dumps,loads
import json

app = Flask(__name__)

db = mongo_db.init_db(hostname = "mongo_db_application")

@app.route("/")
def welcome():
    return "welcome app !"


@app.route("/get", methods = ["GET"])
def getall():
    r=  db.demo.find()
    out = dumps(r)
    return out


@app.route("/post", methods = ["POST"])
def postdata():
    content = request.json
    print(content)
    db.demo.insert(content)
    return "inserted"




