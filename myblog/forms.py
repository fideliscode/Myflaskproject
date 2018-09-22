from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from myblog.models import User, Post

class RegisterForm(FlaskForm):
       username = StringField('username', validators=[DataRequired(), Length(min = 2, max = 30)])
       email = StringField('Email', validators=[DataRequired(), Email()])
       password = PasswordField('password', validators=[DataRequired()])
       confirmpassword = PasswordField('confirmpassword', validators=[DataRequired(), EqualTo('password')])
       submit = SubmitField('sign up') 	

       def validate_username(self, username):
       		user =User.query.filter_by(username=username.data).first()
       		if user:
       			raise ValidationError("the username is already taken,choose another one")

       def validate_email(self, email):
       		user =User.query.filter_by(email=email.data).first()
       		if user:
       			raise ValidationError("the email  already exists")



class LoginForm(FlaskForm):
       email = StringField('email', validators=[DataRequired(), Email()])
       password = PasswordField('password', validators=[DataRequired()])
       remember =BooleanField('remember')
       submit = SubmitField('signin')