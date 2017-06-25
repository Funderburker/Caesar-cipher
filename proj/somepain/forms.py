from django import forms
from .models import InitialText, ChangedText


class Encrypt(forms.Form):
    init = forms.CharField(widget=forms.Textarea)
    ofs = forms.CharField(label="test", max_length=100)