import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    498570021
]



import os
from dotenv import load_dotenv



load_dotenv()

DATABASE_USER = str(os.getenv("DATABASE_USER"))
DATABASE_NAME = str(os.getenv("DATABASE_NAME"))
DATABASE_HOST = str(os.getenv("DATABASE_HOST"))
DATABASE_PASSWORD = str(os.getenv("DATABASE_PASSWORD"))





ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
