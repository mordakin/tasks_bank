from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sing_in', SingInPage.as_view(), name='sing_in'),
    path('login', LoginPage.as_view(), name='login'),
    path('user_page', UserPage.as_view(), name='user_page'),
    path('logout', logout_user, name='logout'),
    path('math_page', MathPage.as_view(), name='math_page'),
    path('russian_language_page', RussianLanguagePage.as_view(), name='russian_language_page'),
    path('lessons_page', LessonsPage.as_view(), name='lessons_page'),
    path('test/<str:subject>/<str:lesson>/', PostFile.as_view(), name='test'),

]