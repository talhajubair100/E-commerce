from django.http.response import HttpResponse
from product.models import Category, Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Setting, ContactMessage
from .forms import ContactForm, SearchForm 


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('-id')[:3] #first 4 products
    latest_product = Product.objects.all().order_by('-id')[:4] #last 4 products
    product_picked = Product.objects.all().order_by('?')[:4] #rendom 4 products


    page = "home"
    context = {'setting': setting,
            'page': page,
            'category': category,
            'product_slider': product_slider,
            'latest_product': latest_product,
            'product_picked': product_picked,
            }

    return render(request ,'index.html', context)

def about(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category}
    return render(request, 'about.html', context)


def contact(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your Message has been sent, Thank you.")
            return HttpResponseRedirect('/contact')

    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contact.html', context)





def category_products(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    setting = Setting.objects.get(pk=1)

    # print(product.title)
    context = {'products': products, 'category': category, 'setting': setting}
    return render(request, 'category_products.html', context)
    #return HttpResponse(products)


# def search(request):
#     if request.method == 'POST': # check post
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             query = form.cleaned_data['query'] # get form input data
#             catid = form.cleaned_data['catid']
#             if catid==0:
#                 products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
#             else:
#                 products = Product.objects.filter(title__icontains=query,category_id=catid)

#             category = Category.objects.all()
#             context = {'products': products, 'query':query,
#                        'category': category }
#             return render(request, 'search_products.html', context)

#     return HttpResponseRedirect('/search/')

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid==0:
                products = Product.objects.filter(title__contains=query)
            else:
                products = Product.objects.filter(title__contains=query, category_id=catid)
            category = Category.objects.all()

            context = {'products': products, 'query':query,
                            'category': category }
            return render(request, 'search_products.html', context)
            
    category = Category.objects.all()

    return render(request, 'search_products.html', {'category': category})
    