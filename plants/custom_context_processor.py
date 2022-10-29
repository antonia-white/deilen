from .models import PlantType


def types_renderer(request):
    return {
       'all_types': PlantType.objects.all(),
       }
