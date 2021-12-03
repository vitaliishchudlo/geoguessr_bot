from utils.notify_users import on_startup_users_cleaning
from utils.notify_admins import on_startup_admin_notify

async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)

    await on_startup_admin_notify(dp) # NOTIFY ONLY ADMINS
    #await on_startup_users_cleaning(dp) # CLEAR KEYBOARDS FOR ALL USERS




if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)  # on_shutdown=[func] - will start when
    # ending bot
