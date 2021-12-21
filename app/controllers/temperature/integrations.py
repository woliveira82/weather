from requests import get
from os import getenv


class OpenWeather:
    
    def __init__(self):
        self.url = 'https://api.openweathermap.org/data/2.5/weather'
        self.params = {'appid': getenv('OPEN_WEATHER_API_KEY')}
   
    def get(self, city_name):
        params = {**self.params, 'q': city_name}
        response = get(self.url, params=params)
        return response
