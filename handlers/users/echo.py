import time

from aiogram.types import Message, ContentType
from asyncio import sleep as get_pause
from keyboards.default.menu import write_menu
from loader import dp


@dp.message_handler()
async def bot_echo(message: Message):
    await message.answer(f"You have been unactive for a long time.\n"
                         f"To return to the menu, enter the command - <b>/menu</b>", reply_markup=write_menu)


@dp.message_handler(commands=['json'])
async def get_username(message: Message):
    await message.answer(f'Your result json: \n{message.as_json()}')  # show json answer


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[3].file_id)
