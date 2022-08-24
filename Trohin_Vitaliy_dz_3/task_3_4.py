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

from hashlib import sha512

some_dict = {}
salt = 'my_salt'


def url_cash(url):
    if url in some_dict.keys():
        print(f'Хэш страницы: {some_dict[url]}')
    else:
        some_dict[url] = sha512(url.encode() + salt.encode()).hexdigest()
        print(f'Для новой страницы: {url} записан хэш: {some_dict[url]}')


url_cash('site.ru')
url_cash('site.ru')
url_cash('website.ru')
url_cash('website.ru')
