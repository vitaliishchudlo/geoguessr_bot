from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, InputFile
from aiogram import types
from keyboards.default.menu import menu
from loader import dp, bot
from states import Menu
from utils.db_api.registration import MySql
from aiogram.types import ReplyKeyboardRemove
from asyncio import sleep
from data.config import photo_base
from utils.db_api.menu_get_account import check_available_account
# from .register_account import create_account
from .menu_choice import get_account

@dp.message_handler(text='Get account', state=Menu.ChoiceMenu)
async def menu_choice_get_account(message: Message):
    account = get_account()

    if not account:  # if account NOT exists
        # account = create_account()
        print(f'Account - {account}')
    else:
        print(f'Akk: {account}')
        print(account)
        #set_account_status = GetAccountMySql().set_account_busy(account[0])  # Встановити ще статус зайнятого аккаунту
        await message.answer(f'Login: {account[0]}\nPassword: {account[1]}')



@dp.message_handler(text='Dice', state=Menu.ChoiceMenu)
async def menu_choice_dice(message: Message):
    bot_dice = await message.answer_dice(reply_markup=ReplyKeyboardRemove())
    await message.answer('Rolling the dice...')
    await sleep(3.2)
    await message.answer(f'The result is {bot_dice.dice.value} :).', reply_markup=menu)

@dp.message_handler(text='Donate', state=Menu.ChoiceMenu)
async def menu_choice_donate(message: Message):
    donate = await message.answer(
        '●▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬●\n'
        '‎‎‎‎‎‎‎‎ ░░░░░░░░░░  WELCOME  ░░░░░░░░░░ \n'
        '●▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬●\n\n'
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
        '░╔═══╦═══╦═╗░╔╦═══╦════╦═══╗░\n'
        '░╚╗╔╗║╔═╗║║╚╗║║╔═╗║╔╗╔╗║╔══╝░\n'
        '░░║║║║║░║║╔╗╚╝║║░║╠╝║║╚╣╚══╗░\n'
        '░░║║║║║░║║║╚╗║║╚═╝║░║║░║╔══╝░\n'
        '░╔╝╚╝║╚═╝║║░║║║╔═╗║░║║░║╚══╗░\n'
        '░╚═══╩═══╩╝░╚═╩╝░╚╝░╚╝░╚═══╝░\n'
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
    )


@dp.message_handler(text='F.A.Q.', state=Menu.ChoiceMenu)
async def menu_choice_faq(message: Message):

    await message.answer_photo(photo=photo_base['10.png'], caption='Requires front\\back licence plates.')
    await message.answer('We don`t know how to use this bot...\n'
                         'P.S. Developers of bot')




@dp.message_handler(commands=['menu_choice'])
async def menu_command(message: Message):
    await message.answer('You are in main menu_choice: ', reply_markup=menu)
    await Menu.ChoiceMenu.set()


@dp.message_handler(state=Menu.ChoiceMenu)
async def menu_echo(message: Message):
    await message.answer(f"Choose button.")
