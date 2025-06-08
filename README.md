# SIM CRM

CRM-система для управления SIM-картами, разработанная на Django.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/sim-crm.git
   cd sim-crm


2. Создайте виртуальное окружение:
   ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Для Windows

3. Установите зависимости:
   ```bash
    pip install -r requirements.txt

4. Примените миграции:
   ```bash
    python manage.py makemigrations
    python manage.py migrate

5. Соберите статические файлы:
   ```bash
    python manage.py collectstatic

6. Создайте суперпользователя:
   ```bash
    python manage.py createsuperuser

7. Запустите сервер:
   ```bash
   python manage.py runserver

8. Откройте в браузере:
    Главная страница: http://127.0.0.1:8000/
    Админ-панель: http://127.0.0.1:8000/admin/

