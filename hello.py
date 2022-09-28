from email.message import EmailMessage
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Email
 
class NameForm (FlaskForm): 
    name = StringField('What is your name?', validators=[DataRequired()]) 
    email = StringField('What is your UofT email address?', validators=[DataRequired(), Email()]) 
    submit = SubmitField('Submit')



app = Flask(__name__)
app.config['SECRET_KEY'] = 'ali'
moment = Moment(app)
bootstrap = Bootstrap(app)



@app.route('/' , methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_email = session.get('email')
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))


    emailMessage = ""
    enteredEmail = session.get('email')
    if enteredEmail is None:
        pass
    elif enteredEmail.find("utoronto") == -1:
        emailMessage = "Please enter a UofT email"
    else:
        emailMessage = "your UofT email is " +  enteredEmail

    return render_template('index.html',
        form = form, name = session.get('name'), emailMessage = emailMessage)





@app.route('/user/<name>')
def user(name):
 return render_template("user.html", name=name)
 
 
#'<h1>Hello, {}!</h1>'.format(name)


if __name__ == "__main__":
    app.run()