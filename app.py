from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from utilities import new_alchemy_encoder

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
        return task
    except Exception as err:
        errors.append("Unable to add item to database: {}".format(err))


def get_all_tasks():
    try:
        return Task.query.all()
    except:
        errors.append("Unable to get any existing tasks")


def get_task_by_id(id):
    """
    Return a task
    :param id:
    :return:
    """
    try:
        return Task.query.filter_by(id=id).first()
    except:
        errors.append("Unable to return task id: {}".format(id))


@app.route('/', methods=['GET', 'POST'])
def index():
    return read_tasks()


# Task Endpoints


@app.route('/task', methods=['POST'])
def create_task():
    data = request.form
    task = create_and_save_task(data)
    return jsonify(task, cls=new_alchemy_encoder(), check_circular=False)


@app.route('/task', methods=['GET'])
def read_tasks():
    tasks = get_all_tasks()
    tasks_dict = {}
    for task in tasks:
        task.__dict__.pop('_sa_instance_state', None)
        task_dict = task.__dict__
        tasks_dict[task_dict['id']] = task_dict
    return jsonify(results=tasks_dict)


@app.route('/task/<id>', methods=['GET'])
def read_task(id):
    print('Getting task ', id)
    task = get_task_by_id(id)
    task.__dict__.pop('_sa_instance_state', None)
    return jsonify(results=task.__dict__)


@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    pass


@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    pass


if __name__ == '__main__':
    app.run(port=6969)
