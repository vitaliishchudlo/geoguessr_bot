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


def user_hash_status(hash):
    conn = connection()
    cursor = conn.cursor()

    request = cursor.execute('SELECT * FROM hashs_data WHERE hash = %s', hash)

    close_connection(cursor, conn)
    return request


def register_hash(hash_user, creator_id):
    conn = connection()
    cursor = conn.cursor()

    sql = 'INSERT INTO hashs_data (hash, creator_id) VALUES (%s, %s)'
    val = (hash_user, creator_id)

    cursor.execute(sql, val)
    conn.commit()

    close_connection(cursor, conn)


