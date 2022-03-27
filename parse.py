import requests
import zipfile
import configparser
import os

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("parse.ini")  # читаем конфиг

print('Обновление справочника БИК с сайта БР...')

url = requests.get(config['Hosts']['host'], timeout=15.001)
if url.status_code == 200:
    print('Все в норме...')
    arch_name = url.headers['Content-Disposition'][-20:]  # получаем имя архива
    print('Получаем имя архива...' + arch_name)
    if os.path.exists(config['Path']['dist_path']):
        f = open(config['Path']['save_path'] + arch_name, "wb")
        f.write(url.content)
        f.close()
        z = zipfile.ZipFile(config['Path']['save_path'] + arch_name)
        z.printdir()  # читаем содержимое файла

        # извлекаем файл
        try:
            z.extractall(config['Path']['dist_path'])
            print('Файл со справочником БИК успешно извлечен в ' + config['Path']['dist_path'])
        except:
            pass
    else:
        print('!!! Не найден каталог назначения...')

# TODO:вывести логирование процесса
