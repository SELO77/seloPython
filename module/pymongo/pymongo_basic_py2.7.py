import pymongo
import traceback

client = pymongo.MongoClient('localhost', 27017)
db = client.test_database

print(type(db))

print db.name
result = db.test_collection.save({"test_v": 28})
print result

# AWS LAMBDA FNC
def lambda_handler(event, context):
    name = event.get('name')
    print timeit.default_timer()
    return "hello %s"%name
