from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from states.order_state import OrderState
from keyboards.order import get_amount_kb, confirm_kb
from keyboards.menu import main_menu_kb

router = Router()

@router.callback_query(F.data == "buy_stars")
async def choose_amount(call: CallbackQuery, state: FSMContext):
    await state.set_state(OrderState.choosing_amount)
    await call.message.edit_text("Выберите количество:", reply_markup=get_amount_kb())

@router.callback_query(OrderState.choosing_amount, F.data.startswith("amt_"))
async def set_amount(call: CallbackQuery, state: FSMContext):
    amt = call.data.split("_")[1]
    await state.update_data(amount=amt, price=int(amt)*1.6)
    await state.set_state(OrderState.waiting_for_username)
    await call.message.edit_text("Введите @username получателя:")

@router.message(OrderState.waiting_for_username)
async def process_username(message: Message, state: FSMContext):
    if not message.text.startswith("@"):
        return await message.answer("Ошибка! Должно начинаться с @")
    await state.update_data(username=message.text)
    data = await state.get_data()
    await message.answer(f"📦 Заявка: {data['amount']} Stars\n💰 Цена: {data['price']} сом\n👤 Юзер: {data['username']}", reply_markup=confirm_kb())
    await state.set_state(OrderState.confirming)