import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.hd_main import router as main_router
from handlers.hd_admin import router as admin_router

load_dotenv()

async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    scheduler = AsyncIOScheduler()
    scheduler.start()
    dp.include_router(main_router)
    dp.include_router(admin_router)
    dp["bot"] = bot  
    dp["scheduler"] = scheduler  
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        scheduler.shutdown()
if __name__ == "__main__":
    asyncio.run(main())
