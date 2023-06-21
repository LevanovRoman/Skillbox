from django.urls import path
from .views import *

app_name = "shopapp"

urlpatterns = [
    path('', shop_index, name='index'),
    path('groups/', groups_list, name='groups_list'),
    path('products/', products_list, name='products_list'),
]