from django import forms
from unittest.util import _MAX_LENGTH
from .models import Document
# from myapp.models import CustomUser


class AdminForm(forms.Form):
    attrs={"type":"password"}
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter the email'}), max_length=250)
    password=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the password'}))

class upload(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('filetype','description', 'document', )