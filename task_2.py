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
import mysql.connector


class Authentication():
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='12345', database='example')
        self.cursor = self.conn.cursor()

    def data(self):
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        salt = hashlib.sha256(login.encode()).hexdigest()
        salted_hash = hashlib.sha256(password.encode() + login.encode()).hexdigest()
        return salt, salted_hash

    def password_authentication(self):
        salt, salted_hash = self.data()
        print(f'В базе данных хранится строка: {salted_hash}')
        table_password = [(salted_hash, salt)]

        try:
            self.cursor.executemany('INSERT INTO password values (%s, %s);', table_password)
        except mysql.connector.errors.IntegrityError:
            print('Ваша учетная запись уже есть в базе данных')
        else:
            self.conn.commit()

    def login(self):
        salt, salted_hash = self.data()
        self.cursor.execute('SELECT password_hash FROM password WHERE salt_hash = %s', (salt,))
        res_2 = self.cursor.fetchall()
        if salted_hash in res_2[0]:
            print('Вы ввели правильный пароль')
        else:
            print('Вы ввели неправильный пароль или логин')


a = Authentication()
a.password_authentication()
a.login()
