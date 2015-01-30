from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired

class EditCollectionForm(Form):
    name = TextField(
        'Collection name',
        validators=[DataRequired()]
    )
    description = TextAreaField(
        'Collection description',
        validators=[DataRequired()]
    )

class AddCollectionForm(Form):
    pass
