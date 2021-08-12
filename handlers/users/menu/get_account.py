from aiogram.types import Message

from loader import dp
from states import MainMenu
from utils.db_api import menu_get_account, set_account_status_busy
from utils.notify_admins import no_accounts_notify


@dp.message_handler(text='Get account', state=MainMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    account_data = menu_get_account()
    if account_data:
        # IF ACCOUNT EXISTS IN DATABASE ---> GIVE IT FOR USER.
        set_account_status_busy(account_data[0])  # Status busy(1) in database.
        await message.answer(f'Here is your <u>free account</u>:\n\n'
                             f'Email: {account_data[0]}\nPassword: {account_data[1]}')
    else:
        # Notify all admins.
        await no_accounts_notify(dp)
        await message.answer(f'There are currently no active accounts. '
                             f'We have already notified the administrator.')
