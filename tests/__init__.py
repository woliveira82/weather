from app import app
import pytest


@pytest.fixture
def client(scope='session'):
    app.testing = True
    app.config['ENV'] = 'development'
    app.config['debug'] = True
    return app.test_client()