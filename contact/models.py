
from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.


class Contact(models.Model):
    name = models.CharField(_("name"), max_length=50)
    address = models.CharField(_("address"), max_length=50)
    phone = models.CharField(_("phone"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    website = models.CharField(_("website"), max_length=50)
    message = models.TextField(_("message"))
    subject = models.CharField(_("subject"), max_length=50)


    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

