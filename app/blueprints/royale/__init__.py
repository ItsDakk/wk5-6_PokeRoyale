from flask import Blueprint

bp = Blueprint('royale', __name__, url_prefix='')

from . import routes