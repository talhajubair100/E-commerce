from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
            'subject' : forms.TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : forms.TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Message','rows':'7'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()