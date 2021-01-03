from django.conf import settings
from django.contrib.admin.sites import site
from django.http.response import HttpResponse, JsonResponse
from product.models import Category, Comment, Product, Images, Variants
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import FAQ, Setting, ContactMessage
from .forms import ContactForm, SearchForm 
import json
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY
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


def product_detail(request, id, slug):
    query = request.GET.get('q')
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    # print(product.title)
    comment = Comment.objects.filter(product_id=id, status=True)
    cmt_count = Comment.objects.filter(product_id=id, status=True).count()
    context = {'product': product, 'category': category, 'images': images, 'comment': comment, 'cmt_count': cmt_count}

    if product.variant != "None":
        if request.method == "POST":
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id)
            colors = Variants.objects.filter(product_id=id, size_id=variant.size_id)
            sizes = Variants.objects.raw('SELECT * FROM product_variants WHERE product_id=%s GROUP BY size_id',[id])
            query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id, size_id=variants[0].size_id)
            sizes = Variants.objects.raw('SELECT * FROM product_variants WHERE product_id=%s GROUP BY size_id',[id])
            variant = Variants.objects.get(id=variants[0].id)
        
        context.update({'sizes': sizes, 'colors': colors, 'variant': variant, 'query': query})
    return render(request, 'product_detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)


def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)

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
    



def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    products = Product.objects.filter(title__icontains=q)
    results = []
    for pro in products:
      product_json = {}
      product_json = pro.title
      results.append(product_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.filter(status="True").order_by("order_number")
    context = {
        "category": category,
        "faq": faq,
    }
    return render(request, 'faq.html', context)