import sqlite3

from datetime import datetime

now_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SQLMobile:

    @staticmethod
    def create_table_mobile_users():
        """Create table: mobile_users."""

        with sqlite3.connect('mobile_operator.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS mobile_users(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_name VARCHAR(255) NOT NULL,
            Balance INTEGER NOT NULL,
            Mobile_tariff_ref INTEGER NOT NULL,
            Activity VARCHAR(255) NOT NULL);''')
            print("Create table mobile_users.")

    @staticmethod
    def create_table_mobile_tariff():
        """Create table: mobile_tariff."""

        with sqlite3.connect('mobile_operator.db') as database:
            cursor = database.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS mobile_tariff(
                TariffID INTEGER PRIMARY KEY AUTOINCREMENT,
                Tariff VARCHAR(255) NOT NULL,
                Price INTEGER NOT NULL);''')
            print("Create table mobile_tariff.")

    @staticmethod
    def insert_user(data_user):
        """Adding user in table mobile_users

        data_user = (str, int, int, str)"""

        with sqlite3.connect('mobile_operator.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            INSERT INTO mobile_users (User_name, Balance, Mobile_tariff_ref, Activity)
            VALUES (?, ?, ?, ?);''', data_user)
            print(f'Adding a user: {data_user}.')

    @staticmethod
    def insert_tariff(data_tariff):
        """Adding tariff in table mobile_tariff

        data_tariff = (str, int)"""
        with sqlite3.connect('mobile_operator.db') as database:
            cursor = database.cursor()
            cursor.execute('''
                INSERT INTO mobile_tariff (Tariff, Price)
                VALUES (?, ?);''', data_tariff)
            print(f'Adding a tariff: {data_tariff}.')
