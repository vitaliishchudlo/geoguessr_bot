from aiogram.types import Message
from loader import dp



@dp.message_handler(commands=['json'])
async def get_username(message: Message):
    await message.answer(f'Your result json: \n{message.as_json()}')  # show json answer