from flask_wtf import Form
from wtforms import StringField, validators
from author.form import RegistrationForm


class SetupForm(RegistrationForm):
    name = StringField('Blog name', [
        validators.Required(),
        validators.Length(max=80)
    ])
