import logging
import sys
from time import gmtime, strftime, sleep, time

from flask import Flask, jsonify
from prometheus_client import start_http_server, Summary, Counter, Histogram, Info

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


version = "1.0"

logger.info("Application is ready to receive traffic")


## Prometheus counter
call_counter = Counter("rest_calls", "Calls to service", ["method", "endpoint"])
root_histogram = Histogram("request_latency_root", "Request latency on root rest call")
json_histogram = Histogram("request_latency_json", "Request latency on json rest call")
i = Info("build", "Version of application")
i.info({"version": version})


logger.info("Starting prometheus server")
start_http_server(8000)

@app.route('/')
def hello_world():
    start = time()
    call_counter.labels("get", "/").inc()
    logger.info("Returning non json data")
    response = f"version: {version} timestamp: {strftime('%Y-%m-%d %H:%M:%S', gmtime())}"
    logger.info(f"data: {response}")
    end = time()
    elapsed = end - start
    logger.info(f"Call took {elapsed} seconds")
    root_histogram.observe(elapsed)
    return response


@app.route("/json")
def version_json():
    start = time()
    call_counter.labels("get", "/json").inc()
    logger.info("Returning json data")
    response = jsonify({"version": f"{version}", "timestamp": strftime("%Y-%m-%d %H:%M:%S", gmtime())})
    logger.info(f"data: {response}")
    response.headers.add('Access-Control-Allow-Origin', '*')
    end = time()
    elapsed = end - start
    logger.info(f"Call took {elapsed} seconds")
    json_histogram.observe(elapsed)
    return response


if __name__ == '__main__':
    logger.info('Starting application')
    app.run()
    logger.info('Application started')
