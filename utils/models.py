from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class PhoneField(models.Model):
    phone = models.CharField(
                max_length=13,
                blank=False,
                validators=[
                    RegexValidator(
                        regex=r'^\d{9,13}$',
                        message=_("Phone number must be between 9 and 13 digits")
                        )
                    ]
                )