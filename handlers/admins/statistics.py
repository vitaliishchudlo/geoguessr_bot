from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default import statistics_menu
from loader import dp
from states import AdminMenu


@dp.message_handler(text='Statistics', state=AdminMenu.GetChoiceMenu)
async def menu_choice_statistics(message: Message, state: FSMContext):
    await message.reply('What statistic about you want to check?', reply_markup=statistics_menu)
    await AdminMenu.WhatStatistics.set()
