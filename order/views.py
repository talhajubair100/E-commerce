from user.models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ShopCart
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ShopCartForm, OrderForm, CardInfoForm
from product.models import Category

# Create your views here.
def order(request):
    return HttpResponse ("Order Page")

@login_required
def add_to_shopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    checkproduct = ShopCart.objects.filter(product_id=id)
    
    if checkproduct:
        control = 1
    else:
        control = 0 

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)

    else:
        if control==1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)


@login_required
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity 
       

    context = { 'category': category, 'shopcart': shopcart, 'total': total}
    return render(request, 'shopcart_products.html', context)

@login_required
def delete_from_shopcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect("/order/shopcart")


def orderproduct(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    data = {'first_name': current_user.first_name,
         'last_name': current_user.last_name,
         'address': profile.address,
         'phone': profile.phone,
         'city': profile.city,
         'country': profile.country}
    form = OrderForm(initial=data)
    form2 = CardInfoForm()
       
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity 
       

    context = { 'category': category, 'shopcart': shopcart, 'total': total, 'form': form, 'form2': form2}
    return render(request, 'order_form.html', context)