import requests
from requests.exceptions import HTTPError

print("Пробуем скачать справочник БИК с сайта БР...")

for url in ['https://api.github.com', 'https://api.github.com/invalid', 'https://ya.ru', 'https://cbr.ru/s/newbik']:
    try:
        response = requests.get(url)

        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Подключаемся к ' + url + ' ...Success!')
