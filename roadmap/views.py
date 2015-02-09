"""
Views for the roadmap app
"""

from roadmap import app
from flask import render_template, url_for
#import models


@app.route('/')
def hello_world():
    return render_template('index.html')
