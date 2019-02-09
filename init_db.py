from proclass import db
from proclass.models import User, Post


user1 = User(username='di', email='diw26@pitt.edu', password='a', year=2017, credit=10)

user2 = User(username='duo', email='duz5@pitt.edu', password='a', year=2016, credit=20)

db.create_all()
db.session.add(user1)
db.session.add(user2)
db.session.commit()

