import sqlite3


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
        print('Select one of the number options: 1.Registration, 2.Authorisation, 3.Password recovery: ')
        try:
            a = int(input())
            if a in options_list:
                return a
        except ValueError:
            print('You must enter a number')

def gen_dict(val):
    result = val
    login_password = {}
    for k, v in list(result):
        login_password[k] = v
        print(k, v)
    print(login_password)
    return login_password


print('Block #1')
'''Creating database'''
try:
    database = sqlite3.connect(r'C:\Users\lambo\PycharmProjects\SQL_Python\registration.db')  # Creating database
    print('Connecting to database')
    cursor = database.cursor()  # Variable to control the database
    '''Create table users_data'''
    # user_value = "('Ivan', 'qwer1234', 1234)"
    # cursor.executescript(f'''CREATE TABLE IF NOT EXISTS users_data
    #                     (Login text not null primary key ,
    #                      Password text not null ,
    #                      Code  integer not null);
    #
    #                      INSERT INTO users_data(Login, Password, Code)
    #                         values {user_value};''')
    # database.commit()
    cursor.execute('''select "Login" from users_data;''')
    user_in_database = cursor.fetchall()
    database.commit()
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
        cursor.execute('''select Login from users_data;''')
        login_on_table = cursor.fetchall()
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
        cursor.execute('''select Login, Password from users_data;''')
        result = cursor.fetchall()
        gen_dict(result)
        print(f'Authorisation complete')
    if choice == 3:
        print(f'Password recovery complete')

finally:
    cursor.close()
