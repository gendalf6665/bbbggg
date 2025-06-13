import os
import sys
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import django
import requests

# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Инициализация Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sim_crm.settings')
django.setup()

from django.conf import settings

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start."""
    await update.message.reply_text('Привет! Я бот для управления SIM-картами. Используй /check_sim <ICCID> для проверки.')

async def check_sim(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /check_sim."""
    if not context.args:
        await update.message.reply_text('Пожалуйста, укажи ICCID. Пример: /check_sim 8970101015600170724')
        return

    iccid = context.args[0]
    api_token = os.getenv('API_TOKEN')
    if not api_token:
        logging.error("API_TOKEN is not set in environment variables")
        await update.message.reply_text('Ошибка: API-токен не настроен.')
        return

    headers = {'Authorization': f'Token {api_token}'}
    logging.info(f"Sending request with headers: {headers}")
    try:
        response = requests.get(f'{settings.DJANGO_API_URL}/api/simcards/?iccid={iccid}', headers=headers)
        response.raise_for_status()
        data = response.json()
        logging.info(f"API response: {data}")
        if data:
            sim = data[0]
            await update.message.reply_text(
                f'SIM-карта:\n'
                f'ICCID: {sim["iccid"]}\n'
                f'Номер: {sim["phone_number"]}\n'
                f'Статус: {sim["status"]}\n'
                f'Баланс: {sim["balance"]}'
            )
        else:
            await update.message.reply_text('SIM-карта не найдена.')
    except requests.RequestException as e:
        error_message = f'Error fetching SIM card: {str(e)}'
        if hasattr(e.response, 'text'):
            error_message += f'\nResponse: {e.response.text}'
        logging.error(error_message)
        await update.message.reply_text(f'Ошибка при запросе: {str(e)}')

def main() -> None:
    """Запуск бота."""
    logging.info("Starting Telegram bot...")
    application = Application.builder().token(os.getenv('TELEGRAM_CONTROL_BOT_TOKEN')).build()

    # Регистрация обработчиков
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('check_sim', check_sim))

    # Запуск polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()