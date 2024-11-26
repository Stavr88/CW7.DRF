from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings
from django.utils import timezone

from habits.models import Habit
from habits.services import send_information_about_new_habit_tg


@shared_task()
def telegram_message():

    timezone.activate(pytz.timezone(settings.CELERY_TIMEZONE))
    zone = pytz.timezone(settings.CELERY_TIMEZONE)
    now_time = datetime.now(zone)
    habits = Habit.objects.all()

    for habit in habits:
        user_tg = habit.user.tg_chat_id
        if (
            user_tg
            and now_time >= habit.time_habit - timedelta(minutes=10)
            and now_time.date() == habit.time_habit.date()
        ):
            message = f"Напоминание: {habit.action} в {habit.time_habit+timedelta(hours=3)} {habit.location}"

            send_information_about_new_habit_tg(user_tg, message)

            if habit.award:
                send_information_about_new_habit_tg(user_tg, f"Поздравляю! Ты получил: {habit.award}")

            habit.time_habit += timedelta(days=habit.period)
            habit.save()
