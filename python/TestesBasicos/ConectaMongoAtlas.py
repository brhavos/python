

import pymongo
from pymongo import MongoClient

#uri = "mongodb+srv://<username>:<password>@cluster0.ahz1ode.mongodb.net/?retryWrites=true&w=majority"
#uri = "mongodb+srv://db-teste:aaa111@cluster0.ahz1ode.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient("mongodb+srv://db-teste:aaa111@cluster-test.fndbj.mongodb.net/UserData?retryWrites=true&w=majority")

db = cluster["db-teste"]
collection = db["cidades"]

collection.insert_one({"_id":998, "nome":"aaaaa"})
collection.insert_one({"_id":999, "nome":"bbbbb"})

