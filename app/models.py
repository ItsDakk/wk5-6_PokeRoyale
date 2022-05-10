from app import db, login
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

pokedex = db.Table('pokedex',
    db.Column('poketeam_id', db.Integer, db.ForeignKey('poketeam.poketeam_id'), primary_key=True),
    db.Column('trainer_id', db.Integer, db.ForeignKey('poketrainer.trainer_id'), primary_key=True)
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    trainer_since = db.Column(db.DateTime, default=dt.utcnow)
    icon = db.Column(db.String)
    poketeams = db.relationship('PokeTeam',
                            secondary = pokedex,
                            primaryjoin=(pokedex.c.poketeam_id == id),
                            backref = db.backref('user', lazy = 'dynamic')
                        
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
    pokemon = db.Column(db.String)
    hp = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Pokedex: {self.pokedex_id} | {self.name} >'

    def edit_team(self, new_pokemon):
        self.pokemon = new_pokemon

    def save_team(self):
        db.session.add(self)
        db.session.commmit()

    def remove_pokemon(self):
        db.session.delete(self)
        db.session.commit()
        

class PokeTrainer(db.Model):
    trainer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    