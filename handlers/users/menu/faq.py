import json

from aiogram.types import Message

from loader import dp
from states import MainMenu


# @dp.message_handler(text='🆘 F.A.Q. 🆘', state=MainMenu.GetChoiceMenu)
# async def menu_choice_faq(message: Message):
#     with open('versions.json', 'r') as file:
#         statistic_json = json.load(file)
#     current_version = statistic_json["current_version"]
#     new_updates = statistic_json['versions'][current_version]['updated']
#     new_fixes = statistic_json['versions'][current_version]['fixed']
#     string_result = ''
#
#     await message.answer(string_result)
#
#     await message.answer(f'Current version: {statistic_json["current_version"]}\n\n')
