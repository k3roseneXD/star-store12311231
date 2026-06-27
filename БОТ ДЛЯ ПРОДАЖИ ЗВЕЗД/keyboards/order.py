from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_amount_kb():
    builder = InlineKeyboardBuilder()
    for amt in [100, 250, 500, 1000, 2500, 5000]:
        builder.button(text=f"⭐ {amt}", callback_data=f"amt_{amt}")
    builder.button(text="✏️ Другое количество", callback_data="other_amount")
    builder.button(text="🏠 Главное меню", callback_data="main_menu")
    builder.adjust(2)
    return builder.as_markup()

def confirm_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Подтвердить", callback_data="confirm")
    builder.button(text="❌ Отмена", callback_data="main_menu")
    return builder.as_markup()