from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class EditUserDetailsForm(Form):
    username = TextField(
        'Username',
        validators=[DataRequired()]
    )
