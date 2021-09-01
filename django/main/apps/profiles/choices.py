from django.db import models


class Role(models.IntegerChoices):
    ADMIN = 0, 'Admin'
    GENERAL = 1, 'General'
    GUEST = 2, 'Guest'
    ACCOUNTING = 3, 'Accounting'
    IT = 4, 'IT'
