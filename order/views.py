from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def order(request):
    return HttpResponse ("Order Page")

@login_required
def add_to_shopcart(request, id):
    # url = request.META.get("HTTP_REFERER")
    # current_user = request.user

    pass