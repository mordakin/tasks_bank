from django.contrib.auth.models import AbstractUser
from django.db import models


class UserData(AbstractUser):
    fio = models.CharField(max_length=255, unique=True)
    personal_number = models.CharField(max_length=255, unique=True)

