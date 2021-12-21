from flask import jsonify, request
from .integrations import OpenWeather
# from webargs import fields
# from webargs.flaskparser import parser

from . import temperature


@temperature.route('/temperature', methods=['GET'])
def get_temperature():
    return 'ok'


@temperature.route('/temperature/<city_name>', methods=['GET'])
def get_temperature_city_name(city_name):
    response = OpenWeather().get(city_name)
    if response.status_code != 200:
        return response.json(), response.status_code
    
    weather_response = response.json()
    final_response = {
        'min': weather_response['main']['temp_min'],
        'max': weather_response['main']['temp_max'],
        'avg': weather_response['main']['temp'],
        'feels_like': weather_response['main']['feels_like'],
        'city': {
            'name': weather_response['name'],
            'country': weather_response['sys']['country'],
        }
    }
    return jsonify(final_response)
