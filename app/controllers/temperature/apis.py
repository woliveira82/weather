from os import getenv
from typing import Optional

from app import cache
from flask import jsonify
from flask_pydantic import validate
from pydantic import BaseModel

from . import temperature
from .integrations import OpenWeather


class Query(BaseModel):
    max: Optional[int] = int(getenv('DEFAULT_MAX_NUMBER', 5))

@temperature.route('/temperature', methods=['GET'])
@validate()
def get_temperature(query: Query):  
    cached_cities = [cache.get(k) for k in cache.cache._cache if k[:5] == 'city-']
    cached_cities.reverse()
    return jsonify(cached_cities[:query.max])


@temperature.route('/temperature/<city_name>', methods=['GET'])
@cache.cached()
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
    cache.set('city-' + final_response['city']['name'], final_response)
    return jsonify(final_response)
