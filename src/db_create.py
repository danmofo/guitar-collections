# This script creates the tables and populates with initial dummy data.
# Also doubles up as a test bed for queries
# todo: move half of this into tests

from project import db
from project.models import Guitar, Collection, User

from sqlalchemy.exc import IntegrityError

db.drop_all()
db.create_all()

# Add dummy users
# note: passwords are in plain text purely for the short-term
db.session.add_all([
    User('admin', 'd@d.com', 'password'),
    User('user123', 'user123@123.com', 'password'),
    User('super', 'd@dan.com', 'password', 2)
])

# Add dummy collections
db.session.add_all([
    Collection(
        'Personal collection!',
        'This is my first collection.', 1,
        'http://lorempixel.com/400/200'
    ),
    Collection(
        'My other collection',
        'This is my second collection.', 1,
        'http://lorempixel.com/400/200'
    ),
    Collection(
        'Fender Classics',
        'This is my third collection.', 1,
        'http://lorempixel.com/400/200'
    ),
    Collection(
        'Gibson Classics',
        'This is my fourth collection.', 1,
        'http://lorempixel.com/400/200'
    ),
    Collection(
        'Test Collection',
        'This is a test', 2
    )
])

db.session.commit()

admin = User.query.filter_by(id=1).first()
superuser = User.query.filter_by(id=3).first()
his = Collection.query.filter_by(id=1).first()
not_his = Collection.query.filter_by(id=5).first()

print admin.has_permission_to_edit(not_his)
print admin.has_permission_to_edit(his)
print superuser.has_permission_to_edit(not_his)
print superuser.has_permission_to_edit(his)

# Add dummy guitars
db.session.add_all([
    Guitar('Gibson', 'SG', 2014),
    Guitar('Gibson', 'Les Paul', 2000),
    Guitar('Gibson', '335', 2010),
    Guitar('Gibson', '339', 2000),
    Guitar('Fender', 'Stratocaster', 1966),
    Guitar('Fender', 'Telecaster', 1999),
    Guitar('Fender', 'Jaguar', 2000),
    Guitar('Fender', 'Firebird', 2015),
    Guitar('Harmony', 'Hollywood', 1966),
    Guitar('Gretch', 'Electromatic', 2014)
])

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

collection.remove_guitars(fenders)


db.session.commit()
