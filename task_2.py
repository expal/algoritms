"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import hashlib
from uuid import uuid4
import mysql.connector
import time


def password_authentication():
    lst = []
    password = input('Введите пароль: ')
    conn = mysql.connector.connect(user='root', password='12345', database='example')
    cursor = conn.cursor()
    salt = uuid4().hex
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    salt_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() # Я не до конца понял куда здесь применять соленый хэш, потому что он постоянно меняется, и из-за этого с ним невозможно что-то делать(сравнивать, хранить и т.д)
    print(f'В базе данных хранится строка: {password_hash}')
    table_password = [(password_hash, salt)]
    cursor.execute('SELECT password_hash FROM password')
    result = cursor.fetchall()

    ####### Сортировка чтобы не было одинаковых хэшей в бд
    if len(result) < 1:
        cursor.executemany('INSERT INTO password values (%s, %s);', table_password)
        conn.commit()
    else:
        for i in result:
            for j in i:
                lst.append(j)

    for i in lst:
        if password_hash in i:
            continue
        elif password_hash not in lst:
            cursor.executemany('INSERT INTO password values (%s, %s);', table_password)
            conn.commit()
    ########

    password = input('Введите пароль еще раз: ')
    cursor.execute('SELECT password_hash FROM password')
    res = cursor.fetchall()
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    for i in res:
        for j in i:
            if password_hash in j:
                return 'Вы ввели правильный пароль'
            else:
                continue


print(password_authentication())
