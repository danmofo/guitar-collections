from project import app, db

from flask import flash, redirect, session, url_for, render_template, request, make_response
from functools import wraps

# helpers
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))


@app.route('/',)
def index():
    return render_template('home.html')

# todo: add logging
@app.errorhandler(404)
def page_not_found(error):
    print error
    return render_template('404.html'), 404

# todo: add logging
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
