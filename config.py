import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/dak/Documents/CodingTemple/pokeroyale_project/wk6_dy1_pokeroyale/wk5-6_PokeRoyale/app.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
