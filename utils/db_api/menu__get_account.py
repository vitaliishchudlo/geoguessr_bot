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


def menu_get_account(status=0):
    conn = connection()
    cursor = conn.cursor()
    request = cursor.execute(f"SELECT email, password FROM accounts_data WHERE status = {status}")

    if request != 0:
        email, password = cursor.fetchone()
        close_connection(cursor, conn)
        return email, password
    else:
        close_connection(cursor, conn)
        return False


def set_account_status_busy(email):
    conn = connection()
    cursor = conn.cursor()

    request = cursor.execute('UPDATE accounts_data SET status=1 WHERE email=%s', email)
    conn.commit()
    close_connection(cursor,conn)
    return request


def get_hash(status=1):
    conn = connection()
    cursor = conn.cursor()

    request = cursor.execute(f" SELECT hash FROM hashs_data WHERE status = %s", status)
    if request != 0:
        return cursor.fetchone()
    else:
        return False
