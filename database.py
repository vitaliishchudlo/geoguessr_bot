import pymysql


connection = pymysql.connect(
    host='remotemysql.com',
    user='JrsFeohzhH',
    database='JrsFeohzhH',
    password='f9Sex6J7vk'
)


class MySql:

    def __init__(self):
        self.connection = connection = pymysql.connect(
            host='remotemysql.com',
            user='JrsFeohzhH',
            database='JrsFeohzhH',
            password='f9Sex6J7vk'
        )
        self.cursor = connection.cursor()

    # def show_all_users(self):
    #     self.cursor.execute('SELECT * FROM hashs_data')
    #     return self.cursor.fetchall()
    #
    #
    #
    # def show_all_hashs(self):
    #     self.cursor.execute('SELECT * FROM users_data')
    #     return self.cursor.fetchall()
    #
    #
    # def count_rows(self):
    #     self.cursor.execute('SELECT * FROM users_data')
    #     result = self.cursor.fetchall()
    #     return len(result)

    def check_exist_user(self, id_telegram):
        return self.cursor.execute("SELECT * FROM users_data WHERE id_telegram = %s", id_telegram, )

    def register_user(self, user_answers, info_user):
        if self.check_exist_user(info_user['id']):
            return 10
        else:
            print(info_user['id'])
            sql = 'INSERT INTO users_data (id_telegram, email, admin) VALUES (%s, %s, %s)'
            val = (info_user['id'], user_answers[0], False)
            self.cursor.execute(sql, val)
            self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

# def test():
#     MySql().
#
#
#
# if __name__ == '__main__':
#     test()
