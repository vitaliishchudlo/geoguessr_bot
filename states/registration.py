from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    GetEmail = State()
    GetHash = State()
