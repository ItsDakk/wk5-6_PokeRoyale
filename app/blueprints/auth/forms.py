from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class PokedexForm(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
            validators=[DataRequired(), EqualTo('password', message='Password Must Match' )])
    submit = SubmitField('Register')

    def validate_username(form, field):
        same_username_user = User.query.filter_by(username = field.data).first()
        if same_username_user:
            raise ValidationError('Username is Taken')

    # Come back to add avatars!!

    
class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
            validators=[DataRequired(), EqualTo('password', message='Password Must Match' )])
    submit = SubmitField('Register')

    # Come back to edit avatars!!