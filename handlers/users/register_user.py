from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default import menu
from loader import dp
from post_shift_api import check_hash_availability
from states import Start
from states.registration import Registration
from utils.db_api import user_hash_status, register_hash, register_user


@dp.message_handler(text='🧭 Register 🚩', state=Start.PressButtonRegister)
async def start_registration_user(message: Message):
    await message.answer('Send me your <u>valid email address</u>.')
    await Registration.GetEmail.set()


@dp.message_handler(state=Registration.GetEmail)
async def get_email_address(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(
        f'1. Follow the link below\n   >>> https://post-shift.ru/api.php?action=reg&email={message.text}\n\n'
        f'2. You will receive a hash in the form: {{"hash":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}}.\n\n'
        f'3. I only need you to send "XXX...."')
    # ADD MORE EMAIL CHECKS FOR TRUTH
    await Registration.next()


@dp.message_handler(text='back', state=Registration.GetHash)
async def go_back(message: Message):
    await message.answer('Send me your <u>valid email address again</u>.')
    await Registration.GetEmail.set()


@dp.message_handler(state=Registration.GetHash)
async def get_hash(message: Message, state: FSMContext):
    await message.answer('Starting hash validation...')

    if not len(message.text) == 32:  # 1. Hash validation - 32 characters.
        await message.answer('Check that the hash entered is <u>correct</u>.')
    else:
        get_result = check_hash_availability(message.text)

        if not get_result:
            await message.answer('Sorry, but it`s not true hash.')
        else:

            if not int(get_result) == 100:  # 3. Check the number of available requests by post-shift request.
                await message.answer(f'It`s hash, but it`s already used. {get_result}')
            else:
                if not user_hash_status(message.text):
                    register_hash(message.text, message.from_user.id)  # registering HASH in database
                    await message.answer('Registering 1\\2 - done.')
                    info = await state.get_data()
                    register_user(message.from_user, info.get('email'))  # registering USER in database
                    await message.answer('Registering 2\\2 - done.\n\nYou have successfully register in system.',
                                         reply_markup=menu)
                    await state.finish()
                else:
                    await message.answer('This hash is already registered in system.')
