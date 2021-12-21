from os import getenv


ENV = getenv('FLASK_ENV', 'development')
DEBUG = bool(getenv('FLASK_DEBUG', True))
CACHE_TTL = getenv('CACHE_TTL', 5)
DEFAULT_MAX_NUMBER = getenv('DEFAULT_MAX_NUMBER', 5)

# Installend Blueprints ('package', 'name', 'version')
BLUEPRINT_LIST = (
    ('temperature', 'temperature', '1'),
)
