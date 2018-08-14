from flask import render_template,flash,redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'newUser'}
    posts = [
        {
            'owner':{'username':'newGuy'},
            'body':'some jacket'
        },
        {
            'owner' : {'username':'Guy'},
            'body': 'some other jacket'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign In',form=form)
