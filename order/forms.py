
from django import forms
from django.db.models import fields
from .models import ShopCart, Order
from user.models import UserProfile 

class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            'address': forms.TextInput(attrs={'class': 'input'}),
            'phone': forms.TextInput(attrs={'class': 'input'}),
            'city': forms.TextInput(attrs={'class': 'input'}),
            'country': forms.TextInput(attrs={'class': 'input'}),

        }

class CardInfoForm(forms.Form):
    card_holder_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Card Holder Name'}))
    card_holder_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Card Holder Number'}))
    card_expire_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'mm/yy'}))
    card_security_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Security Number'}))

