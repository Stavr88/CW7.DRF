from rest_framework.serializers import ModelSerializer

from habits.models import Habit


class HabitSerializer(ModelSerializer):
    """
    Сериализатор для модели Habit.
    """
    class Meta:
        model = Habit
        fields = "__all__"

