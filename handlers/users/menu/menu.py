from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.default import menu, reg
from loader import dp
from states import MainMenu, Start, AdminMenu
# Without states
from utils.db_api import user_registration_status


@dp.message_handler(Text(equals=['menu', 'Menu', 'MENU']))
async def menu_choice_get_account(message: Message):
    if user_registration_status(message.from_user.id):  # if user is already registered in bot
        await message.reply(f'You are in the main menu. Select actions from the keyboard📲', reply_markup=menu)
        await MainMenu.GetChoiceMenu.set()
    else:  # if user is not registered in bot
        await message.reply(f'Hey, {message.from_user.full_name} 👋🏼.\n\n'
                             'I am <b>GeoGuessr Bot.</b>\n'
                             'You are not registered. Please, pass verification.', reply_markup=reg)
        await Start.PressButtonRegister.set()


@dp.message_handler(commands=['menu'])
async def menu_choice_get_account(message: Message):
    if user_registration_status(message.from_user.id):  # if user is already registered in bot
        await message.reply(f'You are in the main menu. Select actions from the keyboard📲', reply_markup=menu)
        await MainMenu.GetChoiceMenu.set()
    else:  # if user is not registered in bot
        await message.reply(f'Hey, {message.from_user.full_name} 👋🏼.\n\n'
                             'I am <b>GeoGuessr Bot.</b>\n'
                             'You are not registered. Please, pass verification.', reply_markup=reg)
        await Start.PressButtonRegister.set()


# In states

@dp.message_handler(Text(equals=['menu', 'Menu', 'MENU']), state=AdminMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    if user_registration_status(message.from_user.id):  # if user is already registered in bot
        await message.reply(f'You are in the main menu. Select actions from the keyboard📲', reply_markup=menu)
        await MainMenu.GetChoiceMenu.set()
    else:  # if user is not registered in bot
        await message.reply(f'Hey, {message.from_user.full_name} 👋🏼.\n\n'
                             'I am <b>GeoGuessr Bot.</b>\n'
                             'You are not registered. Please, pass verification.', reply_markup=reg)
        await Start.PressButtonRegister.set()


@dp.message_handler(commands=['menu'], state=AdminMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    if user_registration_status(message.from_user.id):  # if user is already registered in bot
        await message.reply(f'You are in the main menu. Select actions from the keyboard📲', reply_markup=menu)
        await MainMenu.GetChoiceMenu.set()
    else:  # if user is not registered in bot
        await message.reply(f'Hey, {message.from_user.full_name} 👋🏼.\n\n'
                             'I am <b>GeoGuessr Bot.</b>\n'
                             'You are not registered. Please, pass verification.', reply_markup=reg)
        await Start.PressButtonRegister.set()
