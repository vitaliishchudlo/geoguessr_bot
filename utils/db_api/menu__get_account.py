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
    close_connection(cursor, conn)
    return request


def get_hash(status=0):
    conn = connection()
    cursor = conn.cursor()

    request = cursor.execute(f" SELECT hash FROM hashs_data WHERE status = %s", status)
    if request != 0:
        result = cursor.fetchone()[0]
        close_connection(cursor, conn)
        return result
    else:
        close_connection(cursor, conn)
        return False


def set_hash_status_deactive(hash, status=1):
    conn = connection()
    cursor = conn.cursor()

    request = cursor.execute("UPDATE hashs_data SET status=%s WHERE hash=%s", (status, hash))
    conn.commit()
    close_connection(cursor, conn)


def input_account(email, password, father_hash, status=0):
    conn = connection()
    cursor = conn.cursor()
    request = cursor.execute("INSERT INTO accounts_data(email, password, father_hash, status) VALUES(%s,%s,%s,%s)",
                             (email, password, father_hash, status))
    conn.commit()
    close_connection(cursor, conn)


def check_user_limit(user_id):
    conn = connection()
    cursor = conn.cursor()
    request = cursor.execute("SELECT finish_limit FROM user_limit WHERE user_id=%s", user_id)
    if request != 0:
        result = cursor.fetchone()[0]
        close_connection(cursor, conn)
        return result
    else:
        close_connection(cursor, conn)
        return False


def insert_user_limit(user_id, username, first_name, second_name, finish_limit):
    conn = connection()
    cursor = conn.cursor()
    request = cursor.execute(
        "INSERT INTO user_limit(user_id, username, first_name, second_name, finish_limit) VALUES(%s, %s, %s, %s, %s)",
        (user_id, username, first_name, second_name, finish_limit))
    conn.commit()
    close_connection(cursor, conn)


def delete_user_limit(user_id):
    conn = connection()
    cursor = conn.cursor()
    request = cursor.execute("DELETE FROM user_limit WHERE user_id=%s", user_id)
    conn.commit()
    close_connection(cursor, conn)