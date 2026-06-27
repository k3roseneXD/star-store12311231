from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from config import config
from keyboards.menu import main_menu_kb

router = Router()


@router.callback_query(F.data == "confirm")
async def confirm_order(call: CallbackQuery, state: FSMContext, bot: Bot):  # Добавили bot в аргументы
    data = await state.get_data()

    # Текст заявки для админа
    admin_text = (
        "📥 <b>Новая заявка на пополнение:</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"⭐ <b>Количество:</b> {data['amount']} Stars\n"
        f"💰 <b>Сумма:</b> {data['price']} KGS\n"
        f"👤 <b>Юзернейм:</b> <code>{data['username']}</code>\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )

    try:
        # Отправляем сообщение админу через объект bot, который автоматически передается aiogram
        await bot.send_message(
            chat_id=config.ADMIN_ID,
            text=admin_text,
            parse_mode="HTML"
        )
        # Отвечаем пользователю
        await call.message.edit_text(
            "✅ <b>Заявка успешно отправлена!</b>\n\n"
            "Наш менеджер уже получил уведомление и свяжется с вами в ближайшее время.",
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"Ошибка при отправке админу: {e}")
        await call.message.answer("❌ Произошла ошибка при отправке заявки. Попробуйте позже.")

    await state.clear()