from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.menu import main_menu_kb, back_kb
from utils.content import CONTENT

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    text = (
        "✨ <b>Stars Store — Инновационный сервис пополнения Telegram Stars</b>\n\n"
        "Мы предоставляем частным лицам и бизнесу возможность быстрого и безопасного приобретения внутренней валюты Telegram. Наш сервис построен на принципах прозрачности, высокой скорости и полной конфиденциальности каждой транзакции.\n\n"
        "🚀 <b>Почему выбирают Wallet_toncoin_1:</b>\n"
        "• <b>Официальные протоколы:</b> Полная легальность и безопасность операций.\n"
        "• <b>Выгодный курс:</b> Мы анализируем рынок, чтобы предложить вам оптимальные условия.\n"
        "• <b>Персональный подход:</b> Наша поддержка сопровождает вашу заявку от старта до зачисления Stars.\n"
        "• <b>Моментальная обработка:</b> Стандартное время ответа системы — менее 15 минут.\n\n"
        "<i>Начните работу с профессиональным инструментом — выберите интересующий вас раздел в меню ниже:</i>"
    )
    await message.answer(text, reply_markup=main_menu_kb(), parse_mode="HTML")

@router.callback_query(F.data.in_(["price", "faq", "support"]))
async def show_info(call: CallbackQuery):
    await call.message.edit_text(CONTENT[call.data]["text"], reply_markup=back_kb(), parse_mode="HTML")

@router.callback_query(F.data == "main_menu")
async def back_to_main(call: CallbackQuery):
    text = "✨ <b>Flash Lite Digital Assets — Premium Service</b>\n\nВыберите действие:"
    await call.message.edit_text(text, reply_markup=main_menu_kb(), parse_mode="HTML")