import sqlite3
from database.database_path import DATABASE_DIR


def select_currency():
    options_list = [1, 2, 3]
    while True:
        print('Enter which currency you want to exchange: \n1. RUB \n2. USD \n3. EUR')
        try:
            a = int(input())
            if a in options_list:
                return a
        except ValueError:
            print('You must enter a number')

def what_amount_are_you_interested_in():
    while True:
        print('What amount are you interested in?: ')
        try:
            a = int(input())
            sum = a
            if type(a) == int:
                print(f'You entered sum: {sum}')
                if sum <= 0:
                    print('Sum should be > 0')
                    continue
                else:
                    return a
        except ValueError:
            print('You must enter a number')

def select_currency_for_exchenge(not_change):
    error = not_change
    print('Select a value other than:', error)
    options_list = [1, 2, 3]
    while True:
        print('What currency do you want to exchange: \n1. RUB \n2. USD \n3. EUR')
        currency = int(input())
        if type(currency) != int:
            continue
        elif currency in options_list and error == currency and type(currency) == int:
            print('You cannot exchange the same currencies')
            print('Select another value')
            print('What currency do you want to exchange: \n1. RUB \n2. USD \n3. EUR')
            while True:
                try:
                    b = int(input())
                    sum = b
                    if type(b) == int and b != currency:
                        print(f'You entered: {sum}')
                    else:
                        print('You cannot exchange the same currencies')
                        print('Select another value')
                        print('What currency do you want to exchange: \n1. RUB \n2. USD \n3. EUR')
                        continue
                    return b
                except ValueError:
                    print('You must enter a number')
        else:
            break




'''Creating Database'''
try:
    database = sqlite3.connect(DATABASE_DIR / (r'exchanger' + '.db'))  # Creating database
    print('Connecting to database')
    cursor = database.cursor()  # Variable to control the database
    # '''Create table users_data'''
    # user_value = "('Igor', 100000, 1000, 1000)"
    # cursor.executescript(f'''CREATE TABLE IF NOT EXISTS users_balance
    #                     (Login text not null primary key ,
    #                      Balance_RUB INTEGER not null ,
    #                      Balance_USD INTEGER not null ,
    #                      Balance_EUR INTEGER not null);
    #
    #                      INSERT INTO users_balance(Login, Balance_RUB, Balance_USD, Balance_EUR)
    #                         values {user_value};''')
    # database.commit()
    cursor.execute('''select "Login" from users_balance;''')
    user_in_database = cursor.fetchall()
    # print('Login in database', user_in_database)
    print('Table created')
    print(f'User added')
    print('Welcome to our exchange office, current exchange rate:')
    print('1 USD = 70 RUB\n1 EUR = 80 RUB\n1 USD = 0.87 EUR\n1 EUR = 1.15 USD\n')
    selected_currency = select_currency()
    print(selected_currency)
    sum_for_change = what_amount_are_you_interested_in()
    print(sum_for_change)
    currency_for_exchange = select_currency()
    x = select_currency_for_exchenge(currency_for_exchange)



finally:
    cursor.close()
