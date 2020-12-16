from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from product.models import Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from.models import UserProfile

# Create your views here.
def user_profile(request):
    return HttpResponse("User")



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url

            return HttpResponseRedirect("/")
        else:
            messages.warning(request, "Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect("/login")

    category = Category.objects.all()
    context = {'category': category}
    return render (request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def signup_view(request):
    return HttpResponse("Signup view")


