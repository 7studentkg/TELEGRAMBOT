from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Click here",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration",
        callback_data="fsm_start"
    )
    my_profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )
    random_profile_button = InlineKeyboardButton(
        "View Profile",
        callback_data="random_profiles"
    )
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profile_button)
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


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    user_form_like_button = InlineKeyboardButton(
        "Like 👍",
        callback_data=f"user_form_like_{owner_tg_id}"
    )
    user_form_dislike_button = InlineKeyboardButton(
        "Dislike 👎",
        callback_data="random_profiles"
    )

    markup.add(user_form_like_button)
    markup.add(user_form_dislike_button)
    return markup

async def edit_delete_form_keyboard():
    markup = InlineKeyboardMarkup()
    edit_form_button = InlineKeyboardButton(
        "Edit",
        callback_data="fsm_start"
    )
    delete_form_button = InlineKeyboardButton(
        "Delete",
        callback_data="delete_profile"
    )

    markup.add(edit_form_button)
    markup.add(delete_form_button)
    return markup


async def my_profile_regiter():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        "Registration",
        callback_data="fsm_start"
    )


    markup.add(registration_button)
    return markup
