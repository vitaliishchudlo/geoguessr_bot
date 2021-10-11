from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tips = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌎 WORLD 🌎'),
        ],
        [
            KeyboardButton(text='🌞 Asia 🥢'),
            KeyboardButton(text='🇪🇺 Europe 🇪🇺')
        ],
        [
            KeyboardButton(text='🇺🇸 USA 🇺🇸'),
            KeyboardButton(text='🇦🇺 Australia 🦘')
        ],
        [
            KeyboardButton(text='🔙 Back')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

world_tip = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚗 Left- & Right-hand traffic 🚦')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)