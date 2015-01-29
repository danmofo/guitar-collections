from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(Form):
    username = TextField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    email = TextField(
        'Email address',
        validators=[
            DataRequired(),
            Email(message='Please enter a valid email address'),
            Length(min=3, max=50)
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=3, max=40)
        ]
    )

    confirm_password = PasswordField(
        'Confirm password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match!')
        ]
    )

class LoginForm(Form):
    username = TextField(
        'Username',
        validators=[DataRequired()]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
