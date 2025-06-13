from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton 

#Коллбек-класс Админа
class AdminActions(CallbackData, prefix = '2'):
    action: str

#Функция, возвращающая клавиатуру админ-меню
async def admin_use():
    builder=InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Разослать напоминание", callback_data=AdminActions(action="global_email").pack()))
    return builder.as_markup()

#Функция, добавляющая кнопку возвращения в админ-меню после отправки рассылки
async def backing():
    builder=InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Назад", callback_data=AdminActions(action="backing").pack()))
    return builder.as_markup()
