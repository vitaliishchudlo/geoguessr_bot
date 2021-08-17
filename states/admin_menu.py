from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminMenu(StatesGroup):
    GetChoiceMenu = State()
    CreateAccounts = State()
    CreateAccountsCount = State()
