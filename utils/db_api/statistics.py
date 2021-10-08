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


def get_account_statistic():
    conn = connection()
    cursor = conn.cursor()
    request = cursor.execute('SELECT COUNT(*) FROM accounts_data UNION ALL '
                             'SELECT COUNT(*) FROM accounts_data WHERE status=0 UNION ALL '
                             'SELECT COUNT(*) FROM accounts_data WHERE status=1;')
    response = cursor.fetchall()
    close_connection(cursor, conn)
    result = []
    for select in response:
        for res in select:
            result.append(res)
    return result
