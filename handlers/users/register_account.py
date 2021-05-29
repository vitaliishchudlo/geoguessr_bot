from aiogram.types import Message
from aiogram import types
from loader import dp
from utils.db_api.menu_get_account import GetAccountMySql
from post_shift_api import check_remain_calls, register_mail

def create_account():
    hash = GetAccountMySql().get_hash()
    if hash != 0:
        info_calls = check_remain_calls(hash[0])
        if info_calls:
            info_reg_mail = register_mail(hash[0])
        else:
            print('false')
            # 'error - запит на БД, з цим хешем, і встановити йому статус неактива, заново функцію "взятихеш"'
    else:
        print('No hashs in DATABASE, RETURN CODE ERROR')