from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy.exc import IntegrityError

from project import db
from project.views import login_required
from project.models import User, Collection, Guitar

from forms import EditUserDetailsForm

account_blueprint = Blueprint(
    'account',
    __name__,
    url_prefix='/account',
    template_folder='../templates/account',
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
    return render_template('dashboard.jinja.html', user=user)

@account_blueprint.route('/details', methods=['GET', 'POST'])
@login_required
def details():
    edit_user_details_form = EditUserDetailsForm(request.form)
    user = User.query.filter_by(id=session['user_id']).first()
    error = None

    if request.method == 'POST':
        if user is not None:
            if edit_user_details_form.validate_on_submit():
                # todo: move all of this logic to the models
                try:
                    new_username = edit_user_details_form.username.data
                    user.username = new_username
                    db.session.commit()
                    flash('Details updated successfully')
                    session['username'] = new_username
                except IntegrityError:
                    db.session.rollback()
                    error = 'Username already exists. Pick another!'

    return render_template('details.jinja.html', user=user,
                                                form=edit_user_details_form,
                                                error=error)

@account_blueprint.route('/my_collections')
@login_required
def my_collections():
    collections = Collection.query.filter_by(user_id=session['user_id']).all()
    return render_template('my_collections.jinja.html', collections=collections)
