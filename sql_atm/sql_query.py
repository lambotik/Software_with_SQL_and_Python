import sqlite3


class SQLAtm:

    @staticmethod
    def create_table():
        """Create table: User_data"""
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS User_data(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            Number_card INTEGER NOT NULL,
            Pin_code INTEGER NOT NULL,
            Balance INTEGER NOT NULL);''')
            print("Create table user data")

    @staticmethod
    def adding_user(user_data):
        """Adding a user.

        user_data = (int, int, int)"""
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            INSERT INTO User_data (Number_card, Pin_code, Balance) VALUES (?, ?, ?);''', user_data)
            print("Adding a user")

    @staticmethod
    def input_card(card_number):
        """Enters card number and checks if it is in the database User_data.

        card_number = int"""
        try:
            with sqlite3.connect('atm.db') as database:
                cursor = database.cursor()
                cursor.execute(f'''
                SELECT Number_card
                FROM User_data
                WHERE Number_card = {card_number}''')
                result_card = cursor.fetchone()
                if result_card == None:
                    print('Unknown card number entered')
                    return False
                else:
                    print(f'Entered card number is: {card_number}')
                    return True
        except:
            print('Entered unknown card number')
