from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Click here",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_questionnaire"
    )
    of_course_button = InlineKeyboardButton(
        "Of course",
        callback_data="of_course_questionnaire"
    )
    say_button = InlineKeyboardButton(
        "I can't say",
        callback_data="can't_say_questionnaire"
    )
    woman_button = InlineKeyboardButton(
        "I am woman",
        callback_data="woman_questionnaire"
    )
    f_button = InlineKeyboardButton(
        "Fuck you",
        callback_data="f_questionnaire"
    )
    q_button = InlineKeyboardButton(
        "Are you an idiot?",
        callback_data="q_questionnaire"
    )
    markup.add(yes_button)
    markup.add(of_course_button)
    markup.add(say_button)
    markup.add(q_button)
    markup.add(f_button)
    markup.add(woman_button)
    return markup

async def admin_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list_button = InlineKeyboardButton(
        "User list",
        callback_data="admin_user_list"
    )

    markup.add(admin_user_list_button)
    return markup
