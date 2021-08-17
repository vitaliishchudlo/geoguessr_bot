import datetime

from aiogram.types import Message

from loader import dp
from states import MainMenu
from utils.db_api import menu_get_account, set_account_status_busy, check_user_limit, insert_user_limit, \
    delete_user_limit
from utils.notify_admins import no_accounts_notify


@dp.message_handler(text='Get account', state=MainMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    account_data = menu_get_account()
    if account_data:
        # IF ACCOUNT EXISTS IN DATABASE --> CHECK USER LIMIT --> GIVE ACC FOR USER.
        user_limit = check_user_limit(user_id=message.from_user.id)
        if user_limit:
            user_limit = datetime.datetime.strptime(user_limit, '%Y-%m-%d %H:%M:%S')
            time_now = datetime.datetime.now()
            if time_now < user_limit:
                time_left = str(user_limit - time_now)[:-7]  # to delete microseconds
                return await message.answer('You need to wait before taking the next account.\n'
                                            f'There is time left: <u>{time_left}</u>')

            delete_user_limit(message.from_user.id)
            set_account_status_busy(account_data[0])  # Status busy(1) in database.
            time_end_limit = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=3),
                                                        '%Y-%m-%d %H:%M:%S')
            insert_user_limit(message.from_user.id, message.from_user.username, message.from_user.first_name,
                              message.from_user.last_name, time_end_limit)
            return await message.answer(f'Here is your <u>free account</u>:\n\n'
                                        f'Email: {account_data[0]}\nPassword: {account_data[1]}')
        delete_user_limit(message.from_user.id)
        set_account_status_busy(account_data[0])  # Status busy(1) in database.
        time_end_limit = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=3),
                                                    '%Y-%m-%d %H:%M:%S')
        insert_user_limit(message.from_user.id, message.from_user.username, message.from_user.first_name,
                          message.from_user.last_name, time_end_limit)
        return await message.answer(f'Here is your <u>free account</u>:\n\n'
                                    f'Email: {account_data[0]}\nPassword: {account_data[1]}')
    else:
        # Notify all admins.
        await no_accounts_notify(dp)
        await message.answer(f'There are currently no active accounts. '
                             f'We have already notified the administrator.')
