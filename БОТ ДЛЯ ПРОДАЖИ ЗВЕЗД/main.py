# main.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import config
from handlers import start, order, admin

# Настройка логирования, чтобы видеть ошибки и статус
logging.basicConfig(level=logging.INFO)


async def main():
    print("--- Инициализация бота ---")
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация роутеров
    dp.include_routers(start.router, order.router, admin.router)

    print("--- Роутеры подключены. Запуск поллинга... ---")

    # Очистка очереди обновлений, чтобы бот не "давился" старыми сообщениями
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")