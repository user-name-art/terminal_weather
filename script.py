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


def get_weather_by_city(city, REQUEST_PARAMETRS):
    url = 'https://wttr.in/{}'.format(city)
    response = requests.get(url, params=REQUEST_PARAMETRS)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for city in CITIES:
        print(get_weather_by_city(city, REQUEST_PARAMETRS))
