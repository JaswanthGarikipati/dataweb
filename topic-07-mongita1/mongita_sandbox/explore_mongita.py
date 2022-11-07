from mongita import MongitaClientDisk
client = MongitaClientDisk()
from bson.objectid import ObjectId
hello_world_db = client.hello_world_3_db
mongoose_collection = hello_world_db.mongoose_collection
mongoose_collection.insert_many([{'name':'Meercat','does_not_eat':'Snakes'},{'name':'Yellow mongoose', 'eats':'Snakes'}])

print("# docs = ",mongoose_collection.count_documents({}))

print("initial contents")

print(list(mongoose_collection.find({})))

print("updated contents")

mongoose_collection.update_one({'name':'Meercat'},{'$set':{"weight":2}})

print(list(mongoose_collection.find({})))

print("After deletion, remaining contents")

mongoose_collection.delete_one({'weight':{'$gt':1}})

print(list(mongoose_collection.find({})))