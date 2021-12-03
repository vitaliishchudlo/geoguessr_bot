from aiogram import Dispatcher
from aiogram.types import Message

from .db_api import get_accounts_telegram_ids
from keyboards.default import write_menu


async def on_startup_users_cleaning(dp: Dispatcher):
    users_ids = get_accounts_telegram_ids()
    for user_id in users_ids:
        msg = await dp.bot.send_message(
            user_id,
            f'[SYSTEM] ⚙ [CLEANING CHAT]',
            disable_notification=True,
            reply_markup=write_menu,


        )
        await dp.bot.delete_message(msg.chat.id, msg.message_id)