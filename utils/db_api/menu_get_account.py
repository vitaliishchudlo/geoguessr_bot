# from .config_db import connection

import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    database='geoguessrfree',
    password=''
)


class GetAccountMySql():
    def __init__(self):
        self.cursor = connection.cursor()
        self.connection = connection
    # 14fddffb5fe4df95c09a599c7f029de8

    def get_hash(self, status = 1):
        self.cursor.execute("SELECT hash FROM hashs_data WHERE status = %s", status)
        return self.cursor.fetchone()

    #POST SHIFT API
    def register_mail(self, hash):
        import requests
        url = f'https://post-shift.ru/api.php?action=new&hash={hash}'
        request = requests.get(url=url)
        print(request.json())
        self.check_remain_calls(hash)
        
    def check_remain_calls(self, hash):
        import requests
        url = f'https://post-shift.ru/api.php?action=balance&hash={hash}'
        request = requests.get(url=url)
        if int(request.json()['limit']) >= 2:
            self.register_mail(hash)
        else:
            print('error')




    def create_account(self):
        get_hash = self.get_hash()[0]
        number_of_calls = self.check_remain_calls(get_hash)


    def check_available_accounts(self, status=0):
        request = self.cursor.execute("SELECT email, password FROM accounts_data WHERE status = %s", status)
        if request >= 1:  # if accounts exists
            print(self.cursor.fetchone())
            email, password = self.cursor.fetchone()
            return email, password

        else:  # if accounts !exists
            return 8000






if __name__ == '__main__':

    print(GetAccountMySql().get_hash())

    request = GetAccountMySql().check_available_accounts()
    # print(f'print(request) # {request}')
    if request == 8000:
        GetAccountMySql().create_account()
    else:
        print('unknown error')


    # print(GetAccountMySql().check_available_accounts()) # перевірити чи є вільні юзери





# def check_available_accounts(self, status=0):
    #     request = self.cursor.execute("SELECT email, password FROM accounts_data WHERE status = %s", status)
    #     result = self.cursor.fetchall()
    #
    #     if request >= 1:
    #         login = result[0][0]
    #         password = result[0][1]
    #         print(f'Login {login}\nPassword {password}')
    #         return f'taking and giving account...{request}'
    #     else:
    #         return 'no enough accounts, need to register'