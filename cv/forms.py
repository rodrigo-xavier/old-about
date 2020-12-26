from . import models
from django import forms
from datetime import date
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['name'].widget.attrs.update({
                    'placeholder': _("Enter your name"),
                    'autofocus': "",
                }
            )
            self.fields['born_in'].widget.attrs.update({
                    'value':'2019-01-01'
                }
            )
            self.fields['mail'].widget.attrs.update({
                    'placeholder': _("Enter your email"),
                }
            )
            self.fields['phone'].widget.attrs.update({
                    'placeholder': _("Ex: (00) 00000-0000"),
                    'maxlength':'15',
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
    
    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        name = cleaned_data['name'].split(" ")
        name = "".join(name)
        if not (name.isalpha()):
            self.add_error('name', _('must be alphanumeric'))
            raise forms.ValidationError(_("must be alphanumeric"), code='invalid')

        return cleaned_data


    class Meta:
        model = models.Profile
        fields = ('name', 'born_in', 'mail', 'phone', 'languages', 'link',
            'about', 'current_goals', 'proffessional_description'
        )
        widgets = {
            'born_in': forms.DateInput(attrs={'type': 'date'})
        }


class XPForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(XPForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-group'
            self.fields['company_name'].widget.attrs.update({
                    'placeholder': _("Enter company name"),
                    'required': "",
                    'autofocus': "",
                }
            )
            self.fields['company_description'].widget.attrs.update({
                    'placeholder': _("Describe the company you've been worked"),
                }
            )
            self.fields['company_website'].widget.attrs.update({
                    'placeholder': _("Enter here the company website address"),
                }
            )
            self.fields['company_mail'].widget.attrs.update({
                    'placeholder': _("Enter here the company email address"),
                }
            )
            self.fields['company_phone'].widget.attrs.update({
                    'placeholder': _("Enter here the company phone"),
                }
            )
            self.fields['employee_role'].widget.attrs.update({
                    'placeholder': _("Enter here which was your job on the company"),
                    'required': ""
                }
            )
            self.fields['employee_main_activity'].widget.attrs.update({
                    'placeholder': _("Describe the main activities you performed at the company"),
                    'required': ""
                }
            )
            self.fields['from_period'].widget.attrs.update({
                    'required': ""
                }
            )
            self.fields['until_period'].widget.attrs.update({
                    'required': ""
                }
            )
            self.fields['is_current'].widget.attrs.update({
                }
            )
    
    def validate_name(self, data):
        company_name = data['company_name'].split(" ")
        company_name = "".join(company_name)
        if not (company_name.isalpha()):
            self.add_error('company_name', _('must be alphanumeric'))
            raise forms.ValidationError(_("must be alphanumeric"), code='invalid')

    # def validate_is_current(self, data):
    #     if data['is_current'] is True:
    #         models.XP.objects
    #         if not ():
    #             self.add_error('is_current', _('Is permitted just one checkbox selected'))
    #             raise forms.ValidationError(_("Is permitted just one checkbox selected"), code='invalid')
    
    def clean(self):
        cleaned_data = super(XPForm, self).clean()
        self.validate_name(cleaned_data)
        # self.validate_is_current(cleaned_data)

        return cleaned_data
    
    class Meta:
        widgets = {
            'from_period': forms.DateInput(attrs={'type': 'date'}),
            'until_period': forms.DateInput(attrs={'type': 'date'})
        }


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(EducationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-group'
            self.fields['institution'].widget.attrs.update({
                'placeholder': _("Describe the main activities you performed at the company"),
                'autofocus': "",
                
                }
            )
            self.fields['institution_description'].widget.attrs.update({
                }
            )
            self.fields['institution_website'].widget.attrs.update({
                }
            )
            self.fields['institution_mail'].widget.attrs.update({
                }
            )
            self.fields['institution_phone'].widget.attrs.update({
                }
            )
            self.fields['course'].widget.attrs.update({
                }
            )
            self.fields['course_description'].widget.attrs.update({
                }
            )
            self.fields['from_period'].widget = forms.HiddenInput()
            self.fields['until_period'].widget = forms.HiddenInput()
            self.fields['duration'].widget = forms.HiddenInput()
    
    def clean(self):
        institution = ""
        cleaned_data = super(EducationForm, self).clean()
        if cleaned_data['id'] is not None:
            institution = cleaned_data['institution'].split(" ")
            institution = "".join(institution)
        if not (institution.isalpha()):
            self.add_error('institution', _('must be alphanumeric'))
            raise forms.ValidationError(_("must be alphanumeric"), code='invalid')

        return cleaned_data
    
    class Meta:
        widgets = {
            'from_period': forms.DateInput(attrs={'type': 'date'}),
            'until_period': forms.DateInput(attrs={'type': 'date'})
        }