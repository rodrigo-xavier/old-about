from . import models
from django import forms
from datetime import date
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from utils.constants import LANGUAGES
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['first_name'].widget.attrs.update({
                    'placeholder': _("Enter your first name"),
                    'autofocus': "",
                    'required': "",
                }
            )
            self.fields['last_name'].widget.attrs.update({
                    'placeholder': _("Enter your last name"),
                    'required': "",
                }
            )
            self.fields['email'].widget.attrs.update({
                    'placeholder': _("Enter your email"),
                }
            )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['born_in'].widget.attrs.update({
                    'value':'2019-01-01'
                }
            )
            self.fields['phone'].widget.attrs.update({
                    'placeholder': _("Ex: (00) 00000-0000"),
                    'maxlength':'15',
                }
            )
            self.fields['about'].widget.attrs.update({
                    'placeholder': _("Describe yourself"),
                    'rows': 29,
                }
            )
            self.fields['current_goals'].widget.attrs.update({
                    'placeholder': _("Describe your current goals"),
                    'rows': 13,
                }
            )
            self.fields['proffessional_description'].widget.attrs.update({
                    'placeholder': _("Tell about your professional profile"),
                    'rows': 13,
                }
            )
            self.fields['github'].widget.attrs.update({
                    'placeholder': _("GitHub profile link"),
                }
            )
            self.fields['linkedin'].widget.attrs.update({
                    'placeholder': _("Linkedin profile link"),
                }
            )
            self.fields['instagram'].widget.attrs.update({
                    'placeholder': _("Instagram profile link"),
                }
            )
    
    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        return cleaned_data

    class Meta:
        model = models.Profile
        fields = ('born_in', 'phone', 'github', 'linkedin', 'instagram',
            'about', 'current_goals', 'proffessional_description'
        )
        widgets = {
            'born_in': forms.DateInput(attrs={'type': 'date'}),
        }


class LanguageForm(forms.ModelForm):
    # languages = forms.MultipleChoiceField(required=False, choices=LANGUAGES,)# widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(LanguageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            self.fields['languages'].widget.attrs.update({
                    'placeholder': _("Select languages you can speak"),
                    'class': 'form-control select2',
                }
            )
    
    def clean(self):
        cleaned_data = super(LanguageForm, self).clean()
        return cleaned_data

    class Meta:
        model = models.Language
        fields = ('languages',)
        widgets = {
            'languages': forms.SelectMultiple(),
        }


class XPForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(XPForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-group'
            self.fields['is_current'].widget.attrs.update({
                # 'data-toggle': "toggle",
                # 'data-on': _("Yes"),
                # 'data-off': _("No"),
                # 'data-size': "small",
                # 'data-onstyle': "primary",
                'class': 'bootstrap-toggle',
                }
            )
            self.fields['company'].widget.attrs.update({
                    'placeholder': _("Enter company name"),
                    # 'required': "",
                    'autofocus': "",
                }
            )
            self.fields['company_description'].widget.attrs.update({
                    'placeholder': _("Describe the company you've been worked"),
                    'maxlength':"998",
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
                    # 'required': ""
                }
            )
            self.fields['employee_main_activity'].widget.attrs.update({
                    'placeholder': _("Describe the main activities you performed at the company"),
                    # 'required': ""
                }
            )
            self.fields['from_period'].widget.attrs.update({
                    # 'required': ""
                }
            )
            self.fields['until_period'].widget.attrs.update({
                    # 'required': ""
                }
            )
    
    # def validate_name(self, data): # O nome da empresa nao precisa ser alphanumerico
    #     company = data['company'].split(" ")
    #     company = "".join(company)
    #     if not (company.isalpha()):
    #         self.add_error('company', _('must be alphanumeric'))
    #         raise forms.ValidationError(_("must be alphanumeric"), code='invalid')

    # def validate_is_current(self, data):
    #     if data['is_current'] is True:
    #         models.XP.objects
    #         if not ():
    #             self.add_error('is_current', _('Is permitted just one checkbox selected'))
    #             raise forms.ValidationError(_("Is permitted just one checkbox selected"), code='invalid')
    
    def clean(self):
        cleaned_data = super(XPForm, self).clean()
        # self.validate_name(cleaned_data)
        # self.validate_is_current(cleaned_data)

        return cleaned_data
    
    class Meta:
        CATEGORY = [
            (0, _('Academic')),
            (1, _('Certification')),
        ]
        widgets = {
            'from_period': forms.DateInput(attrs={'type': 'date'}),
            'until_period': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'is_current': _('Is your current Job?')
        }


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(EducationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-group'
            self.fields['is_current'].widget.attrs.update({
                'data-toggle': "toggle",
                'data-on': _("Yes"),
                'data-off': _("No"),
                'data-size': "small",
                'data-onstyle': "primary",
                }
            )
            self.fields['institute'].widget.attrs.update({
                'placeholder': _("Describe the main activities you performed at the company"),
                'autofocus': "",
                
                }
            )
            self.fields['institute_description'].widget.attrs.update({
                }
            )
            self.fields['institute_website'].widget.attrs.update({
                }
            )
            self.fields['institute_mail'].widget.attrs.update({
                }
            )
            self.fields['institute_phone'].widget.attrs.update({
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
    
    def validate_name(self, data):
        institute_name = data['institute'].split(" ")
        institute_name = "".join(institute_name)
        if not (institute_name.isalpha()):
            self.add_error('institute', _('must be alphanumeric'))
            raise forms.ValidationError(_("must be alphanumeric"), code='invalid')

    # def validate_is_current(self, data):
    #     if data['is_current'] is True:
    #         models.Education.objects
    #         if not ():
    #             self.add_error('is_current', _('Is permitted just one checkbox selected'))
    #             raise forms.ValidationError(_("Is permitted just one checkbox selected"), code='invalid')
    
    def clean(self):
        cleaned_data = super(EducationForm, self).clean()
        self.validate_name(cleaned_data)
        # self.validate_is_current(cleaned_data)
    
    class Meta:
        widgets = {
            'from_period': forms.DateInput(attrs={'type': 'date'}),
            'until_period': forms.DateInput(attrs={'type': 'date'})
        }