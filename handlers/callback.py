from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_one_keyboard



async def start_questionnaire(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = f"Are you gay?",
        reply_markup=await questionnaire_one_keyboard()
    )

async def yes_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = "I knew, haha",

    )

async def of_course_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = "Hahaha",

    )

async def say_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = "GAY",

    )

async def coffe_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = "Ok ☕",

    )

async def f_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = "Fuck you to, GAY",

    )

def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(yes_answer,
                                       lambda call: call.data == "yes_questionnaire")
    dp.register_callback_query_handler(of_course_answer,
                                       lambda call: call.data == "of_course_questionnaire")
    dp.register_callback_query_handler(say_answer,
                                       lambda call: call.data == "can't_say_questionnaire")
    dp.register_callback_query_handler(coffe_answer,
                                       lambda call: call.data == "woman_questionnaire")
    dp.register_callback_query_handler(f_answer,
                                       lambda call: call.data == "f_questionnaire")
