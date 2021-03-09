from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'rows' : 3,
    }))

    class Meta:
        model = Comment
        fields = ('content', )