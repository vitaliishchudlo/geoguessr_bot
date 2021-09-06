import json

from aiogram.types import Message

from loader import dp
from states import MainMenu


@dp.message_handler(text='F.A.Q.', state=MainMenu.GetChoiceMenu)
async def menu_choice_faq(message: Message):
    with open('versions.json', 'r') as file:
        statistic_json = json.load(file)
    await message.answer(f'Current version: {statistic_json["current_version"]}\n\n')
