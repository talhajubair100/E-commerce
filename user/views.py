from django.shortcuts import render
from django.http.response import HttpResponse
from product.models import Category

# Create your views here.
def user_profile(request):
    return HttpResponse("User")



def login_view(request):
    category = Category.objects.all()
    context = {'category': category}
    return render (request, 'login.html', context)

def signup_view(request):
    return HttpResponse("Signup view")