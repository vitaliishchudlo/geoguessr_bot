import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from geoguessr_api import send_confirmation_letter, confirm_password
from keyboards.default import confirmation_to_create, admin_menu, count_of_account_to_create, menu
from loader import dp
from post_shift_api import check_hash_availability, delete_all_active_emails_by_ip, register_email, \
    get_confirmation_email
from states import AdminMenu, MainMenu
from utils.db_api import get_hash
from utils.db_api import set_hash_status_deactive, input_account
from utils.processing_functions import generate_password, get_link_token


@dp.message_handler(text='Create accounts', state=AdminMenu.GetChoiceMenu)
async def menu_choice_create_account(message: Message, state: FSMContext):
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
                         f'Accounts can be registered: <u>{int(info_calls) // 2}</u>.\n\n'
                         f'Continue?',
                         reply_markup=confirmation_to_create)
    await state.update_data(hash=hash_from_database)
    await AdminMenu.next()


@dp.message_handler(text='Accept', state=AdminMenu.CreateAccounts)
async def accept_create_accounts(message: Message, state: FSMContext):
    await message.answer('How many accounts create?', reply_markup=count_of_account_to_create)
    await AdminMenu.next()


@dp.message_handler(Text(equals=['1', '2', '3', '4', '5', '10', '15', '20', '25', '50']),
                    state=AdminMenu.CreateAccountsCount)
async def accept_create_accounts(message: Message, state: FSMContext):
    hash_from_db = await state.get_data()
    hash_from_db = hash_from_db.get('hash')
    accounts_count = 0
    for account in range(int(message.text)):
        # 3. Create email address
        email_data = register_email(hash_from_db)
        email_address, email_key = email_data.get('email'), email_data.get('key')
        # 4. 1\2 First step of registration geoguessr account
        send_confirmation_letter(email_address)  # send confrimation letter to email
        # 5. Get a link from a letter that came in an email.
        await asyncio.sleep(5)  # wait for the letter to arrive in your inbox
        email_text = get_confirmation_email(hash_from_db, email_key)  # get letter text from email
        token = await get_link_token(email_text)  # take token, which complements link
        password = await generate_password()  # generate random password
        confirm_password(token, password)  # confirm account and set password
        delete_all_active_emails_by_ip()  # clear all email addresses by ip address
        input_account(email_address, password, hash_from_db)  # Insert account to DB
        await asyncio.sleep(5)
        await message.answer(f'\n{email_address}\n{password}\n\nCreated - ✅\nConfirmated - ✅\nAdded to DB - ✅')
        accounts_count += 1
    await message.answer(f'<b>{accounts_count}</b> account were created.', reply_markup=admin_menu)
    await AdminMenu.GetChoiceMenu.set()


@dp.message_handler(text='< Menu', state=AdminMenu.GetChoiceMenu)
async def go_back(message: Message, state: FSMContext):
    await message.reply('Exiting from admin menu', reply_markup=menu)
    await MainMenu.GetChoiceMenu.set()


@dp.message_handler(text='Cancel', state=AdminMenu.CreateAccounts)
async def go_cancel(message: Message):
    await message.answer('Cancelling...', reply_markup=admin_menu)
    await AdminMenu.GetChoiceMenu.set()
