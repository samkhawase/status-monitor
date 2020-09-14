import requests
import logging
import os
import datetime
import time
from http import HTTPStatus
from flask import Flask, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    log_level = logging.WARN

    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)

    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    log_file = os.path.join(logdir, 'app.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    app.logger.addHandler(handler)

    app.logger.setLevel(log_level)

def check_status(url):
    try:
        status = requests.get(url, timeout=30)
        return status
    except requests.ConnectionError:
        return None

@app.route('/', methods=['GET'])
def get_status():
    # Provide the magnificient URL here, 
    # TODO: prefereably through a settings file.
    url = 'https://httpbin.org/status/500'
    with app.app_context():
        status = check_status(url)
        print(status)
        if status is not None:
            status_string = f'Timestamp: {time.ctime()}, status: {status.status_code}'            
            if status.status_code is not HTTPStatus.OK:
                app.logger.error(f'Timestamp: {time.ctime()}, status: {status.status_code}')
                return render_template('index.html', status_string = status_string)

        return render_template('index.html', status_string = 'Cannot reach URL')

scheduler = BackgroundScheduler()
scheduler.add_job(func=get_status, trigger="interval", seconds=3)
scheduler.start()
