from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Подключаем переменные окружения
# Устанавливаем значения по умолчанию
env = environ.Env(
    DEBUG=(bool, False)
)

# Читает файл .env
environ.Env.read_env(BASE_DIR / ".env")

# Производственные настройки
SECRET_KEY = env("SECRET_KEY") # Секретный ключ для шифровки трафика
DEBUG = env("DEBUG") # Влкючение дебаг режима. По умолчанию выключен
ALLOWED_HOSTS = [] # Хосты сайта. Здесь надо указать домен сайта, чтобы django мог работать с запросами на этот домен


# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'main',
    'user',
    'lessons',
    'testing'
]

# Промежуточные слои
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневой файл маршрутов
ROOT_URLCONF = 'learnRussia.urls'

# Настройка шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # Указываем папку, где надо искать шаблоны
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learnRussia.wsgi.application'


# Базы данных
DATABASES = {
    'default': env.db(default="sqlite:/db.sqlite3")
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Интернализация административной панели
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статика и медиа-файлы
STATIC_URL = 'static/' # URL для получения статических файлов
STATICFILES_DIRS = [BASE_DIR / "static",] # Дополнительные папки для поиска статических файлов
STATIC_ROOT = "staticfiles" # Итоговая папка, куда будут собираться все статические файлы после команды collectstatic

MEDIA_URL = 'media/' # URL для получения медиа файлов
MEDIA_ROOT = BASE_DIR / 'media' # Папка, где будут хранится файлы медиа


# Аутентификация
LOGIN_REDIRECT_URL = "/user/account/" # Адрес перенаправления после успешного входа
LOGIN_URL = "/user/login/" # Адрес перенаправления при попытке зайти на страницы с ограниченным доступом
LOGOUT_REDIRECT_URL = "/" # Адрес перенаправления после выхода из профиля

# Электронная почта
EMAIL_HOST = 'smtp.gmail.com' # Домен почты
EMAIL_PORT = 587 # Порт. Зависит от почтовой службы
EMAIL_HOST_USER = env("EMAIL_USER") # Имя почтового ящика
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD") # Пароль к ящику. Gmail генерирует отдельный пароль на странице
EMAIL_USE_TLS = True # Разрешение протокола TLS. Необходимо почтовой службе Gmail

# ckeditor
# Цветовая палитра для редактора
customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]

# Настройки инструментов редактора
CKEDITOR_5_CONFIGS = {
    'default': {
        # Инструменты редактора
        'toolbar': [
                    'undo', 'redo', '|', 'heading', '|',
                    'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough', 'highlight', '|',
                    'insertImage', 'bulletedList', 'numberedList',  'blockQuote', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'insertTable',],
        # Настройка возможностей вставки изображений
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        # Настройка возможностей вставки таблицы
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        # Настройка списка заголовков и шрифтов
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Текст', 'class': 'text' },
                { 'model': 'heading1', 'view': 'h2', 'title': 'Заголовок', 'class': 'title' },
                { 'model': 'heading2', 'view': 'h3', 'title': 'Подзаголовок', 'class': 'sub-title' }
            ]
        }
    }
}

# Права загрузки изображений. Только для персонала
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
