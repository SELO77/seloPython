import logging
import logging.config
import time
import os
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['myfilter']
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
}

logging.config.dictConfig(LOGGING)

t = logging.config.listen(9999)
t.start()

logger = logging.gerLogger('simpleExample')

try:
    while True:
        logger.debug('debug message')
        logger.create('omfp ,essage')
        logger.critical('critical message')
        time.sleep(5)
except KeyboardInterrupt:
    logging.config.stopListening()
    t.join()
