from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy.exc import IntegrityError

from project import bcrypt, db
from project.views import login_required
from project.models import User

from forms import RegisterForm, LoginForm

users_blueprint = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    template_folder='templates',
    static_folder='../assets'
)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    login_form = LoginForm(request.form)

    if request.method == 'GET':
        return render_template('login.html', form=LoginForm(request.form))

    if request.method == 'POST':
        if login_form.validate_on_submit():
            user = User.query.filter_by(
                username=login_form.username.data
            ).first()

            if user is not None:
                session['logged_in'] = True
                session['user_id'] = user.id
                flash('You have successfully logged in!')
                return redirect(url_for('account.dashboard'))
            else:
                error = 'Invalid username or password, please try again'
                return render_template('login.html', form=login_form, error=error)
        else:
            return render_template('login.html', form=login_form)

@users_blueprint.route('/logout', methods=['GET'])
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
        session.pop('user_id', None)
        flash('You have been logged out successfully.')
        return redirect(url_for('users.login'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm(request.form)
    if request.method == 'GET':
        return render_template('register.html', form=register_form)

    if request.method == 'POST':
        if register_form.validate_on_submit():
            new_user = User(
                register_form.username.data,
                register_form.email.data,
                register_form.password.data
            )

            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thank you for registering, please login.')
                return redirect(url_for('users.login'))
            except IntegrityError:
                error = 'Username or email already exist, please pick another email.'
                return render_template('register.html', form=register_form, error=error)
        else:
            return render_template('register.html', form=register_form)
