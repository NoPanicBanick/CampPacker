import json
import requests

class WeatherAPI:
    
    def __init__(self, token) -> None:
        self.token = token

    def daily_forcast(self, latitude, longitude, days=16):
        '''Given a latitude and longitude, provides the weather forcast for the next 1-16 days'''
        url = f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&appid={self.token}&units=metric'
        response = requests.get(url=url)
        if response.status_code != 200:
            raise Exception('Call failed') # Remove exception flow of control
        json_body = json.loads(response.text)
        return response
