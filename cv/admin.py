from django.contrib import admin
from cv import models
from reversion.admin import VersionAdmin

@admin.register(models.Profile)
class ProfileAdmin(VersionAdmin):
    pass
@admin.register(models.XP)
class XPAdmin(VersionAdmin):
    pass
@admin.register(models.Education)
class EducationAdmin(VersionAdmin):
    pass

# admin.site.register(models.Profile)
# admin.site.register(models.XP)
# admin.site.register(models.Education)
# admin.site.register(models.AdditionalEducation)