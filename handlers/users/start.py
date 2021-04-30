from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import reg
from loader import dp
from utils.db_api import MySql

from states import Menu
from keyboards.default.menu import menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if MySql().check_exist_user(message.from_user.id):
        await message.answer('You are already registered', reply_markup=menu)
        await Menu.GetMenu.set()
    else:
        await message.answer(f"Hello, {message.from_user.full_name}. I am <b>GeoGuessr Bot.</b>\n\n"
                             f"» You are not registered in system. Please, pass verification.", reply_markup=reg)
        
