from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Create accounts'),
        ],
        [
            KeyboardButton(text='<- Back'),
            KeyboardButton(text='Others... (unwork)'),
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

confirmation_to_create = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Accept'),
            KeyboardButton(text='Cancel')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)


count_of_account_to_create = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
        ],
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='15'),
            KeyboardButton(text='20'),
            KeyboardButton(text='25'),
            KeyboardButton(text='50'),
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)