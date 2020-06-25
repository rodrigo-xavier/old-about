from . import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

class ProfileForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     pass

    class Meta:
        model = models.Profile
        fields = ('name', 'born', 'mail', 'mail', 'phone', 'languages', 'link', 
            'about', 'current_goals', 'proffessional_description'
        )