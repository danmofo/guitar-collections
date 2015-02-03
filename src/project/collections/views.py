from flask import Blueprint, session, render_template, abort, request, flash, redirect, url_for

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
    collections = Collection.query.all()
    return render_template('browse.jinja.html',
                            collections=collections)

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
    collection_query = Collection.query.filter_by(id=collection_id)
    collection = collection_query.first()

    # Collection doesnt exist
    if collection is None:
        flash('Collection doesnt exist.')
        return redirect(url_for('collections.browse'))

    # Probably quicker to just compare against session['user_id']
    if collection.user.has_permission_to_edit(collection):
        if request.method == 'GET':
            # This is really crap, can't find a better way..
            edit_collection_form.description.data = collection.description
            return render_template('edit.jinja.html',
                                    collection=collection,
                                    form=edit_collection_form)
        if request.method == 'POST':
            collection_query.update({
                'name': edit_collection_form.name.data,
                'description': edit_collection_form.description.data
            })
            db.session.commit()
            flash('Collection updated successfully.')
            return redirect(url_for('collections.edit', collection_id=collection_id))


    # User doesn't have sufficient permissions
    flash('You dont have permission to edit this collection!')
    return redirect(url_for('collections.browse_specific',
                            collection_id=collection_id))

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
@collections_blueprint.route('/edit/<int:collection_id>/delete/<int:guitar_id>', methods=['GET'])
def remove_guitar(collection_id, guitar_id):
    guitar = Guitar.query.filter_by(id=guitar_id).first()
    collection = Collection.query.filter_by(id=collection_id).first()

    if session['user_id'] == collection.user.id:
        collection.remove_guitar(guitar)
        db.session.commit()
        flash('Guitar removed from collection')

    return redirect(url_for('collections.edit', collection_id=collection_id))




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
