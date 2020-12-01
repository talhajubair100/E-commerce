from django.shortcuts import redirect, render
from .models import Setting

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    page = "home"
    context = {'setting': setting, 'page': page}

    return render(request ,'index.html', context)

def about(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'contact.html', context)
