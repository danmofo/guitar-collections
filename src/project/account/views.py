from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from project import db
from project.views import login_required
from project.models import User, Collection, Guitar

account_blueprint = Blueprint(
    'account',
    __name__,
    url_prefix='/account',
    template_folder='templates',
    static_folder='../assets'
)

# this should probably live on the web server level
@account_blueprint.route('/')
def index():
    return redirect(url_for('account.dashboard'))

@account_blueprint.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(id=session['user_id']).first()
    return render_template('dashboard.html', user=user)

@account_blueprint.route('/details')
@login_required
def details():
    user = User.query.filter_by(id=session['user_id']).first()
    return render_template('details.html', user=user)

@account_blueprint.route('/my_collections')
@login_required
def my_collections():
    collections = Collection.query.filter_by(user_id=session['user_id']).all()
    return render_template('my_collections.html', collections=collections)
