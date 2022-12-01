from django.urls import path
from .views import *

app_name = 'books'
urlpatterns = [
    path('', books_view, name='Books'),   
    path('<int:id>/details/', Book_details, name='details'),]