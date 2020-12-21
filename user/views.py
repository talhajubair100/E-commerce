from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from product.models import Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from.models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def user_profile(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'profile': profile}
    return render(request, 'user_profile.html', context)


def user_update(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.userprofile)
    category = Category.objects.all()
    context = {'user_form': user_form, 'profile_form': profile_form, 'category': category}
    return render(request, 'user_update.html', context)




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
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  #signup complete here
            
            
            # this code for auto login 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="media/users/user.jpg"
            data.save()
            messages.success(request, 'Your account has been created!')
          

            return HttpResponseRedirect("/login/")
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')
    
    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category, 'form': form}

    return render (request, 'signup.html', context)


