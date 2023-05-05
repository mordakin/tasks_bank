from django.contrib.auth.models import AbstractUser
from django.db import models


class UserData(AbstractUser):
    fio = models.CharField(max_length=255, unique=True)
    personal_number = models.CharField(max_length=255, unique=True)


SUBJECT_CHOICES = [
    ('math', 'Математика'),
    ('rus', 'Русский язык'),
    ('inform', 'Информатика'),
]


class BankTasks(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255, choices=SUBJECT_CHOICES)
    lesson = models.IntegerField(null=True)
    account_user = models.ForeignKey('UserData', on_delete=models.PROTECT, null=True)
