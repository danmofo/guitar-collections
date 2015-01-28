from project import db

# student_identifier = db.Table('student_identifier',
#     db.Column('class_id', db.Integer, db.ForeignKey('classes.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('students.id'))
# )

# class Student(db.Model):

#     __tablename__ = 'students'

#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(64))
#     lastname = db.Column(db.String(64))
#     email = db.Column(db.String(128), unique=True)

#     def __init__(self, firstname, lastname, email):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.email = email

# class Class(db.Model):

#     __tablename__ = 'classes'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), unique=True)
#     children = db.relationship("Student",
#                     secondary=student_identifier)

#     def __init__(self, name, children=[]):
#         self.name = name
#         self.children = children

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
