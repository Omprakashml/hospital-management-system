from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'code',
        'name',
        'head_of_department',
        'location',
        'phone',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'code',
        'location',
        'phone',
    )

    list_editable = (
        'is_active',
    )

    ordering = ('name',)