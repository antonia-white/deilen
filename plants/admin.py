from django.contrib import admin
from .models import Plant, PlantDifficulty, PlantType

# Register your models here.
admin.site.register(Plant)
admin.site.register(PlantType)
admin.site.register(PlantDifficulty)
