from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm
from .models import Contact


def view_contact(request):
    """
    A view to return the contact page.
    """
    contact_form = ContactForm()

    if request.method == "POST":
        form_data = {
            "name": request.POST["name"],
            "from_email": request.POST["from_email"],
            "phone_number": request.POST["phone_number"],
            "message": request.POST["message"],
        }
        contact_form = ContactForm(form_data)
        # Save contact form if valid
        if contact_form.is_valid():
            customer_message = contact_form.save()
            # Does ID not exist??
            print(customer_message)

            # Feed contact_success the message id
            return redirect(
                reverse("contact_success", args=[
                    customer_message._id])
            )
        else:
            messages.error(
                request,
                "There was an error with your form. \
                    Please check and try again.",
            )

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


# Process message success
def contact_success(request, _id):
    """
    Handle successful contact messages
    """

    contact = get_object_or_404(Contact, contact_id=_id)

    # Toast message success
    messages.success(
        request,
        f"Thank you {contact.name} for getting in touch! \
        We have recieved your message and will reply as \
        soon as we can. Please check your inbox at \
        {contact.from_email} for our reply.",
    )

    template = 'contact/contact_success.html'
    context = {
        "contact": contact,
    }

    return render(request, template, context)
