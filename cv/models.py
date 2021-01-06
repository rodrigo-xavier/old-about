# CV = Curriculum Vitae

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from datetime import date, timedelta, datetime
from phonenumber_field.modelfields import PhoneNumberField
from utils.utils import capitalize
from utils.constants import LANGUAGES
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    born_in = models.DateField(verbose_name=_("Born In"), default=date.today() - timedelta(23*365))
    phone = PhoneNumberField(verbose_name=_('Phone'), max_length=255)
    about = models.TextField(verbose_name=_("About You"), max_length=2000, default='', blank=True)
    current_goals = models.TextField(verbose_name=_("Current Goals"), max_length=1000, default='', blank=True) # Objetivos atuais
    proffessional_description = models.TextField(verbose_name=_("Professional Description"), max_length=1000, default='', blank=True) # Descricao profissional (Pode nao ser necessario)
    last = models.DateTimeField(verbose_name=_("Last Modification"), unique=True, auto_now=True)
    github = models.URLField(max_length=200, default='', blank=True)
    linkedin = models.URLField(max_length=200, default='', blank=True)
    instagram = models.URLField(max_length=200, default='', blank=True)
    # logo
    # image

    def __str__(self):
        return str(self.user)
    
    @property
    def age(self):
        days_on_year = 365.2425
        return int((datetime.now().date() - self.born_in).days / days_on_year)
    
    def save(self, *args, **kwargs):
        self.clean()
        return super(Profile, self).save(**kwargs)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class XP(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    is_current = models.BooleanField(verbose_name=_("Is Current"), default=False, blank=True)
    company = models.CharField(verbose_name=_("Company Name"), unique=True, max_length=100, default='', blank=True)
    company_description = models.TextField(verbose_name=_("Company Description"), max_length=1000, default='', blank=True)
    company_website = models.URLField(verbose_name=_("Company Website"), max_length=200, default='', blank=True)
    company_mail = models.EmailField(verbose_name=_("Company Mail"), max_length=255, default='', blank=True)
    company_phone = PhoneNumberField(verbose_name=_('Company Phone'), max_length=255, blank=True)
    employee_role = models.CharField(verbose_name=_("Role"), max_length=100, default='', blank=True) # Cargo
    employee_main_activity = models.TextField(verbose_name=_("Main Activities"), max_length=500, default='', blank=True)
    from_period = models.DateField(verbose_name=_("From Period"), default='', blank=True)
    until_period = models.DateField(verbose_name=_("Until Period"), default='', blank=True)

    def __str__(self):
        return self.company
    
    def clean(self):
        super(XP, self).clean()
        self.company = capitalize(self.company.split(' '))
    
    def save(self, *args, **kwargs):
        self.clean()
        return super(XP, self).save(**kwargs)

    class Meta:
        verbose_name = _("Professional Experience")
        verbose_name_plural = _("Professional Experiences")


class Education(models.Model):
    CATEGORY = [
        (0, _('Academic')),
        (1, _('Certification')),
    ]
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    is_current = models.BooleanField(verbose_name=_("Is Current"), default=False, blank=True)
    category = models.PositiveSmallIntegerField(choices=CATEGORY, verbose_name=_("Category"), default=0)
    institute = models.CharField(verbose_name=_("Institute"), max_length=100, default='', blank=True)
    institute_description = models.TextField(verbose_name=_("Company Description"), max_length=1000, default='', blank=True)
    institute_website = models.URLField(verbose_name=_("Company Website"), max_length=200, default='', blank=True)
    institute_mail = models.EmailField(verbose_name=_("Company Mail"), max_length=255, default='', blank=True)
    institute_phone = PhoneNumberField(verbose_name=_('Company Phone'), max_length=255, blank=True)
    course = models.CharField(verbose_name=_("Course"), max_length=100, default='', blank=True)
    course_description = models.TextField(verbose_name=_("Course Description"), max_length=1000, default='', blank=True)
    from_period = models.DateField(verbose_name=_("From Period"), default='', null=True, blank=True)
    until_period = models.DateField(verbose_name=_("Until Period"), default='', null=True, blank=True)
    duration = models.PositiveSmallIntegerField(verbose_name=_("Duration (In hours)"), default=0, blank=True)

    def __str__(self):
        return self.institute
    
    def clean(self):
        super(Education, self).clean()       
        self.institute = capitalize(self.institute.split(' '))
    
    def save(self, *args, **kwargs):
        self.clean()
        return super(Education, self).save(**kwargs)
    
    class Meta:
        verbose_name = _("Education")



# TODO: Ao clicar na opcao desejada, utilizar jquery/Ajax para
# selecionar a opcao de fluencia em uma caixa de selecao ao lado da de linguagens.
class Language(models.Model):
    FLUENCY = [
        (0, _('Basic')),
        (1, _('Intermediary')),
        (2, _('Advanced')),
        (3, _('Fluent')),
    ]

    # profile = models.ManyToManyField(Profile, verbose_name=_("Profile"))
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    languages = models.PositiveSmallIntegerField(choices=LANGUAGES, verbose_name=_("Languages"), blank=True, null=True)
    fluency_level = models.PositiveSmallIntegerField(choices=FLUENCY, verbose_name=_("Fluency"), blank=True, null=True)

    # @receiver(post_save, sender=Profile)
    # def create_profile_language(sender, instance, created, **kwargs):
    #     if created:
    #         Language.objects.create(profile=instance)

    # @receiver(post_save, sender=Profile)
    # def save_profile_language(sender, instance, **kwargs):
    #     instance.profile.save()