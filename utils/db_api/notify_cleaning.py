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


def get_accounts_telegram_ids():
    conn = connection()
    cursor = conn.cursor()
    request = cursor.execute('SELECT id_telegram FROM users_data')
    response = cursor.fetchall()
    close_connection(cursor, conn)
    result = []
    for x in response:
        for id in x:
            result.append(id)
    return result
