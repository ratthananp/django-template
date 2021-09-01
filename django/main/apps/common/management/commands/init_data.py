from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from main.apps.profiles.models import Profile, Role


class Command(BaseCommand):
    """Command to initialize data on first run"""
    help = 'Create initial project data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self._create_initial_user()

    @staticmethod
    def _create_initial_user():
        if not User.objects.exists():
            user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                first_name='admin',
                last_name='admin',
                password='admin'  # NOSONAR
            )

            Profile.objects.create(
                role=Role.ADMIN,
                user=user,
                created_user=user,
                updated_user=user
            )
