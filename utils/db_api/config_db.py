import pymysql
from config.config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER


def create_connection():
    try:
        connection = pymysql.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            database=DATABASE_NAME,
            password=DATABASE_PASSWORD,
        )
        return connection
    except Exception as err:
        return False




