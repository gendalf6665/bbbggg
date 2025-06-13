from celery import shared_task
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

@shared_task
def example_task():
    logger.info("Example task executed successfully!")
    return "Example task completed"

@shared_task
def send_command_to_bot(bot_id, command, params=None):
    """
    Отправляет команду внешнему Telegram-боту через его API.
    :param bot_id: ID бота в модели ExternalBot
    :param command: Команда для бота (например, 'check_balance')
    :param params: Дополнительные параметры (например, {'sim_iccid': '89701...'})
    """
    from .models import ExternalBot
    try:
        bot = ExternalBot.objects.get(id=bot_id)
        payload = {
            'command': command,
            'params': params or {},
            'token': bot.api_token
        }
        response = requests.post(bot.api_url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Command '{command}' sent to bot {bot.name} (ID: {bot_id}): {response.json()}")
        return response.json()
    except ExternalBot.DoesNotExist:
        logger.error(f"Bot with ID {bot_id} not found")
        raise
    except requests.RequestException as e:
        logger.error(f"Failed to send command '{command}' to bot ID {bot_id}: {str(e)}")
        raise