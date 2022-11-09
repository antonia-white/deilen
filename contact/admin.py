from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    readonly_fields = (
        "name",
        "from_email",
        "phone_number",
        "message",
    )

    fields = (
        "name",
        "from_email",
        "phone_number",
        "message",
    )

    list_display = (
        "name",
        "from_email",
        "phone_number",
        "message",
    )


admin.site.register(Contact, ContactAdmin)
