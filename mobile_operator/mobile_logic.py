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

    @staticmethod
    def period_calculation(period):
        with sqlite3.connect('mobile_operator.db') as database:
            try:
                if int(period) <= 0:
                    print('Wrong data!')
                    return False
                cursor = database.cursor()
                cursor.execute('''
                SELECT User_name, Price, Balance, Activity
                FROM mobile_tariff
                LEFT JOIN mobile_users ON "Mobile_tariff_ref" = "TariffID"
                ORDER BY "UserID"''')
                all_data = cursor.fetchall()
                x = []
                for data in all_data:
                    x.append(list(data))
                print('List users: ', *x)
                count = 0
                flag = True
                while count != int(period) and flag is True:
                    for data in x:
                        if data[3] == 'Yes':
                            data[2] = data[2] - data[1]
                            if data[1] > data[2]:
                                data[3] = 'No'
                                new_value_data = (data[2], data[3], data[0])
                                cursor.execute(f'''
                                UPDATE mobile_users
                                SET Balance = ?, Activity = ?
                                WHERE User_name = ?;''', new_value_data)
                                database.commit()
                            new_value_data = (data[2], data[3], data[0])
                            cursor.execute(f'''
                            UPDATE mobile_users
                            SET Balance = ?, Activity = ?
                            WHERE User_name = ?;''', new_value_data)
                            database.commit()
                            print(f'Data {data[0]} has been updated')
                        elif data[3] == 'Yes':
                            print(f'{data[0]} have not enough founds')
                            data[2] = 0
                            data[3] = 'No'
                            cursor.execute(f'''
                                UPDATE mobile_users
                                SET (Balance = {data[2]}, Activity = {data[3]})
                                WHERE User_name = {data[0]};''')
                            database.commit()
                            print(f'Data {data[0]} has been updated')
                    cursor.execute('''
                    SELECT User_name, Balance, Activity
                    FROM mobile_users;''')
                    after = cursor.fetchall()
                    flag = 'Yes' in [after[i][2] for i in range(len(after))]
                    count += 1
                    print(f'After {count} month:', *after)

            except:
                print('Somthing went wrong!')
