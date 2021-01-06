from django import forms
from django.contrib.auth.forms import  UserChangeForm
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ChangePasswordForm, ResetPasswordKeyForm, AddEmailForm

from django.contrib.auth.models import User
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import TextInput
from .models import UserProfile
#from django.forms import widgets

class CustomeLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomeLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'
        })

class CustomeSetPassForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(CustomeSetPassForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

class CustomeChngPassForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomeChngPassForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })


class CustomeResetPassForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomeResetPassForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })

class CustomeAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(CustomeAddEmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })


class CustomeSignupForm(SignupForm):


    def __init__(self, *args, **kwargs):
        super(CustomeSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

    def save(self, request):
        user = super(CustomeSignupForm, self).save(request)
        
        user_profile = UserProfile.objects.get_or_create(user=user)

        return user
        


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