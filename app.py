from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import os
import requests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == 'POST':
        try:
            data = request.form
            print("Title: ", data['title'])
            print("Description: ", data['desc'])
            print("Due Date: ", data['date'])
            print("Duration: ", data['duration'])
            print("Risk Factor: ", data['risk'])
            print("Location: ", data['location'])
        except Exception as err:
            errors.append("Error: {}".format(err))
    return render_template('index.html', errors=errors, results=results)


if __name__ == '__main__':
    app.run(port=6969)
