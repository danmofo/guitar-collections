from project import db

collection_guitars = db.Table('collection_guitars',
    db.Column('collection_id', db.Integer, db.ForeignKey('collections.id')),
    db.Column('guitar_id', db.Integer, db.ForeignKey('guitars.id'))
)

class User(db.Model):

    __tablename__ = 'users'

    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String, unique=True, nullable=False)
    password    = db.Column(db.String, nullable=False)
    role        = db.Column(db.Integer, default=1)
    collections = db.relationship('Collection', backref='collections', lazy='dynamic')

    def __init__(self, email, password, role):
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
    created_on  = db.Column(db.Date, default=datetime.utcnow())
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'))
    guitars     = db.relationship('Guitar',
                                    secondary='collection_guitars')

    def __init__(self, name, created_on, user_id, guitars=[]):
        self.name = name
        self.created_on = created_on
        self.user_id = user_id
        self.guitars = guitars

    def __repr__(self):
        return '<Collection {}>'.format(self.name)


class Guitar(db.Model):

    __tablename__ = 'guitars'

    id      = db.Column(db.Integer,primary_key=True)
    brand   = db.Column(db.String, nullable=False)
    model   = db.Column(db.String, nullable=False)

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return '<Guitar {}, {}>'.format(self.brand, self.model)
