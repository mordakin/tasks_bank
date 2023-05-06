from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Имя аккаунта',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    personal_number = forms.IntegerField(
        label='Номер студенческого', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fio = forms.CharField(label='ФИО', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', max_length=255,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторение пароля', max_length=255,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserData
        fields = ['username', 'personal_number',
                  'fio', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class FileForm(forms.ModelForm):
    file = forms.FileField(
        label='Прикрепите файл', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BankTasks
        fields = ['file']


class SearchForm(forms.Form):
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES,
                                label='Предмет', widget=forms.Select(attrs={'class': 'form-select'}))
    lesson = forms.IntegerField(label='Урок', widget=forms.NumberInput(attrs={'class': 'form-control'}))

