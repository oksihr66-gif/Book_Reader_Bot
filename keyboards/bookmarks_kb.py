from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, LEXICON_START


def create_language_keyboard():
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в клавиатуру в конце
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON_START["language_ru"], callback_data="ru"
        ),
        InlineKeyboardButton(text=LEXICON_START["language_ro"], callback_data="ro"),
        InlineKeyboardButton(text=LEXICON_START["language_ua"], callback_data="ua"),
        InlineKeyboardButton(text=LEXICON_START["language_en"], callback_data="en"),
        width=2,
    )
    return kb_builder.as_markup()

def create_start_read_book_keyboard():
    # Создаем объект клавиатуры
    button = InlineKeyboardButton(text=LEXICON['start_read_button'], callback_data='start_read_button')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard


def create_bookmarks_keyboard(*args: int, book: dict) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f"{button} - {book[button][:100]}", callback_data=str(button)
            )
        )
    # Добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON["edit_bookmarks_button"], callback_data="edit_bookmarks"
        ),
        InlineKeyboardButton(text=LEXICON["cancel"], callback_data="cancel"),
        width=2,
    )
    return kb_builder.as_markup()


def create_edit_keyboard(*args: int, book: dict) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f"{LEXICON['del']} {button} - {book[button][:100]}",
                callback_data=f"{button}del",
            )
        )
    # Добавляем в конец клавиатуры кнопку "Отменить"
    kb_builder.row(InlineKeyboardButton(text=LEXICON["cancel"], callback_data="cancel"))
    return kb_builder.as_markup()