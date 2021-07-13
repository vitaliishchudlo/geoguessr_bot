from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp

from post_shift_api import check_hash_availability, check_hash_usage
from states.registration import Registration

import json
from states import Start



@dp.message_handler(text='🧭 Register 🚩', state=Start.PressButtonRegister)
async def start_registration_user(message: Message):
    await message.answer('Send me your <u>valid email address</u>.')
    await Registration.GetEmail.set()



@dp.message_handler(state=Registration.GetEmail)
async def get_email_address(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(f'1. Follow the link below\n   >>> https://post-shift.ru/api.php?action=reg&email={message.text}\n\n'
                         f'2. You will receive a hash in the form: {{"hash":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}}.\n\n'
                         f'3. I only need you to send "XXX...."')
    # ADD MORE EMAIL CHECKS FOR TRUTH
    await Registration.next()



@dp.message_handler(state=Registration.GetHash)
async def get_hash(message: Message, state: FSMContext):
    # 1. Перевірка правильності хешу - 32 символи.
    # 2. Перевірити запитом на post-shift чи це адекватний хеш.
    # 3. Перевірити запитом на post-shift скільки залишилося запитів.
    # 4. Перевірити чи вже такий хеш є в БД.

    if not len(message.text) == 32:  # 1
        await message.answer('Check that the hash entered is <u>correct</u>.')
    else:
        get_result = check_hash_availability(message.text) # 2
        if get_result:
            if int(get_result) == 100:
                await message.answer('It`s okay hash. Registering')
            else:
                await message.answer(f'It`s hash, but it`s already used. {get_result}')
        else:
            await message.answer('Sorry, but it`s not true hash.')




