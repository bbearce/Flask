# from flask import Flask, render_template, flash, redirect, url_for
import flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_login import UserMixin

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['USERNAME'] = "bbearce"
app.config['PASSWORD'] = "secret"


# Form Management
class MyForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


# Views
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        log_in_status = flask.session['logged_in']
    except KeyError:
        log_in_status = False

    return flask.render_template('index.html', logged_in=log_in_status)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form=MyForm()
    if flask.request.method == 'POST':
        if flask.request.form['username'] != app.config['USERNAME']:
            flask.flash('Invalid Username')
        elif flask.request.form['password'] != app.config['PASSWORD']:
            flask.flash('Invalid password')
        else:
            flask.session['logged_in'] = True
            flask.flash('You were logged in')
            return flask.redirect(flask.url_for('index'))
    return flask.render_template('login.html', form=form)

@app.route('/logout')
def logout():
    flask.session.pop('logged_in', None)
    flask.flash('You were logged out')
    return flask.redirect(flask.url_for('index'))

@app.route('/secret')
def secret():
    try:
        log_in_status = flask.session['logged_in']
    except KeyError:
        log_in_status = False

    if log_in_status == True:
        flask.flash('You made it!!!')
        return flask.render_template('secret.html')
    else:
        flask.flash('You need to be logged in to see that page.')
        return flask.redirect(flask.url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)












