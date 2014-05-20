from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Image


class ImageForm(forms.Form):
    image = forms.ImageField(label=_(u'Image'))
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'a short description of the image for screen ' +
            'readers and search engines',
        }),
        label=_(u'Description')
    )
    size = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(
            ('billboard', _(u'Billboard')),
            ('small', _(u'Small')),
            ('medium', _(u'Medium')),
            ('large', _(u'Large')),
            ('original', _(u'Original')),
        ),
        initial = 'Billboard',
        label=_(u'Size')
    )


class LibraryForm(forms.Form):
    image = forms.ModelChoiceField(
        queryset=Image.objects.all(),
        widget=forms.HiddenInput,
        label=_(u'Image')
    )
    size = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(
            ('billboard', _(u'Billboard')),
            ('small', _(u'Small')),
            ('medium', _(u'Medium')),
            ('large', _(u'Large')),
            ('original', _(u'Original')),
        ),
        initial = 'Billboard',
        label=_(u'Size')
    )
