# file for data models in the database

from datetime import datetime
from proclass import db

# the data model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    credit = db.Column(db.Integer, nullable=False)


# the data model for professor
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), unique=True, nullable=False)

class ProClass(db.Model):
    professor_id = db.Column(db.Integer, primary_key=True, nullable=False)
