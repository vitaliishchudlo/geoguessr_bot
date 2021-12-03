import os

import pymysql
from dotenv import load_dotenv


def connection():
    load_dotenv()
    conn = pymysql.connect(
        host=str(os.getenv("DATABASE_HOST")),
        user=str(os.getenv("DATABASE_USER")),
        database=str(os.getenv("DATABASE_NAME")),
        password=str(os.getenv("DATABASE_PASSWORD")),
    )
    return conn


def close_connection(cursor, conn):
    cursor.close()
    conn.close()


def user_registration_status(id_telegram):
    conn = connection()  # create connection to db
    cursor = conn.cursor()  # create cursor

    request = cursor.execute('SELECT * FROM users_data WHERE id_telegram = %s', id_telegram)

    close_connection(cursor, conn)  # close cursor and connection to db

    return request


def register_user(user_info, email):
    conn = connection()  # create connection to db
    cursor = conn.cursor()  # create cursor

    sql = 'INSERT INTO users_data(id_telegram, username, first_name, second_name, email) VALUES (%s, %s, %s, %s, %s)'
    val = (user_info['id'], user_info['username'], user_info['first_name'], user_info['last_name'], email)
    request = cursor.execute(sql, val)
    conn.commit()

    close_connection(cursor, conn)  # close cursor and connection to db
