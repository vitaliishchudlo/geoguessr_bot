# import pymysql
# import random
# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     database='geoguessrfree',
#     password=''
# )
# cursor = connection.cursor()
#
#
# def register_hash(hash_user, creator_id):
#     sql = 'INSERT INTO hashs_data (hash, creator_id) VALUES (%s, %s)'
#     val = (hash_user, creator_id)
#     try:
#         cursor.execute(sql, val)
#         connection.commit()
#         return True
#     except Exception as err:
#         return err
#
#
# if __name__ == '__main__':
#     print(register_hash('412151g315t1ge7895338e9e54d5', 514242))

import time

# sec = (int(time.time()))
# min = sec / 60
# hours = min / 60
# days = hours / 24
# print(days)
