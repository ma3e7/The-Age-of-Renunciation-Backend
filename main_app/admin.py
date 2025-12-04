from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import GameUser, Hero, Ability

class GameUserAdmin(BaseUserAdmin):
    list_display = ('name', 'is_staff', 'is_superuser', 'hours_played')
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
        ('Game data', {'fields': ('hours_played', 'achievements')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('last_login',)

admin.site.register(GameUser, GameUserAdmin)
admin.site.register(Hero)
admin.site.register(Ability)
