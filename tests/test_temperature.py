from tests import client


def test_get_temperature_city_ok(client):
    cities = [
        'London',
        'Manaus',
        'Tokyo'
    ]
    for city in cities:
        response = client.get(f'/api/v1/temperature/{city}')
        assert response.status_code == 200
        json_response = response.json
        assert 'city' in json_response
        assert 'country' in json_response['city']
        assert json_response['city']['name'] == city


def test_get_temperature_wrong_city_name(client):
    cities = [
        'xwz',
        'abc123'
    ]
    for city in cities:
        response = client.get(f'/api/v1/temperature/{city}')
        assert response.status_code == 404
        json_response = response.json
    
    
def test_get_temperature_ok(client):
    response = client.get('/api/v1/temperature')
    assert response.status_code == 200
    json_response = response.json
    assert type(json_response) == list
    
    
def test_get_temperature_max_ok(client):
    for value in [1, 2, 3]:
        response = client.get(f'/api/v1/temperature?max={value}')
        assert response.status_code == 200
        json_response = response.json
        assert type(json_response) == list
        assert len(json_response) == value
    
    
    