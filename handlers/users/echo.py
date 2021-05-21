from aiogram.types import Message
from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: Message):
    await message.answer(f"Make the true choice!\n"
                         f"You can type '/' and select the correct command.")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)