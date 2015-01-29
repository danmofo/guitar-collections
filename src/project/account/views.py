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
    return render_template('dashboard.html')

@account_blueprint.route('/details')
@login_required
def details():
    return render_template('account_details.html')
