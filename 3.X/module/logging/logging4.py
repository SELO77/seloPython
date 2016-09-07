import logging
from mongoLogger import MongoHandler

print MongoHandler
if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(MongoHandler('mongolog','log'))
#    logger.debug('test debug')
#    logger.info('test info')
#    logger.warning('test warning')
    logger.error("error", {"name": "SELO", "phone": "010-7565-5583"}, [1,2,3,4,5], range(10))
