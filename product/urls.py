from django.urls import path 
from .views import product, addcomment

urlpatterns = [
    path('', product, name='product'),
    path('addcomment/<int:id>', addcomment, name='addcomment'),
]
