from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.inline_buttons import (
    like_dislike_keyboard,
    edit_delete_form_keyboard,
    my_profile_regiter

)
import sqlite3
import sqlite3
import random
import re


class FormStates(StatesGroup):
    nickname = State()
    hobby = State()
    age = State()
    occupation = State()
    photo = State()





async def fsm_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id = call.from_user.id, # call.chat.id / chat_id
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
        user = Database().sql_select_user_form_query(
            telegram_id= message.from_user.id
        )
        if user:
            Database().sql_update_user_form_query(
                nickname = data['nickname'],
                hobby = data['hobby'],
                age = data['age'],
                occupation= data['occupation'],
                photo= path.name,
                telegram_id=message.from_user.id
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
                text = 'Updated successfully '
            )
        else:
            print('No user')

        # try:
        Database().sql_insert_user_form_query(
            telegram_id=message.from_user.id,
            nickname=data['nickname'],
            hobby=data['hobby'],
            age=data['age'],
            occupation=data['occupation'],
            photo = path.name,


        )
        # except sqlite3.IntegrityError:
        #     await bot.send_message(
        #         chat_id= message.from_user.id,
        #         text = "You have registered before, please go to your profile"
        #     )
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
    try:
        with open (user_form[0]["photo"], 'rb') as photo:
                await bot.send_photo(
                    chat_id = call.from_user.id,
                    photo = photo,
                    caption=f"Nickname: {user_form[0]['nickname']}\n"
                            f"Hobby: {user_form[0]['hobby']}\n"
                            f"Age: {user_form[0]['age']}\n"
                            f"Occupation: {user_form[0]['occupation']}\n",
                    reply_markup=await edit_delete_form_keyboard()

                )

    except IndexError:
        await bot.send_message(
            chat_id = call.from_user.id,
            text = "You have no form, please register",
            reply_markup= await my_profile_regiter()
        )


async def random_profiles_call(call: types.CallbackQuery):
    users = Database().sql_select_all_user_form_query()
    try:
        random_form = random.choice(users)
    except IndexError:
        await bot.send_message(
            chat_id= call.from_user.id,
            text = 'Profile list empty\n' # с этим еще надо поработать !
            "Please register",
            reply_markup= await my_profile_regiter()
        )
    with open(random_form['photo'], 'rb') as photo: # -
        await bot.send_photo(
            chat_id = call.from_user.id,
            photo = photo,
            caption=f"Nickname: {random_form['nickname']}\n"
                    f"Hobby: {random_form['hobby']}\n"
                    f"Age: {random_form['age']}\n"
                    f"Occupation: {random_form['occupation']}\n",
            reply_markup= await like_dislike_keyboard(
                owner_tg_id= random_form['telegram_id']
            )

        )


async def like_detect_call(call: types.CallbackQuery):
    owner_tg_id = re.sub("user_form_like_", "", call.data)
    print(owner_tg_id)
    try:
        Database().sql_insert_like_query(
            owner = owner_tg_id,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text = 'You already liked form before'
        )

    finally:
        await random_profiles_call(call=call)

async def delete_form_call(call: types.CallbackQuery):
    Database().sql_delete_form_query(
        owner = call.from_user.id
    )
    await bot.send_message(
        chat_id= call.from_user.id,
        text = 'Your form deleted successfully'
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
    dp.register_callback_query_handler(random_profiles_call,
                                        lambda call: call.data == 'random_profiles')
    dp.register_callback_query_handler(like_detect_call,
                                        lambda call: 'user_form_like_' in call.data)
    dp.register_callback_query_handler(delete_form_call,
                                        lambda call: call.data == 'delete_profile')
