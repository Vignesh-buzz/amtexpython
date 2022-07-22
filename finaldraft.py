import pymongo
from pymongo import MongoClient
class mongo:
#To make the connection
    def get_mongodb_connection(
            host: int,
            port: Union[str, int],
            user: str,
            password: str,

    ):
        return pymongo.MongoClient(
            host=host,
            port=int(port),
            username=user,
            password=password,
        )

    x = get_mongodb_connection('localhost', 27017, 'pallavi', '', 'filedata')
    print(x)
#This is to create tha database function
     def db(dbname,collectionname):
         myclient = MongoClient("mongodb://localhost:27017")
         dbname = myclient.get_database()
         collectionname = db.get_collection()
    db("amtexdemo","amtex")

