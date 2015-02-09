from flask import flash, redirect, session, url_for, render_template, request, make_response, session
from functools import wraps
from random import randint

from project        import app, db
from project.models import Collection, Guitar

# helpers
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        print session
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

@app.route('/',)
def index():
    if 'logged_in' in session:
        return redirect(url_for('collections.browse'))

    featured_collections = Collection.query.filter_by(featured=1).limit(4).all()
    random_guitar = Guitar.query.filter_by(id=randint(1, 10)).first()

    return render_template('home.jinja.html',
                            featured_collections=featured_collections,
                            random_guitar=random_guitar)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.jinja.html')

# todo: add logging
@app.errorhandler(404)
def page_not_found(error):
    print error
    return render_template('404.jinja.html'), 404

# todo: add logging
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.jinja.html'), 500
