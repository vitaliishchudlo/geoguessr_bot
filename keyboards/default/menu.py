from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reg = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Зарегисрироваться'),
            ],
        ],
        resize_keyboard=True, one_time_keyboard=True
    )
nextt = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Продолжить'),
            ],
        ],
        resize_keyboard=True, one_time_keyboard=True
    )


menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Get account'),
                KeyboardButton(text='Delete account')
            ],
            [
                KeyboardButton(text='Donate'),
            ],
        ],
        resize_keyboard=True, one_time_keyboard=True
    )

