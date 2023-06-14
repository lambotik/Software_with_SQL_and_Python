import sqlite3


class SQLAtm:

    @staticmethod
    def create_table():
        """Create table: User_data."""
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS User_data(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            Number_card INTEGER NOT NULL,
            Pin_code INTEGER NOT NULL,
            Balance INTEGER NOT NULL);''')
            print("Create table user data.")

    @staticmethod
    def adding_user(user_data):
        """Adding a user.

        user_data = (int, int, int)"""
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            INSERT INTO User_data (Number_card, Pin_code, Balance) VALUES (?, ?, ?);''', user_data)
            print("Adding a user.")

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
                if result_card is None:
                    print('Unknown card number entered.')
                    return False
                else:
                    print(f'Entered card number is: {card_number}.')
                    return True
        except:
            print('Entered unknown card number.')

    @staticmethod
    def input_and_check_pincode(card_number):
        """Input and check pincode.

        card_number = int"""
        pincode = input('Enter please pincode from the card: ')
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute(f'''
            SELECT Pin_code
            FROM User_data
            WHERE Number_card = {card_number}''')
            result_pincode = cursor.fetchone()
            entered_pincode = result_pincode[0]
            try:
                if int(pincode) == entered_pincode:
                    print(f'You entered right pincode.')
                    return True
                else:
                    print('Entered incorrect pincode.')
                    return False
            except:
                print('Entered incorrect pincode.')
                return False

    @staticmethod
    def info_balance(card_number):
        """Displaying the balance of the card

        card_number = int"""
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute(f'''
                SELECT Balance
                FROM User_data
                WHERE Number_card = {card_number}''')
            result_balance = cursor.fetchone()
            card_balance = result_balance[0]
            print(f'Balance your card is: {card_balance}.')

    @staticmethod
    def withdrawing_money(card_number):
        """Withdrawing money from the card balance

        card_number = int"""
        amount_money = input('Enter how much money you want withdrawing: ')
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute(f'''
                    SELECT Balance
                    FROM User_data
                    WHERE Number_card = {card_number}''')
            result_balance = cursor.fetchone()
            card_balance = result_balance[0]
            print(f'Balance your card is: {card_balance}.')
            try:
                if int(amount_money) > card_balance:
                    print('You have not enough founds.')
                    return False
                if int(amount_money) <= 0:
                    print('Amount should be bigger than 0')
                    return False
                else:
                    cursor.execute(f'''
                        UPDATE User_data
                        SET Balance = Balance - {amount_money}
                        WHERE Number_card = {card_number};''')
                    database.commit()
                    SQLAtm.info_balance(card_number)
                    return True
            except:
                print('Attempt to do something wrong')
                return False

    @staticmethod
    def depositing_money(card_number):
        """Deposit money into account.

        card_number = int"""
        deposit_money = input('Enter the amount you would like to deposit: ')

        with sqlite3.connect('atm.db') as database:
            try:
                if int(deposit_money) <= 0:
                    print('Amount should be bigger than 0')
                    return False
                cursor = database.cursor()
                cursor.execute(f'''
                UPDATE User_data
                SET Balance = Balance + {deposit_money};''')
                database.commit()
                SQLAtm.info_balance(card_number)
            except:
                print('Attempt to do something wrong')
                return False

    @staticmethod
    def select_operation(card_number):
        """Select operation :

        1.Show balance information -> str

        2.Withdraw money -> str

        3.Deposit money -> str

        4.Finish work -> str

        Incoming data: card_number -> int"""
        while True:
            operation = input('Select please operation which you want to do:\n'
                              '1. Show balance information.\n'
                              '2. Withdraw money.\n'
                              '3. Deposit money.\n'
                              '4. Finish work.\n')
            if operation == '1':
                SQLAtm.info_balance(card_number)
            elif operation == '2':
                SQLAtm.withdrawing_money(card_number)
            elif operation == '3':
                SQLAtm.depositing_money(card_number)
            elif operation == '4':
                print('Thank you for your visit. Have a good day.')
                return False
            else:
                print('This operation is unavailable. We apologize.\nTry another operation.')
