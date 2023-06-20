import csv
import sqlite3

from datetime import datetime

now_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SQLAtm:

    @staticmethod
    def create_table():
        """Create table: Users_data."""

        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users_data(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            Number_card INTEGER NOT NULL,
            Pin_code INTEGER NOT NULL,
            Balance INTEGER NOT NULL);''')
            print("Create table user data.")

    @staticmethod
    def insert_users(data_user):
        """Adding a card.

        users_data = (int, int, int)"""

        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute('''
            INSERT INTO Users_data (Number_card, Pin_code, Balance) 
            VALUES (?, ?, ?);''', data_user)
            print("Adding a card.")

    @staticmethod
    def input_card(number_card):
        """Enters card number and checks if it is in the database Users_data.

        card_number = str"""
        try:
            with sqlite3.connect('atm.db') as database:
                cursor = database.cursor()
                cursor.execute(f'''
                SELECT Number_card
                FROM Users_data
                WHERE Number_card = {number_card}''')
                result_card = cursor.fetchone()
                if result_card is None:
                    print('Unknown card number entered.')
                    return False
                else:
                    print(f'Entered card number is: {number_card}.')
                    return True
        except:
            print('Entered unknown card number.')

    @staticmethod
    def input_code(card_number):
        """Input and check pincode.

        card_number = str"""
        pincode = input('Enter please pincode from the card: ')
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute(f'''
            SELECT Pin_code
            FROM Users_data
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
        """Displaying the balance of the card.

        card_number = str"""
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute(f'''
                SELECT Balance
                FROM Users_data
                WHERE Number_card = {card_number}''')
            result_balance = cursor.fetchone()
            card_balance = result_balance[0]
            print(f'Balance your card is: {card_balance}.')
            return card_balance

    @staticmethod
    def withdrawing_money(card_number):
        """Withdrawing money from the card balance.

        card_number = str"""
        amount_money = input('Enter how much money you want withdrawing: ')
        with sqlite3.connect('atm.db') as database:
            cursor = database.cursor()
            cursor.execute(f'''
                    SELECT Balance
                    FROM Users_data
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
                        UPDATE Users_data
                        SET Balance = Balance - {amount_money}
                        WHERE Number_card = {card_number};''')
                    database.commit()
                    SQLAtm.info_balance(card_number)
                    SQLAtm.report_operation_1(now_date, card_number, '1', amount_money, '')
                    return True
            except:
                print('Attempt to do something wrong')
                return False

    @staticmethod
    def depositing_money(card_number):
        """Deposit money into account.

        card_number = str"""
        deposit_money = input('Enter the amount you would like to deposit: ')

        with sqlite3.connect('atm.db') as database:
            try:
                if int(deposit_money) <= 0:
                    print('Amount should be bigger than 0')
                    return False
                cursor = database.cursor()
                cursor.execute(f'''
                UPDATE Users_data
                SET Balance = Balance + {deposit_money};''')
                database.commit()
                SQLAtm.info_balance(card_number)
                SQLAtm.report_operation_1(now_date, card_number, '2', deposit_money, '')
            except:
                print('Attempt to do something wrong')
                return False

    @staticmethod
    def transfer_money(card_number):
        """Transferring money to another card.

        card_number = str"""

        user_money = SQLAtm.info_balance(card_number)
        with sqlite3.connect('atm.db') as database:
            try:
                cursor = database.cursor()
                cursor.execute('''
                SELECT Number_card 
                FROM Users_data''')
                result = cursor.fetchall()
                list_cards = []
                for i in range(len(result)):
                    list_cards.append(result[i][0])
                number_for_transfer = input('Enter the card number to which you want to transfer money:')
                if int(number_for_transfer) not in list_cards or int(number_for_transfer) == int(card_number):
                    print('Invalid card number.')
                    return False
                if int(number_for_transfer) in list_cards:
                    money = input('Enter how much do you want to transfer:')
                    if int(money) <= 0:
                        print('Amount should be bigger than 0')
                        return False
                    if f'{int(money)}' < f'{int(user_money)}':
                        cursor.execute(f'''
                        UPDATE Users_data
                        SET Balance = Balance + {int(money)}
                        WHERE Number_card LIKE {number_for_transfer};''')
                        database.commit()
                        cursor.execute(f'''
                        UPDATE Users_data
                        Set Balance = Balance - {int(money)}
                        WHERE Number_card LIKE {card_number};''')
                        database.commit()
                        print('Transfer done')
                        return True
                    else:
                        print('You have not enough founds')
                        return False
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

        5.Transfer money -> str

        Incoming data: card_number -> str"""
        while True:
            operation = input('Select please operation which you want to do:\n'
                              '1. Show balance information.\n'
                              '2. Withdraw money.\n'
                              '3. Deposit money.\n'
                              '4. Finish work.\n'
                              '5. Transfer money.\n')
            if operation == '1':
                SQLAtm.info_balance(card_number)
            elif operation == '2':
                SQLAtm.withdrawing_money(card_number)
            elif operation == '3':
                SQLAtm.depositing_money(card_number)
            elif operation == '4':
                print('Thank you for your visit. Have a good day.')
                return False
            elif operation == '5':
                SQLAtm.transfer_money(card_number)
            else:
                print('This operation is unavailable. We apologize.\nTry another operation.')

    @staticmethod
    def report_operation_1(date, number_card, type_operation, amount, payee):
        # now_date, number_card, type_operation, amount, payee
        """Operations Report.

        Type_operation:

        1 = Withdrawals

        2 = Balance replenishment

        3 = Transfer money"""
        user_data = [
            (date, number_card, type_operation, amount, payee)  # Table headers
        ]
        with open('report_1.csv', 'a', newline='') as file:  # newline - whitespace exception on newline
            writer = csv.writer(file, delimiter=';')  # delimiter - separates newlines with ;
            writer.writerows(
                user_data
            )
        print('Data has been entered')

# SQLAtm.report_operation_1()
