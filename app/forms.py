from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired

class PokedexForm(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[InputRequired()])
    submit = SubmitField('Submit')