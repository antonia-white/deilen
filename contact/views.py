from django.shortcuts import render


def view_contact(request):
    """
    A view to return the contact page.
    """
    return render(request, 'contact/contact.html')
