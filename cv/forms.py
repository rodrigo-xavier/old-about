from . import models
from django import forms
from datetime import date
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['name'].widget.attrs.update({
                    'placeholder': _("Enter your name"),
                    'autofocus': "",
                }
            )
            self.fields['born'].widget.attrs.update({
                    'value':'2019-01-01'
                }
            )
            self.fields['mail'].widget.attrs.update({
                    'placeholder': _("Enter your email"),
                }
            )
            self.fields['phone'].widget.attrs.update({
                    'placeholder': _("Enter your phone. Ex: (00) 00000-0000"),
                }
            )
            self.fields['languages'].widget.attrs.update({
                    'placeholder': _("Select languages you can speak"),
                }
            )
            self.fields['link'].widget.attrs.update({
                    'placeholder': _("Input your links"),
                }
            )
            self.fields['about'].widget.attrs.update({
                    'placeholder': _("Describe yourself"),
                    'rows': 19,
                }
            )
            self.fields['current_goals'].widget.attrs.update({
                    'placeholder': _("Describe your current goals"),
                    'rows': 8,
                }
            )
            self.fields['proffessional_description'].widget.attrs.update({
                    'placeholder': _("Tell about your professional profile"),
                    'rows': 8,
                }
            )

    class Meta:
        model = models.Profile
        fields = ('name', 'born', 'mail', 'phone', 'languages', 'link', 
            'about', 'current_goals', 'proffessional_description'
        )
        widgets = {
            'born': forms.DateInput(attrs={'type': 'date'})
        }