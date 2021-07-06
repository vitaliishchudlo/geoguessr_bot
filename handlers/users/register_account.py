from aiogram.types import Message
from aiogram import types
from loader import dp

from post_shift_api import check_remain_calls, register_mail, get_text_mail


# def create_account():
#     hash = GetAccountMySql().get_hash()
#     print(f'Hash is {hash[0]}')
#     if hash != 0:
#         info_calls = check_remain_calls(hash[0])
#         if info_calls:
#             info_reg_mail = register_mail(hash[0])
#             if info_reg_mail:
#                 print(f'Info reg mail: {info_reg_mail}')
#                 get_link_for_resitering = get_text_mail(info_reg_mail)
#                 print(f'Link is: {get_link_for_resitering}')
#
#             else:
#                 print(f'Some troubles with registering mail {info_reg_mail}')
#         else:
#             print(f'False, Запит на БД, і встановлення цьому хешу статусу неактива. \nHash: {hash}')
#             # 'error - запит на БД, з цим хешем, і встановити йому статус неактива, заново функцію "взятихеш"'
#     else:
#         print('No hashs in DATABASE, RETURN CODE ERROR, ASK ADMIN TO FIX IT')
