from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):

    # Команды для русскоязычных пользователей
    ru_commands = [
        BotCommand(command="/beginning", description="В начало книги"),
        BotCommand(command="/continue", description="Продолжить чтение"),
        BotCommand(command="/bookmarks", description="Мои закладки"),
        BotCommand(command="/help", description="Справка по работе бота"),
    ]
    # Команды для англоязычных пользователей
    en_commands = [
        BotCommand(command="/beginning", description="go to the beginning of the book"),
        BotCommand(command="/continue", description="continue reading"),
        BotCommand(command="/bookmarks", description="view the list of bookmarks"),
        BotCommand(command="/help", description="bot usage help"),
    ]
    ro_commands = [
        BotCommand(command="/beginning", description="mergi la începutul cărții"),
        BotCommand(command="/continue", description="continuă citirea"),
        BotCommand(command="/bookmarks", description="vezi lista semnelor de carte"),
        BotCommand(command="/help", description="ajutor pentru utilizarea botului"),
    ]
    uk_commands = [
        BotCommand(command="/beginning", description="перейти на початок книги"),
        BotCommand(command="/continue", description="продовжити читання"),
        BotCommand(command="/bookmarks", description="переглянути список закладок"),
        BotCommand(command="/help", description="довідка по роботі бота"),
    ]


    scope = BotCommandScopeAllPrivateChats()

    await bot.set_my_commands(
        commands=ru_commands,
        scope=scope,
        language_code="ru"
    )
    await bot.set_my_commands(
        commands=en_commands,
        scope=scope,
        language_code="en"
    )
    await bot.set_my_commands(
        commands=ro_commands,
        scope=scope,
        language_code="ro"
    )

    await bot.set_my_commands(
        commands=uk_commands,
        scope=scope,
        language_code="uk"
    )