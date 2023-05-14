from django.contrib import admin

from fytnez_backend.register.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
