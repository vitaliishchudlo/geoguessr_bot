from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from data.config import admins
from keyboards.default import admin_menu
from loader import dp
from states import AdminMenu, MainMenu


# Without states

@dp.message_handler(Text(equals=['Admin', 'admin', 'ADMIN']))
async def menu_choice_get_account(message: Message):
    if message.from_user.id in admins:
        await message.reply('You are administrator.', reply_markup=admin_menu)
        await AdminMenu.GetChoiceMenu.set()
    else:
        await message.reply('Sorry, but you are not administrator.')


@dp.message_handler(commands=['admin'])
async def menu_choice_get_account(message: Message):
    if message.from_user.id in admins:
        await message.reply('You are administrator.', reply_markup=admin_menu)
        await AdminMenu.GetChoiceMenu.set()
    else:
        await message.reply('Sorry, but you are not administrator.')


# In states

@dp.message_handler(Text(equals=['Admin', 'admin', 'ADMIN']), state=MainMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    if message.from_user.id in admins:
        await message.reply('You are administrator.', reply_markup=admin_menu)
        await AdminMenu.GetChoiceMenu.set()
    else:
        await message.reply('Sorry, but you are not administrator.')


@dp.message_handler(commands=['admin'], state=MainMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    if message.from_user.id in admins:
        await message.reply('You are administrator.', reply_markup=admin_menu)
        await AdminMenu.GetChoiceMenu.set()
    else:
        await message.reply('Sorry, but you are not administrator.')
