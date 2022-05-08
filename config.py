import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/dak/Documents/CodingTemple/week5/main_pokedex/wk5_dy3_pokedex /wk5_dy1_pokedex/app.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
