import requests


CITIES = [
    'Лондон',
    'Шереметьево',
    'Череповец',
]

REQUEST_PARAMETRS = {
    'nTqu': '',
    'm': '',
    'M': '',
    'lang': 'ru',
}


def get_weather_by_city(city, request_options):
    url = 'https://wttr.in/{}'.format(city)
    response = requests.get(url, params=request_options)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for city in CITIES:
        print(get_weather_by_city(city, REQUEST_PARAMETRS))
