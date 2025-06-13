import asyncio
from database.config import settings
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.hd_main import router as main_router
from handlers.hd_admin import router as admin_router



async def main():
    bot = Bot(settings.TOKEN)
    dp = Dispatcher()
    scheduler = AsyncIOScheduler()   #Инициализируем планировщик
    scheduler.start()
    dp.include_router(main_router)    #Добавляем все роутеры
    dp.include_router(admin_router)
    dp["bot"] = bot  
    dp["scheduler"] = scheduler  
    try:
        await bot.delete_webhook(drop_pending_updates=True)   #Пропускаем все сообщения, отправленные до запуска бота
        await dp.start_polling(bot)
    finally:
        scheduler.shutdown()
if __name__ == "__main__":
    asyncio.run(main())
