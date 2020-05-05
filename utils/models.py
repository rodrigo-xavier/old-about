from django.db import models
from django.core.validators import RegexValidator


class PhoneField(models.Model):
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                                        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], 
                                                        max_length=15, blank=True)