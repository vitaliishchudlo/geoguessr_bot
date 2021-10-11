from aiogram.types import Message

from loader import dp
from states import MainMenu


@dp.message_handler(text='🆘 F.A.Q. 🆘', state=MainMenu.GetChoiceMenu)
async def menu_choice_faq(message: Message):
    await message.reply(
        '<b>GeoGuessrFreeBot</b> - bot which gives you the opportunity to play the game '
        '<a href="https://www.geoguessr.com/">Geoguessr</a> <u>for free.</u>\n\n'
        'For more details, <u><a href="https://www.youtube.com/">follow the link</a></u>',
        parse_mode='HTML',
        disable_web_page_preview=True
    )
