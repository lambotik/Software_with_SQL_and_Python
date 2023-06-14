from sql_atm.sql_query import SQLAtm


class ATM:

    def atm_logic(self):
        SQLAtm.create_table()
        SQLAtm.adding_user((1234, 1111, 10000))
        card_number = input('Please enter card number: ')
        while True:
            if SQLAtm.input_card(card_number):
                if SQLAtm.input_and_check_pincode(card_number):
                    print('Entered correct card number')
                    SQLAtm.select_operation(card_number)
                    break
                else:
                    break
            else:
                break


start = ATM()
start.atm_logic()
