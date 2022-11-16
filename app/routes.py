from flask import render_template
from app import app

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