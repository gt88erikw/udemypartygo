from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea
from user.models import User


class BaseUserForm(FlaskForm):
    name = StringField('Your name', [validators.DataRequired(), validators.Length(min=2, max=30)])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])


class RegistrationForm(BaseUserForm):
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')

    @staticmethod
    def validate_email(self, field):
        if User.objects.filter(email=field.data.lower()).first():
            raise ValidationError('Email address already signed up')


class EditProfileForm(BaseUserForm):
    bio = StringField('Bio',
                      widget=TextArea(),
                      validators=[validators.Length(max=200)])


class LoginForm(FlaskForm):
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
