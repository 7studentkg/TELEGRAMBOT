from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup
    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_questionnaire"
    )
    of_course_button = InlineKeyboardButton(
        "Of course",
        callback_data="of_course_questionnaire"
    )
    markup.add(yes_button)
    markup.add(of_course_button)
    return markup
