from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.menu import menu, nextt
from loader import dp
from states.new import New


@dp.message_handler(text='Зарегисрироваться')
async def get_username(message: Message, state: FSMContext):
    await message.answer("Пришли мне свой E-mail:")
    await New.Email.set()


@dp.message_handler(state=New.Email)
async def enter_message(message: Message, state: FSMContext):
    email = message.text
    emailsave = message.from_user
    await state.update_data(emailsave=emailsave)
    await message.answer(f"https://......&email={email}:\n"
                         f"Перейдите по ссылке, сервер выдаст вам хэш,\n"
                         f" передайте этот хэш мне")
    await New.next()

@dp.message_handler(state=New.Email)
async def enter_message(message: Message, state: FSMContext):
    email = message.text
    emailsave = message.from_user
    await state.update_data(emailsave=emailsave)
    await message.answer(f"https://......&email={email}:\n"
                         f"Перейдите по ссылке, сервер выдаст вам хэш,\n"
                         f" передайте этот хэш мне"
                             ,reply_markup=menu)
    await New.next()

@dp.message_handler(state=New.Emailsave)
async def enter_message(message: Message, state: FSMContext):
    hash = message.text

    data = await state.get_data()

    emailsave = data.get("emailsave")


    await message.answer(f"Вы зарегистрированы\n"
                             ,reply_markup=menu)
    await New.next()

@dp.message_handler(Text(equals=['Get account','Delete account', 'Donate']),state=New.Menu)
async def get_food(message: Message, state: FSMContext):
    await message.answer(f"Вы выбрали {message.text}. Спасибо", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler()
async def bot_echo(message: Message):
    await message.answer(f"Сделайте свой выбор!")