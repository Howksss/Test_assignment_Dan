from sqlalchemy import Integer, String, Text, text
from sqlalchemy.orm  import Mapped, mapped_column
from typing import Annotated
import datetime
from database.db_setup import Base


#Оформление аннотаций алхимии (устойчивые однообразные типы, которые в будущем можно удобно применять в разных таблицах простым обозначением Mapped[idpk])
idpk = Annotated[int, mapped_column(primary_key = True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]


#Объявление таблицы Pictures and Descriptios и столбцов с ограничениями 
class PnDsOrm(Base):
    __tablename__ = "pnds"

    stage_name: Mapped[str] = mapped_column(String(64),primary_key=True)
    desc_content: Mapped[str | None] = mapped_column(Text())
    pic_content: Mapped[str | None] = mapped_column(String(128))
    visits: Mapped[int] = mapped_column(Integer(), default=0)

#Объявление таблицы users и столбцов с ограничениями 
class UserOrm(Base):
    __tablename__ = "users"

    user_id: Mapped[idpk]
    user_name: Mapped[str] = mapped_column(Text())
    created_at: Mapped[created_at]

