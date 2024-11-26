from rest_framework.serializers import ModelSerializer

from habits.models import Habit, Habit_pleasant


class HabitSerializer(ModelSerializer):
    """
    Сериализатор для модели Habit.
    """
    class Meta:
        model = Habit
        fields = "__all__"


class Habit_pleasantSerializer(ModelSerializer):
    """
    Сериализатор для модели Habit_pleasant.
    """
    class Meta:
        model = Habit_pleasant
        fields = "__all__"

