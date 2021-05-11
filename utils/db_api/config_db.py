import pymysql
from data.config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER

connection = pymysql.connect(
    host=DATABASE_HOST,
    user=DATABASE_USER,
    database=DATABASE_NAME,
    password=DATABASE_PASSWORD
)
