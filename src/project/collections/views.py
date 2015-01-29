from flask import Blueprint, session

from project import db
from project.views import login_required
from project.models import Collection

collections_blueprint = Blueprint(
    'collections',
    __name__,
    url_prefix='/collections',
    template_folder='../templates/collections',
    static_folder='../assets'
)

@collections_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    return 'Add a collection'

@collections_blueprint.route('/browse', methods=['GET'])
def browse():
    return 'Browse collections'

# todo: refactor this slightly, lots of repeated logic
@collections_blueprint.route('/edit/<int:collection_id>')
@login_required
def edit(collection_id):
    collection = Collection.query.filter_by(id=collection_id).first()
    if collection is not None:
        if collection.user.id == session['user_id']:
            return 'Editing collection id {}, it belongs to {}'.format(collection_id, collection.user.username)
        return 'You cant edit someone elses'

    return 'Collection doesnt exist!'

# todo: make POST only
@collections_blueprint.route('/delete/<int:collection_id>')
@login_required
def delete(collection_id):
    collection = Collection.query.filter_by(id=collection_id).first()
    if collection is not None:
        if collection.user.id == session['user_id']:
            # Dont know what cases this can fail in - todo: find out
            try:
                Collection.query.filter_by(id=collection_id).delete()
                db.session.commit()
            except:
                db.session.rollback()
            return 'Collection deleted!'
        else:
            return 'Cant delete what you don\'t own'
    return 'Collection doesnt exist!'
