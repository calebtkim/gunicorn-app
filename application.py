import os
import datetime
from flask import Flask
import logging

if not os.path.isdir(os.environ.get('LOG_PATH', 'log')):
  os.mkdir(os.environ.get('LOG_PATH', 'log'))


app = Flask(__name__)

logger = logging.getLogger(__name__)


@app.route("/")
def index():
  return "Your Flask App Works!!"

@app.route("/hello")
def hello():
  logger.debug('The hello path was called')
  return "Hello World!"

@app.route("/other")
def other():
  logger.debug('The other path was called')
  return "You're viewing the other path!"


@app.route("/health")
def health():
  selected_date = datetime.datetime.now()
  logger.debug('The health path was called')
  return f'HealthCheck performed at: {selected_date}'


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=False)
