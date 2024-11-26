from django.contrib import admin

from habits.models import Habit, Habit_pleasant


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    list_filter = ('is_public',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Habit_pleasant)
class Habit_pleasantAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

