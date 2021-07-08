# from .config_db import connection
#
#
# class GetAccountMySql:
#     def __init__(self):
#         self.cursor = connection.cursor()
#         self.connection = connection
#
#
#     def get_hash(self, status=0):
#         request = self.cursor.execute("SELECT hash FROM hashs_data WHERE status = %s", status)
#
#         if request == 0:
#             return 0
#         else:
#             return self.cursor.fetchone()
#
#
#
#
#     def set_account_busy(self, email):
#         request = self.cursor.execute("UPDATE accounts_data SET status=1 WHERE email =%s", email)
#         connection.commit()
#         print(f'Account {email} setted status "1" - unactive.')
#
#     def check_available_account(self, status=0):
#         # check if an account is available in the database
#         request = self.cursor.execute("SELECT email, password FROM accounts_data WHERE status = %s", status)
#         self.cursor.close()
#         self.connection.close()
#
#         if request != 0:  # if account exists
#             email, password = self.cursor.fetchone()
#             return email, password
#         else:  # if account NOT exists
#             return False
#

from config.config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER
import pymysql


connection = pymysql.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        database=DATABASE_NAME,
        password=DATABASE_PASSWORD,
    )


cursor = connection.cursor()


def check_available_account(self, status=0):
        # check if an account is available in the database
        request = self.cursor.execute("SELECT email, password FROM accounts_data WHERE status = %s", status)
        cursor.close()
        connection.close()

        if request != 0:  # if account exists
            email, password = self.cursor.fetchone()
            return email, password
        else:  # if account NOT exists
            return False













