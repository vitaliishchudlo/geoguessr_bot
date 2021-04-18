from aiogram.types import Message

from loader import dp


@dp.message_handler()
async def bot_echo(message: Message):
    chat_id = message.from_user.id
    text = message.text
    from loader import bot

    await bot.send_message(chat_id=chat_id, text=text)
