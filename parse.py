import requests
import zipfile
import configparser
import os
import logging

# Обновление справочника БИК с сайта БР

config = configparser.ConfigParser()  # создаём объект парсера
config.read("parse.ini")  # читаем конфиг

logging.basicConfig(level=logging.DEBUG,
                    filename='parse.log',
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
logging.info('parse.py')

url = requests.get(config['Hosts']['host'], timeout=20)
if url.status_code == 200:
    print('Все в норме...')
    arch_name = url.headers['Content-Disposition'][-20:]  # получаем имя архива из хедера страницы
    print('Получаем имя архива...' + arch_name)
    if os.path.exists(config['Path']['dist_path']):  # проверяем на наличие каталога назначения, вдруг его нет
        f = open(config['Path']['save_path'] + arch_name, "wb")
        f.write(url.content)
        f.close()
        z = zipfile.ZipFile(config['Path']['save_path'] + arch_name)
        print('Архив содержит:')
        z.printdir()  # читаем содержимое архива
        try:
            z.extractall(config['Path']['dist_path'])  # извлекаем файлы из архива
            print('Файл со справочником БИК успешно извлечен в ' + config['Path']['dist_path'])
        except:
            pass
    else:
        print('!!! Не найден каталог назначения...просьба проверить')
elif url.status_code == 403:
    print('Сработала защита от DDos на хосте')

# TODO:вывести логирование процесса
