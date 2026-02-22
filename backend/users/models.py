from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)

    is_student = models.BooleanField(default=True)
    is_instructor = models.BooleanField(default=False)

    profile_image = models.ImageField(
        upload_to='profile_images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username