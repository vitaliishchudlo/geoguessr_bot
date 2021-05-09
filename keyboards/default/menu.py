from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧭 Register 🚩'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Get account'),
            KeyboardButton(text='Dice')
        ],
        [
            KeyboardButton(text='Donate'),
            KeyboardButton(text='F.A.Q.')
        ],
    ],
    resize_keyboard=True, one_time_keyboard=False
)

# next = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text='Продолжить'),
#             ],
#         ],
#         resize_keyboard=True, one_time_keyboard=True
#     )