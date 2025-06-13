from aiogram import Router, F
from aiogram.types import CallbackQuery
from database.queries.orm import Users, PnDs
from keyboards.kb_admin import AdminActions, backing, admin_use
from database.config import settings
from aiogram import Bot

router = Router()
bot = Bot(settings.TOKEN)


#Роутер, отлавливающий коллбек события отправки рассылки и реализуюзий рассылку по списку всех пользователей
@router.callback_query(AdminActions.filter(F.action =="global_email"))
async def global_email_handler(callback: CallbackQuery, callback_data: AdminActions):
    for each in await Users.all_users():
        await bot.send_message(chat_id=each, text = await PnDs.get_desc("spam_2"), parse_mode='HTML')
    await callback.message.answer(text="Рассылка проведена успешно", parse_mode='HTML', reply_markup=await backing())


#Роутер, отлавливающий нажатие кнопки назад после выполнения рассылки и возвращающий в админ-меню
@router.callback_query(AdminActions.filter(F.action =="backing"))
async def backing_handler(callback: CallbackQuery, callback_data: AdminActions):
    await callback.message.edit_text(text="Вы находитесь в админ-панели", parse_mode='HTML', reply_markup=await admin_use())




