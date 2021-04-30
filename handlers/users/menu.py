import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from keyboards.default.menu import menu  # next
from loader import dp
from states import Menu, Registration
from utils.db_api.registration import MySql
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(state=Registration.GetEmail)
async def get_email_address(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(f"Follow the link and get hash-code:\n"
                         f"https://post-shift.ru/api.php?action=reg&email={message.text}\n"
                         f"Give me that hash")
    await Registration.next()


@dp.message_handler(state=Registration.GetHash)
async def enter_message(message: Message, state: FSMContext):
    hash_user = message.text
    data = await state.get_data()

    if MySql().register_user(
            message.from_user, data.get('email'), hash_user) is True:
        await message.answer('You have successfully registered!', reply_markup=menu)
        await Menu.GetMenu.set()
    else:
        await message.answer('Something went wrong.\nPlease try again /start.')
        await state.finish()


@dp.message_handler(Text(equals=['Get account', 'Delete account', 'Donate']), state=Menu.GetMenu)
async def get_food(message: Message, state: FSMContext):
    await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(state=Menu.GetMenu)
async def bot_echo(message: Message):
    #await message.answer(message.as_json())
    await message.answer(f"Choose button.")

@dp.message_handler(state=Menu.GetMenu)
async def bot_echo(message: Message):
    #await message.answer(message.as_json())
    await message.answer(f"Choose button.")

@dp.message_handler(text='🧭 Register 🚩')
async def get_username(message: Message):
    await message.answer("Send me your <u>email</u> address, please.", reply_markup=ReplyKeyboardRemove())
    await Registration.GetEmail.set()


@dp.message_handler()
async def bot_echo(message: Message):
    # await message.answer(message.as_json()) # show json answer
    await message.answer(f"Make the true choice!\n"
                         f"You can type '/' and select the correct command.")

