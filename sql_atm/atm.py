from sql_atm.sql_query import SQLAtm


class ATM:

    def atm_logic(self):
        SQLAtm.create_table()
        # SQLAtm.insert_users((1234, 1111, 10000))
        # SQLAtm.insert_users((2345, 2222, 10000))
        number_card = input('Please enter card number: ')
        while True:
            if SQLAtm.input_card(number_card):
                if SQLAtm.input_code(number_card):
                    print('Entered correct card number')
                    SQLAtm.select_operation(number_card)
                    break
                else:
                    break
            else:
                break


start = ATM()
start.atm_logic()
