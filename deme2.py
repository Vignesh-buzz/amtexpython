"""import json
import pandas as pd
from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")
# database
db = myclient["sampledatbase"]
Collection = db["sample"]

# Loading or Opening the json file
df = pd.read_json('sample.json', lines=True)
#df = pd.read_json(r"C:/Users/VigneshNatchimuthu/PycharmProjects/pythonProject/sample.json")

with open('sample.json') as file:
    file_data = json.loads(file)

if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)
"""

import json

with open("test.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))
