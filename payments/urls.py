from django.urls import path
from .views import *

app_name = 'payments'
urlpatterns = [
    path('', checkout_view, name='check-out'),
    path('<int:id>/', confirmation_view, name='confirm'),
    path('process_order/', processOrder, name="process_order"),
]