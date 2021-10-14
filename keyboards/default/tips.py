from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tips = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌎 WORLD 🌎'),
        ],
        [
            KeyboardButton(text='🌞 Asia 🥢(UNWORKED)'),
            KeyboardButton(text='🇪🇺 Europe 🇪🇺(UNWORKED)')
        ],
        [
            KeyboardButton(text='🇺🇸 USA 🇺🇸'),
            KeyboardButton(text='🇦🇺 Australia 🦘(UNWORKED)')
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
            KeyboardButton(text='🚗 Left- & Right-hand traffics 🚦')
        ],
        [
            KeyboardButton(text='🌎 Map of countries with Google Street View 👁')
        ],
        [
            KeyboardButton(text='🔙 Back')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)


usa_tip = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚘 Blurred car plates in the states 🚍')
        ],
        [
            KeyboardButton(text='🚙 Requirement for front & rear license plates 🚗')
        ],
        [
            KeyboardButton(text='🪧 Speed highway signs in the states 🪧')
        ],
        [
            KeyboardButton(text='🔙 Back')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)