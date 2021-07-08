import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

DATABASE_USER = str(os.getenv("DATABASE_USER"))
DATABASE_NAME = str(os.getenv("DATABASE_NAME"))
DATABASE_HOST = str(os.getenv("DATABASE_HOST"))
DATABASE_PASSWORD = str(os.getenv("DATABASE_PASSWORD"))

admins = [
    498570021
    ]
# 728123098 - kre4kivskii
# 447755416 - ilonka
# 575871953 - sasheeek

def create_connection():
    connection = pymysql.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        database=DATABASE_NAME,
        password=DATABASE_PASSWORD,
    )
    return connection


a = create_connection()

photo_base = {
    '10.png':'AgACAgIAAxkBAAIPh2CmfQnXz0KT2SHqac1_VbMON_kyAALfszEbW8o5Scp3kWqKiRqm0XaAoy4AAwEAAwIAA3kAA6IEAQABHwQ'
}


# can comment downer
ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}