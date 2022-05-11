from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    trainer_since = db.Column(db.DateTime, default=dt.utcnow)
    icon = db.Column(db.String)
    win_loss = db.Column(db.Integer)
    team = db.relationship('PokeTeam',
            # secondary = 'Pokemon',
            )
    
    def __repr__(self):
        return f'<User: {self.username} | {self.id} >'    

    def __str__(self):
        return f'<User: {self.username} | {self.first_name} {self.last_name}>'

    def hash_password(self, orinigal_password):
        return generate_password_hash(orinigal_password)

    def check_hash_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.username = data['username']
        self.password = self.hash_password(data['password'])
        self.icon = data['icon']

    def save(self):
        db.session.add(self)
        db.session.commit() 
        t = PokeTeam()
        t.user_id = self.id
        db.session.add(t)
        db.session.commit()

    def get_icon_url(self):
        return f"{self.icon}"

    # def is_captured(self, pokemon_caught):
    #     return self.poketeams.filter(poketeam.c.pokedex_id == pokemon_caught.id)

    # def full_team(self, pokemon_team_check):
    #     return self.poketeams.filter(poketeam.c.pokedex_id == pokemon_team_check.id).count() == 5

    # def catch_em_all(self, pokemon_caught):
    #     if not self.full_team(pokemon_caught):
    #         self.poketeams.append(pokemon_caught)
    #         db.session.commit() 

class PokeTeam(db.Model):
    poketeam_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pokemon = db.relationship('Pokemon',
                            secondary = 'pokedex',
                            backref = 'user', lazy = 'dynamic')

    def __repr__(self):
        return f'<Pokedex: {self.pokedex_id} | {self.name} >'

    def edit_team(self, new_pokemon):
        self.pokemon.append(new_pokemon)

    def save_team(self):
        db.session.commit()

    def remove_pokemon(self, pokemon):
        self.pokemon.remove(pokemon)
        db.session.commit()

    # def is_caught(self, pokemon_is_caught):
    #     return self.pokemon.filter(pokemon.c.)

class Pokemon(db.Model):
    pokemon_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bexp = db.Column(db.String)
    shiny = db.Column(db.String)
    ability = db.Column(db.String)
    hp = db.Column(db.String)
    atk = db.Column(db.String)
    defense = db.Column(db.String)

    def from_dict(self, data):
        self.bexp = data['bexp']
        self.name = data['name']
        self.shiny = data['shiny']
        self.ability = data['ability']
        self.hp = data['hp']
        self.atk = data['attack']
        self.defense = data['defense']

    def save(self):
        db.session.add(self)
        db.session.commit()


class Pokedex(db.Model):
    pokedex_id = db.Column(db.Integer, primary_key=True)
    poketeam_id = db.Column(db.Integer, db.ForeignKey(PokeTeam.poketeam_id))
    name =  db.Column(db.Integer, db.ForeignKey('pokemon.name'))

   

    
        

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    