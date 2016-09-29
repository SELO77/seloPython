# -*- coding: utf-8 -*-
import logging
import os
import json


from pymongo import MongoClient

#
MONGO_LOG_CONNECTION_INFO = {
    "HOST": 'localhost',
    "PORT": 27017,
    "DB": 'LOGTestDB',
}

# class JSONMessage(object):
#     def __init__(self, **kwargs):
#         self.kwargs = kwargs
#
#     def __str__(self):
#         return


# class MongoLogger():
class SELOLogger(object):

    def __init__(self, collection):
        self.mongoLogger = logging.getLogger()
        self.mongoLogger.setLevel(logging.DEBUG)
        self.mongoLogger.addHandler(MongoHandler(collection=collection))
        # You can add one more handler. ex) stream, file
        # if os.environ['MMT_ENV'] == "development":
        #     streamHandler = logging.StreamHandler()
        #     self.mongoLogger.addHandler(streamHandler)

    def create(self, **kwargs):
        # self.mongoLogger.info(args[1])
        self.mongoLogger.info(kwargs)
        # for v in kwargs.iteritems():
        #     print v
        #     # if i == 0:
        #     #     continue
        #     # if not isinstance(v, dict):
        #     #     raise TypeError('argument must be dict object')
        #     try:
        #         self.mongoLogger.info(v)
        #     except TypeError:
        #         pass

        # for v in kwargs.iteritems():
        #     self.mongoLogger.info({v[0]: v[1]})


class MongoHandler(logging.Handler):

    def __init__(self, host=MONGO_LOG_CONNECTION_INFO['HOST'],
                 port=MONGO_LOG_CONNECTION_INFO['PORT'],
                 db=MONGO_LOG_CONNECTION_INFO['DB'],
                 collection='None',
                 level=logging.NOTSET):
        logging.Handler.__init__(self, level)
        self.collection = MongoClient(host, port)[db][collection]

    def emit(self, record):
        # default
        # record_dict = record.__dict__.copy()
        # data = {
        #
        # }

        # extract args
        data = record.__dict__.copy()['msg']
        try:
            self.collection.save(data)
        except TypeError:
            pass

