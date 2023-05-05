from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('sing_in', SingInPage.as_view(), name='sing_in'),
    path('login', LoginPage.as_view(), name='login'),
    path('', UserPage.as_view(), name='user_page'),
    path('logout', logout_user, name='logout'),
    path('math_page', MathPage.as_view(), name='math_page'),
    path('russian_language_page', RussianLanguagePage.as_view(), name='russian_language_page'),
    path('inf_page', InfPage.as_view(), name='inf_page'),
    path('lessons_page', LessonsPage.as_view(), name='lessons_page'),
    path('test/<str:subject>/<str:lesson>/', PostFile.as_view(), name='test'),

]