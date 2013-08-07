from django.contrib import admin
from django.db import models

from models import Settings
    
class SettingsAdmin(admin.ModelAdmin):
    pass
    class Meta:
    	verbose_name = "Easy Twitter Settings"
    
    
admin.site.register(Settings, SettingsAdmin)