from aiogram import Router, F
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from database.db_setup import Database, UsersDatabase, InterDatabase
from keyboards.kb_main import tabs, Movements
from keyboards.kb_admin import AdminActions, backing, admin_use
from aiogram.types import InputMediaPhoto, InputMediaVideo, FSInputFile
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot
import os 

media_db = Database()

load_dotenv()
router = Router()
db = Database() 
usr_db = UsersDatabase()
bot = Bot(os.getenv('TOKEN'))


@router.callback_query(AdminActions.filter(F.action =="global_email"))
async def global_email_handler(callback: CallbackQuery, callback_data: AdminActions):
    for each in usr_db.all_users():
        await bot.send_message(chat_id=each[0], text =db.get_desc("spam_2"), parse_mode='HTML')
    await callback.message.answer(text="Рассылка проведена успешно", parse_mode='HTML', reply_markup=await backing())


    
@router.callback_query(AdminActions.filter(F.action =="backing"))
async def backing_handler(callback: CallbackQuery, callback_data: AdminActions):
    await callback.message.edit_text(text="Вы находитесь в админ-панели", parse_mode='HTML', reply_markup=await admin_use())




