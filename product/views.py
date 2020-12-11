from django.core.checks import messages
from product.models import Comment
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CommentForm
from django.contrib import messages
# Create your views here.
def product(request):
    return HttpResponse('hello i am talha')

def addcomment(request, id):
    url = request.META.get('HTTP_REFERER') # get last url
    #return HttpResponse(url)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Your review has ben sent. Thank you for your interest.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)



