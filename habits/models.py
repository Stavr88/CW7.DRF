from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy

from config import settings


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name="Создатель урока",
        null=True,
        blank=True,
        related_name='habits',
    )

    location = models.CharField(
        max_length=200,
        verbose_name="Укажите место привычки",
        null=True,
        blank=True,
    )
    time_habit = models.DateTimeField(
        verbose_name="Укажите дату и время выполнения привычки"
    )
    periodicity = models.PositiveIntegerField(
        verbose_name="Укажите периодичность выполнения привычки",
        validators=(не реже 1 раза в неделю),
    )
    time_execution_habit = models.PositiveIntegerField(
        verbose_name="Укажите время выполнения привычки в секундах",
        validators=(не более 120 сек),
    )
    action = models.TextField(
        verbose_name="Опишите действие, которое представляет собой привычка",
        default=None,
        null=True,
        blank=True,
    )

    def clean(self):
        """
        Функция для проверки периодичности выполнения привычки
        :return:
        """
        interval = [1, 2, 3, 4, 5, 6, 7]
        if self.periodicity not in interval:
            raise ValidationError(
                {"periodicity": gettext_lazy("Значение должно быть в диапазоне от 1 до 7, включительно")}
            )


