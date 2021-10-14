from aiogram.types import Message, InputFile

from keyboards.default import usa_tip, tips
from loader import dp
from states import Tips


@dp.message_handler(text='🇺🇸 USA 🇺🇸', state=Tips.GetRegionTips)
async def tips_usa(message: Message):
    await message.reply('You have chosen the <u>USA</u>. Make the next choice.', reply_markup=usa_tip)
    await Tips.ChoiceUsaTips.set()


@dp.message_handler(text='🔙 Back', state=Tips.ChoiceUsaTips)
async def tips_usa_go_back(message: Message):
    await message.reply('Returning back', reply_markup=tips)
    await Tips.GetRegionTips.set()


@dp.message_handler(text='🚘 Blurred car plates in the states 🚍', state=Tips.ChoiceUsaTips)
async def left_right_hand_traffic(message: Message):
    photo = InputFile('/home/vitalii/PycharmProjects/geoguessr_bot/media/usa/Blurred.png')
    await message.reply_photo(photo=photo, caption='Map of orientation in the states by blurred license plates\n\n'
                                                   '❗ Indiana - not specified ❗', reply_markup=tips)
    await Tips.GetRegionTips.set()


@dp.message_handler(text='🚙 Requirement for front & rear license plates 🚗', state=Tips.ChoiceUsaTips)
async def left_right_hand_traffic(message: Message):
    photo = InputFile('/home/vitalii/PycharmProjects/geoguessr_bot/media/usa/front&rear.png')
    await message.reply_photo(photo=photo, caption='🔵 Blue - needs car plates <u>only rear.</u>\n'
                                                   '🟢 Green - needs car plates on <u>front and rear.</u> ',
                              reply_markup=tips)
    await Tips.GetRegionTips.set()


@dp.message_handler(text='🪧 Speed highway signs in the states 🪧', state=Tips.ChoiceUsaTips)
async def left_right_hand_traffic(message: Message):
    photo = InputFile('/home/vitalii/PycharmProjects/geoguessr_bot/media/usa/state-highway-signs.png')
    await message.reply_photo(photo=photo, caption='Map of orientation in the states by speed signs on highway',
                              reply_markup=tips)
    await Tips.GetRegionTips.set()
