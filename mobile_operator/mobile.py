from mobile_logic import SQLMobile


class MOBILE:
    def mobile_balance_check(self):
        SQLMobile.create_table_mobile_users()
        SQLMobile.create_table_mobile_tariff()
        SQLMobile.insert_user(('User1', 10000, 2, 'Yes'))
        SQLMobile.insert_user(('User2', 10000, 3, 'Yes'))
        SQLMobile.insert_user(('User3', 10000, 1, 'Yes'))
        SQLMobile.insert_tariff(('Standard', 500))
        SQLMobile.insert_tariff(('VIP', 1000))
        SQLMobile.insert_tariff(('Premium', 1500))
        period = input('Enter period calculation:')
        SQLMobile.period_calculation(period)

start = MOBILE()
start.mobile_balance_check()
