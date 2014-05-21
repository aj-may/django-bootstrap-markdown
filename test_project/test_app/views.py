from django.shortcuts import render
from .forms import TestForm


def test_view(request):
    return render(request, 'test.html', {
        'form': TestForm,
    })
