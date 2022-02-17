"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

salt = uuid4().hex
url_dict = {}


def func(url):
    salt_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url in url_dict.keys():
        return f'Хэш этого домена {url}: {url_dict[url]}'
    else:
        url_dict[url] = salt_url
        return f'Для домена {url} добавлен новый хэш {url_dict[url]}'


print(func('https://www.youtube.com'))
print(func('https://www.youtube.com'))
print(func('https://vk.com'))
print(func('https://vk.com'))