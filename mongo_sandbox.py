from pymongo import MongoClient
#import json
#with open("/c/Users/gjasw/Desktop/Advanced DBSD/HW4/dataweb/.private.json","r") as f:
#    private = json.load(f)

#password = private[mongo]
#password = "Jaswanth2000"
client = MongoClient("mongodb+srv://jaswanth_dbms:Jaswanth2000@cluster0.1s2mqg8.mongodb.net/?retryWrites=true&w=majority")

from bson.objectid import ObjectId

shopping_db = client.shopping_db
list_collection = shopping_db.list_collection

list_collection.delete_many({})
list_collection.insert_many([
        { "description": 'apples' },
        { "description": 'broccoli' },
        { "description": 'pizza' },
        { "description": 'tangerine' },
        { "description": 'potatoes' }
    ])

items = list(list_collection.find())
print(items)