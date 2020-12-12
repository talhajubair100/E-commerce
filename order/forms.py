
from django import forms
from .models import ShopCart

class ShopCart(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']