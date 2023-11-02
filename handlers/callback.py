from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_one_keyboard
from scraping.news_scraper import NewsScraper
from scraping.async_scraper import AsyncNewsScraper


async def start_questionnaire(call: types.CallbackQuery):
    print(call.data)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = f"Are you gay?",
        reply_markup=await questionnaire_one_keyboard()
    )

async def yes_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text = "Are you gay?",

    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = f"Yes",
    )
    # with open("F:\VsCode\TelegramBot\my_first_bot\media\РикардоМилас.gif", "rb") as animation:
    #     await bot.send_animation(
    #         chat_id= call.message.chat.id,
    #         animation=animation,       # закоментировать анимацию!

    #     )


async def of_course_answer(call: types.CallbackQuery):
    print(call.data)
    # await bot.send_message(
    #     chat_id=call.message.chat.id,
    #     text = "Hahaha",

    # )
    with open ("F:\VsCode\TelegramBot\my_first_bot\media\GWantNigger.webp", "rb") as photo:
        await bot.send_photo(
            chat_id= call.message.chat.id,
            photo=photo,
        )
async def say_answer(call: types.CallbackQuery):
    # print(call.data)
    # await bot.send_message(
    #     chat_id=call.message.chat.id,
    #     text = "GAY",

    # )
    with open("F:\VsCode\TelegramBot\my_first_bot\media\GNigger.webp", "rb") as photo:
        await bot.send_photo(
            chat_id = call.message.chat.id,
            photo=photo,
            caption=f"Why sweety?",
        )

async def coffe_answer(call: types.CallbackQuery):
    print(call.data)
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,

    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text = "I'm a Bot ☕",

    )

async def f_answer(call: types.CallbackQuery):
    print(call.data)
    # await bot.send_message(
    #     chat_id=call.message.chat.id,
    #     text = "Fuck off, piece of meat",

    # )
    with open ("F:\VsCode\TelegramBot\my_first_bot\media\Bender.png", "rb") as photo:
        await bot.send_photo(
            chat_id = call.message.chat.id,
            photo =photo,
        )


async def q_answer(call: types.CallbackQuery):
    print(call.data)
    # await bot.send_message(
    #     chat_id=call.message.chat.id,
    #     text = f"All idiots: You, I, Elon Musk.\nThis is my philosophy",
    # )
    with open("F:\VsCode\TelegramBot\my_first_bot\media\All_idiots.gif", "rb") as animation:
        await bot.send_animation(
            chat_id = call.message.chat.id,
            animation=animation,
            caption = f"All idiots: You, I, even Elon Musk.\nThis is my philosophy",

        )

async def anime_films(call: types.CallbackQuery):
    print(call.data)
    scraper = NewsScraper()
    links = scraper.parse_data()

    for link in links:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text = scraper.PLUS_A + link,

        )

async def news_ecology(call: types.CallbackQuery):
    print(call.data)
    scraper = AsyncNewsScraper()
    links = await scraper.parse_pages()
    print(links)


    for link in links:

        await bot.send_message(
            chat_id=call.message.chat.id,
            text = scraper.PLUS_E + link,

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
    dp.register_callback_query_handler(q_answer,
                                       lambda call: call.data == "q_questionnaire")
    dp.register_callback_query_handler(anime_films,
                                       lambda call: call.data == "anime_films")
    dp.register_callback_query_handler(news_ecology,
                                       lambda call: call.data == "new_ecology")
