from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateApiView,
    HabitDestroyApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
    PublicHabitListApiView
)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListApiView.as_view(), name="habits"),
    path("public/", PublicHabitListApiView.as_view(), name="public"),
    path("create/", HabitCreateApiView.as_view(), name="create"),
    path("retrieve/<int:pk>/", HabitRetrieveApiView.as_view(), name="retrieve"),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name="update"),
    path("delete/<int:pk>/", HabitDestroyApiView.as_view(), name="delete"),
]
