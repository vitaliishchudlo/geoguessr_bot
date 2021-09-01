from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Get account'),
        ],
        #[
        #    KeyboardButton(text='Tips'),
        #    # KeyboardButton(text='Maps')
        #],
        #[
        #    KeyboardButton(text='Donate'),
        #    KeyboardButton(text='F.A.Q.')
        #]
    ],
    resize_keyboard=True, one_time_keyboard=False
)
