import os
import logging
import logging.handlers


logger = logging.getLogger('mylogger')

formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

if os.environ['MMT_ENV'] == 'local':
    loggerLevel = logging.DEBUG
    filename = './logger3_local.log'
elif os.environ['MMT_ENV'] == 'development':
    loggerLevel = logging.DEBUG
    filename = './logger3_dev.log'
else:
    loggerLevel = logging.INFO
    filename = './logger3_else.log'

fileHandler = logging.FileHandler(filename)
streamHandler = logging.StreamHandler()
