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
    group_name = forms.ModelChoiceField(label='Номер группы', widget=forms.Select(
        attrs={'class': 'form-control'}), queryset=Groups.objects.all())
    password1 = forms.CharField(label='Пароль', max_length=255,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторение пароля', max_length=255,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserData
        fields = ['username', 'personal_number',
                  'fio', 'group_name', 'password1', 'password2']

    def clean_fio(self):
        """Валидатор ФИО"""
        fio = self.cleaned_data['fio']
        count_space = fio.count(' ')
        if (any(x.isalpha() for x in fio)
                and any(x.isspace() for x in fio)
                and all(x.isalpha() or x.isspace() for x in fio)
                and count_space == 2):
            return fio
        else:
            raise ValidationError(
                'В ФИО могут быть только буквы и фио состоит из трёх слов разделённых пробелом')

    def clean_personal_number(self):
        personal_number = self.cleaned_data['personal_number']
        check_personal_number = UserData.objects.filter(personal_number=personal_number)
        test_length = str(personal_number)
        if len(test_length) != 7:
            raise ValidationError(
                'Номер студенческого должен состоять из 7 цифр')
        if check_personal_number:
            raise ValidationError('Такой номер студенческого уже зарегистрирован')
        else:
            return personal_number


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
    subject = forms.ModelChoiceField(queryset=Subjects.objects.all(),
                                     label='Предмет', widget=forms.Select(attrs={'class': 'form-select'}))
    lesson = forms.ModelChoiceField(label='Урок', widget=forms.Select(attrs={'class': 'form-control'}),
                                    queryset=Lessons.objects.all())
    group = forms.ModelChoiceField(label='Группа', widget=forms.Select(attrs={'class': 'form-control'}),
                                   queryset=Groups.objects.all())


class AddSubjectForm(forms.ModelForm):
    subject_name = forms.CharField(
        label='Название предмета', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Subjects
        fields = ['subject_name']
