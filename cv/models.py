# CV = Curriculum Vitae

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

class Profile(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=30)
    mail = models.EmailField(verbose_name=_("Mail"), max_length=255, unique=True)
    phone = models.CharField(
                verbose_name=_('Phone'), max_length=13, unique=True,
                validators=[RegexValidator(
                    regex=r'^\d{9,13}$',
                    message=_("Phone number must be between 9 and 13 digits")
                    )])
    about = models.TextField(verbose_name=_("About"), max_length=3000)
    current_goals = models.TextField(verbose_name=_("Current Goals"), max_length=1000) # Objetivos atuais
    proffessional_description = models.TextField(verbose_name=_("Professional Description"), max_length=1000) # Descricao profissional (Pode nao ser necessario)
    link = models.URLField(verbose_name=_("Other Platform"), max_length=100) # Have to be a dict
    born = models.DateField(verbose_name=_("Born"), unique=True)
    fluency = models.CharField(verbose_name=_("Fluency"), max_length=30) # Have to be a dict

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class XP(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    company = models.CharField(verbose_name=_("Company"), unique=True, max_length=100)
    role = models.CharField(verbose_name=_("Role"), max_length=100)               # Cargo
    main_activities = models.CharField(verbose_name=_("Main Activities"), max_length=100)
    from_period = models.DateField(verbose_name=_("From Period"))
    until_period = models.DateField(verbose_name=_("Until Period"))

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = _("Professional Experience")
        verbose_name_plural = _("Professional Experiences")

class Academic(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    school = models.CharField(verbose_name=_("School"), max_length=100)
    description = models.TextField(verbose_name=_("Description"), max_length=1000)
    from_period = models.DateField(verbose_name=_("From Period"))
    until_period = models.DateField(verbose_name=_("Until Period"))

    def __str__(self):
        return self.school
    
    class Meta:
        verbose_name = _("Academic Training")


class Certified(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE)
    dispatcher = models.CharField(verbose_name=_("Dispatcher"), max_length=100)
    description = models.TextField(verbose_name=_("Description"), max_length=1000)
    duration = models.PositiveSmallIntegerField(verbose_name=_("Duration"))

    def __str__(self):
        return self.dispatcher

    class Meta:
        verbose_name = _("Extra Curricular Course")
        verbose_name_plural = _("Extra Curricular Courses")