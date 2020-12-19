import user
from user.models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Order, OrderProduct, ShopCart
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ShopCartForm, OrderForm, CardInfoForm
from product.models import Category, Product

from django.utils.crypto import get_random_string

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

@login_required
def orderproduct(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

       
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity 
    
    
    #form2 = CardInfoForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()
            
            for pro in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = pro.product_id
                detail.user_id = current_user.id
                detail.quantity = pro.quantity
                detail.price = pro.product.price
                detail.amount = pro.amount
                detail.save()

                ########
                product = Product.objects.get(id=pro.product_id)
                product.amount -= pro.quantity
                product.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request, "your order is done")
            return render(request, 'order_form.html', {'category': category})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    pro_data = {'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'address': profile.address,
            'phone': profile.phone,
            'city': profile.city,
            'country': profile.country}
    form = OrderForm(initial=pro_data)


    context = { 'category': category, 'shopcart': shopcart, 'total': total, 'form': form}
    return render(request, 'order_form.html', context)