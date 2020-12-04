from django.http.response import HttpResponse
from product.models import Category, Product
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Setting, ContactMessage
from .forms import ContactForm


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('-id')[:3]
    page = "home"
    context = {'setting': setting, 'page': page, 'category': category, 'product_slider': product_slider}

    return render(request ,'index.html', context)

def about(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    setting = Setting.objects.get(pk=1)
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

    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    products = Product.objects.filter(category_id=id)
    # print(product.title)
    # context = {'product': product}
    # return render(request, 'category_products.html', context)
    return HttpResponse(products)
