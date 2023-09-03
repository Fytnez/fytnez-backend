from django.contrib import admin

from fytnez_backend.register.models.user import User


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('name', 'email', 'total_points', 'height', 'weight', 'birthday')
    list_filter = ('name', 'email', 'total_points', 'height', 'weight', 'birthday')
    search_fields = ('name', 'email', 'total_points', 'height', 'weight', 'birthday')
    readonly_fields = ('create_at', 'update_at', 'delete_at')
    ordering = ('name', 'email', 'total_points', 'height', 'weight', 'birthday')
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'total_points', 'height', 'weight', 'birthday')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'total_points', 'height', 'weight', 'birthday')
        }),
    )