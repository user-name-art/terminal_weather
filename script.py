import requests


CITIES = [
    'Лондон',
    'Шереметьево',
    'Череповец',
]


def get_weather_by_city(city):
    url = 'https://wttr.in/{}?nTqu&?m&?M&lang=ru'.format(city)
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for city in CITIES:
        print(get_weather_by_city(city))
