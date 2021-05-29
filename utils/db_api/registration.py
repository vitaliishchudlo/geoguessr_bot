from .config_db import connection


class MySql:

    def __init__(self):
        self.cursor = connection.cursor()
        self.connection = connection
        # self.connection.connect_timeout = 9999

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
        except Exception as err:
            return err

    def register_hash(self, hash_user, creator_id):
        sql = 'INSERT INTO hashs_data (hash, creator_id) VALUES (%s, %s)'
        val = (hash_user, creator_id)
        try:
            self.cursor.execute(sql, val)
            connection.commit()
            return True
        except Exception as err:
            return err

    def close(self):
        self.cursor.close()
        connection.close()
