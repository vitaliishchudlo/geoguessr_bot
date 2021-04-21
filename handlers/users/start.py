from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import reg
from loader import dp
from states.new import New


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"првиет,{message.from_user.username}, я бот \n"
                         f"» Пожалуйста, пройди регистрацию", reply_markup=reg)



