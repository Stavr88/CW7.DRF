from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование полезных привычек."""

    def setUp(self):
        self.user = User.objects.create(email="test1@mail.ru")
        self.habit = Habit.objects.create(
            user=self.user,
            location="москва",
            time_habit="2024-11-05T14:31:00+03:00",
            periodicity=7,
            time_execution_habit=120,
            action="встать в 7 утра",
            is_public="True",
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        url = reverse("habits:habits")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        url = reverse("habits:create")
        data = {
            "user": self.user.pk,
            "location": "москва",
            "time_habit": "2024-11-05T14:31:00+03:00",
            "periodicity": 7,
            "time_execution_habit": 120,
            "action": "встать в 7 утра",
            "is_public": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_retrieve(self):
        url = reverse("habits:retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("periodicity"), self.habit.periodicity)

    def test_habit_update(self):
        url = reverse("habits:update", args=(self.habit.pk,))
        data = {
            "location": "СПб",
            "time_habit": "2024-11-25T17:08:38Z",
            "periodicity": 7,
            "time_execution_habit": 120,
            "action": "встать в 7 утра",
            "is_public": True,
            "associated_habit": 2,
        }
        # response = self.client.get(url, format='json')
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("location"), "СПб")

    def test_habit_delete(self):
        url = reverse("habits:delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_public_list(self):
        url = reverse("habits:public")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
