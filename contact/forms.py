from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "from_email",
            "phone_number",
            "message",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Name",
            "from_email": "example@email.com",
            "phone_number": "0123456789",
            "message": "Please enter your message here...",
        }

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
