from project import db

from sqlalchemy import UniqueConstraint

collection_guitars = db.Table('collection_guitars',
    db.Column('collection_id', db.Integer, db.ForeignKey('collections.id')),
    db.Column('guitar_id', db.Integer, db.ForeignKey('guitars.id'))
)

class User(db.Model):

    __tablename__ = 'users'

    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String, unique=True, nullable=False)
    email       = db.Column(db.String, unique=True, nullable=False)
    password    = db.Column(db.String, nullable=False)
    role        = db.Column(db.Integer, default=1)
    collections = db.relationship('Collection', backref='collections', lazy='dynamic')

    def __init__(self, username, email, password, role=1):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User {}>'.format(self.email)

class Collection(db.Model):

    from datetime import datetime

    __tablename__ = 'collections'

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    image_url   = db.Column(db.String)
    created_on  = db.Column(db.Date, default=datetime.utcnow())
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'))
    user        = db.relationship('User', backref='added_by')
    guitars     = db.relationship('Guitar',
                                    secondary='collection_guitars')

    def __init__(self, name, description, user_id, image_url=None):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.image_url = image_url

    def __repr__(self):
        return '<Collection {}>'.format(self.name)


class Guitar(db.Model):

    __tablename__   = 'guitars'
    __table_args__  = (UniqueConstraint('model', 'year', name='unique_guitar'),)

    id          = db.Column(db.Integer,primary_key=True)
    brand       = db.Column(db.String, nullable=False)
    model       = db.Column(db.String, nullable=False)
    year        = db.Column(db.Integer, nullable=False)
    collections = db.relationship('Collection',
                                    secondary='collection_guitars')

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return '<Guitar {}, {}>'.format(self.brand, self.model)
