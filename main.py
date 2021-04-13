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


@dp.message_handler(commands=['start'])
async def get_user_mailbox(message: types.Message):
    await message.answer('Enter your mailbox address: ')
    await GetUserInfo.waiting_for_user_mailbox.set()


@dp.message_handler(state=GetUserInfo.waiting_for_user_mailbox, content_types=types.ContentTypes.TEXT)
async def mail_handler(message: types.Message, state: FSMContext):
    await message.answer(f'Ваша почта: {message.text}')
    GetUserInfo.lister.append(message.text)
    await message.answer('Now enter your hash code: ')
    await GetUserInfo.next()


@dp.message_handler(state=GetUserInfo.waiting_for_user_hash, content_types=types.ContentTypes.TEXT)
async def get_user_hash(message: types.Message, state: FSMContext):
        await state.update_data(hash=message.text)
        await message.answer('Checking hash...')
        GetUserInfo.lister.append(message.text)
        if message.text.lower() == '1':
            print('lol')
        else:
            print('xd')
        await state.finish()

        await message.answer(f'Your {GetUserInfo.lister}')
        await get_user_mailbox(message)


#     user_data = await state.get_data()
#     await message.answer(f'Your info: {user_data}')


if __name__ == '__main__':
    # starting bot
    executor.start_polling(dp, skip_updates=True)
