from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from applications.core.mixins.admin import ExportCsvMixin
from .models import User, UserProfile, Blacklist


class ExportUserCSVMixin(ExportCsvMixin):
    @classmethod
    def get_field_names(cls):
        return ['First Name', 'Last Name', 'Phone Number', 'Email', 'Created_at']

    @classmethod
    def get_query_data(cls):
        return User.objects.all().values_list('first_name', 'last_name', 'phone_no', 'email', 'created_at')


class CustomUserAdmin(UserAdmin, ExportCsvMixin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_no',
                    'created_at')
    list_filter = ('created_at', 'is_active', 'is_staff')
    search_fields = ('phone_no', "email")
    ordering = ('created_at',)
    fieldsets = (
        ('Identity', {'fields': ('first_name', 'last_name'), }),
        ('Personal info', {'fields': ('phone_no', 'email', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    actions = ["export_as_csv"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Blacklist)