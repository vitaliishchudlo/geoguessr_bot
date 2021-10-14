from aiogram.types import Message, InputFile

from keyboards.default import world_tip, tips
from loader import dp
from states import Tips


@dp.message_handler(text='🌎 WORLD 🌎', state=Tips.GetRegionTips)
async def tips_world(message: Message):
    await message.reply('You have chosen the <u>world</u>. Make the next choice.', reply_markup=world_tip)
    await Tips.ChoiceWorldTips.set()


@dp.message_handler(text='🔙 Back', state=Tips.ChoiceWorldTips)
async def tips_world_go_back(message: Message):
    await message.reply('Returning back', reply_markup=tips)
    await Tips.GetRegionTips.set()


@dp.message_handler(text='🚗 Left- & Right-hand traffics 🚦', state=Tips.ChoiceWorldTips)
async def left_right_hand_traffic(message: Message):
    photo = InputFile('/home/vitalii/PycharmProjects/geoguessr_bot/media/world/main.png')
    await message.reply_photo(photo=photo, caption='🟦 ↑↓ Drives on the left\n🟥 ↓↑ Drives on the right',
                              reply_markup=tips)
    await Tips.GetRegionTips.set()


@dp.message_handler(text='🌎 Map of countries with Google Street View 👁', state=Tips.ChoiceWorldTips)
async def google_street_view(message: Message):
    photo = InputFile('/home/vitalii/PycharmProjects/geoguessr_bot/media/world/second.png')
    await message.reply_photo(photo=photo, caption='🗺World map of all the countries that have Google Street View🌐',
                              reply_markup=tips)
    await Tips.GetRegionTips.set()
