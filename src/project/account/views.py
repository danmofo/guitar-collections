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

@account_blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
