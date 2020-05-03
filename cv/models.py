# CV = Curriculum Vitae

from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.models import PhoneField

class Profile(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    phone = PhoneField(_('Phone'))
    mail = models.EmailField(_("Mail"), max_length=254)

