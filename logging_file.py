import logging, sys
from time import gmtime, strftime, time

timestart = time()

if sys.argv[1] in ('dev', 'sit', 'prd'):
    print('Environment available')
else:
    print("Environment not available")
    sys.exit()


logging.basicConfig(filename='C:/Users/Explore/Desktop/Logtest/Logging.log',level=logging.INFO)

try:
    x = 3/1
    logging.info("      {} snzMains Updated successfully in {} environment, command took {}sec".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), sys.argv[1], round(time() - timestart, 5)))
except Exception as e:
    logging.warning("   {} Error {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), e))

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print(round(time() - timestart, 5), "sec")
print(sys.argv[1])