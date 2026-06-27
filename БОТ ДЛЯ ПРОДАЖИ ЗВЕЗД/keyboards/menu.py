from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="⚡ Оформить покупку", callback_data="buy_stars")
    builder.button(text="💎 Актуальный прайс", callback_data="price")
    builder.button(text="🛡️ Гарантии и FAQ", callback_data="faq")
    builder.button(text="🤝 Центр поддержки", callback_data="support")
    builder.adjust(2)
    return builder.as_markup()

def back_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="🏠 Главное меню", callback_data="main_menu")
    return builder.as_markup()