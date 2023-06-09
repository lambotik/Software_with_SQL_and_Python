import sqlite3
from database.database_path import DATABASE_DIR


def check_that_int():
    """This function check that user enter int character"""
    while True:
        print('Enter the Code number:')
        try:
            num = int(input())
            return num
            break
        except ValueError:
            print('You must enter a number!')


def select_one_option():
    """Select one position from options:
    1=Registration

    2=Authorisation

    3=Password recovery"""

    options_list = [1, 2, 3]
    while True:
        print('Select one of the number options: \n1.Registration \n2.Authorisation \n3.Password recovery: ')
        try:
            option = int(input())
            if option in options_list:
                return option
        except ValueError:
            print('You must enter a number')


def check_login():
    database = sqlite3.connect(DATABASE_DIR / (r'registration' + '.db'))  # Creating database
    print('Connecting to database')
    cursor = database.cursor()  # Variable to control the database
    cursor.execute('''select Login, Password, Code from users_data;''')
    login_on_table = cursor.fetchall()
    # print(login_on_table)
    loginID_list = []
    for i in range(len(login_on_table)):
        loginID_list.append(login_on_table[i][0])
    # print('LoginID list: ', loginID_list)
    while True:
        print('Input your Login:')
        login = input()
        if len(login) < 2:
            print('Login should be longer than 1 symbols')
            print('Try again?')
            print('Select Y/N')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                continue
            else:
                break
        elif login in loginID_list:
            print('Login is busy')
            print('Try again?')
            print('Select Y/N')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                continue
            else:
                break
        elif login not in loginID_list and len(login) >= 2:
            return login
        else:
            return check_login()


def check_password():
    while True:
        print('Input your Password:')
        password = input()
        if len(password) <= 5:
            print('Password should be longer than 5 symbols')
            print('Try again?')
            print('Select Y/N')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                continue
            else:
                break
        if len(password) > 5:
            print(f'Password is: {password}')
            return password
        else:
            return check_password()


def check_that_int():
    while True:
        print('Enter the Code number:')
        try:
            num = int(input())
            return num
            break
        except ValueError:
            print('You must enter a number!')
            print('Try again?')
            print('Select Y/N')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                continue
            else:
                break
        return check_that_int()


def registration():
    while True:
        login = check_login()
        if login == None:
            break
        password = check_password()
        if password == None:
            break
        if login != None and password != None:
            try:
                code = check_that_int()
                return login, password, code
            except:
                print('You entered bad data')
                break
        else:
            print('You entered bad data')
            break


def gen_dict(val):
    result = val
    login_password = {}
    for login, password, code in list(result):
        login_password[login] = password, code
    # print(login_password)
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
            print('Try again?')
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
            while login not in database_dict:
                print('User is not registration')
                break
            break
        print('Input your Code: ')
        code = input()
        if code == str(database_dict.get(login)[1]):
            # print(database_dict.get(login)[1])
            print('Code is correct')
            while True:
                print('Input your new Password:')
                password = input()
                if len(password) <= 5:
                    print('password should be longer than 5 symbols')
                    print('Try again?')
                    print('Select Y/N')
                    answer = input()
                    answer = answer.lower()
                    if answer == 'y':
                        continue
                if len(password) > 5:
                    print(f'Your new password is: {password}')
                    print('Password has been recovered')
                    return password, login
                else:
                    break

            break
        else:
            print('Code is not correct')
            print('Try again?')
            print('Select Y/N')
            answer = input()
            answer = answer.lower()
            if answer == 'y':
                continue
            else:
                break


print('Part #1')
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
    print('Table created')
    print('User added')

    print('\nPart #2')
    choice = select_one_option()
    if choice == 1:
        try:
            login, password, code = registration()
        except TypeError:
            print('Required fields: Login, Password, Code!!!')
        cursor.execute('''select Login, Password, Code from users_data;''')
        login_on_table = cursor.fetchall()
        loginID_list = []
        for i in range(len(login_on_table)):
            loginID_list.append(login_on_table[i][0])
        try:
            if login not in loginID_list:
                cursor.execute(f'''INSERT INTO users_data
                                    VALUES ('{login}','{password}', {code})''')
                database.commit()
                print(f'You have successfully created a user:')
                print(f'Login: {login}', f'Password: {password}', f'Code: {code}.', sep=', ')
                print(f'Registration complete')
            else:
                print('Login is busy!!!')
        except NameError:
            print('Try Again!')

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
        try:
            new_password, user_name = recovery_password(database_dict)
            cursor.execute(f"""UPDATE users_data SET Password = '{new_password}' WHERE Login = '{user_name}';""")
            database.commit()
        except TypeError:
            print('Password has been recovered')

finally:
    cursor.close()
