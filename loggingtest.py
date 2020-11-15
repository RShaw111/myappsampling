import logging
from time import gmtime, strftime

logging.basicConfig(filename='C:/Users/Explore/Desktop/Logtest/Logging.log',level=logging.INFO)

try:
    x = 3/1
    logging.info("Update successful at {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
except Exception as e:
    logging.warning("Error occured {}".format(e))
    
print('Done')