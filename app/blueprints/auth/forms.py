from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User
import random
from jinja2.utils import markupsafe

class PokedexForm(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
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

    
    ash_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/ash-johto.png" height="80px">')
    ash1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/ash-capbackward.png" height="80px">')
    brock_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/brock-gen3.png" height="80px">')
    brock1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/brock.png" height="80px">')
    misty_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/misty.png" height="80px">')
    misty1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/misty-gen1.png" height="80px">')
    tr_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/teamrocket.png" height="80px">')

    icon = RadioField('Avatar', validators=[DataRequired()],
        choices=[(ash_img), (ash1_img), (brock_img), (brock1_img), (misty_img), (misty1_img), (tr_img),   ]
    )

    
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