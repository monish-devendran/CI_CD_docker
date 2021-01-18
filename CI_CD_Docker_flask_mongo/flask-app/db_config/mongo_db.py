import pymongo
from pymongo import MongoClient


def init_db(hostname):
    client = MongoClient(host=hostname,port=27017)
    connect = client["FountainHead"]

    return connect