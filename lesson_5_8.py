import sqlite3
from database.database_path import DATABASE_DIR


def check_that_int():
    while True:
        print('Enter the Code number:')
        try:
            num = int(input())
            return num
            break
        except ValueError:
            print('You must enter a number!')


def select_one_option():
    options_list = [1, 2, 3]
    while True:
        print('Select one of the number options: \n1.Registration \n2.Authorisation \n3.Password recovery: ')
        try:
            a = int(input())
            if a in options_list:
                return a
        except ValueError:
            print('You must enter a number')


def gen_dict(val):
    result = val
    login_password = {}
    for login, password, code in list(result):
        login_password[login] = password, code
    print(login_password)
    return login_password


def check_login_and_password(database_dict):
    while True:
        print('Input your Login: ')
        login = input()
        if login in database_dict:
            print('Login is correct')
        else:
            login in database_dict == False
            print('User not registered')
            break
        print('Input your Password: ')
        password = input()
        if password in database_dict.get(login):
            print('Password is correct')
            print('Authorization Success')
            break
        else:
            print('Password is not correct')
            print('Try again')
            print('Select Y/N')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                continue
            else:
                break


def recovery_password(database_dict):
    while True:
        print('Input your Login: ')
        login = input()
        if login in database_dict:
            print('Login is correct')
        else:
            login in database_dict == False
            print('User is not registration')
            break
        print('Input your Code: ')
        code = input()
        if code in str(database_dict.get(login)[1]):
            print(database_dict.get(login)[1])
            print('Code is correct')
            print('Input new password')
            password = input()
            print('Password has been recovered')
            break
        else:
            print('Code is not correct')
            print('Try again')
            print('Select Y/N')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                continue
            else:
                break


print('Block #1')
'''Creating database'''
try:
    # database = sqlite3.connect(r'C:\Users\lambo\PycharmProjects\SQL_Python\registration.db')  # Creating database
    database = sqlite3.connect(DATABASE_DIR / (r'registration' + '.db'))  # Creating database
    print('Connecting to database')
    cursor = database.cursor()  # Variable to control the database
    '''Create table users_data'''
    user_value = "('Ivan', 'qwer1234', 1234)"
    cursor.executescript(f'''CREATE TABLE IF NOT EXISTS users_data
                        (Login text not null primary key ,
                         Password text not null ,
                         Code  integer not null);

                         INSERT INTO users_data(Login, Password, Code)
                            values {user_value};''')
    database.commit()
    cursor.execute('''select "Login" from users_data;''')
    user_in_database = cursor.fetchall()
    print('Login in database', user_in_database)
    print('Table created')
    print('User added')

    print('\nBlock #2')
    choice = select_one_option()
    if choice == 1:
        print('Input your Login:')
        login = input()
        login_output = login
        print('Input your Password:')
        password = input()
        password_output = password
        code = check_that_int()
        code_output = code
        cursor.execute('''select Login, Password, Code from users_data;''')
        login_on_table = cursor.fetchall()
        print(login_on_table)
        loginID_list = []
        for i in range(len(login_on_table)):
            loginID_list.append(login_on_table[i][0])
        print('LoginID list: ', loginID_list)
        if login_output not in loginID_list:
            cursor.execute(f'''INSERT INTO users_data
                                VALUES ('{login_output}','{password_output}', {code_output})''')
            database.commit()
            print(f'You have successfully created a user:')
            print(f'Login: {login_output}', f'Password: {password_output}', f'Code: {code_output}.', sep=', ')
            print(f'Registration complete')
        else:
            print('Login is busy!!!')

    if choice == 2:
        print('Authorization in the system')
        cursor.execute('''Select Login, Password, Code from users_data;''')
        result = cursor.fetchall()
        database_dict = gen_dict(result)
        check_login_and_password(database_dict)
    if choice == 3:
        cursor.execute('''Select Login, Password, Code from users_data;''')
        result = cursor.fetchall()
        database_dict = gen_dict(result)
        recovery_password(database_dict)
        print(f'Password recovery complete')

finally:
    cursor.close()
