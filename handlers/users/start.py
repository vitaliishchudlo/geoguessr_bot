from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from keyboards.default import reg, menu
from loader import dp
from states import Start
from utils.db_api import user_registration_status

@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f'Hey, {message.from_user.full_name} 👋🏼.')  # Congratulations to the user

    if user_registration_status(message.from_user.id):  # if user is already registered in bot
        await message.answer(f'Welcome back, {message.from_user.first_name}.\nYou are already registered!',
                             reply_markup=menu)
        # await .set() MENU CHOICE
    else:  # if user is not registered in bot
        await message.answer('I am <b>GeoGuessr Bot.</b>\n\n'
                             'You are not registered. Please pass verification.', reply_markup=reg)
        await Start.PressButtonRegister.set()


@dp.message_handler(state=Start.PressButtonRegister)
async def error_button_register(message: Message):
    await message.answer('Please, press button on keyboard.')
