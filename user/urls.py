from django.urls import path 
from .views import user_profile, user_update, user_password, user_orders, order_details


urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('update/', user_update, name='user_update'),
    path('password/', user_password, name='user_password'),
    path('orders/', user_orders, name='user_orders'),
    path('order_details/<int:id>', order_details, name='order_details'),

    


]
