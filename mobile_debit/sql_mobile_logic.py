import csv
import random
import sqlite3

from datetime import datetime

now_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SQLMobileLogic:

    @staticmethod
    def create_table_mobile_users():
        """Create table: mobile_users."""

        with sqlite3.connect('mobile_calls.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS mobile_users(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            User VARCHAR(255) NOT NULL,
            Balance INTEGER NOT NULL);''')
            print("Create table mobile_users.")

    @staticmethod
    def create_table_mobile_price():
        """Create table: mobile_price."""

        with sqlite3.connect('mobile_calls.db') as database:
            cursor = database.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS mobile_price(
                PriceID INTEGER PRIMARY KEY AUTOINCREMENT,
                Mts_Mts INTEGER NOT NULL,
                Mts_Tele2 INTEGER NOT NULL,
                Mts_Yota INTEGER NOT NULL);''')
            print("Create table mobile_price.")

    @staticmethod
    def insert_user(data_user):
        """Adding user in table mobile_users

        data_user = (str, int)"""

        with sqlite3.connect('mobile_calls.db') as database:
            cursor = database.cursor()
            cursor.execute('''
                INSERT INTO mobile_users (User, Balance)
                VALUES (?, ?);''', data_user)
            print(f'Adding a user: {data_user}.')

    @staticmethod
    def insert_price(data_tariff):
        """Adding tariff in table mobile_price

        data_tariff = (int, int, int)"""
        with sqlite3.connect('mobile_calls.db') as database:
            cursor = database.cursor()
            cursor.execute('''
                    INSERT INTO mobile_price (Mts_Mts, Mts_Tele2, Mts_Yota)
                    VALUES (?, ?, ?);''', data_tariff)
            print(f'Adding a tariff: {data_tariff}.')

    @staticmethod
    def create_report_mobile():
        """Operations Report.

        Type_operation:

        1 = Mts_Mts

        2 = Mts_Tele2

        3 = Mts_Yota"""
        user_data = [
            ('Date', 'Operator', 'Count_min', 'Amount')  # Table headers
        ]
        with open('report_mobile.csv', 'a', newline='') as file:  # newline - whitespace exception on newline
            writer = csv.writer(file, delimiter=';')  # delimiter - separates newlines with ;
            writer.writerows(
                user_data
            )
        print('Has been created: report_mobile.csv')

    @staticmethod
    def added_data_to_report_mobile(date, operator, minute, amount):
        f"""
        Operations Report.

        Type_operation:

        1 = Mts_Mts

        2 = Mts_Tele2

        3 = Mts_Yota
        :param date: {now_date}
        :param operator: random.choice() from Mts_Mts, Mts_Tele2, Mts_Yota 
        :param minute: random.randint(1, 10)
        :param amount: random_operator * random_minute
        :return: 
        """
        user_data = [
            (date, operator, minute, amount)  # Table headers
        ]
        with open('report_mobile.csv', 'a', newline='') as file:  # newline - whitespace exception on newline
            writer = csv.writer(file, delimiter=';')  # delimiter - separates newlines with ;
            writer.writerows(
                user_data
            )
        print('Data has been added to: report_mobile.csv')

    @staticmethod
    def cycle():
        """
        :return:
        """
        with sqlite3.connect('mobile_calls.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            SELECT Mts_Mts, Mts_Tele2, Mts_Yota FROM mobile_price''')
            operators_id = cursor.fetchone()
            count = 30
            while count != 0:
                operator = {1: 'Mts_Mts', 2: 'Mts_Tele2', 3: 'Mts_Yota'}
                random_operator = random.choice(operators_id)
                random_minute = random.randint(1, 10)
                cursor.execute('''
                SELECT Balance FROM mobile_users''')
                user_balance = cursor.fetchone()
                amount = random_operator * random_minute
                if user_balance[0] > 0 and (user_balance[0] - amount) > 0:
                    cursor.execute(f'''
                    UPDATE mobile_users
                    SET Balance = Balance - {amount};''')
                    database.commit()
                    SQLMobileLogic.added_data_to_report_mobile(
                        now_date, operator.get(random_operator), random_minute, amount)
                    count -= 1
                    cursor.execute('''
                            SELECT Balance FROM mobile_users''')
                    final_balance = cursor.fetchone()
                    print('Operator: ', operator.get(random_operator), '.', 'Minute: ',
                          random_minute, '.', 'Amount: ', amount, '.', 'User balance: ', final_balance[0], '.')
                else:
                    print('User balance:', user_balance[0])
                    print('User have not enough funds!')
                    return False

        cursor.execute('''
        SELECT Balance FROM mobile_users''')
        final_balance = cursor.fetchone()
        print('Final balance:', final_balance[0])

# SQLMobileLogic.create_report_mobile()  # Uncomment and run this file to create a .csv report, then comment again
