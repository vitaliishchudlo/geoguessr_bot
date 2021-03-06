from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tips = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='π WORLD π'),
        ],
        [
            KeyboardButton(text='π Asia π₯’(UNWORKED)'),
            KeyboardButton(text='πͺπΊ Europe πͺπΊ(UNWORKED)')
        ],
        [
            KeyboardButton(text='πΊπΈ USA πΊπΈ'),
            KeyboardButton(text='π¦πΊ Australia π¦(UNWORKED)')
        ],
        [
            KeyboardButton(text='π Back')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

world_tip = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='π Left- & Right-hand traffics π¦')
        ],
        [
            KeyboardButton(text='π Map of countries with Google Street View π')
        ],
        [
            KeyboardButton(text='π Back')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

usa_tip = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='π Blurred car plates in the states π')
        ],
        [
            KeyboardButton(text='π Requirement for front & rear license plates π')
        ],
        [
            KeyboardButton(text='πͺ§ Speed highway signs in the states πͺ§')
        ],
        [
            KeyboardButton(text='π Back')
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)
