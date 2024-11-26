from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit, Habit_pleasant
from habits.paginations import HabitPaginator
from habits.serializers import HabitSerializer, Habit_pleasantSerializer
from habits.services import send_information_about_new_habit_tg
from users.permission import IsOwner


class Habit_pleasantViewSet(ModelViewSet):
    queryset = Habit_pleasant.objects.all()
    serializer_class = Habit_pleasantSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitCreateApiView(CreateAPIView):
    """
    Конкретное представление для создания экземпляра модели.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()
        if habit.user.tg_chat_id:
            send_information_about_new_habit_tg(habit.user.tg_chat_id, "Создана новая привычка!")


class HabitListApiView(ListAPIView):
    """
    Конкретное представление для отображения набора запросов.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsOwner]
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListApiView(ListAPIView):
    """
    Конкретное представление для отображения публичных привычек.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = HabitPaginator


class HabitRetrieveApiView(RetrieveAPIView):
    """
    Конкретное представление для извлечения экземпляра модели.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated,  IsOwner]
    pagination_class = HabitPaginator


class HabitUpdateApiView(UpdateAPIView):
    """
    Конкретное представление для обновления экземпляра модели.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated,  IsOwner]


class HabitDestroyApiView(DestroyAPIView):
    """
    Конкретное представление для удаления экземпляра модели.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
