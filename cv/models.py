# CV = Curriculum Vitae

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from datetime import date, timedelta, datetime
from phonenumber_field.modelfields import PhoneNumberField
from utils.utils import capitalize


class Profile(models.Model):
    LANGUAGES = [
        (0, _('None')),
        (1, _('English')),
        (2, _('Chinese')),
        (3, _('Portuguese')),
    ]
    FLUENCY = [
        (1, _('Basic')),
        (2, _('Intermediary')),
        (3, _('Advanced')),
    ]

    name = models.CharField(verbose_name=_('Name'), max_length=40, default='')
    birth = models.DateField(verbose_name=_("Born"), default=date.today() - timedelta(23*365))
    mail = models.EmailField(verbose_name=_("Mail"), max_length=255, default='')
    languages = models.PositiveSmallIntegerField(choices=LANGUAGES, verbose_name=_("Languages"), default=0) # Have to be a dict
    phone = PhoneNumberField(verbose_name=_('Phone'), max_length=255)
    # fluency = models.ChoiceField(choices=[FLUENCY], verbose_name=_("Fluency"))
    # nickname
    link = models.URLField(verbose_name=_("Other Platform"), max_length=200, default='', blank=True) # Have to be a dict
    about = models.TextField(verbose_name=_("About"), max_length=2000, default='', blank=True)
    current_goals = models.TextField(verbose_name=_("Current Goals"), max_length=1000, default='', blank=True) # Objetivos atuais
    proffessional_description = models.TextField(verbose_name=_("Professional Description"), max_length=1000, default='', blank=True) # Descricao profissional (Pode nao ser necessario)
    last = models.DateTimeField(verbose_name=_("Last Modification"), unique=True, auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def age(self):
        days_on_year = 365.2425
        return int((datetime.now().date() - self.birth).days / days_on_year)

    @property
    def first_name(self):
        return self.name.split(' ')[0]

    @property
    def last_name(self):
        return self.name.split(' ')[-1]

    def clean(self):
        super(Profile, self).clean()       
        self.name = capitalize(self.name.split(' '))
    
    def save(self, *args, **kwargs):
        self.clean()
        return super(Profile, self).save(**kwargs)
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class XP(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    company_name = models.CharField(verbose_name=_("Company Name"), unique=True, max_length=100, default='')
    company_description = models.TextField(verbose_name=_("Company Description"), max_length=1000, default='', blank=True)
    company_website = models.URLField(verbose_name=_("Company Website"), max_length=200, default='', blank=True)
    company_mail = models.EmailField(verbose_name=_("Company Mail"), max_length=255, default='')
    company_phone = PhoneNumberField(verbose_name=_('Company Phone'), max_length=255, blank=True)
    employee_role = models.CharField(verbose_name=_("Role"), max_length=100, default='') # Cargo
    employee_main_activity = models.TextField(verbose_name=_("Main Activities"), max_length=500, default='')
    from_period = models.DateField(verbose_name=_("From Period"), default='')
    until_period = models.DateField(verbose_name=_("Until Period"), default='')

    def __str__(self):
        return self.company
    
    def clean(self):
        super(XP, self).clean()       
        self.company_name = capitalize(self.company_name.split(' '))
    
    def save(self, *args, **kwargs):
        self.clean()
        return super(XP, self).save(**kwargs)

    class Meta:
        verbose_name = _("Professional Experience")
        verbose_name_plural = _("Professional Experiences")


class Education(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    institution = models.CharField(verbose_name=_("Institution"), max_length=100, default='')
    description = models.TextField(verbose_name=_("Description"), max_length=1000, default='')
    from_period = models.DateField(verbose_name=_("From Period"), default='', null=True)
    until_period = models.DateField(verbose_name=_("Until Period"), default='', null=True)
    # site da universidade

    def __str__(self):
        return self.institution
    
    class Meta:
        verbose_name = _("Education")


class AdditionalEducation(Education):
    duration = models.PositiveSmallIntegerField(verbose_name=_("Duration"), default=0)
    from_period = None
    until_period = None

    def clean(self):
        self.from_period = None
        self.until_period = None
        return super(AdditionalEducation, self).clean()
    
    def save(self, *args, **kwargs):
        self.clean()
        return super(AdditionalEducation, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Additional Education")
        verbose_name_plural = _("Additional Education")

