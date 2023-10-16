from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
import sqlite3

async def chat_actions(message: types.Message):
    ban_words = ['fuck', 'bitch', 'damn', 'asshole', 'cunt'
                  'dick', 'pussy', 'motherfucker', 'ass', 'bastard', 'dickhead']

    print(message.chat.id)
    if message.chat.id == -1001983654490:
        for word in ban_words:
            if word in message.text.lower().replace(" ", ""):
                user = Database().sql_select_user_query(
                    telegram_id= message.from_user.id
                )
                print(user)
                if user:
                    Database().sql_update_ban_user_query(
                        telegram_id=message.from_user.id
                    )
                else:
                    Database().sql_insert_ban_user_query(
                        telegram_id = message.from_user.id,
                        username=message.from_user.username
                    )

                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Don't use bad words in my group !\n"
                        f'Username: @{message.from_user.username}\n'
                        f'Ты очень подозрительный\nВозможно можешь быть забанен !'


                )
    else:
        await message.reply(
            text='There is no such command\n'
                "Maybe you mispronounced"
        )


def register_chat_actions_handler(dp: Dispatcher):
    dp.register_message_handler(chat_actions)
