from django.contrib import admin
from fytnez_backend.register.models.hydric_consumption import HydricConsumption


@admin.register(HydricConsumption)
class HydricConsumptionAdmin(admin.ModelAdmin):
    pass
