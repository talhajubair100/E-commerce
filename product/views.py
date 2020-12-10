from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def product(request):
    return HttpResponse('hello i am talha')

def addcomment(request, id):
    pass