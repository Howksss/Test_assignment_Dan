from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from database.queries.orm import PnDs, Users
from keyboards.kb_main import tabs, Movements
from keyboards.kb_admin import admin_use
from database.config import settings
from aiogram.types import InputMediaPhoto
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot

router = Router()
bot = Bot(settings.TOKEN)

#Функция отправки сообщения, вызывается по таймеру, который задается на 32,5
async def send_reminder(chat_id: int):
    print("gugugaga")
    await bot.send_photo(chat_id=chat_id, caption = await PnDs.get_desc("spam"), photo= await PnDs.get_pic("spam"), parse_mode='HTML', reply_markup=await tabs(3))

#Роутер, отлавливающий отправку команды /start.
@router.message(Command("start"))
async def starting_command(message: Message, scheduler: AsyncIOScheduler):
    if str(message.from_user.id) == settings.ADMIN: #Проверяет юзера на админ-статус
        await message.answer(text="Вы находитесь в админ-панели", parse_mode='HTML', reply_markup=await admin_use())
    if await Users.user_exists(message.from_user.id) == False: #Проверяет использовал ли данный юзер бота раньше и если нет - записывает в бд.
        await Users.add_user(message.from_user.id, f'{message.from_user.first_name}_{message.from_user.last_name}')
    await message.answer_photo(photo= await PnDs.get_pic("main_table_0"),
                                caption= await PnDs.get_desc("main_table_0"),
                                parse_mode='HTML', reply_markup=await tabs(0))
    scheduler.add_job(
        send_reminder,
        'date',
        run_date=datetime.now() + timedelta(minutes=5),
        args=[message.from_user.id]
    ) #Функция планироващика, который запускает таймер на 5 минут и выполняет функцию send_reminder() по истечению времени


#Главный роутер всех страниц. 
@router.callback_query(Movements.filter())
async def movements_handler(callback: CallbackQuery, callback_data: Movements):
    await PnDs.add_visit(f'{callback_data.placement}_{callback_data.level}')
    print(f'{callback_data.placement}_{callback_data.level}')
    await callback.message.edit_media(InputMediaPhoto(media= await PnDs.get_pic(f'{callback_data.placement}_{callback_data.level}'), caption= await PnDs.get_desc(f'{callback_data.placement}_{callback_data.level}'), parse_mode='HTML'),reply_markup=await tabs(callback_data.level,callback_data.placement))



