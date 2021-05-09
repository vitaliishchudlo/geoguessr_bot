from aiogram.dispatcher.filters.state import StatesGroup, State


class Menu(StatesGroup):
    ShowMenu = State()

class ResultChoice(StatesGroup):
    GetAccount = State()
    Dice = State()
    FAQ = State()
    Donate = StatesGroup()