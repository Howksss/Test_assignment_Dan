from aiogram import Router
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from database.db_setup import Database, UsersDatabase, InterDatabase
from keyboards.kb_main import tabs, Movements
from keyboards.kb_admin import admin_use
from aiogram.types import InputMediaPhoto, InputMediaVideo, FSInputFile
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot
import os 
from ast import literal_eval

media_db = Database()

load_dotenv()
router = Router()
db = Database() 
usr_db = UsersDatabase()
acts_db = InterDatabase()
bot = Bot(os.getenv('TOKEN'))

async def send_reminder(chat_id: int):
    print("gugugaga")
    await bot.send_photo(chat_id=chat_id, caption =db.get_desc("spam"), photo=db.get_pic("spam"), parse_mode='HTML', reply_markup=await tabs(3))


@router.message(Command("start"))
async def starting_command(message: Message, scheduler: AsyncIOScheduler):
    if str(message.from_user.id) in literal_eval(os.getenv("ADMIN")):
        await message.answer(text="Вы находитесь в админ-панели", parse_mode='HTML', reply_markup=await admin_use())
    if usr_db.user_exists(message.from_user.id) == False:
        usr_db.add_user(message.from_user.id, f'{message.from_user.first_name}_{message.from_user.last_name}')
    await message.answer_photo(photo=db.get_pic("main_table_0"),
                                caption=db.get_desc("main_table_0"),
                                parse_mode='HTML', reply_markup=await tabs(0))
    scheduler.add_job(
        send_reminder,
        'date',
        run_date=datetime.now() + timedelta(minutes=5),
        args=[message.from_user.id]
    )



@router.callback_query(Movements.filter())
async def movements_handler(callback: CallbackQuery, callback_data: Movements):
    acts_db.add_visit(f'{callback_data.placement}_{callback_data.level}')
    print(f'{callback_data.placement}_{callback_data.level}')
    await callback.message.edit_media(InputMediaPhoto(media=db.get_pic(f'{callback_data.placement}_{callback_data.level}'), caption=db.get_desc(f'{callback_data.placement}_{callback_data.level}'), parse_mode='HTML'),reply_markup=await tabs(callback_data.level,callback_data.placement))



