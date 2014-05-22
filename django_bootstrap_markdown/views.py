from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_bootstrap_markdown.models import Image
from django_bootstrap_markdown.forms import ImageForm, LibraryForm


@login_required
def markdown_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image()
            image.original = form.cleaned_data['image']
            image.description = form.cleaned_data['description']
            image.save()

            if form.cleaned_data['size'] == 'small':
                thumbnail = image.small
            elif form.cleaned_data['size'] == 'medium':
                thumbnail = image.medium
            elif form.cleaned_data['size'] == 'large':
                thumbnail = image.large
            elif form.cleaned_data['size'] == 'original':
                thumbnail = image.original
            else:
                thumbnail = image.billboard

            return render(
                request,
                'django_bootstrap_markdown/markdown_image.html', {
                    'form': form,
                    'image': image,
                    'thumbnail': thumbnail,
                }
            )
    else:
        form = ImageForm()

    return render(request, 'django_bootstrap_markdown/markdown_image.html', {
        'form': form,
    })


@login_required
def markdown_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            image = form.cleaned_data['image']

            if form.cleaned_data['size'] == 'small':
                thumbnail = image.small
            elif form.cleaned_data['size'] == 'medium':
                thumbnail = image.medium
            elif form.cleaned_data['size'] == 'large':
                thumbnail = image.large
            elif form.cleaned_data['size'] == 'original':
                thumbnail = image.original
            else:
                thumbnail = image.billboard

            return render(
                request,
                'django_bootstrap_markdown/markdown_library.html', {
                    'form': form,
                    'image': image,
                    'thumbnail': thumbnail,
                }
            )
    else:
        form = LibraryForm()

    return render(request, 'django_bootstrap_markdown/markdown_library.html', {
        'images': Image.objects.all(),
        'form': form,
    })
