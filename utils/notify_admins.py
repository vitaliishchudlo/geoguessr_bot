import logging

from aiogram import Dispatcher

from config.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Bot launched and ready to go!")
        except Exception as err:
            logging.exception(err)
