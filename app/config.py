from os import getenv


ENV = getenv('FLASK_ENV', 'development')
DEBUG = bool(getenv('FLASK_DEBUG', True))

# Cache configuration
CACHE_TYPE = 'SimpleCache'
CACHE_DEFAULT_TIMEOUT = int(getenv('CACHE_DEFAULT_TIMEOUT', 300))

# Installend Blueprints ('package', 'name', 'version')
BLUEPRINT_LIST = (
    ('temperature', 'temperature', '1'),
)
