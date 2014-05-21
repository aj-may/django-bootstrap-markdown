from django import forms
from django_bootstrap_markdown.widgets import MarkdownInput


class TestForm(forms.Form):
    markdown = forms.CharField(widget=MarkdownInput)
