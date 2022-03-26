import requests

print("Пробуем скачать справочник БИК с сайта БР...")
r = requests.get('https://cbr.ru/s/newbik')
print(r)
if r.status_code == 200:
    print("Success...")
elif r.status_code == 403:
    print("Not Found")