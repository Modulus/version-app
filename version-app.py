from flask import Flask
import logging
import sys
from time import gmtime, strftime


app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


@app.route('/')
def hello_world():
    return 'Version: {} @ {}\n'.format(2.0, strftime("%Y-%m-%d %H:%M:%S", gmtime()))


if __name__ == '__main__':
    logger.info('Starting application')
    app.run()
    logger.info('Application started')
