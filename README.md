SIM CRM
CRM-система для управления SIM-картами, разработанная на Django с интеграцией Telegram-ботов.
Установка
Локальная установка без Docker

Клонируйте репозиторий:
git clone https://github.com/your-username/sim-crm.git
cd sim-crm


Создайте виртуальное окружение:
python -m venv venv
.\venv\Scripts\activate  # Для Windows


Установите зависимости:
pip install -r requirements.txt


Создайте файл .env на основе .env.example:
copy .env.example .env

Обновите DJANGO_SECRET_KEY, TELEGRAM_CONTROL_BOT_TOKEN, API_TOKEN, и DJANGO_API_URL.

Примените миграции:
python manage.py makemigrations sim_management
python manage.py migrate


Соберите статические файлы:
python manage.py collectstatic


Создайте суперпользователя:
python manage.py createsuperuser


Создайте API-токен:
python manage.py drf_create_token <username>


Запустите сервер:
python manage.py runserver


Откройте в браузере:

Главная страница: http://127.0.0.1:8000/
Детальная страница SIM-карты: http://127.0.0.1:8000/simcard//
Админ-панель: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/api/



Установка с Docker

Убедитесь, что Docker и Docker Compose установлены:
docker --version
docker-compose --version


Создайте файл .env на основе .env.example:
copy .env.example .env

Обновите DJANGO_SECRET_KEY, TELEGRAM_CONTROL_BOT_TOKEN, API_TOKEN, и DJANGO_API_URL.

Запустите проект:
docker-compose up -d --build


Примените миграции:
docker-compose exec django python manage.py makemigrations sim_management
docker-compose exec django python manage.py migrate


Соберите статические файлы:
docker-compose exec django python manage.py collectstatic --noinput


Создайте суперпользователя:
docker-compose exec django python manage.py createsuperuser


Создайте API-токен:
docker-compose exec django python manage.py drf_create_token <username>


Откройте в браузере:

Главная страница: http://localhost/
Детальная страница SIM-карты: http://localhost/simcard//
Админ-панель: http://localhost/admin/
API: http://localhost/api/



Добавление тестовых данных

Откройте Django shell:
docker-compose exec django python manage.py shell


Выполните:
from sim_management.models import MCC, MNCOperator, MOBIL, SimCard, ExternalBot

# Add MCC
MCC.objects.create(code="701", country="rus")

# Add MNC
MNCOperator.objects.create(code="018", operator="MTS")
MNCOperator.objects.create(code="02", operator="Megafon")
MNCOperator.objects.create(code="20", operator="Tele2")
MNCOperator.objects.create(code="501", operator="Sber")
MNCOperator.objects.create(code="452", operator="Gaz")

# Add MOBIL
MOBIL.objects.create(code="89", country="rus")

# Add test SIM card
SimCard.objects.create(
    iccid="8970101015600170724",
    phone_number="+79991234567",
    status="active",
    balance=100.00
)

# Add test ExternalBot
ExternalBot.objects.create(
    name="TestBot",
    api_token="test-token",
    api_url="http://example.com/api",
    is_active=True
)



Работа с Telegram-ботом

Найдите бота в Telegram, используя токен из .env (TELEGRAM_CONTROL_BOT_TOKEN).
Отправьте команды:
/start: Приветственное сообщение.
/check_sim <ICCID>: Проверка SIM-карты (например, /check_sim 8970101015600170724).



Работа с API

Используйте API-токен для аутентификации.
Примеры запросов:
Получить SIM-карты: GET /api/simcards/
Отправить команду боту: POST /api/bots/<id>/send_command/{
    "command": "check_balance",
    "params": {"sim_iccid": "8970101015600170724"}
}





Разработка

Celery: Для асинхронных задач, таких как отправка команд Telegram-ботам.
Telegram-боты: Поддержка взаимодействия с готовыми ботами через API и собственного бота для управления CRM.
REST API: Управление SIM-картами и ботами через /api/.
Docker: Контейнеризация Django, Celery, PostgreSQL, Redis и ботов.

Устранение неполадок

Ошибка миграций: Удалите папку migrations и пересоздайте миграции.
Celery не запускается: Проверьте Redis (docker logs sim_crm_redis) и переменные CELERY_BROKER_URL, CELERY_RESULT_BACKEND.
NoReverseMatch: Убедитесь, что app_name указано в sim_management/urls.py.

