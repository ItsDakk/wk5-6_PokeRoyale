from flask import render_template, request
import requests
from .forms import PokedexForm
from app import app



@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/pokedex', methods = ['GET', 'POST'])
def pokedex():
    form = PokedexForm()
    if request.method == 'POST' and form.validate_on_submit():
        pokemon_name = form.pokemon_name.lower()

        pokemon_name = request.form.get('pokemon_name')

        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'.lower()
        response = requests.get(url)
        if not response.ok:
            error_string = "Invalid Pokemon name"
            return render_template('pokedex.html.j2', error = error_string)
        data = response.json()
        if not response.json():
            error_string = "We had an error"
            return render_template('pokedex.html.j2', error = error_string)

        pokemon_dict = {
            "name": data['name'],
            "bexp" : data['base_experience'],
            "shiny": data['sprites']['front_shiny'],
            "ability": data['abilities'][0]['ability']['name'],
            "hp": data['stats'][0]['base_stat'],
            "attack": data['stats'][1]['base_stat'],
            "defense": data['stats'][0]['base_stat'],
            }

    return render_template('pokedex.html.j2')# ,pokemon = pokemon_dict) -- not working ???