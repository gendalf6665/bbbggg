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

9. Локал 
   ```bash
   python manage.py runserver 0.0.0.0:8000
   http://<ваш_IP_адрес>:8000

45. дефолтние данние

   ``bash
   python manage.py shell

   from sim_management.models import MCC, MNCOperator, MOBIL, SimCard

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

