from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('sing_in', SingInPage.as_view(), name='sing_in'),
    path('create_lesson', AddLesson.as_view(), name='create_lesson'),
    path('login', LoginPage.as_view(), name='login'),
    path('search', TeacherPage.as_view(), name='search'),
    path('', UserPage.as_view(), name='user_page'),
    path('logout', logout_user, name='logout'),
    path('create_subject', AddSubject.as_view(), name='create_subject'),
    path('<str:subject_page>', SubjectPage.as_view(), name='subject_page'),
    path('<str:subject>/<str:lesson>/', PostFile.as_view(), name='test'),

]
