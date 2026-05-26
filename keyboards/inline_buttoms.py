from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# Создаем объекты инлайн-кнопок
url_button_1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"', url="https://stepik.org/120924"
)
url_button_2 = InlineKeyboardButton(
    text="Продвинутый курс по ботам", url="https://stepik.org/course/153850/"
)
url_button_3 = InlineKeyboardButton(
    text="Документация Telegram Bot API", url="https://core.telegram.org/bots/api"
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1], [url_button_2], [url_button_3]]
)
# Создаем объекты инлайн-кнопок
group_name = "aiogram_stepik_course"
url_button_3 = InlineKeyboardButton(
    text='Группа "Телеграм-боты на AIOgram"', url=f"tg://resolve?domain={group_name}"
)

user_id = 946623219
url_button_4 = InlineKeyboardButton(
    text="Автор курса на Степике по телеграм-ботам", url=f"tg://user?id={user_id}"
)

channel_name = "toBeAnMLspecialist"
url_button_5 = InlineKeyboardButton(
    text='Канал "Стать специалистом по машинному обучению"',
    url=f"https://t.me/{channel_name}",
)

# Создаем объект инлайн-клавиатуры
keyboard_2 = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_3], [url_button_4], [url_button_5]]
)

