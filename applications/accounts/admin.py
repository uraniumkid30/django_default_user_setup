import csv
from datetime import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.contrib.auth.admin import UserAdmin


from .models import User, UserProfile, Blacklist


admin.site.register(UserProfile)
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        """ Refer to comment on line 34"""
        # field_names = [field.name for field in meta.fields]
        field_names = ['First Name', 'Last Name', 'Phone Number', 'Email','Created_at']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=lottoly-user-{}.csv'.format(datetime.now())
        writer = csv.writer(response)

        writer.writerow(field_names)
        """ Commented this out to handle the logic better for making this export feature more generic"""
        # for obj in queryset:
        #     row = writer.writerow([getattr(obj, field) for field in field_names])

        users = User.objects.all().values_list('first_name', 'last_name', 'phone_no', 'email','created_at')
        for user in users:
            writer.writerow(user)

        return response

    export_as_csv.short_description = "Export as Csv"


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