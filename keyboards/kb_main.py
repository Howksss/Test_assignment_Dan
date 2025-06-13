from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton  

#Коллбек-класс основного роутера
class Movements(CallbackData, prefix = ' 1'):
    placement: str
    level: int

#Функция, возвращающая клавиатуры в зависимости от страницы level.
async def tabs(level,stage="main_table"):
    match level:
        case 0:
            builder=InlineKeyboardBuilder()
            builder.row(InlineKeyboardButton(text="Далее", callback_data=Movements(placement=stage, level = 1).pack()), 
                        InlineKeyboardButton(text = "Оплатить", callback_data=Movements(placement=stage, level = 3).pack()))
            return builder.as_markup()
        case 1:
            builder=InlineKeyboardBuilder()
            builder.row(InlineKeyboardButton(text="Понятно, дальше", callback_data=Movements(placement=stage, level = 2).pack()))
            return builder.as_markup()
        case 2:
            builder=InlineKeyboardBuilder()
            builder.row(InlineKeyboardButton(text="А сколько стоит?", callback_data=Movements(placement=stage, level = 3).pack()))
            return builder.as_markup()
        case 3:
            builder=InlineKeyboardBuilder()
            builder.row(InlineKeyboardButton(text="Карта РФ", url="", callback_data=Movements(placement="", level = 1).pack()), 
                        InlineKeyboardButton(text = "Stripe (в $)", url="", callback_data=Movements(placement="", level = 1).pack()))
            builder.row(InlineKeyboardButton(text="Lava (в $)", url="", callback_data=Movements(placement="", level = 1).pack()), 
                        InlineKeyboardButton(text = "Служба заботы", url="https://t.me/Howksss", callback_data=Movements(placement="", level = 1).pack()))
            return builder.as_markup()
        
