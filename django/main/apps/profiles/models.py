from django.contrib.auth.models import User
from django.db import models
from model_controller.models import AbstractModelController

from main.apps.profiles.choices import Role


class Profile(AbstractModelController):
    role = models.IntegerField(choices=Role.choices, default=Role.GENERAL)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
