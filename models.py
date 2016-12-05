# models.py
from app import db
from sqlalchemy.dialects.postgresql import JSON
import datetime


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    due_date = db.Column(db.DateTime())
    duration = db.Column(db.Integer)
    risk = db.Column(db.Float())
    str_location = db.Column(db.String())

    def __init__(self, title, description, due_date, duration, risk, str_location):
        self.title = title
        self.description = description

        if isinstance(due_date, str):
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%S")
        self.due_date = due_date

        if isinstance(duration, str):
            duration = int(duration)
        self.duration = duration

        if isinstance(risk, str):
            risk = float(risk)
        self.risk = risk

        self.str_location = str_location

    def __repr__(self):
        return 'Task: {0} is due {1}. It will take {2} hours.'.format(self.title, self.due_date, self.duration)
