from django.contrib import admin
from fytnez_backend.register.models.user_config import UserConfig


@admin.register(UserConfig)
class UserConfigAdmin(admin.ModelAdmin):
    pass
