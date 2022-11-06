from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, FullOrder
from plants.models import Plant
from bag.contexts import bag_contents

import stripe


def checkout(request):
    """
    A view to return the checkout page.
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }
        order_form = OrderForm(form_data)
        # Save order form if valid
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    plant = Plant.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Plant.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of your chosen plants was not found in \
                                our database."
                            "Please contact us for assistance."
                        ),
                    )
                    order.delete()
                    return redirect(reverse("view_bag"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                "There was an error with your form. \
                    Please check and try again.",
            )
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There are currently \
                no items in your bag.")
            return redirect(reverse('plants'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        # Stripe requires integer
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        message.warning(request, 'The Stripe public key is missing. \
            Please ensure this is set in your environment.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(FullOrder, order_number=order_number)

    messages.success(
        request,
        f"CONGRATULATIONS! Your order was successfully processed! \
        We are getting your new plants to you as fast as we can! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
