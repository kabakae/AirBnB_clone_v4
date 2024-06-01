#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
import os
import uuid

app = Flask(__name__)

@app.route('/0-hbnb/')
def hbnb():
    cache_id = uuid.uuid4()
    if os.path.exists('web_dynamic/templates/0-hbnb.html'):
        template = '0-hbnb.html'
    else:
        template = '8-hbnb.html'
    return render_template(template, cache_id=cache_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
