from django.contrib.auth.models import AbstractUser
from django.db import models


class UserData(AbstractUser):
    fio = models.CharField(max_length=255, unique=True)
    group_name = models.CharField(max_length=255, null=True)
    personal_number = models.CharField(max_length=255, unique=True)


class Subjects(models.Model):
    subject_name = models.CharField(max_length=255)


class Lessons(models.Model):
    lesson_number = models.IntegerField(null=True)


class BankTasks(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    account_user = models.ForeignKey('UserData', on_delete=models.PROTECT, null=True)
    subject = models.ForeignKey('Subjects', on_delete=models.PROTECT, null=True)
    lesson = models.ForeignKey('Lessons', on_delete=models.PROTECT, null=True)
