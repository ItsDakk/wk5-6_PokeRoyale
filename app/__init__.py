from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Intializing
app = Flask(__name__,)
app.config.from_object(Config)

# init DB Manager
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register plug-ins
login = LoginManager(app)

# Configure settings
login.login_view = 'login'
login.login_message = 'Please login, Pokemon Trainer!'
login.login_message_catergory='warning'



from app import routes, models 