# CV = Curriculum Vitae

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from datetime import date, timedelta, datetime
from phonenumber_field.modelfields import PhoneNumberField


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

    name = models.CharField(verbose_name=_('Name'), max_length=30, default='')
    birth = models.DateField(verbose_name=_("Born"), default=date.today() - timedelta(23*365))
    mail = models.EmailField(verbose_name=_("Mail"), max_length=255, default='')
    languages = models.PositiveSmallIntegerField(choices=LANGUAGES, verbose_name=_("Languages"), default=0) # Have to be a dict
    phone = PhoneNumberField(verbose_name=_('Phone'), max_length=255)
    # fluency = models.ChoiceField(choices=[FLUENCY], verbose_name=_("Fluency"))
    # nickname
    link = models.URLField(verbose_name=_("Other Platform"), max_length=100, default='', blank=True) # Have to be a dict
    about = models.TextField(verbose_name=_("About"), max_length=2000, default='', blank=True)
    current_goals = models.TextField(verbose_name=_("Current Goals"), max_length=1000, default='', blank=True) # Objetivos atuais
    proffessional_description = models.TextField(verbose_name=_("Professional Description"), max_length=1000, default='', blank=True) # Descricao profissional (Pode nao ser necessario)
    last = models.DateTimeField(verbose_name=_("Last Modification"), unique=True, default=datetime.now)

    def __str__(self):
        return self.name
    
    @property
    def age(self):
        return int((datetime.now().date() - self.birth).days / 365.2425)
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class XP(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    company = models.CharField(verbose_name=_("Company"), unique=True, max_length=100, default='')
    role = models.CharField(verbose_name=_("Role"), max_length=100, default='')               # Cargo
    main_activities = models.CharField(verbose_name=_("Main Activities"), max_length=100, default='')
    from_period = models.DateField(verbose_name=_("From Period"), auto_now_add=True)
    until_period = models.DateField(verbose_name=_("Until Period"), auto_now_add=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = _("Professional Experience")
        verbose_name_plural = _("Professional Experiences")

class Academic(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    school = models.CharField(verbose_name=_("School"), max_length=100, default='')
    description = models.TextField(verbose_name=_("Description"), max_length=1000, default='')
    from_period = models.DateField(verbose_name=_("From Period"), auto_now_add=True)
    until_period = models.DateField(verbose_name=_("Until Period"), auto_now_add=True)

    def __str__(self):
        return self.school
    
    class Meta:
        verbose_name = _("Academic Training")


class Certified(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    dispatcher = models.CharField(verbose_name=_("Dispatcher"), max_length=100, default='')
    description = models.TextField(verbose_name=_("Description"), max_length=1000, default='')
    duration = models.PositiveSmallIntegerField(verbose_name=_("Duration"), default=0)

    def __str__(self):
        return self.dispatcher

    class Meta:
        verbose_name = _("Extra Curricular Course")
        verbose_name_plural = _("Extra Curricular Courses")


