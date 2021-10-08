from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default import statistics_menu, admin_menu
from loader import dp
from states import AdminMenu
from utils.db_api import get_account_statistic


@dp.message_handler(text='🌐 Statistics 📶', state=AdminMenu.GetChoiceMenu)
async def menu_choice_statistics(message: Message, state: FSMContext):
    await message.reply('What statistic about you want to check?', reply_markup=statistics_menu)
    await AdminMenu.WhatStatistics.set()


@dp.message_handler(text='🔙 Go back', state=AdminMenu.WhatStatistics)
async def menu_choice_go_back(message: Message, state: FSMContext):
    await message.reply('Going back', reply_markup=admin_menu)
    await AdminMenu.GetChoiceMenu.set()


@dp.message_handler(text='All account statistics', state=AdminMenu.WhatStatistics)
async def statistic_account(message: Message, state: FSMContext):
    res = get_account_statistic()
    await message.reply(f'Count of all accounts: {res[0]}\nAvailable accounts: {res[1]}\nBusy accounts: {res[2]}',
                        reply_markup=admin_menu)
    await AdminMenu.GetChoiceMenu.set()
