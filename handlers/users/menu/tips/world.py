from aiogram.types import Message, InputFile

from keyboards.default import world_tip
from loader import dp
from states import Tips


@dp.message_handler(text='🌎 WORLD 🌎', state=Tips.GetRegionTips)
async def tips_world(message: Message):
    await message.reply('You have chosen the <u>world</u>. Make the next choice.', reply_markup=world_tip)
    await Tips.ChoiceWorldTips.set()


@dp.message_handler(text='🚗 Left- & Right-hand traffic 🚦', state=Tips.ChoiceWorldTips)
async def left_right_hand_traffic(message: Message):
    photo = InputFile('/home/vitalii/PycharmProjects/geoguessr_bot/media/main.png')
    await message.reply_photo(photo=photo, caption='🟦 ↑↓ Drives on the left\n🟥 ↓↑ Drives on the right')
