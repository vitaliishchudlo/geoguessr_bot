from aiogram.dispatcher.filters.state import StatesGroup, State


class MainMenu(StatesGroup):
    GetChoiceMenu = State()


class Tips(StatesGroup):
    GetRegionTips = State()

    ChoiceWorldTips = State()
    ChoiceUsaTips = State()