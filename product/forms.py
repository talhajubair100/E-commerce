from django.db.models import fields
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

        widgets = {
            'subject' : forms.TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'comment' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Comment','rows':'2'}),
        }