import os
from flask import Flask

import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler

logger = logging.getLogger(__name__)

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   logger.info('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   logger.info('Get name popup')
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       logger.info(f"Request for hello page received with name= {name}")  
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       logger.warning('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
       print('Healthcheck request')
       logger.info('Healthcheck request')
       return render_template('hello.html', name = 'healthcheck')

if __name__ == '__main__':
   app.run()
