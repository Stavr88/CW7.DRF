from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy

from config import settings


class Habit(models.Model):
    """
    Модель для создания полезной привычки
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
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
        default=1,
        null=True,
        blank=True,
    )
    time_execution_habit = models.PositiveIntegerField(
        verbose_name="Укажите время выполнения привычки в секундах",
        default=120,
        null=True,
        blank=True,
    )
    action = models.TextField(
        verbose_name="Опишите действие, которое представляет собой привычка",
        default=None,
        null=True,
        blank=True,
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name="Публичность привычки"
    )
    award = models.CharField(
        max_length=255,
        verbose_name="Вознаграждение",
        null=True,
        blank=True,
    )
    associated_habit = models.ForeignKey(
        "Habit_pleasant",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # def clean(self):
    def validate_unique(self, exclude=None):
        """
        Функция для:
         1. Проверки периодичности выполнения привычки, поле "periodicity";
         2. Проверки длительности выполнения привычки, поле "time_execution_habit";
        :return:
        """
        interval = [1, 2, 3, 4, 5, 6, 7]

        if self.periodicity not in interval:
            raise ValidationError(
                {"periodicity": gettext_lazy("Значение должно быть в диапазоне от 1 до 7, включительно")}
            )
        elif self.time_execution_habit > 120 or self.time_execution_habit == 0:
            raise ValidationError(
                {"periodicity": gettext_lazy("Время выполнения привычки не должно равняться 0 и превышать 120 сек.")}
            )

    def clean_fields(self, exclude=None):
        if self.award and self.associated_habit:
            raise ValidationError(
                {"periodicity": gettext_lazy("Нельзя выбирать одновременно и вознаграждение и приятную привычку")}
            )

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def get_absolute_url(self):
        """
        Функция для отображения ссылки на страницу сайта с админпанели
        :return:
        """
        return reverse('post', kwargs={'post_slug': self.slug})

class Habit_pleasant(models.Model):
    """
    Класс описывающий приятную привычку, в качестве вознаграждения за выполнение полезной привычки
    """
    name = models.CharField(
        max_length=150,
        verbose_name="Название привычки",
        null=True,
        blank=True,
    )
    action = models.TextField(
        verbose_name="Опишите, что представляет собой привычка",
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятные привычки"
