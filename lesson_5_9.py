import sqlite3
from database.database_path import DATABASE_DIR

exchange_data = {1: 'RUB', 2: 'USD', 3: 'EUR'}
database_users = {1: 'Balance_RUB', 2: 'Balance_USD', 3: 'Balance_EUR'}
exchange_rates = {'USD': {'RUB': 70, 'EUR': 0.87},
                  'EUR': {'USD': 1.15, 'RUB': 80},
                  'RUB': {'USD': 0.07, 'EUR': 0.08}}


def select_currency():
    '''Returns one value from the given options
    :return -> int'''
    options_list = [1, 2, 3]
    while True:
        print('Enter which currency you want to exchange: \n1. RUB \n2. USD \n3. EUR')
        try:
            option = int(input())
            if option in options_list:
                return option
        except ValueError:
            print('You must enter a number')


def what_amount_are_you_interested_in():
    '''Takes a sum value and checks if it is greater than 0
    :return -> int'''
    while True:
        print('How much do you want to exchange?: ')
        try:
            option = int(input())
            sum = option
            if type(option) == int:
                print(f'You entered sum: {sum}')
                if sum <= 0:
                    print('Sum should be > 0')
                    continue
                else:
                    return option
        except ValueError:
            print('You must enter option number')


def select_currency_for_exchenge(error):
    '''Offers to choose from the available options, excluding the passed value (error)
    :param error -> int'''
    options_list = [1, 2, 3]
    while True:
        print('Enter which currency you want to exchange: \n1. RUB \n2. USD \n3. EUR')
        print('Remember that you cannot exchange the same currencies')
        print(f'Select another value than {error}')
        try:
            option = input()
            if int(option) in options_list and int(option) != error:
                return int(option)
        except ValueError:
            print('You must enter option number')


def check_that_user_have_enough_money(user_money, request):
    '''Compare that user have enough money:
    :return request -> int
    :param user_money -> int(intput())
    :param request -> int(intput())
    '''
    while True:
        if user_money > request:
            return request
        else:
            while user_money < request:
                print('You have not enough money')
                request = what_amount_are_you_interested_in()
            return request


'''Creating Database'''
try:
    database = sqlite3.connect(DATABASE_DIR / (r'exchanger' + '.db'))  # Creating database
    print('Connecting to database')
    cursor = database.cursor()  # Variable to control the database
    '''Create table users_data'''
    user_value = "('Igor', 100000, 1000, 1000)"
    cursor.executescript(f'''CREATE TABLE IF NOT EXISTS users_balance
                        (Login text not null primary key ,
                         Balance_RUB INTEGER not null ,
                         Balance_USD INTEGER not null ,
                         Balance_EUR INTEGER not null);

                         INSERT INTO users_balance(Login, Balance_RUB, Balance_USD, Balance_EUR)
                            values {user_value};''')
    database.commit()
    cursor.execute('''select "Login" from users_balance;''')
    user_in_database = cursor.fetchall()
    print('Table created')
    print(f'User added')
    print('Welcome to our exchange office, current exchange rate:')
    print('1 USD = 70 RUB\n1 EUR = 80 RUB\n1 USD = 0.87 EUR\n1 EUR = 1.15 USD\n')
    selected_currency = select_currency()
    cursor.execute(f'''select {database_users.get(selected_currency)} from users_balance
        Where Login == 'Igor';''')
    user_data = cursor.fetchall()
    print('On your balance:', (user_data[0][0]), exchange_data.get(selected_currency))
    sum_for_change = what_amount_are_you_interested_in()
    selected_sum = check_that_user_have_enough_money(int(user_data[0][0]), sum_for_change)
    currency_for_exchange = select_currency_for_exchenge(selected_currency)
    print()
    print('Available funds for exchange', user_data[0][0], exchange_data.get(selected_currency))
    print('Currency to be exchanged:', selected_sum, exchange_data.get(selected_currency))
    rate = exchange_rates.get(exchange_data.get(selected_currency)).get(exchange_data.get(currency_for_exchange))
    cash = selected_sum * rate
    # print('Rate',
    #       exchange_rates.get(exchange_data.get(selected_currency)).get(exchange_data.get(currency_for_exchange)))
    print('Currency to which we change', exchange_data.get(currency_for_exchange))
    print(f'You are getting: {round(cash, 2)}', exchange_data.get(currency_for_exchange))


finally:
    cursor.close()
