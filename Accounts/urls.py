from django.urls import path
from .views import *

app_name = 'Accounts'
urlpatterns = [
    path('login/', loginPage, name='login'),
    path('signup/', registerPage, name='sign-up'),
    path('logout/', logoutUser, name='logout'),
    path('forget_password/', resetpassword_view, name='reset'),
]