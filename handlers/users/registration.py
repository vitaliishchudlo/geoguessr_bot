from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default import menu
from loader import dp
from states.menu import Menu
from states.registration import Registration
from utils.db_api import MySql


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