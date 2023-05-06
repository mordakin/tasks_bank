from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from tasks_students_bank.forms import RegisterUserForm, LoginUserForm, FileForm, SearchForm
from tasks_students_bank.models import BankTasks, SUBJECT_CHOICES


def page_not_found(request, exception):
    """Страница не найдена"""
    return HttpResponseNotFound('Такой страницы нет((')


@method_decorator(login_required, name='dispatch')
class PostFile(CreateView):
    form_class = FileForm
    template_name = 'tasks_students_bank/lessons_post.html'
    extra_context = {'title': 'Test'}
    success_url = reverse_lazy('user_page')

    def dispatch(self, request, *args, **kwargs):
        self.subject = self.kwargs.get('subject')
        self.lesson = self.kwargs.get('lesson')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = self.subject
        context['lesson'] = self.lesson
        user_file = BankTasks.objects.filter(account_user=self.request.user, subject=self.subject, lesson=self.lesson)
        context['file_data'] = user_file
        return context

    def form_valid(self, form):
        form.instance.account_user = self.request.user
        form.instance.subject = self.kwargs['subject']
        print(form.instance.subject)
        form.instance.lesson = int(self.kwargs.get('lesson'))
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RussianLanguagePage(ListView):
    model = BankTasks
    template_name = 'tasks_students_bank/practical_page.html'
    extra_context = {'title': 'Русский язык'}
    context_object_name = 'subject'
    success_url = reverse_lazy('user_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        practicals_links = []
        for i in range(1, 13):
            practicals_links.append(('/test/rus/' + str(i), 'Практическая работа ' + str(i)))
        context['practicals_links'] = practicals_links
        return context


@method_decorator(login_required, name='dispatch')
class InfPage(ListView):
    model = BankTasks
    template_name = 'tasks_students_bank/practical_page.html'
    extra_context = {'title': 'Информатика'}
    context_object_name = 'subject'
    success_url = reverse_lazy('user_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        practicals_links = []
        for i in range(1, 13):
            practicals_links.append(('/test/inform/' + str(i), 'Практическая работа ' + str(i)))
        context['practicals_links'] = practicals_links
        return context


@method_decorator(login_required, name='dispatch')
class UserPage(ListView):
    model = BankTasks
    template_name = 'tasks_students_bank/user_page.html'
    extra_context = {'title': 'Страница пользователя'}
    context_object_name = 'subject'
    success_url = reverse_lazy('user_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = SUBJECT_CHOICES
        return context


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
    success_url = reverse_lazy('user_page')

    def get_success_url(self):
        """Ссылка перехода"""
        return reverse_lazy('user_page')

    def form_invalid(self, form):
        """Вывод при неверном пароле"""
        form.add_error(None, "Неверный логин или пароль")
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class MathPage(ListView):
    model = BankTasks
    template_name = 'tasks_students_bank/practical_page.html'
    extra_context = {'title': 'Математика'}
    context_object_name = 'subject'
    success_url = reverse_lazy('user_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        practicals_links = []
        for i in range(1, 13):
            practicals_links.append(('/test/math/' + str(i), 'Практическая работа ' + str(i)))
        context['practicals_links'] = practicals_links
        return context


def is_staff(user):
    return user.is_staff


@method_decorator(user_passes_test(is_staff), name='dispatch')
class TeacherPage(ListView):
    model = BankTasks
    template_name = 'tasks_students_bank/search.html'
    extra_context = {'title': 'Поиск'}
    form_class = SearchForm
    success_url = reverse_lazy('user_page')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:  # Проверяем, есть ли GET параметры
            context['form'] = SearchForm(self.request.GET)
        else:
            context['form'] = SearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            lesson = form.cleaned_data['lesson']
            queryset = queryset.filter(subject=subject, lesson=lesson)
        else:
            queryset = queryset.none()
        return queryset.select_related('account_user')


def logout_user(request):
    """Выход из аккаунта"""
    logout(request)
    return redirect('login')
