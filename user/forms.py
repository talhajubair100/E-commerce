from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, label="User Name")
    email = forms.EmailField(max_length=100, label="Email")
    first_name = forms.CharField(max_length=100, help_text="First Name", label="First Name")
    last_name = forms.CharField(max_length=100, help_text="Last Name", label="Last Name")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )