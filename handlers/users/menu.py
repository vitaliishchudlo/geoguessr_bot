from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram import types
from keyboards.default.menu import menu
from loader import dp, bot
from states import Menu, Registration
from utils.db_api.registration import MySql
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(Text(equals=['Get account', 'Donate', 'F.A.Q.']), state=Menu.ShowMenu)
async def result_choice(message: Message, state: FSMContext):
    if message.text == 'Get account':
        print('go')
    elif message.text == 'Dice':
        print('dice cube')
        result = bot.send_dice(chat_id=message.from_user.id)


    elif message.text == 'Donate':
        print('donate')
    else:
        print('FAQ')

@dp.message_handler(Text(equals=['Dice']), state=Menu.ShowMenu)
async def result_choice(message: Message):
    message = await
    print (message)
    value= message.dice.value
    await message.answer(f'{value}')
    if value == 1:
        await message.answer(f'Ты  выйграл!')
    else:
        await message.answer(f'Ты проиграл! Я загадал 1')



@dp.message_handler(commands=['menu'])
async def menu_command(message: Message, state: FSMContext):
    await message.answer('You are in main menu', reply_markup=menu)
    await Menu.ShowMenu.set()


@dp.message_handler(state=Menu.ShowMenu)
async def bot_echo(message: Message):
    await message.answer(f"Choose button.")
