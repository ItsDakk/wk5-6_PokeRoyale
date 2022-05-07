from flask import render_template, request
import requests
from app.blueprints.auth.forms import PokedexForm
from . import bp as main
from flask_login import login_required

@main.route('/', methods = ['GET'])
# @login_required
def index():
    return render_template('index.html.j2')

@main.route('/poketeam', methods = ['GET', 'POST'])
def poketeam():
    return render_template('poketeam.html.j2')

@main.route('/pokedex', methods = ['GET', 'POST'])
def pokedex():
    # @login_required
    form = PokedexForm()
    if request.method == 'POST' and form.validate_on_submit():
        pokemon_name = form.pokemon_name.data.lower()

        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'.lower()
        response = requests.get(url)
        if not response.ok:
            error_string = "Invalid Pokemon name"
            return render_template('pokedex.html.j2', error = error_string, form=form)
        data = response.json()
        if not response.json():
            error_string = "We had an error"
            return render_template('pokedex.html.j2', error = error_string, form=form)

        pokemon_dict = {
            "name": data['name'],
            "bexp" : data['base_experience'],
            "shiny": data['sprites']['front_shiny'],
            "ability": data['abilities'][0]['ability']['name'],
            "hp": data['stats'][0]['base_stat'],
            "attack": data['stats'][1]['base_stat'],
            "defense": data['stats'][0]['base_stat'],
            }

        return render_template('pokedex.html.j2', pokemon = pokemon_dict, form=form)
    return render_template('pokedex.html.j2', form=form)

