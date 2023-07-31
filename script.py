import requests


cities = [
    'Лондон',
    'Шереметьево',
    'Череповец',
]


def get_weather_by_city(city):
    url = 'https://wttr.in/{}?nTqu&?m&?M&lang=ru'.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


for city in cities:
    get_weather_by_city(city)
