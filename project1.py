import json

from pymongo import MongoClient

with open(r"C:\Users\VigneshNatchimuthu\PycharmProjects\amtexdemo\venv\file.json") as file:
    file_data = json.load(file)

myclient = MongoClient("mongodb://localhost:27017")
db = myclient.get_database("amtex")
sample_collection = db.get_collection("amtexdemo")
sample_collection.insert_one(file_data)
