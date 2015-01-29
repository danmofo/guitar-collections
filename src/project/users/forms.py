from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(Form):
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
    email = TextField(
        'Email address',
        validators=[
            DataRequired(),
            Email(message='Please enter a valid email address'),
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
