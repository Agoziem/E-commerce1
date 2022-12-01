from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', profile_view, name='Books'),
    path('cart/', cart_view, name='cart'),
    path('update_item/', updateItem, name='update_item'),
    path('delete_item/', delete_item, name='delete_item'),
    path('review_item/', review_item, name='review_item'),
    path('like/', like_book, name='like_book'),
]