from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, InputFile
from aiogram import types
from keyboards.default.menu import menu
from loader import dp, bot
from states import MainMenu
from .choice__get_account import get_account, register_new_account
from utils.db_api import set_account_status_busy

from asyncio import sleep


# Wait, we are creating for you new account :)

@dp.message_handler(text='Get account', state=MainMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    account_data = get_account()
    # ALWAYS RETURN (TRUE/FALSE , RESULT)
    if not account_data:  # IF NO ACCOUNT IN DATABASE ---> register new account
        account_data = register_new_account()
        if not account_data[0]:
            await message.answer(f'[Error]: {account_data[1]}')
        else:
            await message.answer(f'Account data: {account_data[0],account_data[1]}')
    else:  # IF ACCOUNT EXISTS IN DATABASE ---> GIVE IT FOR USER
        # 1. Set account busy in DB.
        account_status = set_account_status_busy(account_data[0])
        # 2. Message about data of account.
        await message.answer(f'Here is your <u>free account</u>:\n\n'
                             f'Email: {account_data[0]}\nPassword: {account_data[1]}')
