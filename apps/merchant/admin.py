from django.contrib import admin
from . import models

admin.site.register(models.Merchant)
admin.site.register(models.FrequencySettings)
admin.site.register(models.InstallmentConfiguration)