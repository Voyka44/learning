import requests
import zipfile

print('Обновление справочника БИК с сайта БР...')
Arch_name = open(r'C:\temp\bik.zip', "wb")
url = requests.get('https://cbr.ru/s/newbik')
Arch_name.write(url.content)
Arch_name.close()
