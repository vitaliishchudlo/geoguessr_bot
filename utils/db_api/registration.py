from .config_db import connection

# import pymysql
#
# connection = pymysql.connect(
#     host='remotemysql.com',
#     user='JrsFeohzhH',
#     database='JrsFeohzhH',
#     password='f9Sex6J7vk'
# )
#


class MySql:

    def __init__(self):
        self.cursor = connection.cursor()
        self.connection = connection
        self.connection.connect_timeout = 9999


    # Вже в процесі використання перевірити чи потрібно робити self.cursor.close чи ні.

    def check_exist_user(self, id_telegram):
        request = self.cursor.execute("SELECT * FROM users_data WHERE id_telegram = %s", id_telegram, )

        return request

    def register_user(self, info_user, email):
        sql = 'INSERT INTO users_data (' \
              'id_telegram, email, admin) ' \
              'VALUES (%s, %s, %s)'
        val = (info_user['id'], email, False)

        try:
            self.cursor.execute(sql, val)
            connection.commit()
            return True
        except Exception as error:
            return error

    # def register_user(self, user_answers, info_user):
    #     if self.check_exist_user(info_user['id']):
    #         return 10
    #     else:
    #         print(info_user['id'])
    #         sql = 'INSERT INTO users_data (id_telegram, email, admin) VALUES (%s, %s, %s)'
    #         val = (info_user['id'], user_answers[0], False)
    #         self.cursor.execute(sql, val)
    #         self.connection.commit()

    def close(self):
        self.cursor.close()
        connection.close()



