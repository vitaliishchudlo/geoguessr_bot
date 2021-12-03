import asyncio
import datetime

from aiogram.types import Message

from geoguessr_api import change_password_geoAPI
from loader import dp, bot
from states import MainMenu
from utils.db_api import menu_get_account, set_account_status_busy, check_user_limit, insert_user_limit, \
    delete_user_limit, change_account_password
from utils.notify_admins import no_accounts_notify
from utils.processing_functions.admin import generate_password


@dp.message_handler(text='🔺 Get account 🔻', state=MainMenu.GetChoiceMenu)
async def menu_choice_get_account(message: Message):
    msg_reply = await message.reply('I am starting creating account for you')
    account_data = menu_get_account()
    if account_data:
        # IF ACCOUNT EXISTS IN DATABASE --> CHECK USER LIMIT --> GIVE ACC FOR USER.
        user_limit = check_user_limit(id_telegram=message.from_user.id)
        if user_limit:
            user_limit = datetime.datetime.strptime(user_limit, '%Y-%m-%d %H:%M:%S')
            time_now = datetime.datetime.now()
            if time_now < user_limit:
                time_left = str(user_limit - time_now)[:-7]  # to delete microseconds
                return await bot.edit_message_text(
                    text=f'You need to wait before taking the next account.\nThere is time left: <u>{time_left}</u>',
                    chat_id=msg_reply.chat.id,
                    message_id=msg_reply.message_id
                )
            delete_user_limit(message.from_user.id)
            set_account_status_busy(account_data[0])  # Status busy(1) in database.
            time_end_limit = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=3),
                                                        '%Y-%m-%d %H:%M:%S')
            insert_user_limit(message.from_user.id, message.from_user.username, message.from_user.first_name,
                              message.from_user.last_name, time_end_limit)
            await bot.edit_message_text(
                text=f'Here is your <u>free account</u>:\n\nEmail: {account_data[0]}\nPassword: {account_data[1]}',
                chat_id=msg_reply.chat.id,
                message_id=msg_reply.message_id
            )
            await asyncio.sleep(300)
            new_password = await generate_password()
            change_password_geoAPI(account_data[0], account_data[1], new_password)
            change_account_password(account_data[0], account_data[1], new_password)
            return await bot.edit_message_text(
                text=f'Account expired :-(',
                chat_id=msg_reply.chat.id,
                message_id=msg_reply.message_id
            )
        delete_user_limit(message.from_user.id)
        set_account_status_busy(account_data[0])  # Status busy(1) in database.
        time_end_limit = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=3),
                                                    '%Y-%m-%d %H:%M:%S')
        insert_user_limit(message.from_user.id, message.from_user.username, message.from_user.first_name,
                          message.from_user.last_name, time_end_limit)
        await bot.edit_message_text(
            text=f'Here is your <u>free account</u>:\n\nEmail: {account_data[0]}\nPassword: {account_data[1]}',
            chat_id=msg_reply.chat.id,
            message_id=msg_reply.message_id
        )
        await asyncio.sleep(300)
        new_password = await generate_password()
        change_password_geoAPI(account_data[0], account_data[1], new_password)
        change_account_password(account_data[0], account_data[1], new_password)
        return await bot.edit_message_text(
            text=f'Account expired :-(',
            chat_id=msg_reply.chat.id,
            message_id=msg_reply.message_id
        )
    else:
        # Notify all admins.
        await no_accounts_notify(dp)
        await message.reply('There are currently no active accounts. We have already notified the administrator.')
