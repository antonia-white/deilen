from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """
    Display the user's profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders=profile.orders.all()

    form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form':form,
        'orders':orders,
    }

    return render(request, template, context)
