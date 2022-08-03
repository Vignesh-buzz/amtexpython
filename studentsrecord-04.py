import sys
import csv
from pymongo import MongoClient

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

DB_NAME = 'SCHOOL1'
COLLECTION_NAME = 'SCHOOLDBCL1'
FILENAME = 'test.csv'
#COLUMNS = ('emp ID','FirstName','LastName','Technology','Project name','Emp age','Company Name','Designation','Leaves')
def connect_mongo():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

def read_csv():
    reader = open(r'C:\Users\VigneshNatchimuthu\PycharmProjects\amtexdemo\venv\testfile.csv', 'r')
    return csv.DictReader(reader)
def save_to_mongo():
    collection = connect_mongo()
    data = read_csv()
    result = collection.insert_many(data)
    print(result)
def create():
    #To create the value in database
    COLLECTIONS = connect_mongo()
    reg=COLLECTIONS.insert_one({"EMPID":112,"FIRSTNAME":'vignesh',"LASTNAME":'Natchimuthu',"TECHNOLOGY":'Python',"PROJECTNAME":'PCC',"EMPAGE":26,"COMPANYNAME":'amtex',"DESIGNATION":'associate developer',"LEAVES":2})
    print(reg)
def read():
    
    #To read the value in database
    collection = connect_mongo()
    # Read data with limit
    rd = collection.find().limit(2)
    print(rd)
    print(rd.next())
    print(rd.next())
    # Read data with required fields
    rd1 = collection.find({}, {"FIRSTNAME": True, "_id": False})
    print(rd1)
    print(rd1.next())
    print(rd1.next())
    # Read data with given condition
    rd2 = collection.find_one({"$or": [{"FIRSTNAME": 'Adam'}, {'EMPAGE': 26}]})
    print(rd2)

def delete():
    # To delete the value in database
    collection = connect_mongo()
    query = {"LASTNAME": "Kelvin"}
    y = collection.delete_many(query)
    for d in collection.find():
           print(d)
def update():
    #To update the value in database
    collection = connect_mongo()
    myquery = {"name":"vignesh"}
    newvalue = {"$set":{"name":"vinu"}}
    collection.update_one(myquery,newvalue)
    for result in collection.find():
        print(result)
connect_mongo()
read_csv()
save_to_mongo()
create()
delete()
read()
update()
