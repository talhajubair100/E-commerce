
from django import forms
from django.db.models import fields
from .models import ShopCart, Order

class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firdt_name', 'last_name', 'address', 'phone', 'city', 'country']
        