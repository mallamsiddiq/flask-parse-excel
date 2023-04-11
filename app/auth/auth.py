from flask import render_template, request, redirect, session, flash,  url_for

from app import database as db, bcrypt

from app.models import User, Unit, Employment

from . import auth_blueprint


from flask_login import login_user, current_user, logout_user, login_required


@auth_blueprint.route('/users/create', methods = ['POST', 'GET'])
def create_user():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user_intance = db.session.query(User).filter_by(name = username).one_or_none()

        if user_intance:

            flash('User with this already exists')

            return render_template('posts/createuser.html', title = "POST")

        user_intance = User(name = username, password=hashed_password, salary = 30)

        db.session.add(user_intance)
        db.session.commit()

        flash(f'Account created succesfully for {user_intance.name}')

        return redirect(url_for("auth.login"))

    
    return render_template('posts/createuser.html', title = "POST")

@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.all_users'))

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        keep_me_in = 'keep_me_in' in request.form

        print(keep_me_in)

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = db.session.query(User).filter_by(name = username).one_or_none()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember = keep_me_in)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home.all_users'))

        flash(f'Invalid credentials')

    return render_template("posts/login.html")


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))