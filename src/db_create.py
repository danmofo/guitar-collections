# This script creates the tables and populates with initial dummy data.
# Also doubles up as a test bed for queries

from project import db
from project.models import Guitar, Collection, User

from sqlalchemy.exc import IntegrityError

db.drop_all()
db.create_all()

# Add dummy users
# note: passwords are in plain text purely for the short-term
db.session.add(
    User('admin', 'd@d.com', 'password')
)

# Add dummy collections
db.session.add_all([
    Collection('My collection!', 'This is my first collection.', 1),
    Collection('My other collection', 'This is my second collection.', 1),
    Collection('Fender Classics', 'This is my third collection.', 1),
    Collection('Gibson Classics', 'This is my fourth collection.', 1),
])

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
    db.session.add(
        Guitar('Gretch', 'Electromatic', 2014)
    )
    db.session.commit()
except IntegrityError:
    db.session.rollback()

db.session.add(
    Guitar('Gretch', 'Electromatic', 2013)
)

collection = Collection.query.filter_by(id=1).first()

collection.guitars.append(
    Guitar.query.filter_by(id=1).first()
)

db.session.commit()
