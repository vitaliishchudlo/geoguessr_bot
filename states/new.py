from aiogram.dispatcher.filters.state import StatesGroup, State


class New(StatesGroup):
    Email = State()
    Emailsave = State()
    Menu = State()

