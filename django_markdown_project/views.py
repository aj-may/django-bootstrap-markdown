from django.shortcuts import render
from django_markdown_project.forms import TestForm

def test(request):
    form = TestForm()

    return render(request, 'test.html', {
        'form': form,
    })