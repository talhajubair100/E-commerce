from django.contrib.auth.forms import PasswordChangeForm
from .forms import  UserUpdateForm, ProfileUpdateForm
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from product.models import Category, Comment
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import UserProfile
from order.models import Order, OrderProduct
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def user_profile(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'profile': profile}
    return render(request, 'user_profile.html', context)

@login_required
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been update')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'user_form': user_form, 'profile_form': profile_form, 'category': category}
        return render(request, 'user_update.html', context)

@login_required
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #important 
            messages.success(request, "Your password was successfully update !")
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {'category': category, 'form': form}
        return render(request, 'user_password.html', context)


@login_required
def user_orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id).order_by('-create_at')

    context = {'category': category, 'orders': orders}
    return render(request, 'user_orders.html', context)

@login_required
def order_details(request, id):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {'category': category, 'orders': orders, 'orderitems': orderitems}
    return render(request, 'user_order_detail.html', context)



@login_required
def user_orders_product(request):
    category = Category.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id).order_by('-id')
    context = {'category': category, 'order_product': order_product}
    return render(request, 'user_orders_product.html', context)


@login_required
def user_order_product_details(request, id, oid):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(id=id, user_id=current_user.id)
    context = {'category': category, 'orderitems': orderitems, 'orders': orders}
    return render(request, 'user_order_detail.html', context)


@login_required
def user_comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category, 'comments': comments}
    return render(request, 'user_comments.html', context)

@login_required
def user_delete_comment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id ,user_id=current_user.id).delete()
    messages.success(request, "Secessfully delete comment....")
    return HttpResponseRedirect('user/comments/')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             current_user = request.user
#             userprofile = UserProfile.objects.get(user_id=current_user.id)
#             request.session['userimage'] = userprofile.image.url

#             return HttpResponseRedirect("/")
#         else:
#             messages.warning(request, "Login Error !! Username or Password is incorrect")
#             return HttpResponseRedirect("/login")

#     category = Category.objects.all()
#     context = {'category': category}
#     return render (request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


# def signup_view(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()  #signup complete here
            
            
#             # this code for auto login 
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)

#             # Create data in profile table for user
#             current_user = request.user
#             data=UserProfile()
#             data.user_id=current_user.id
#             data.image="media/users/user.jpg"
#             data.save()
#             messages.success(request, 'Your account has been created!')
          

#             return HttpResponseRedirect("/login/")
#         else:
#             messages.warning(request,form.errors)
#             return HttpResponseRedirect('/signup')
    
#     form = SignUpForm()
#     category = Category.objects.all()
#     context = {'category': category, 'form': form}

#     return render (request, 'signup.html', context)


