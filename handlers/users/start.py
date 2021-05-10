from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import reg, menu
from loader import dp
from states import Menu, Start, Registration
from utils.db_api import MySql


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f'Hey, {message.from_user.full_name}.')
    if MySql().check_exist_user(message.from_user.id):
        await message.answer('You are already registered!', reply_markup=menu)
        await Menu.ChoiceMenu.set()
    else:
        await message.answer(f'I am <b>GeoGuessr Bot.</b>\n\n'
                             f'You are not registered in system. Please, pass verification.', reply_markup=reg)
        await Start.PressButtonRegister.set()


@dp.message_handler(text='🧭 Register 🚩', state=Start.PressButtonRegister)
async def take_button_register(message: Message):
    await message.answer("Send me your <u>email</u> address, please.", reply_markup=ReplyKeyboardRemove())
    await Registration.GetEmail.set()


@dp.message_handler(state=Start.PressButtonRegister)
async def error_button_register(message: Message):
    await message.answer('Please, press button on keyboard')