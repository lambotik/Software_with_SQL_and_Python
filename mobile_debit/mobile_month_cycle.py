from sql_mobile_logic import SQLMobileLogic


class MonthCycle:
    def month_cycle(self):
        SQLMobileLogic.create_table_mobile_users()
        SQLMobileLogic.create_table_mobile_price()
        SQLMobileLogic.insert_user(('User1', 500))
        SQLMobileLogic.insert_price((1, 2, 3))
        SQLMobileLogic.cycle()


start = MonthCycle()
start.month_cycle()
exit()
