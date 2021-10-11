from aiogram.types import Message

from keyboards.default import tips
from loader import dp
from states import MainMenu, Tips


@dp.message_handler(text='✨ Tips 💫', state=MainMenu.GetChoiceMenu)
async def menu_choice_tips(message: Message):
    await message.reply('Choose the region', reply_markup=tips)
    await Tips.GetRegionTips.set()
