import fytnez_backend.register.models_admin.user_admin
import fytnez_backend.register.models_admin.achievement_admin
import fytnez_backend.register.models_admin.achievement_type_admin
import fytnez_backend.register.models_admin.user_achievement_admin
from django.contrib import admin

from fytnez_backend.register.models.user import User


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'total_points', 'height', 'weight', 'birthday')
    list_filter = ('username', 'email', 'total_points', 'height', 'weight', 'birthday')
    search_fields = ('username', 'email', 'total_points', 'height', 'weight', 'birthday')
    readonly_fields = ('create_at', 'update_at', 'delete_at')
    ordering = ('username', 'email', 'total_points', 'height', 'weight', 'birthday')
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'total_points', 'height', 'weight', 'birthday')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'total_points', 'height', 'weight', 'birthday')
        }),
    )

