import requests
import zipfile

print('Обновление справочника БИК с сайта БР...')
path_save = 'c:\\temp\\'
Arch_name = 'bik.zip'
f = open(path_save + Arch_name, "wb")
url = requests.get('https://cbr.ru/s/newbik', timeout=15.001)
f.write(url.content)
f.close()
