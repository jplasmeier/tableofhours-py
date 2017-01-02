from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import logger

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CAT_TASK = "Tasks"
CAT_EVENT = "Events"


from models import Task


def create_and_save_task(data):
    try:
        task = Task(data['title'], data['desc'], data['date'], data['duration'], data['risk'], data['location'])
        print('task before add', task)
        db.session.add(task)
        db.session.commit()
        task.__dict__.pop('_sa_instance_state')
        return task.__dict__
    except Exception as err:
        logger.log_error(CAT_TASK, err)

def get_all_tasks_dict():
    try:
        tasks = Task.query.all()
        tasks_dict = {}
        for task in tasks:
            task.__dict__.pop('_sa_instance_state', None)
            task_dict = task.__dict__
            tasks_dict[task_dict['id']] = task_dict
        return tasks_dict
    except Exception as err:
        logger.log_error(CAT_TASK, err)


def get_task_dict_by_id(id):
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
    except Exception as err:
        logger.log_error(CAT_TASK, "Unable to return task of id {0}: {1}".format(id, err))


def update_task_by_id(id, task_dict):
    """
    Return a task in database
    :param id:
    :return:
    """
    task_object = Task.query.get(id).update()

    return task_dict


@app.route('/', methods=['GET', 'POST'])
def index():
    return read_tasks()


# Task Endpoints


@app.route('/task', methods=['POST'])
def create_task():
    data_dict = request.json
    task = create_and_save_task(data_dict)
    return jsonify(results=task)


@app.route('/task', methods=['GET'])
def read_tasks():
    tasks_dict = get_all_tasks_dict()
    return jsonify(results=tasks_dict)


@app.route('/task/<id>', methods=['GET'])
def read_task(id):
    task_dict = get_task_dict_by_id(id)
    return jsonify(results=task_dict)


@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    updated_task_dict = update_task_by_id(id, request.json)
    return jsonify(results=updated_task_dict)

@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    pass


if __name__ == '__main__':
    app.run(port=6969)
