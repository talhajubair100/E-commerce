from django.urls import path 
from .views import order, add_to_shopcart, shopcart, delete_from_shopcart, orderproduct

urlpatterns = [
   path('', order, name='order'),
   path('shopcart', shopcart, name='shopcart'),
   path('add_to_shopcart/<int:id>', add_to_shopcart, name='add_to_shopcart'),
   path('delete_from_shopcart/<int:id>', delete_from_shopcart, name='delete_from_shopcart'),
   path('orderproduct', orderproduct, name='orderproduct'),



]
