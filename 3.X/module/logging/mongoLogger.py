import logging
from pymongo import MongoClient
#from bson import invalidDocument


class MongoHandler(logging.Handler):

    def __init__(self, db='mongologtest', collection='log', host='localhost', port=27017, level=logging.NOTSET):
        logging.Handler.__init__(self, level)
        self.collection = MongoClient(host, port)[db][collection]

    def emit(self, record):
        data = record.__dict__.copy()
#        print data
#        print type(data)

        self.collection.save(data)

#if __name__ == "__main__":
#    MongoHandler('mongolog', 'test')
