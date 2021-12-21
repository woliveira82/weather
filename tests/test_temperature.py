from tests import client


def test_get_temperature_ok(client):
    response = client.get('/api/v1/temperature/London')
    assert response.status_code == 200
    json_response = response.json
    assert 'city' in json_response
    assert 'country' in json_response['city']
    assert json_response['city']['country'] == 'GB'
    assert json_response['city']['name'] == 'London'
