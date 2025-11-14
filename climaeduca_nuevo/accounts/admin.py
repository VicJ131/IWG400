from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'comuna', 'puntaje_total', 'racha_actual', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('comuna', 'puntaje_total', 'racha_actual')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {'fields': ('email', 'comuna')}),
    )