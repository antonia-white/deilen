from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404,
)
from django.contrib import messages

from plants.models import Plant, PlantDifficulty, PlantType


def view_bag(request):
    """Renders the shopping bag page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Adds a quantity of a specific plant to the bag"""

    plant = get_object_or_404(Plant, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f"Updated {plant.name} in your wheelbarrow to {bag[item_id]}",
        )

    else:
        bag[item_id] = quantity
        messages.success(request, f"{plant.name} has been added to your wheelbarrow")

    request.session["bag"] = bag
    return redirect(redirect_url)
