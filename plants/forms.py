from django import forms
from .models import Plant, PlantDifficulty, PlantType


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        plant_difficulties = PlantDifficulty.objects.all()
        plant_types = PlantType.objects.all()
        difficulty_names = [(c.id, c.name) for c in plant_difficulties]
        types_names = [(c.id, c.name) for c in plant_types]

        self.fields["plant_difficulty"].choices = difficulty_names
        self.fields["plant_type"].choices = types_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-1"
