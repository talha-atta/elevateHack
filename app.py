from flask import Flask, render_template, url_for, request, redirect, session, logging, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



#USER PAGES
@app.route('/', methods=['GET', 'POST'])
def home():
		return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
		return render_template('login.html')

@app.route('/match', methods=['GET', 'POST'])
def match():
		return render_template('match.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
		return render_template('profile.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
		return render_template('register.html')

@app.route('/rating', methods=['GET', 'POST'])
def rating():
	if request.method == 'POST':
		return results()
	else:
		return render_template('rating.html')

@app.route('/result', methods=['GET', 'POST'])
def results():
	data = random.randrange(2, 6, 1)
	return render_template('result.html', data=data)




if __name__ == "__main__":
    app.debug = True
    db.create_all()
    app.secret_key = '123'
    app.run(host='0.0.0.0')

