"""
Roadmap's main flask app.


"""

import os
from porc import Client
from flask import Flask
from flask.ext.appconfig import AppConfig


def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)
    return app


app = create_app()

# mail = Mail(app)
# db = SQLAlchemy(app)


client = Client(app.config['ORCHESTRATE_KEY'])
client.ping().raise_for_status()

import roadmap.views


if __name__ == '__main__':
    app.run()
