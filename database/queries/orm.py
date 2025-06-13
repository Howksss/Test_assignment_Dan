from sqlalchemy import select
from database.db_setup import async_engine, async_session, Base
from database.models import PnDsOrm, UserOrm

#Класс общения с таблицей Pictures and Descriptions
class PnDs():


    #Стартовый метод создания всех таблиц, используется один раз
    @staticmethod
    async def create_tables():
        async_engine.echo = False
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        async_engine.echo = True

    #Добавление данных о странице
    @staticmethod
    async def insert_data(stage_name, desc_content, pic_content):
        async with async_session() as s:  
            page = PnDsOrm(stage_name=stage_name, desc_content= desc_content, pic_content=pic_content)
            s.add(page)
            await s.commit()  
            await s.close()

    #Получение текста(description) на определенной странице
    @staticmethod
    async def get_desc(stage_name: str):
        async with async_session() as s:
            page = await s.get(PnDsOrm, stage_name)
            return page.desc_content
        
    #Получение медиа(picture) на определенной странице   
    @staticmethod
    async def get_pic(stage_name: str):
        async with async_session() as s:
            page = await s.get(PnDsOrm, stage_name)
            return page.pic_content

    #Добавление визита на определенную страницу(элементарная статистика)
    @staticmethod
    async def add_visit(stage_name: str):
        async with async_session() as s:
            updated_page = await s.get(PnDsOrm, stage_name)
            updated_page.visits +=1
            await s.commit()
            await s.close()  

#Класс общения с таблицей Users
class Users():

    #Добавление нового пользователя в бд
    @staticmethod
    async def add_user(user_id: int, user_name: str):
        async with async_session() as s:  
            user = UserOrm(user_id = user_id, user_name = user_name)
            s.add(user)
            await s.commit()  
            await s.close()  

    #Проверка, существует ли пользователь True/False
    @staticmethod
    async def user_exists(user_id: str):
        async with async_session() as s:
            user = await s.get(UserOrm, user_id)
            return (bool(user))
        
    #Получение всех пользователей, когда-либо запускавших бота
    @staticmethod
    async def all_users():
        async with async_session() as s:
            query = select(UserOrm)
            res = await s.execute(query)
            result = res.scalars().all()
            users = []
            for each in range(0, len(result)):
                users.append(result[each].user_id)     #Возвращает именно id
            print(users)

