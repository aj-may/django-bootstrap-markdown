from django import forms
from django_bootstrap_markdown.widgets import MarkdownInput

class TestForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput( attrs={'class':'form-control'} )
    )
    slug = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'If left blank a slug will automaticly be created.'
        })
    )
    body = forms.CharField(
        widget=MarkdownInput(image_control=True)
    )
    published = forms.BooleanField(required=False)