from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contact, name='contact'),
    path(
        "contact_success",
        views.contact_success,
        name="contact_success",
    ),
]
