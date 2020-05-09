from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class PhoneField(models.Model):
    def set_phone(self, phone, verbose_name, max_length=15, unique=True):
        phone = models.CharField(
                verbose_name=verbose_name,
                max_length=max_length,
                unique=unique,
                validators=[
                    RegexValidator(
                        regex=r'^\d{9,13}$',
                        message=_("Phone number must be between 9 and 13 digits")
                    )
                ]
            )