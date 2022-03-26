import requests
import zipfile
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("parse.ini")  # читаем конфиг


print('Обновление справочника БИК с сайта БР...')

# f = open(path_save + Arch_name, "wb")
# url = requests.get('https://cbr.ru/s/newbik', timeout=15.001)
# f.write(url.content)
# f.close()
z = zipfile.ZipFile(config['Path']['save_path'] + config['Name']['arch_name'])

# читаем содержимое файла
z.printdir()

# извлекаем файл
try:
    z.extractall(config['Path']['dist_path'])
except:
    pass

#TODO:добавить проверку каталога назначения



#TODO:вывести переменную хоста в конфиг


#TODO:вывести логирование процесса


