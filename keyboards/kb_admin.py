from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton 
from database.db_setup import ButonsDatabase

class AdminActions(CallbackData, prefix = '2'):
    action: str


async def admin_use():
    builder=InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Разослать напоминание", callback_data=AdminActions(action="global_email").pack()))
    return builder.as_markup()

async def backing():
    builder=InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Назад", callback_data=AdminActions(action="backing").pack()))
    return builder.as_markup()
