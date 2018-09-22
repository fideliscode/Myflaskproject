from flask import Flask, render_template, url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#creating an instance of flask
app= Flask(__name__)

app.config['SECRET_KEY']= '7f8aada424bdc6c59ad74394c1f1f46a'
#where the database is located
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
#creating the database instance
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
db = SQLAlchemy(app)

from myblog import routes