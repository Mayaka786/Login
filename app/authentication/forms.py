from os import name
from wtforms import EmailField, validators
from wtforms.fields.simple import BooleanField, PasswordField
from wtforms.form import Form


class LoginForm(Form):
    # email field
    email = EmailField(
        label='Enter Email',
        name='email',
        validators=[validators.DataRequired('Email is required.')])
    # pass field
    password = PasswordField(
        label='Enter Password',
        name='password',
        validators=[
            validators.DataRequired('Password is required.'),
            # validators.EqualTo('confirm', message='Passwords must match')
        ])
    remember = BooleanField('Remember me?', name='remember')

    # confirm = PasswordField(
    #     label='Confirm Registration',
    #     validators=[
    #         validators.DataRequired('Password is required.'),
    #     ])
