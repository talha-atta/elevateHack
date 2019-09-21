from flask import Flask, render_template, url_for, request, redirect, session, logging, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
		return render_template('STUlogin.html')

@app.route('/frontenddev', methods=['GET', 'POST'])
def frontenddev():
		return render_template('frontenddev.html')

@app.route('/match', methods=['GET', 'POST'])
def match():
		return render_template('STUmatch.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
		return render_template('STUprofile.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
		return render_template('STUregister.html')

@app.route('/training', methods=['GET', 'POST'])
def training():
		return render_template('training.html')

#BUSINESS ADMIN PAGES
@app.route('/Blogin', methods=['GET', 'POST'])
def Blogin():
		return render_template('BUSlogin.html')

@app.route('/Bprofile', methods=['GET', 'POST'])
def Bprofile():
		return render_template('BUSprofile.html')

@app.route('/Bregister', methods=['GET', 'POST'])
def Bregister():
		return render_template('BUSregister.html')


if __name__ == "__main__":
    app.debug = True
    db.create_all()
    app.secret_key = '123'
    app.run(host='0.0.0.0')

