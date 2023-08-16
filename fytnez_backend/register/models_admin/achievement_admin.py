from django.contrib import admin

from fytnez_backend.register.models.achievement import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass
