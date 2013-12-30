from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django_bootstrap_markdown.models import Image
from django_bootstrap_markdown.forms import ImageForm

def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def markdown_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image()
            image.original = form.cleaned_data['image']
            image.description = form.cleaned_data['description']
            image.save()

            return render(request, 'markdown_image.html', {
                'form': form,
                'image': image,
            })
    else:
        form = ImageForm()

    return render(request, 'markdown_image.html', {
        'form': form,
    })