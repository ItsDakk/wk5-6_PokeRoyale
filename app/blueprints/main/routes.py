import re
from flask import render_template, request, flash, redirect, url_for
import requests
from app.blueprints.auth.forms import PokedexForm
from . import bp as main
from flask_login import login_required, current_user
from app.models import Pokemon, PokeTeam

@main.route('/', methods = ['GET'])
# @login_required
def index():
    return render_template('index.html.j2')

@main.route('/poketeam', methods = ['GET', 'POST'])
def poketeam():
    team = current_user.team.all()
    




    return render_template('poketeam.html.j2', team = team)

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
            "name": data['name'].capitalize(),
            "bexp" : data['base_experience'],
            "shiny": data['sprites']['front_shiny'],
            "ability": data['abilities'][0]['ability']['name'].capitalize(),
            "hp": data['stats'][0]['base_stat'],
            "attack": data['stats'][1]['base_stat'],
            "defense": data['stats'][0]['base_stat'],
            }

        p = Pokemon.query.filter_by(name = pokemon_dict['name']).first()
        if p in current_user.team.all():
            is_caught = True;
        else:
            is_caught = False;

        if p:
            pass
        else:
            p = Pokemon()
            p.from_dict(pokemon_dict)
            p.save()

        return render_template('pokedex.html.j2', pokemon = pokemon_dict, form=form, pokemon_id = p.pokemon_id, is_caught = is_caught)
    return render_template('pokedex.html.j2', form=form)

@main.route('/catch/<int:id>', methods = ['GET', 'POST'])
def catch(id):
    if len(current_user.team.all()) == 5:
        flash('Your team is full', 'danger')
        return redirect(url_for('main.pokedex'))
    flash('Captured!', 'success')
        
    p = Pokemon.query.filter_by(pokemon_id = id).first()
    current_user.edit_team(p)
    current_user.save()

    return redirect(url_for('main.pokedex'))

@main.route('/pokeroyale', methods = ['GET', 'POST'])
# @login_required
def pokeroyale():
    pass
    
    return render_template('pokeroyale.html.j2')



