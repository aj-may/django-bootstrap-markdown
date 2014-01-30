from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField()
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'a short description of the image for screen readers and search engines',
        })
    )
    size = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = (
            ('Billboard', 'Billboard'),
            ('Small', 'Small'),
            ('Medium', 'Medium'),
            ('Large', 'Large'),
            ('Original', 'Original'),
        ),
        initial = 'Billboard'
    )