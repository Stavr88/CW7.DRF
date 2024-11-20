import os

from django.core.management import BaseCommand

from users.models import User

from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email=os.getenv("email_ensure_adminuser"))
        user.set_password(os.getenv("password_ensure_adminuser"))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

