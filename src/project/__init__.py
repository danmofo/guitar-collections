from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__, static_folder='assets')
bcrypt = Bcrypt(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from project import views, models
from project.users.views import users_blueprint
from project.account.views import account_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(account_blueprint)
