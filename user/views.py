from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def user_profile(request):
    return HttpResponse("User")