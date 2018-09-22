from flask import render_template, url_for, flash, redirect, request
from myblog.models import User, Post
from myblog import app, db, bcrypt, login_manager
from myblog.forms import RegisterForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


posts = [{
    'title': 'mouthful',
    'content': 'content mouthful is mouthful',
    'author': 'author is goin to be mouthful too',
    'date_posted': '2018-04-09'
},
    {
    'title': 'noisy',
    'content': 'content noisy isnoisy',
    'author': 'author is goin to be noisy too',
    'date_posted': '2018-04-09'
}]


@app.route("/")
@app.route("/home")
def Home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def About():
    return render_template('about.html', posts=posts, title="about")


@app.route("/register", methods=['GET', 'POST'])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f'successful created account for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Home'))
        else:
            flash('Incorrect email or password', 'danger')
    return render_template('login.html', title="login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html', title="account")
