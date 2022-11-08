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
    plant_types = None
    plant_difficulties = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                plants = plants.annotate(lower_name=Lower('name'))
            if sortkey == 'plant_type':
                sortkey = 'plant_type__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            plants = plants.order_by(sortkey)

        if 'plant_type' in request.GET:
            plant_types = request.GET['plant_type'].split(',')
            plants = plants.filter(plant_type__name__in=plant_types)
            plant_types = PlantType.objects.filter(name__in=plant_types)

        if 'plant_difficulty' in request.GET:
            plant_difficulties = request.GET['plant_difficulty'].split(',')
            plants = plants.filter(
                plant_difficulty__name__in=plant_difficulties)
            plant_difficulties = PlantDifficulty.objects.filter(
                name__in=plant_difficulties)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Oops! You didn't search for \
                    anything. Here's all of our amazing products instead!")
                return redirect(reverse('plants'))

            # Case insensitive searching, name and description
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            plants = plants.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'plants': plants,
        'search_term': query,
        'current_plant_types': plant_types,
        'current_plant_difficulties': plant_difficulties,
        'current_sorting': current_sorting,
    }

    return render(request, 'plants/plants.html', context)


def plant_detail(request, plant_id):
    """View to render an indvidual plant page"""

    plant = get_object_or_404(Plant, pk=plant_id)

    context = {
        "plant": plant
    }

    return render(request, "plants/plant_detail.html", context)
