from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from checkout.models import FullOrder
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display the user's profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, "Profile update failed. Please check \
                the form and try again")
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(FullOrder, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}."
            f"A confirmation email was sent on {order.date}."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {"order": order, "from_profile": True}

    return render(request, template, context)
