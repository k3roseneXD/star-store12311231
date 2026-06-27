from aiogram.fsm.state import State, StatesGroup

class OrderState(StatesGroup):
    choosing_amount = State()
    waiting_for_amount = State()
    waiting_for_username = State()
    confirming = State()