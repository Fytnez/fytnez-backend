from django.contrib import admin

from fytnez_backend.register.models.achievement_type import AchievementType


@admin.register(AchievementType)
class AchievementTypeAdmin(admin.ModelAdmin):
    pass
