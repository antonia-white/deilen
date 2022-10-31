from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Plant, PlantDifficulty, PlantType


def all_plants(request):
    """ A view to show all plants, including sorting and search queries """

    plants = Plant.objects.all()
    query = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('plants'))
            
            # Case insensitive searching, name and description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            plants = plants.filter(queries)

    context = {
        'plants': plants,
        'search_term': query,
    }

    return render(request, 'plants/plants.html', context)


def plant_detail(request, plant_id):
    """View to render an indvidual plant page"""

    plant = get_object_or_404(Plant, pk=plant_id)

    context = {
        "plant": plant
    }

    return render(request, "plants/plant_detail.html", context)
