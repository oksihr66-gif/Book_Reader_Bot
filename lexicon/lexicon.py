LEXICON_START = {"/start": "Choose language",
                "language_ru": "Русский",
                "language_en": "English",
                "language_ro": "Română",
                "language_ua": "Українська"
                }
LEXICON = {}
LANGUAGES = { 'ru':{
    "forward": ">>",
    "backward": "<<",
    "greetings": "<b>📚 Добро пожаловать в Book Reader Bot!</b>\n\n"
                        "✨ Здесь вы можете:\n\n"
                        "📖 Читать книги\n\n"
                        "🌍 Переводить слова(эта функция еще в разработке)\n\n"
                        "🔖 Сохранять закладки\n\n"
                        "📑 Загружать свои TXT книги\n\n"
                 "Тебе всего лишь нужно загрузить документ в формате ТХТ,\n"
               'который ты можешь скачать в интернете\n\n'
              'Чтобы посмотреть список доступных '
              "команд - набери /help",
    "/help": "<b>Доступные команды:</b>\n\n/beginning - "
             "перейти в начало книги\n/continue - продолжить "
             "чтение\n/bookmarks - посмотреть список закладок\n/help - "
             "справка по работе бота\n\nЧтобы сохранить закладку - "
             "нажмите на кнопку с номером страницы\n\n<b>Приятного чтения!</b>",
    "/bookmarks": "<b>Это список ваших закладок:</b>",
    "edit_bookmarks": "<b>Редактировать закладки</b>",
    "edit_bookmarks_button": "❌ РЕДАКТИРОВАТЬ",
    "del": "❌",
    "cancel": "ОТМЕНИТЬ",
    "no_bookmarks": "У вас пока нет ни одной закладки.\n\nЧтобы "
                    "добавить страницу в закладки - во время чтения "
                    "книги нажмите на кнопку с номером этой "
                    "страницы\n\n/continue - продолжить чтение",
    "cancel_text": "/continue - продолжить чтение",
    "start_read_button": "Начать читать книгу",
    "start_read": "Чтобы начать читать новую книгу нажмите на кнопку",
    "add_bookmark": "Страница добавлена в закладки!",
    "no_book": "Вы еще не загрузили книгу",
    'error': 'Я не могу открыть этот документ, попробуйте загрузить другой.',
    "wrong_format": "Не верный формат документа, загрузите файл в формате TXT"
    },

'ua': {
    "forward": ">>",
    "backward": "<<",
    "greetings": "<b>📚 Ласкаво просимо до Book Reader Bot!</b>\n\n"
                 "✨ Тут ви можете:\n\n"
                 "📖 Читати книги\n\n"
                 "🌍 Перекладати слова (ця функція ще в розробці)\n\n"
                 "🔖 Зберігати закладки\n\n"
                 "📑 Завантажувати свої TXT книги\n\n"
                 "Вам лише потрібно завантажити документ у форматі TXT,\n"
                 "який ви можете скачати в інтернеті\n\n"
                 "Щоб переглянути список доступних "
                 "команд — введіть /help",
    "/help": "<b>Доступні команди:</b>\n\n/beginning - "
             "перейти на початок книги\n/continue - продовжити "
             "читання\n/bookmarks - переглянути список закладок\n/help - "
             "довідка по роботі бота\n\nЩоб додати книгу, потрібно скачати її з інтернету у форматі TXT "
             "та завантажити в Telegram-бот.\n\nЩоб змінити мову, натисніть /start \n\n"
             "Щоб зберегти закладку — натисніть на кнопку з номером сторінки\n\n"
             "<b>Приємного читання!</b>",
    "/bookmarks": "<b>Це список ваших закладок:</b>",
    "edit_bookmarks": "<b>Редагувати закладки</b>",
    "edit_bookmarks_button": "❌ РЕДАГУВАТИ",
    "del": "❌",
    "cancel": "СКАСУВАТИ",
    "no_bookmarks": "У вас поки немає жодної закладки.\n\nЩоб "
                    "додати сторінку в закладки — під час читання "
                    "книги натисніть на кнопку з номером цієї "
                    "сторінки\n\n/continue - продовжити читання",
    "cancel_text": "/continue - продовжити читання",
    "start_read_button": "Почати читати книгу",
    "start_read": "Щоб почати читати нову книгу, натисніть на кнопку",
    "add_bookmark": "Сторінку додано до закладок!",
    "no_book": "Ви ще не завантажили книгу",
    "error": "Я не можу відкрити цей документ, спробуйте завантажити інший.",
    "wrong_format": "Невірний формат документа, завантажте файл у форматі TXT."
},

'ro': {
    "forward": ">>",
    "backward": "<<",
    "greetings": "<b>📚 Bine ai venit la Book Reader Bot!</b>\n\n"
                 "✨ Aici poți:\n\n"
                 "📖 Citi cărți\n\n"
                 "🌍 Traduce cuvinte (această funcție este încă în dezvoltare)\n\n"
                 "🔖 Salva semne de carte\n\n"
                 "📑 Încărca propriile cărți TXT\n\n"
                 "Tot ce trebuie să faci este să încarci un document în format TXT,\n"
                 "pe care îl poți descărca de pe internet\n\n"
                 "Pentru a vedea lista comenzilor disponibile "
                 "tastează /help",
    "/help": "<b>Comenzi disponibile:</b>\n\n/beginning - "
             "mergi la începutul cărții\n/continue - continuă "
             "citirea\n/bookmarks - vezi lista semnelor de carte\n/help - "
             "ajutor pentru utilizarea botului\n\nPentru a salva un semn de carte — "
             "apasă butonul cu numărul paginii\n\n<b>Lectură plăcută!</b>",
    "/bookmarks": "<b>Aceasta este lista semnelor tale de carte:</b>",
    "edit_bookmarks": "<b>Editează semnele de carte</b>",
    "edit_bookmarks_button": "❌ EDITEAZĂ",
    "del": "❌",
    "cancel": "ANULEAZĂ",
    "no_bookmarks": "Încă nu ai niciun semn de carte.\n\nPentru "
                    "a adăuga o pagină la semne de carte — în timpul citirii "
                    "apasă butonul cu numărul acestei "
                    "pagini\n\n/continue - continuă citirea",
    "cancel_text": "/continue - continuă citirea",
    "start_read_button": "Începe să citești cartea",
    "start_read": "Pentru a începe să citești o carte nouă, apasă pe buton",
    "add_bookmark": "Pagina a fost adăugată la semnele de carte!",
    "no_book": "Încă nu ați încărcat o carte",
    "error": "Nu pot deschide acest document, încercați să încărcați altul.",
    "wrong_format": "Format de document invalid, încărcați un fișier în format TXT."
},

'en': {
    "forward": ">>",
    "backward": "<<",
    "greetings": "<b>📚 Welcome to Book Reader Bot!</b>\n\n"
                 "✨ Here you can:\n\n"
                 "📖 Read books\n\n"
                 "🌍 Translate words (this feature is still in development)\n\n"
                 "🔖 Save bookmarks\n\n"
                 "📑 Upload your own TXT books\n\n"
                 "You only need to upload a TXT document,\n"
                 "which you can download from the internet\n\n"
                 "To see the list of available "
                 "commands — type /help",
    "/help": "<b>Available commands:</b>\n\n/beginning - "
             "go to the beginning of the book\n/continue - continue "
             "reading\n/bookmarks - view the list of bookmarks\n/help - "
             "bot usage help\n\nTo save a bookmark — "
             "press the button with the page number\n\n<b>Enjoy reading!</b>",
    "/bookmarks": "<b>This is the list of your bookmarks:</b>",
    "edit_bookmarks": "<b>Edit bookmarks</b>",
    "edit_bookmarks_button": "❌ EDIT",
    "del": "❌",
    "cancel": "CANCEL",
    "no_bookmarks": "You don't have any bookmarks yet.\n\nTo "
                    "add a page to bookmarks — while reading "
                    "the book, press the button with the number of that "
                    "page\n\n/continue - continue reading",
    "cancel_text": "/continue - continue reading",
    "start_read_button": "Start reading the book",
    "start_read": "To start reading a new book, press the button",
    "add_bookmark": "The page has been added to bookmarks!",
    "no_book": "You haven't uploaded a book yet",
    "error": "I can't open this document, please try uploading another one.",
    "wrong_format": "Invalid document format, upload a file in TXT format"
}

}

