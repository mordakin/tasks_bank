from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sing_in', SingInPage.as_view(), name='sing_in'),
    path('login', LoginPage.as_view(), name='login'),
    path('user_page', user_page, name='user_page'),
    path('logout', logout_user, name='logout'),
    # path('user_page', UserPage.as_view(), name='user_page'),

]