# This script creates the tables and populates with initial dummy data.
# Also doubles up as a test bed for queries
# todo: move half of this into tests

from project                    import db
from project.models             import Guitar, Collection, User
from project.mock.collection    import dummy_collections
from project.mock.user          import dummy_users
from project.mock.guitar        import dummy_guitars

from sqlalchemy.exc             import IntegrityError

db.drop_all()
db.create_all()

# Add dummy users
db.session.add_all(dummy_users)
db.session.commit()

# Add dummy collections
db.session.add_all(dummy_collections)
db.session.commit()

# Add dummy guitars
db.session.add_all(dummy_guitars)
db.session.commit()

try:
    db.session.add(Guitar('Gretch', 'Electromatic', 2014))
    db.session.commit()
except IntegrityError:
    db.session.rollback()

db.session.add(
    Guitar('Gretch', 'Electromatic', 2013)
)

collection = Collection.query.filter_by(id=1).first()

gibsons = Guitar.query.filter_by(brand='Gibson').all()
fenders = Guitar.query.filter_by(brand='Fender').all()

collection.add_guitars(gibsons)
collection.add_guitars(fenders)

Collection.query.filter_by(id=2).first().add_guitars([
    Guitar.query.filter_by(id=5).first(),
    Guitar.query.filter_by(id=6).first(),
    Guitar.query.filter_by(id=7).first()
])

Collection.query.filter_by(id=3).first().add_guitars([
    Guitar.query.filter_by(id=10).first(),
    Guitar.query.filter_by(id=9).first(),
])

Collection.query.filter_by(id=4).first().add_guitars([
    Guitar.query.filter_by(id=1).first(),
    Guitar.query.filter_by(id=10).first(),
])

Collection.query.filter_by(id=5).first().add_guitar(
    Guitar.query.filter_by(id=3).first()
)

db.session.commit()
