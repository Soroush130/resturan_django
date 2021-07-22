from django.contrib import admin

# Register your models here.
from setting_site.models import AboutUs, SiteSetting, TeamUs

admin.site.register(SiteSetting)
admin.site.register(AboutUs)
admin.site.register(TeamUs)