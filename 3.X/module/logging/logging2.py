import logging
import logging.handlers


logger = logging.getLogger('mylogger')

formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')


fileHandler = logging.FileHandler('./loggerTest2.log')
streamHandler = logging.StreamHandler()


fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)


logger.addHandler(fileHandler)
logger.addHandler(streamHandler)


logger.setLevel(logging.DEBUG)
logger.debug("==========")
logger.create("TEST START")
logger.warning("Stream")
logger.error("file?")
logger.create("TEST END")
logger.debug("==========")
