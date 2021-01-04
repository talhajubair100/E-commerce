from django import forms
from django.contrib.auth.forms import  UserChangeForm
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ChangePasswordForm, ResetPasswordKeyForm, AddEmailForm

from django.contrib.auth.models import User
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from .models import UserProfile
#from django.forms import widgets


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