import user
from user.models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Order, OrderProduct, ShopCart
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ShopCartForm, OrderForm, CardInfoForm
from product.models import Category, Product, Variants
from django.utils.crypto import get_random_string

# Create your views here.
def order(request):
    return HttpResponse ("Order Page")

@login_required
def add_to_shopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = Product.objects.get(pk=id)

    if product.variant != 'None':
        variantid = request.POST.get('variantid')
        checkvariant = ShopCart.objects.filter(variant_id=variantid, user_id=current_user.id)
        if checkvariant:
            control = 1
        else:
            control = 0 
    else:
        checkproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id)
        if checkproduct:
            control = 1
        else:
            control = 0 

    if request.method == 'POST':
        variantid = request.POST.get('variantid')
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1:
                if product.variant == 'None':
                    data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                else:
                    data = ShopCart.objects.get(product_id=id, variant_id=variantid, user_id=current_user.id)

                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)

    else:
        if control==1:
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.variant_id = None
            data.save()
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)


@login_required
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity 
        else:
            total += rs.variant.price * rs.quantity
        

    print(total)   

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
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity 
        else:
            total += rs.variant.price * rs.quantity 

    
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
                if pro.product.variant == 'None':
                    detail.price = pro.product.price
                else:
                    detail.price = pro.variant.price
                detail.variant_id = pro.variant_id
                detail.amount = pro.amount
                detail.save()

                ########
                if pro.product.variant == 'None':
                    product = Product.objects.get(id=pro.product_id)
                    product.amount -= pro.quantity
                    product.save()
                else:
                    variant = Variants.objects.get(id=pro.variant_id)
                    variant.quantity -= pro.quantity
                    variant.save()


            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request, "your order is done")
            return render(request, 'order_complete.html', {'category': category, 'ordercode': ordercode})
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