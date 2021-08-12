from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminMenu(StatesGroup):
    GetChoiceMenu = State()
    CreateAccountsCount = State()
