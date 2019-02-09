from proclass import app
from flask import render_template, request, url_for
from proclass.models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        user = User.quest.filter_by(email=email).first()
        if user and user.password == password:
            # login succeed
            session['email'] = email
            return redirect(url_for('home'))


    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))
