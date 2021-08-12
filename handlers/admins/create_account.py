from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default import confirmation_to_create, admin_menu
from loader import dp
from post_shift_api import check_hash_availability
from states import AdminMenu
from utils.db_api import get_hash, set_hash_status_deactive





@dp.message_handler(text='Create accounts', state=AdminMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    # 1. Get hash from DB, if false > say user
    hash_from_database = get_hash()  # hash from db --> 2868985227b081ea418f29533e3eaafa
    if not hash_from_database:
        await message.answer('No available hash for registering account in database.')
    # 2. Check hash for available requests >= 2-3, if false - set unactive in DB table, status 1
    info_calls = check_hash_availability(hash_from_database)
    if not info_calls or int(info_calls) <= 3:
        # Set unactive status in DB for this hash
        set_hash_status_deactive(hash_from_database)
        return await message.answer(f'Hash: <b>{hash_from_database}</b> was deactivated.\n'
                                    f'Number of requests: <u>{info_calls}</u>')
    await message.answer(f'Hash: <b>{hash_from_database}</b> is ready.\n'
                         f'Number of requests: <u>{info_calls}</u>.\n'
                         f'Accounts will be registered: <u>{int(info_calls) // 2}</u>.\n\n'
                         f'Continue?',
                         reply_markup=confirmation_to_create)
    await AdminMenu.next()


@dp.message_handler(text='<- Back', state=AdminMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    await message.answer('Going back', reply_markup=ReplyKeyboardRemove())
    await AdminMenu

@dp.message_handler(text='Accept', state=AdminMenu.CreateAccountsCount)
async def menu_choice_get_account(message: Message):
    pass


@dp.message_handler(text='Cancel', state=AdminMenu.CreateAccountsCount)
async def menu_choice_get_account(message: Message):
    await message.answer('Cancelling...', reply_markup=admin_menu)
