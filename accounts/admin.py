from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from .models import Department, Group, User


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at',
                    'updated_at', 'is_deleted')
    list_filter = ('created_at', 'updated_at', 'is_deleted')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'department',
                    'created_at', 'updated_at', 'is_deleted')
    list_filter = ('created_at', 'updated_at', 'is_deleted')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_active',
                    'created_at', 'updated_at', 'is_deleted')
    list_filter = ('is_staff', 'is_active', 'created_at',
                   'updated_at', 'is_deleted')
    search_fields = ('email', 'name')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {
         'fields': ('is_deleted',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions',)


# Register permission model in the admin
admin.site.register(Permission)
