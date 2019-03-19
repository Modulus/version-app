from flask import Flask, jsonify
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


version = "2.0"

logger.info("Application is ready to receive traffic")


@app.route('/')
def hello_world():
    logger.info("Returning non json data")
    response = f"version: {version} timestamp: {strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
    logger.info(f"data: {response}")
    return


@app.route("/json")
def version_json():
    logger.info("Returning json data")
    response = jsonify({"version": f"{version}", "timestamp": strftime("%Y-%m-%d %H:%M:%S", gmtime())})
    logger.info(f"data: {response}")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    logger.info('Starting application')
    app.run()
    logger.info('Application started')
