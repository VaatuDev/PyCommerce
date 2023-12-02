import os
from django.contrib.auth.models import AbstractUser
from django.db import models


def locate_profile_photo(instance, filename: str):
    return os.path.join(f"profile/{instance.email}", filename)


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=40, unique=False)
    email = models.EmailField(unique=True)
    photo = models.ImageField(
        upload_to=locate_profile_photo, default="profile/default.png", blank=True
    )
    stripe_id = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
