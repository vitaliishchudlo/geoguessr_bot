from aiogram import Bot, Dispatcher, types, executor
from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging

# bot object
bot = Bot("1718029958:AAFyyDpFHcSO-5JGiA_Oeibeck5Kt7t_UiE", parse_mode=types.ParseMode.HTML)
# dispatcher for bot
dp = Dispatcher(bot, storage=MemoryStorage())
# Включаємо логування, щоб не пропустити важливі повідомлнення
logging.basicConfig(level=logging.INFO)


class GetUserInfo(StatesGroup):
    waiting_for_user_mailbox = State()
    waiting_for_user_hash = State()
    lister = []


# def register_handlers_food(dp: Dispatcher):
#     dp.register_message_handler(get_user_mailbox, commands='start', state=GetUserInfo.waiting_for_user_mailbox)
#     dp.register_message_handler(get_user_hash, state=GetUserInfo.waiting_for_user_hash)


@dp.message_handler(commands=['start'])
async def get_user_mailbox(message: types.Message):
    await message.answer('Enter your mailbox address: ')
    await GetUserInfo.next()


@dp.message_handler(state=GetUserInfo.waiting_for_user_mailbox, content_types=types.ContentTypes.TEXT)
async def mail_handler(message: types.Message, state: FSMContext):
    await message.answer(f'Ваша почта: {message.text}')
    GetUserInfo.lister.append(message.text)
    await message.answer('Now enter your hash code')
    await GetUserInfo.waiting_for_user_hash.set()


@dp.message_handler(state=GetUserInfo.waiting_for_user_hash, content_types=types.ContentTypes.TEXT)
async def get_user_hash(message: types.Message, state: FSMContext):
    await message.answer('checking hash')
    GetUserInfo.lister.append(message.text)
    print(message.text)
    if message.text.lower() == 1:
        print('lol')
    else:
        print('xd')
    await state.finish()
    await message.answer(f'Your info {GetUserInfo.lister[0]}, {GetUserInfo.lister[1]}')
    GetUserInfo.lister.clear()
    await get_user_mailbox(message)

# async def confirmation_info(message: types.Message, state: FSMContext):
#     if message.text.lower() == 2 or 3:
#         await message.answer('Two or Three')
#     else:
#         print('lol')
#         await message.answer('Something Else')
#
#     user_data = await state.get_data()
#     await message.answer(f'Your info: {user_data}')


if __name__ == '__main__':
    # starting bot
    executor.start_polling(dp, skip_updates=True)
