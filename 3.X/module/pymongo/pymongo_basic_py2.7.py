import pymongo
import traceback

client = pymongo.MongoClient('localhost', 27017)
db = client.test_database


result = db.test_collection.save({"test_v": 28})

# AWS LAMBDA FNC
def lambda_handler(event, context):
    name = event.get('name')
    return "hello %s"%name
