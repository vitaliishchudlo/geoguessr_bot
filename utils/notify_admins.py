import datetime
import logging

from aiogram import Dispatcher

from data.config import admins
from keyboards.default import write_menu


async def on_startup_admin_notify(dp: Dispatcher):
    for admin in admins:
        try:
            msg = await dp.bot.send_message(
                admin,
                f'[{datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}] ⚙ The bot has started!',
                reply_markup=write_menu
                # disable_notification = True
            )
            # await dp.bot.delete_message(msg.chat.id, msg.message_id)
        except Exception as err:
            logging.exception(err)


async def no_accounts_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(
                admin,
                f'[{datetime.datetime.now().strftime("%y/%m/%d, %H:%M:%S")}] ⚙ Accounts finished.'
            )

        except Exception as err:
            logging.exception(err)
