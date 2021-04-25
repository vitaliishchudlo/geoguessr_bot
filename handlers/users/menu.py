from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.default.menu import menu  # next
from loader import dp
from states import Menu, Registration


@dp.message_handler(state=Registration.GetEmail)
async def get_email_address(message: Message, state: FSMContext):
    email = message.text
    emailsave = message.from_user
    await state.update_data(emailsave=emailsave)
    await state.update_data(email=email)
    await message.answer(f"Follow the link and get hash-code:\n"
                         f"https://post-shift.ru/api.php?action=reg&email={email}\n"
                         f"Give me that hash")
    await Registration.next()


@dp.message_handler(state=Registration.GetHash)
async def enter_message(message: Message, state: FSMContext):
    hash = message.text
    data = await state.get_data()

    print(data.get('email'))


@dp.message_handler(state=Registration.GetEmail)
async def enter_message(message: Message, state: FSMContext):
    hash = message.text

    data = await state.get_data()

    emailsave = data.get("emailsave")

    await message.answer(f"Вы зарегистрированы\n"
                         , reply_markup=menu)
    await Registration.next()


# @dp.message_handler(Text(equals=['Get account', 'Delete account', 'Donate']), state=Registration.Menu)
# async def get_food(message: Message, state: FSMContext):
#     await message.answer(f"Вы выбрали {message.text}. Спасибо")  # , reply_markup=ReplyKeyboardRemove()
#     await state.finish()


@dp.message_handler(text='🧭 Register 🚩')
async def get_username(message: Message, state: FSMContext):
    await message.answer("Send me your <u>email</u> address, please.")
    await Registration.GetEmail.set()



@dp.message_handler()
async def bot_echo(message: Message):
    await message.answer(f"Make the true choice!")