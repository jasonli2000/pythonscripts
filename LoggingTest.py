import logging 
logger = logging.getLogger("Testing")

def initLogging(outputFileName):
    logger.setLevel(logging.DEBUG)
    fileHandle = logging.FileHandler(outputFileName)
    fileHandle.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandle.setFormatter(formatter)
    #set up the stream handle (console)
    consoleHandle = logging.StreamHandler()
    consoleHandle.setLevel(logging.INFO)
    consoleFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    consoleHandle.setFormatter(consoleFormatter)
    logger.addHandler(fileHandle)
    logger.addHandler(consoleHandle)
#======================================
if __name__ == '__main__':
    initLogging("C:/Temp/TestLogging.log")
    logger.warn("Test")
    logger.info("Test")
    logger.debug("Test")
    logger.error("Test")
    