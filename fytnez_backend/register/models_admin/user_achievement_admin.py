from django.contrib import admin

from fytnez_backend.register.models.user_achievement import UserAchievement


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    pass
