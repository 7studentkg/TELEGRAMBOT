from aiogram import executor
from config import dp
from handlers import start
from database.sql_commands import Databass



async def onstart_up(_):
    db=Databass()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)



if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=onstart_up
    )
