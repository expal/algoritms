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

    def password_authentication(self):
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        salt = hashlib.sha256(login.encode()).hexdigest()
        salted_hash = hashlib.sha256(password.encode() + login.encode()).hexdigest()
        print(f'В базе данных хранится строка: {password_hash}')
        table_password = [(salted_hash, salt)]

        try:
            self.cursor.executemany('INSERT INTO password values (%s, %s);', table_password)
        except mysql.connector.errors.IntegrityError:
            print('Ваша учетная запись уже есть в базе данных')
        else:
            self.conn.commit()

    def login(self):
        login_2 = input('Введите логин еще раз: ')
        password_2 = input('Введите пароль еще раз: ')
        salt = hashlib.sha256(login_2.encode()).hexdigest()
        salted_hash = hashlib.sha256(password_2.encode() + login_2.encode()).hexdigest()
        self.cursor.execute('SELECT password_hash, salt_hash FROM password WHERE password_hash = %s', (salted_hash,))
        res_2 = self.cursor.fetchall()
        try:
            if (salted_hash and salt) in res_2[0]:
                print('Вы ввели правильный пароль')
        except IndexError:
            print('Вы ввели неправильный пароль или логин')


a = Authentication()
a.password_authentication()
a.login()
