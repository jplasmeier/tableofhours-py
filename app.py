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
        print('data in: ', data)
        task = Task(data['title'], data['desc'], data['date'], data['duration'], data['risk'], data['location'])
        print('task before add', task)
        db.session.add(task)
        db.session.commit()
        print("task after commit ", task)
        print("tasl dicgt", task.__dict__)
        task.__dict__.pop('_sa_instance_state')
        return task.__dict__
    except Exception as err:
        errors.append("Unable to add item to database: {}".format(err))


def get_all_tasks():
    try:
        tasks = Task.query.all()
        tasks_dict = {}
        for task in tasks:
            task.__dict__.pop('_sa_instance_state', None)
            task_dict = task.__dict__
            tasks_dict[task_dict['id']] = task_dict
        return tasks_dict
    except:
        errors.append("Unable to get any existing tasks")


def get_task_by_id(id):
    """
    Return a task
    :param id:
    :return:
    """
    try:
        task_obj = Task.query.filter_by(id=id).first()
        task_dict = task_obj.__dict__
        task_dict.pop('_sa_instance_state', None)
        return task_dict
    except:
        errors.append("Unable to return task id: {}".format(id))


@app.route('/', methods=['GET', 'POST'])
def index():
    return read_tasks()


# Task Endpoints


@app.route('/task', methods=['POST'])
def create_task():
    data = request.json
    task = create_and_save_task(data)
    print("errs", errors)
    return jsonify(results=task)


@app.route('/task', methods=['GET'])
def read_tasks():
    tasks_dict = get_all_tasks()
    return jsonify(results=tasks_dict)


@app.route('/task/<id>', methods=['GET'])
def read_task(id):
    task_dict = get_task_by_id(id)
    return jsonify(results=task_dict)


@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    pass


@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    pass


if __name__ == '__main__':
    app.run(port=6969)
