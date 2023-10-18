from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3



class FormStates(StatesGroup):
    nickname = State()
    hobby = State()
    age = State()
    occupation = State()
    photo = State()





async def fsm_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id = call.from_user.id,
        text = 'Send me your Nickname, please.'
    )
    await FormStates.nickname.set()

async def load_nickname(message: types.Message,
                        state: FSMContext):

    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id = message.from_user.id,
        text = 'Ok, Your hobby:'
    )

    await FormStates.next()

async def load_hobby(message: types.Message,
                        state: FSMContext):

    async with state.proxy() as data:
        data['hobby'] = message.text
        print(data)

    await bot.send_message(
        chat_id = message.from_user.id,
        text = f'How old are you ?\n(Use only number)\n'
            f'Example: 25 '
    )
    await FormStates.next()


async def load_age(message: types.Message,
                        state: FSMContext):
    try:

        if type(int(message.text)) != int:
            await message.reply(
                text='Error, Please use only number !'
            )
            await state.finish()
            return

        async with state.proxy() as data:
            data['age'] = message.text
            print(data)

        await bot.send_message(
            chat_id = message.from_user.id,
            text = 'What your occupation?'
        )
        await FormStates.next()

    except ValueError as e:
        await message.reply(
            text = 'Error Please use only number !'
        )
        await state.finish()
        return

async def load_occupation(message: types.Message,
                        state: FSMContext):

    async with state.proxy() as data:
        data['occupation'] = message.text
        print(data)

    await bot.send_message(
        chat_id = message.from_user.id,
        text = 'Send me your photo, not file'
    )
    await FormStates.next()

async def load_photo(message: types.Message,
                        state: FSMContext):
    print(message.photo, message.text)
    path = await message.photo[-1].download(
        destination_dir='F:\VsCode\TelegramBot\my_first_bot\media\Registration_photo'
    )
    async with state.proxy() as data:
        Database().sql_insert_user_form_query(
            telegram_id=message.from_user.id,
            nickname=data['nickname'],
            hobby=data['hobby'],
            age=data['age'],
            occupation=data['occupation'],
            photo = path.name,


        )
        with open (path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id = message.chat.id,
                photo = photo,
                caption=f"Nickname: {data['nickname']}\n"
                        f"Hobby: {data['hobby']}\n"
                        f"Age: {data['age']}\n"
                        f"Occupation: {data['occupation']}\n"

            )

        await bot.send_message(
            chat_id = message.from_user.id,
            text = 'Registration successfully '
        )
        await state.finish()



async def my_profile_call(call: types.CallbackQuery):
    user_form = Database().sql_select_user_form_query(
        telegram_id=call.from_user.id,
    )
    with open (user_form[0]["photo"], 'rb') as photo:
            await bot.send_photo(
                chat_id = call.from_user.id,
                photo = photo,
                caption=f"Nickname: {user_form[0]['nickname']}\n"
                        f"Hobby: {user_form[0]['hobby']}\n"
                        f"Age: {user_form[0]['age']}\n"
                        f"Occupation: {user_form[0]['occupation']}\n"

            )




def register_fsm_form_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(fsm_start, lambda call: call.data == 'fsm_start')
    dp.register_message_handler(load_nickname,
                                state = FormStates.nickname,
                                content_types = ['text'] )
    dp.register_message_handler(load_hobby,
                                state = FormStates.hobby,
                                content_types = ['text'] )
    dp.register_message_handler(load_age,
                                state = FormStates.age,
                                content_types = ['text'] )
    dp.register_message_handler(load_occupation,
                                state = FormStates.occupation,
                                content_types = ['text'] )
    dp.register_message_handler(load_photo,
                                state = FormStates.photo,
                                content_types =types.ContentTypes.PHOTO )
    dp.register_callback_query_handler(my_profile_call, lambda call: call.data == 'my_profile')
