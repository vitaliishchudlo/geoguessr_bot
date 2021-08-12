from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧭 Register 🚩'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)
