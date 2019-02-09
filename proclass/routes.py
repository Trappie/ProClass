from proclass import app
from flask import render_template, request, url_for, session, redirect
from proclass.models import User

@app.route('/')
def home(): # the root of the website
    if 'email' in session:
        return redirect(url_for('homepage'))
    return redirect(url_for('login'))

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    email = session['email']
    user = User.query.filter_by(email=email).first()
    return render_template('homepage.html', user=user)
    # if 'email' in session:
    #     user = User.query.filter_by(email=session['email'])
    #     return render_template('homepage.html', user=user)
    # else:
    #     return redirect()
def get_professors_by_class(class_name):
    return ['class1, 1', 'class2, 2', 'class3, 3']

def get_class_by_professor(professor_name):
    return ['professor1, 1', 'professor2, 2', 'professor3, 3']

@app.route('/class_search', methods=['GET', 'POST'])
def class_search():
    class_name = request.form['classinput']
    results = get_professors_by_class(class_name) # get the professor taught by the professor
    return render_template('searchresult.html', category='Class', name=class_name, results=results)

@app.route('/professor_search', methods=['GET', 'POST'])
def professor_search():
    professor_name = request.form['professorinput']
    results = get_class_by_professor(professor_name) # get the class taught by the professor
    return render_template('searchresult.html', category='Professor', name=professor_name, results=results)

@app.route('/user_search', methods=['GET', 'POST'])
def user_search():
    user_name = request.form['userinput']
    user = User.query.filter_by(username=username).first()
    if user:
        return "show the user's public portfolio"
    else:
        return "can't find user"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        print(user)
        if user and user.password == password:
            # login succeed
            session['email'] = email
            return redirect(url_for('homepage'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/my_portfolio')
def portfolio():
    if 'email' in session:
        print('in session')
    else:
        print('not in session')
    user = User.query.filter_by(email=session['email']).first()
    return render_template('my_portfolio.html', user=user)
