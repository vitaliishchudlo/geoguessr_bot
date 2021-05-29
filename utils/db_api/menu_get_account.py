from .config_db import connection


class GetAccountMySql:
    def __init__(self):
        self.cursor = connection.cursor()
        self.connection = connection


    def get_hash(self, status=1):
        request = self.cursor.execute("SELECT hash FROM hashs_data WHERE status = %s", status)

        if request ==0:
            return 0
        else:
            return self.cursor.fetchone()




    def set_account_busy(self, email, password, status=1):
        request = self.cursor.execute("UPDATE accounts_data SET status=1 WHERE email =%s", email)
        connection.commit()
        print(f'Account {email} setted status "1" - unactive.')

    def check_available_account(self, status=0):
        # check if an account is available in the database
        request = self.cursor.execute("SELECT email, password FROM accounts_data WHERE status = %s", status)

        if request != 0:  # if account exists
            email, password = self.cursor.fetchone()
            return email, password
        else:  # if account NOT exists
            return 8000


