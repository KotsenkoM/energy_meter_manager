from django.contrib import admin

from .models import EnergyMeter, EnergyMeasurements


@admin.register(EnergyMeter)
class EnergyMeterAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(EnergyMeasurements)
class EnergyMeasurementsAdmin(admin.ModelAdmin):
    list_display = ('number',)
