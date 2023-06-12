from sql_atm.sql_query import SQL_Atm


class ATM:

    def atm_logic(self):
        SQL_Atm.create_table()
        # SQL_Atm.adding_user((1234, 1111, 10000))
        card_number = input('Please enter card number: ')
        while True:
            if SQL_Atm.input_card(card_number):
                print('Entered correct card number')
            else:
                break



start = ATM()
start.atm_logic()
