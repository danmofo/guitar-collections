from flask import Blueprint, session, render_template, abort, request

from project import db
from project.views import login_required
from project.models import Collection, Guitar
from project.collections.forms import EditCollectionForm

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
    return render_template('add.jinja.html')

@collections_blueprint.route('/browse', methods=['GET'])
def browse():
    return render_template('browse.jinja.html')

@collections_blueprint.route('/browse/<int:collection_id>')
def browse_specific(collection_id):
    collection = Collection.query.filter_by(id=collection_id).first()
    if collection is not None:
        return render_template('browse_specific.jinja.html', collection=collection)
    return abort(404)

# todo: refactor this slightly, lots of repeated logic
@collections_blueprint.route('/edit/<int:collection_id>', methods=['GET', 'POST'])
@login_required
def edit(collection_id):
    edit_collection_form = EditCollectionForm(request.form)
    collection = Collection.query.filter_by(id=collection_id).first()
    if collection is not None:
        if request.method == 'GET':
            if collection.user.id == session['user_id']:
                # This is really crap, can't find a better way..
                edit_collection_form.description.data = collection.description
                return render_template('edit.jinja.html',
                                        collection=collection,
                                        form=edit_collection_form)
            return 'You cant edit someone elses'
        if request.method == 'POST':
            # todo: verify user owns the collection
            pass

    return 'Collection doesnt exist!'

# This is probably really bad and I should think of a better way to do this!
@collections_blueprint.route('/edit/<int:collection_id>/add/<int:guitar_id>')
def add_guitar(collection_id, guitar_id):
    guitar = Guitar.query.filter_by(id=guitar_id).first()
    collection = Collection.query.filter_by(id=collection_id).first()

    return 'You want to add {} which is a {} {} {} , to collection {}'.format(
            guitar.id,
            guitar.model,
            guitar.brand,
            '({})'.format(guitar.year),
            collection.name
        )

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
