import os
from dotenv import load_dotenv
import pymysql


def connection():
    load_dotenv()
    conn = pymysql.connect(
        host=str(os.getenv("DATABASE_HOST")),
        user=str(os.getenv("DATABASE_USER")),
        database=str(os.getenv("DATABASE_NAME")),
        password=str(os.getenv("DATABASE_PASSWORD")),
    )
    return conn



def user_registration_status(id_telegram):
    conn = connection()
    cursor = conn.cursor()

    request = cursor.execute("SELECT * FROM users_data WHERE id_telegram = %s", id_telegram)
    return request



