from django.shortcuts import render
from django.conf import settings


def index(request):
    """
    A view to return the index page.
    """
    context = {
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }

    template = 'home/index.html'

    return render(request, template, context)
