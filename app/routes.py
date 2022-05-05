from flask import render_template, request, flash, url_for, redirect
import requests
from .forms import PokedexForm, LoginForm, RegisterForm
from app import app
from .models import User



@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/login', methods = ['GET'])
def login():
    form = LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        trainer=User.query.filter_by(username=username).first()
        if trainer and trainer.checked_hashed_password(password):
            login_user(trainer)
            flash('Welcome back Trainer!')
            return redirect(url_for('index'))
        flash("Doesn't look like you typed that in right.", 'danger')
        return render_template('login.html.j2', form=form)
    return render_template('login.html.j2', form=form)

@app.route('/register', methods = ['GET'])
def register():
    form = RegisterForm()
    if request.method=='POST' and form.validate_on_submit():
        try:
            new_user_data = {
                "first_name": form.first_name.data.title(),
                "last_name": form.last_name.data.title(),
                "username": form.username.data,
                "email": form.email.data,
                "password": form.password.data
                
            }

            new_user_object = User()
            new_user_object.form_dict(new_user_data)
            new_user_object.save()
        except:
            flash("Whoops! Looks like there was an unexpected error on our end. Please try again later!", 'danger')
            return render_template('register.html.j2')
        flash("Welcome back, Trainer!", 'success')
        return redirect(url_for('login'))
    return render_template('register.html.j2', form=form)

@app.route('/pokedex', methods = ['GET', 'POST'])
def pokedex():
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