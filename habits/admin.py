from django.contrib import admin

from habits.models import Habit, Habit_pleasant


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(Habit_pleasant)
class Habit_pleasantAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

