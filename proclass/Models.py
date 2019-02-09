# file for data models in the database

from datetime import datetime
from proclass import db

# the data model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    major = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(5000))
    rate_post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"email: {self.email}, username: {self.username}"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True, nullable=False)


# the data model for professor
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    difficulty = db.Column(db.Integer, nullable=False) # 1 to 10
    lecture = db.Column(db.Integer, nullable=False) # 1 to 10
    organization = db.Column(db.Integer, nullable=False) # 1 to 10


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), unique=True, nullable=False)

class Professor_course(db.Model):
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False)
