import requests

from config import settings


def send_information_about_new_habit_tg(chat_id, message):
    """Функция для отправки сообщений в Телеграм."""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        params=params,
    )
