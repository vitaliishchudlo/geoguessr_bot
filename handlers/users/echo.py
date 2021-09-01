from aiogram.types import Message, ContentType, ReplyKeyboardRemove

from loader import dp


@dp.message_handler()
async def bot_echo(message: Message):
    await message.answer(f"You entered bad command.\n"
                         f"You can type <b>'/'</b> and select the correct command.", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['json'])
async def get_username(message: Message):
    await message.answer(f'Your result json: \n{message.as_json()}')  # show json answer


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[3].file_id)
