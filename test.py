import requests

# Изучаем заголовки ответа
r = requests.get('https://cbr.ru/s/newbik')
print(r.headers)