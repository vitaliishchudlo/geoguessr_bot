from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f'Hello, {message.from_user.full_name}!')
