from fileinput import filename

import requests

# Изучаем заголовки ответа
r = requests.get('https://cbr.ru/s/newbik')
#print(r.headers)
print(r.headers['Content-Disposition'])
print(r.headers['Content-Disposition'][-20:])