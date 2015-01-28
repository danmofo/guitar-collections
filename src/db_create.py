# This script creates the tables and populates with initial dummy data
from project import db
from project.models import Guitar, Collection, User

from datetime import datetime

db.drop_all()
db.create_all()

# note: passwords are in plain text purely for the short-term
db.session.add(
    User('danmofo@gmail.com', 'mypassword', 1)
)

db.session.add(
    User('foobar@gmail.com', 'mypassword', 2)
)

db.session.add(
    Collection('My collection!', datetime.utcnow(), 1)
)

db.session.add(
    Collection('My other collection', datetime.utcnow(), 1)
)

db.session.add(Guitar('Gibson', 'SG'))
db.session.add(Guitar('Gibson', 'Les Paul'))
db.session.add(Guitar('Gibson', '335'))
db.session.add(Guitar('Gibson', '339'))
db.session.add(Guitar('Fender', 'Stratocaster'))
db.session.add(Guitar('Fender', 'Telecaster'))
db.session.add(Guitar('Fender', 'Jaguar'))
db.session.add(Guitar('Fender', 'Firebird'))
db.session.add(Guitar('Harmony', 'Hollywood'))
db.session.add(Guitar('Gretch', 'Electromatic'))


db.session.commit()
