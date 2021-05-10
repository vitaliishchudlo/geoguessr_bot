from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.default import menu
from loader import dp
from post_shift_api import check_hash
from states.menu import Menu
from states.registration import Registration
from utils.db_api import MySql


@dp.message_handler(state=Registration.GetEmail)
async def get_email_address(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(f"Follow the link and get hash-code:\n"
                         f"https://post-shift.ru/api.php?action=reg&email={message.text}\n"
                         "GIVE ME ONLY '..XXX..'. EXAMPLE: {'hash':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}  ")
    await Registration.next()


@dp.message_handler(state=Registration.GetHash)
async def get_user_hash(message: Message, state: FSMContext):
    result_hash = check_hash(message.text)
    if message.text == '{error	"this_email_is_already_in_use"}' or \
        message.text == '{"error":"a_person_with_this_ip_is_already_registered"}':
        await message.answer('You found mistery pasxalka.', reply_markup=menu)
        MySql().register_hash(message.text, message.from_user.id)
        data = await state.get_data()
        req = MySql().register_user(message.from_user, data.get('email'))
        if req is True:
            await message.answer('You have successfully registered!', reply_markup=menu)
            await Menu.ChoiceMenu.set()
        else:
            await message.answer(f'Something went wrong.\n{req}\nPlease try again /start.')
            await state.finish()
        await Menu.ChoiceMenu.set()
    else:
        if result_hash == 6000:
            MySql().register_hash(message.text, message.from_user.id)
            data = await state.get_data()
            req = MySql().register_user(message.from_user, data.get('email'))
            if req is True:
                await message.answer('You have successfully registered!', reply_markup=menu)
                await Menu.ChoiceMenu.set()
            else:
                await message.answer(f'Something went wrong.\n{req}\nPlease try again /start.')
                await state.finish()
        elif result_hash == 6001:
            await message.answer('This hash already used. Try write correctly hash')
        else:
            await message.answer(f'This is not hash, try again.\nReason:\n{result_hash}')



