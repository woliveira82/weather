import importlib

from flask import Flask

from app.config import BLUEPRINT_LIST

app = Flask(__name__)
app.config.from_pyfile('config.py')


for bluprint in BLUEPRINT_LIST:
    module = importlib.import_module(f'.{bluprint["package"]}', package='app.controllers')
    app.register_blueprint(
        getattr(module, bluprint['name']),
        url_prefix=f'/api/v{bluprint["version"]}'
    )
