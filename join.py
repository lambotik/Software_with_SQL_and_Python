import sqlite3

'''Connecting to database'''
database = sqlite3.connect(r'database/sql_join.db')  # Connecting to database
print('Connecting to database is complete\n')
cursor = database.cursor()  # Variable to control the database
# cursor.execute('''select * from Positions''')
# data = cursor.fetchall()
# print(data)

'''Merging tables with INNER JOIN'''
print('Merging tables with INNER JOIN')
cursor.execute(
    '''SELECT PersonID, First_name, Position
    FROM Persons
    INNER JOIN Positions ON PositionID = Position_ref''')
result_all = cursor.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''Merging tables with LEFT JOIN'''
print('Merging tables with LEFT JOIN')
cursor.execute(
    '''SELECT PersonID, First_name, Position
    FROM Persons
    LEFT JOIN Positions ON PositionID = Position_ref''')
result_all = cursor.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''Merging tables with RIGHT JOIN'''
print('Merging tables with RIGHT JOIN')
cursor.execute(
    '''SELECT PersonID, First_name, Position
    FROM Persons
    RIGHT JOIN Positions ON PositionID = Position_ref''')
result_all = cursor.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''Merging tables with FULL JOIN'''
print('Merging tables with FULL JOIN')
cursor.execute(
    '''SELECT PersonID, First_name, Position
    FROM Positions
    FULL JOIN Persons ON PositionID = Position_ref''')
result_all = cursor.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''Merging tables with FULL(UNION) JOIN'''
print('Merging tables with FULL(UNION) JOIN')
cursor.execute(
    '''SELECT PersonID, First_name, Position
    FROM Persons
    LEFT JOIN Positions ON PositionID = Position_ref
    UNION
    SELECT PersonID, First_name, Position
    FROM Persons
    RIGHT JOIN Positions ON PositionID = Position_ref''')
result_all = cursor.fetchall()
for result in result_all:
    print(result)
print('*' * 50)

'''Difference between tables'''
print('Difference between tables')
cursor.execute(
    '''SELECT PersonID, First_name, Position
    FROM Persons
    LEFT JOIN Positions ON PositionID = Position_ref
    WHERE PositionID IS NULL
    UNION
    SELECT PersonID, First_name, Position
    FROM Persons
    RIGHT JOIN Positions ON PositionID = Position_ref
    WHERE Position_ref IS NULL''')
result_all = cursor.fetchall()
for result in result_all:
    print(result)
print('*' * 50)