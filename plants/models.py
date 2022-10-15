from django.db import models


class PlantType(models.Model):
    """Plant types"""

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class PlantDifficulty(models.Model):
    """Plant care difficulties"""

    class Meta:
        verbose_name_plural = 'Plant difficulties'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Plant(models.Model):
    """Individual plant details"""

    plant_type = models.ForeignKey(
        'PlantType', null=True, blank=True, on_delete=models.SET_NULL)
    plant_difficulty = models.ForeignKey(
        'PlantDifficulty', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
