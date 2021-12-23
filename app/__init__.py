import importlib

from flask import Flask
from flask_caching import Cache

from app.config import BLUEPRINT_LIST

app = Flask(__name__)
app.config.from_pyfile('config.py')
cache = Cache(app)

for bluprint in BLUEPRINT_LIST:
    module = importlib.import_module(f'.{bluprint[0]}', package='app.controllers')
    app.register_blueprint(
        getattr(module, bluprint[1]),
        url_prefix=f'/api/v{bluprint[2]}'
    )
