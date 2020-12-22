from django.urls import path 
from .views import user_profile, user_update, user_password, user_orders


urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('update/', user_update, name='user_update'),
    path('password/', user_password, name='user_password'),
    path('orders/', user_orders, name='user_orders'),


]
