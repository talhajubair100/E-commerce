from django.urls import path 
from .views import user_profile, user_update


urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('update/', user_update, name='user_update'),
]
