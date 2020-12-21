from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from .models import UserProfile
#from django.forms import widgets

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="User Name")
    email = forms.EmailField(max_length=100, label="Email")
    first_name = forms.CharField(max_length=100, help_text="First Name", label="First Name")
    last_name = forms.CharField(max_length=100, help_text="Last Name", label="Last Name")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class': 'input','placeholder':'E-Mail'}),
            'first_name': forms.TextInput(attrs={'class': 'input','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input','placeholder':'Last Name'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input','placeholder':'Phone'}),
            'address': forms.TextInput(attrs={'class': 'input','placeholder':'Address'}),
            'city': forms.TextInput(attrs={'class': 'input','placeholder':'City'}),
            'country': forms.TextInput(attrs={'class': 'input','placeholder':'Country'}),
            'image': forms.FileInput(attrs={'class': 'input','placeholder':'Image'}),


        }