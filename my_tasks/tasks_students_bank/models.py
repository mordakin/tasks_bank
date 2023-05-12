from django.contrib.auth.models import AbstractUser
from django.db import models


class UserData(AbstractUser):
    fio = models.CharField(max_length=255, unique=True)
    personal_number = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey('Groups', on_delete=models.PROTECT, null=True)


class Groups(models.Model):
    group_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.group_name


class Subjects(models.Model):
    subject_name = models.CharField(max_length=255)

    def __str__(self):
        return self.subject_name


class Lessons(models.Model):
    lesson_number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.lesson_number)


class BankTasks(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    account_user = models.ForeignKey('UserData', on_delete=models.PROTECT, null=True)
    subject = models.ForeignKey('Subjects', on_delete=models.PROTECT, null=True)
    lesson = models.ForeignKey('Lessons', on_delete=models.PROTECT, null=True)
