from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User
from jinja2.utils import markupsafe

class PokedexForm(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CatchEm(FlaskForm):
    capture = SubmitField("Catch 'em!")
    release = SubmitField("Release")


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

    r1 = "https://play.pokemonshowdown.com/sprites/trainers/ash-johto.png"
    r2 = "https://play.pokemonshowdown.com/sprites/trainers/ash-capbackward.png"
    r3 = "https://play.pokemonshowdown.com/sprites/trainers/brock-gen3.png"
    r4 = "https://play.pokemonshowdown.com/sprites/trainers/brock.png"
    r5 = "https://play.pokemonshowdown.com/sprites/trainers/misty.png"
    r6 = "https://play.pokemonshowdown.com/sprites/trainers/misty-gen1.png"
    r7 = "https://play.pokemonshowdown.com/sprites/trainers/teamrocket.png"

    
    ash_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/ash-johto.png" height="75px">')
    ash1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/ash-capbackward.png" height="75px">')
    brock_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/brock-gen3.png" height="75px">')
    brock1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/brock.png" height="75px">')
    misty_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/misty.png" height="75px">')
    misty1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/misty-gen1.png" height="75px">')
    tr_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/teamrocket.png" height="75px">')

    icon = RadioField('Avatar', validators=[DataRequired()],
        choices=[(r1, ash_img), (r2, ash1_img), (r3, brock_img), (r4, brock1_img), (r5, misty_img), (r6, misty1_img), (r7, tr_img),   ]
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

    r1 = "https://play.pokemonshowdown.com/sprites/trainers/ash-johto.png"
    r2 = "https://play.pokemonshowdown.com/sprites/trainers/ash-capbackward.png"
    r3 = "https://play.pokemonshowdown.com/sprites/trainers/brock-gen3.png"
    r4 = "https://play.pokemonshowdown.com/sprites/trainers/brock.png"
    r5 = "https://play.pokemonshowdown.com/sprites/trainers/misty.png"
    r6 = "https://play.pokemonshowdown.com/sprites/trainers/misty-gen1.png"
    r7 = "https://play.pokemonshowdown.com/sprites/trainers/teamrocket.png"


    ash_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/ash-johto.png" height="75px">')
    ash1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/ash-capbackward.png" height="75px">')
    brock_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/brock-gen3.png" height="75px">')
    brock1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/brock.png" height="75px">')
    misty_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/misty.png" height="75px">')
    misty1_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/misty-gen1.png" height="75px">')
    tr_img = markupsafe.Markup(f'<img src="https://play.pokemonshowdown.com/sprites/trainers/teamrocket.png" height="75px">')

    icon = RadioField('Avatar', validators=[DataRequired()],
        choices=[(r1, ash_img), (r2, ash1_img), (r3, brock_img), (r4, brock1_img), (r5, misty_img), (r6, misty1_img), (r7, tr_img),   ]
    )