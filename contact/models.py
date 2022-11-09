from django.db import models


class Contact(models.Model):
    """
    Holds contact information and communication
    """

    class Meta:
        verbose_name_plural = 'Customer messages'

    name = models.CharField(max_length=50, null=False, blank=False)
    from_email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=False, blank=False, default="")
