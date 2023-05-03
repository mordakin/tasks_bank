from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tasks_students_bank.forms import RegisterUserForm, LoginUserForm


def page_not_found(request, exception):
    """Страница не найдена"""
    return HttpResponseNotFound('Такой страницы нет((')


def index(request):
    return HttpResponse('Hello')


def user_page(request):
    return HttpResponse('user_page')


class SingInPage(CreateView):
    """Страница регистрации"""
    form_class = RegisterUserForm
    template_name = 'tasks_students_bank/sing_in.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('user_page')

    def form_valid(self, form):
        """Внос данных в бд"""
        user = form.save()
        login(self.request, user)
        return redirect('user_page')


class LoginPage(LoginView):
    """Страница авторизации"""
    form_class = LoginUserForm
    template_name = 'tasks_students_bank/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        """Ссылка перехода"""
        return reverse_lazy('user_page')

    def form_invalid(self, form):
        """Вывод при неверном пароле"""
        form.add_error(None, "Неверный логин или пароль")
        return super().form_invalid(form)


def logout_user(request):
    """Выход из аккаунта"""
    logout(request)
    return redirect('login')
