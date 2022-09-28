from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
 return render_template("index.html", current_time=datetime.utcnow())



@app.route('/user/<name>')
def user(name):
 return render_template("user.html", name=name)
 
 
#'<h1>Hello, {}!</h1>'.format(name)


if __name__ == "__main__":
    app.run()