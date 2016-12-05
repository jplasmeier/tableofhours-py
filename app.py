from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

errors = []

from models import Task


def create_and_save_task(data):
    try:
        task = Task(data['title'], data['desc'], data['date'], data['duration'], data['risk'], data['location'])
        db.session.add(task)
        db.session.commit()
    except Exception as err:
        errors.append("Unable to add item to database: {}".format(err))


def get_all_tasks():
    try:
        return Task.query.all()
    except:
        errors.append("Unable to get any existing tasks")


@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == 'POST':
        try:
            data = request.form
            create_and_save_task(data)
        except Exception as err:
            errors.append("Error: {}".format(err))
    tasks = get_all_tasks()
    return render_template('index.html', errors=errors, results=results, tasks=tasks)


if __name__ == '__main__':
    app.run(port=6969)
