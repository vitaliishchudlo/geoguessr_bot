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
    resize_keyboard=True, one_time_keyboard=False
)

confirmation_to_create = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Accept'),
            KeyboardButton(text='Cancel')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=False
)
