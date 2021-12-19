from os import getenv


ENV = getenv('FLASK_ENV', 'development')
DEBUG = bool(getenv('FLASK_DEBUG', True))

# Installend Blueprints ('package', 'name', 'version')
BLUEPRINT_LIST = (
    # ('package', 'name', 'version')
)
