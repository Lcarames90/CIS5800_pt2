from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

@app.route('/')

@app.route('/index')
def index():
    user = { 'username': 'Lee'}

    posts = [
        {
            'author': {'username': 'Jefferson'},
            'body':'Table Plus & CockroachDB are foreign to me'
        },
        {
            'author':{'username': 'Avinash'},
            'body':'Lee, hurry up!'
        },

        {
            'author':{'username': 'Lee'},
            'body': 'Sorry Professors!'
        },
    ]
    return render_template('index.html', title = 'Home', user=user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login requested for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
            return redirect(url_for('index'))
        login_user(user, remember = form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)