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
        req = self.cursor.execute("SELECT hash FROM hashs_data WHERE status = %s", status)
        if req == 0:
            return 0
        else:
            return self.cursor.fetchone()


    def register_account(self, email, key):



    #POST SHIFT API
    def register_mail(self, hash):
        import requests
        url = f'https://post-shift.ru/api.php?action=new&hash={hash}'
        request = requests.get(url=url)
        print(f'Result: {request.text}')
        email, key = request.json()['email'], request.json()['key']
        self.register_account(email, key)



    def check_remain_calls(self, hash):
        import requests
        url = f'https://post-shift.ru/api.php?action=balance&hash={hash}'
        request = requests.get(url=url)
        print(request.json())
        if int(request.json()['limit']) >= 2:
            self.register_mail(hash)
        else:
            print('error')

    def create_account(self):
        hash = self.get_hash()
        print(f'hash - {hash}')
        if hash != 0: # взяти хеш з бази
            number_of_calls = self.check_remain_calls(hash[0])

        else:
            print('NO HASHS IN DATABASE')



    # ===============================================================


    # Перевірка чи є аккаунт (Логін,Пароль) в БД.
    def check_available_accounts(self, status=0):
        request = self.cursor.execute("SELECT email, password FROM accounts_data WHERE status = %s", status)

        if request >= 1:  # if accounts exists
            email, password = self.cursor.fetchone()
            return email, password

        else:  # if accounts !exists
            return 8000






if __name__ == '__main__':
    # print(GetAccountMySql().get_hash()[0])
    request = GetAccountMySql().check_available_accounts()

    if request == 8000: # немає акк
        GetAccountMySql().create_account()
    else: # є акк
        email, password = request
        print(f'{email}\n{password}')


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