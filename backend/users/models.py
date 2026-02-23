from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",
        blank=True,
    )

    def __str__(self):
        return self.username
    
    