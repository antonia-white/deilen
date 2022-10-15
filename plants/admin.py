from django.contrib import admin
from .models import Plant, PlantDifficulty, PlantType

# Register your models here.


class PlantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'plant_type',
        'plant_difficulty',
        'price',
        'image',
    )

    ordering = ('plant_type', 'plant_difficulty')


class PlantDifficultyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class PlantTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Plant, PlantAdmin)
admin.site.register(PlantType, PlantTypeAdmin)
admin.site.register(PlantDifficulty, PlantDifficultyAdmin)
