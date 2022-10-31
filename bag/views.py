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


def adjust_bag(request, item_id):
    """Adjust quantites of an item in bag"""

    plant = get_object_or_404(Plant, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f"The quantity of {plant.name} in your bag has been \
                updated to {bag[item_id]}",
        )

    else:
        bag.pop(item_id)
        messages.success(
            request, f"{plant.name} has been removed from your bag"
        )

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove a product from the shopping bag"""

    try:
        plant = get_object_or_404(Plant, pk=item_id)
        bag = request.session.get("bag", {})
        bag.pop(item_id)
        messages.success(
            request, f"{plant.name} has been removed from your bag"
        )

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing {e} from your bag")
        return HttpResponse(status=500)
